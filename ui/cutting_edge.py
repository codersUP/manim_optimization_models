import streamlit as st
import sys
import os
import json
import subprocess


def init_state():
    # required for preparing context switching
    st.session_state.current = 'cutedge'
    st.session_state.cutedge = True
    ##########################################

    # Variable initializations
    st.session_state.variables_size = 2


def cutedge():
    st.title("Introduzca los datos necesarios para su computo")

    if not "cutedge" in st.session_state:
        init_state()

    sz, *var_sections = st.columns(st.session_state['variables_size'] + 1)

    with sz:
        var_cant = st.number_input(
            "Cantidad de variables", 
            value=st.session_state.variables_size, 
            key="variables_size",
            min_value=2, 
            max_value=2, 
            step=1, 
            help="varaiables de su ecuación no lineal"
        )

        var_names = [section.text_input("", key=f"key-x{i}") for i, section in enumerate(var_sections)]

    form = st.text_input("Fórmula", help=
        'Una expresión matemática.'
        'Los operadores soportados son:'
        '+, -, *, **, \\, ^, &, ...'
    )

    contr_cant = st.number_input(
        "Cantidad de condiciones", 
        value=0, 
        min_value=0, 
        step=1, 
        help="condiciones que cumple su ecuación no lineal"
    )

    if contr_cant:
        var_sections = []
        for x in range(0, contr_cant, 4):
            var_sections.extend(st.columns(min(4, contr_cant - x)))
        constrains = []
        for i, section in enumerate(var_sections):
            with section:
                st.latex(r"r_{%d}\\[-100pt]" % (i))
                constrains.append(st.text_input("", key=f"key_r{i}"))


    st.latex(r"\text{Intervalo a graficar en el eje X:}")
    x_axis = st.columns(2)
    u0 = x_axis[0].number_input("inicio", key="x0")
    u1 = x_axis[1].number_input("fin", key="x1")

    st.latex(r"\text{Intervalo a graficar en el eje Y:}")
    y_axis = st.columns(2)
    v0 = y_axis[0].number_input("inicio", key="y0")
    v1 = y_axis[1].number_input("fin", key="y1")

    if contr_cant:
        st.latex(r"\text{Matriz de coeficientes (}a_{i,j}\text{) y términos independientes (}b_i\text{)}")
        A, B = [], []
        for i in range(contr_cant):
            A.append([])
            items = st.columns(var_cant + 1)

            # populate columns
            for j in range(var_cant):
                with items[j]:
                    st.latex(r"a_{%d,%d}\\[-100pt]" % (i, j))
                    A[-1].append(
                        st.number_input("", key=f"key_a_{i},{j}")
                    ) 

            # A.append([item.number_input(f"a_{i},{j}") for j, item in enumerate(items[:-1])])
            with items[-1]:
                st.latex(r"b_{%d}\\[-100pt]" % (i))
                B.append(st.number_input("", key=f"key_b_{i}"))

    st.latex(r"\text{Coeficientes de la función objetivo (}c_j\text{)}")  
    C = []
    for j, col in enumerate(st.columns(var_cant)):
        with col:
            st.latex(r"c_{%d}\\[-100pt]" % (j))
            C.append(st.number_input("", key=f"key_c_{j}"))

    run = st.button("Computar")
    if run:
        placeholder = st.empty() # For displaying messages
        placeholder.success("Ejecutando...")

        data = {
            "vars": [v for v in var_names],
            "func": form,
            "constraints": constrains,
            "x_range": [u0, u1],
            "y_range": [v0, v1],
            "A": A,
            "b": B,
            "c": C

        }
        json_object = json.dumps(data, indent = 4)
        
        path = os.path.abspath(os.path.join(__file__, "../../src/cutting_planes/model_cp.json"))
        with open(path, "w") as outfile:
            outfile.write(json_object)

        
        # Execute Manim graphics
        subprocess.run(["manim", "-ql", "main.py", "CuttingPlanes"])
        video_path = "media/videos/main/480p15/CuttingPlanes.mp4"

        # clear the placeholder at the end
        placeholder.empty()

        st.video(video_path)

        # <some logic here to run the code HERE>
        # variables are
        # var_names: Nombre de las variables
        # form: Formula
        # contrains: Condiciones de la formula
        # u0, u1: Rango a graficar en las X
        # v0, v1: Rango a graficar en las Y
        # A: Matriz de coeficientes
        # B: Terminos ind
        # C: Coeficientes de la func objetivo
        
        # clear the placeholder at the end
        placeholder.empty()
