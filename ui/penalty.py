import streamlit as st
import sys
import os
import json
import subprocess

def init_state():
    # required for preparing context switching
    st.session_state.current = 'penalty'
    st.session_state.penalty = True
    ##########################################

    # Variable initializations
    st.session_state.pfactor = 0.1
    st.session_state.ufactor = 0.155
    st.session_state.minmax = 0
    st.session_state.seq = 20
    st.session_state.variables_size = 2
    st.session_state.variables = ['x','y']
    st.session_state.x_axis = [-20, 20]
    st.session_state.y_axis = [-20, 20]
    st.session_state.initial = [0.11, 0.1]
    st.session_state.form = "(x**2 + y - 11)+(x + y**2 - 7)**2"
    st.session_state.contr_cant = 3
    st.session_state.example = ["x>=0", "y>=0", "(x-5)**2 + y**2 - 26 >= 0"]

def penalty():
    st.title("Introduzca los datos necesarios para su cómputo")

    if not "penalty" in st.session_state:
        init_state()

    sz, *var_sections = st.columns(st.session_state['variables_size'] + 1)

    with sz:
        st.number_input(
            "Cantidad de variables", 
            key="variables_size",
            min_value=2, 
            max_value=3, 
            step=1, 
            help="variables de su ecuación no lineal"
        )

        var_names = [section.text_input("", key=f"x{i}", value=st.session_state.variables[i]) for i, section in enumerate(var_sections)]

    form = st.text_input("Fórmula", help=
        'Una expresión matemática.'
        'Los operadores soportados son:'
        '+, -, *, **, \\, ^, &, ...', 
        value = st.session_state.form
    )

    contr_cant = st.number_input(
        "Cantidad de condiciones", 
        value=st.session_state.contr_cant, 
        min_value=0, 
        step=1, 
        help="condiciones que cumple su ecuación no lineal"
    )

    contrains = []
    if contr_cant:
        var_sections = []
        for x in range(0, contr_cant, 4):
            var_sections.extend(st.columns(min(4, contr_cant - x)))
        for i, section in enumerate(var_sections):
            with section:
                st.latex(r"r_{%d}\\[-100pt]" % (i))
                try:
                    contrains.append(st.text_input("", key=f"key_r{i}", value=st.session_state.example[i]))
                except Exception as e:
                    contrains.append(st.text_input("", key=f"key_r{i}"))

    st.latex(r"\text{Punto inicial:}")
    initial = st.columns(2)
    x0 = initial[0].number_input("X", help="Coordenada X del punto inicial", value=st.session_state.initial[0])
    y0 = initial[1].number_input("Y", help="Coordenada Y del punto inicial", value=st.session_state.initial[1])

    st.latex(r"\text{Intervalo a graficar en el eje X:}")
    x_axis = st.columns(2)
    u0 = x_axis[0].number_input("inicio", key="keyx0", value=st.session_state.x_axis[0])
    u1 = x_axis[1].number_input("fin", key="keyx1", value=st.session_state.x_axis[1])

    st.latex(r"\text{Intervalo a graficar en el eje Y:}")
    y_axis = st.columns(2)
    v0 = y_axis[0].number_input("inicio", key="keyy0", value=st.session_state.y_axis[0])
    v1 = y_axis[1].number_input("inicio", key="keyy1", value=st.session_state.y_axis[1])

    cols = st.columns(4)

    minmax = cols[0].number_input(
        "Mínimo o máximo",
        key="minmax",
    )

    ufactor = cols[1].number_input(
        "Factor de actualización",
        key="ufactor",
        help="Valor del factor de actualización",
    )

    pfactor = cols[2].number_input(
        "Factor de penalización",
        key="pfactor",
        help="Valor del factor de penalización",
    )

    seq = cols[3].number_input(
        "Número de sequencia",
        step=1,
        key="seq",
        help="Cantidad de iteraciones máximas que se desean realizar para obtener una aproximación del mínimo valor",
    )

    run = st.button("Computar")
    if run:
        placeholder = st.empty() # For displaying messages
        placeholder.success("Ejecutando...")
        path = os.path.abspath(
            os.path.join(__file__, "../../src/Penalty/penalty_settings.json")
        )
        # with open(path, 'r') as settings:
        #     data = json.load(settings)
        if form != '' and len(var_names) != 0:
            data = {}
            data["Penalty_number_of_sequence"]= seq
            data["Penalty_penalty_factor"]= pfactor
            data["Penalty_update_factor"]= ufactor
            constraints_ = []
            for con in contrains:
                if con != '':
                    constraints_.append(con)
            data["Penalty_constraints"] = constraints_
            data["Penalty_max_or_min"]= minmax,
            data["Penalty_init_point"]= [x0, y0]
            data["Penalty_x_range"]= [u0, u1, 1]
            data["Penalty_y_range"]= [v0, v1, 1]
            data["Penalty_func"]= form
            data["Penalty_vars"]= var_names
            json_object = json.dumps(data, indent = 4)
            with open(path, 'w') as settings:
                settings.write(json_object)
            
        # Execute Manim graphics
        subprocess.run(["manim", "-ql", "main.py", "ThreeDPenalty_Manim"])
        video_path = "media/videos/ThreeDPenalty_Manim/480p15/Penalty_Manim_ManimCE_v0.14.0.mp4"
        # # # with open(".temp", "r") as fp:
        # # #     msg = fp.read()

        
        # # # os.remove(".temp")
        # # # clear the placeholder at the end
        placeholder.empty()

        st.write("Resultado")
        st.video(video_path)
        # <some logic here to run the code HERE>
        # variables are
        # var_names: Nombre de las variables
        # form: Formula
        # contrains: Condiciones de la formula
        # x0, y0: Punto inicial
        # u0, u1: Rango a graficar en las X
        # v0, v1: Rango a graficar en las Y
        # stroke: Stroke
        # cycles: Los ciclos :-P
        
        # clear the placeholder at the end
        placeholder.empty()
