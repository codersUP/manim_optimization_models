import streamlit as st
import sys
import os
import json
import subprocess



def init_state():
    # required for preparing context switching
    st.session_state.current = 'linesearch'
    st.session_state.linesearch = True
    ##########################################

    # Variable initializations
    st.session_state.variables_size = 2
    st.session_state.phi = -120
    st.session_state.theta = 45


def linesearch():
    st.title("Introduzca los datos necesarios para su computo")

    if not "linesearch" in st.session_state:
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

    st.latex(r"\text{Punto inicial:}")
    initial_p = st.columns(2)
    x0 = initial_p[0].number_input("X")
    y1 = initial_p[1].number_input("Y")

    st.latex(r"\text{Intervalo a graficar en el eje X:}")
    x_axis = st.columns(2)
    u0 = x_axis[0].number_input("inicio", key="x0")
    u1 = x_axis[1].number_input("fin", key="x1")

    st.latex(r"\text{Intervalo a graficar en el eje Y:}")
    y_axis = st.columns(2)
    v0 = y_axis[0].number_input("inicio", key="y0")
    v1 = y_axis[1].number_input("fin", key="y1")

    col = st.columns(2)

    phi = col[0].number_input(
        "Phi",
        value=st.session_state.phi,
        help="Camera phi",
    )

    theta = col[1].number_input(
        "theta",
        value=st.session_state.theta,
        help="Camera theta",
    )

    run = st.button("Computar")
    if run:
        placeholder = st.empty() # For displaying messages
        placeholder.success("Ejecutando...")
        
        data = {
            "vars": [v for v in var_names],
            "func": form,
            "constraints": constrains,
            "initial_point": [x0, y1],
            "x_range": [u0, u1],
            "y_range": [v0, v1],
            "camera_phi": phi,
            "camera_theta": theta

        }
        json_object = json.dumps(data, indent = 4)
        
        path = os.path.abspath(os.path.join(__file__, "../../src/line_search/model_ls.json"))
        with open(path, "w") as outfile:
            outfile.write(json_object)

        
        # Execute Manim graphics
        subprocess.run(["manim", "-ql", "main.py", "LineSearch"])
        video_path = "media/videos/line_search/480p15/ThreeDCanvas.mp4"

        # clear the placeholder at the end
        placeholder.empty()

        st.video(video_path)

        # clear the placeholder at the end
        placeholder.empty()
