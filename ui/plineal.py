import json
import os
import subprocess
from time import sleep
import streamlit as st


def init_state():
    # required for preparing context switching
    st.session_state.current = "plineal"
    st.session_state.plineal = True
    ##########################################

    # Variable initializations
    st.session_state.cycles = 500
    st.session_state.stroke = 0.5
    st.session_state.variables_size = 2


def plineal():
    st.title("Introduzca los datos necesarios para su cómputo")

    if not "plineal" in st.session_state:
        init_state()

    sz, *var_sections = st.columns(st.session_state["variables_size"] + 1)

    with sz:
        st.number_input(
            "Cantidad de variables",
            value=st.session_state.variables_size,
            key="variables_size",
            min_value=1,
            max_value=2,
            step=1,
            help="varaiables de su ecuación no lineal",
        )

        var_names = [
            section.text_input("", key=f"x{i}")
            for i, section in enumerate(var_sections)
        ]

    form = st.text_input(
        "Fórmula",
        help="Una expresión matemática."
        "Los operadores soportados son:"
        "+, -, *, **, \\, ^, &, ...",
    )

    st.latex(r"\text{Punto inicial:}")

    sz, *init_point = st.columns(st.session_state["variables_size"] + 1)
    with sz:
        initial_value = [
            section.number_input(f"{i}", help=f"Coordenada {i} del punto inicial")
            for i, section in enumerate(init_point)
        ]

    st.latex(r"\text{Intervalo a graficar en el eje X:}")
    x_axis = st.columns(2)
    u0 = x_axis[0].number_input("inicio", key="keyx0")
    u1 = x_axis[1].number_input("fin", key="keyx1")

    st.latex(r"\text{Intervalo a graficar en el eje Y:}")
    y_axis = st.columns(2)
    v0 = y_axis[0].number_input("inicio", key="keyy0")
    v1 = y_axis[1].number_input("fin", key="keyy1")

    cols = st.columns(2)

    stroke = cols[0].number_input(
        "Gosor de las lineas a utilizar",
        value=st.session_state.stroke,
        min_value=0.5,
        key="stroke",
    )

    cycles = cols[1].number_input(
        "Iteraciones máximas",
        value=st.session_state.cycles,
        step=1,
        key="cycles",
        help="Cantidad de iteraciones máximas que se desean realizar para obtener una aproximación del mínimo valor",
    )

    run = st.button("Computar")
    if run:
        placeholder = st.empty()  # For displaying messages
        placeholder.success("Ejecutando...")

        # <some logic here to run the code HERE>
        # variables are
        # var_names: Nombre de las variables
        # form: Formula
        # x0, y0: Punto inicial
        # u0, u1: Rango a graficar en las X
        # v0, v1: Rango a graficar en las Y
        # stroke: Stroke
        # cycles: Los ciclos

        # generate json for input data
        data = {
            "vars": var_names,
            "func": form,
            "initial_point": initial_value,
            "u_range": [u0, u1],
            "v_range": [v0, v1],
            "stroke_width": stroke,
            "cycles": cycles,
        }
        json_object = json.dumps(data, indent=4)

        # Writing to input.json in no package
        path = os.path.abspath(
            os.path.join(__file__, "../../src/Numerical_Optimization/input.json")
        )
        with open(path, "w") as outfile:
            outfile.write(json_object)

        # Execute Manim graphics
        video_path = None
        if st.session_state["variables_size"] == 2:
            subprocess.run(["manim", "-ql", "main.py", "ThreeDNO"])
            video_path = "media/videos/main/480p15/ThreeDNO.mp4"

        elif st.session_state["variables_size"] == 1:
            subprocess.run(["manim", "-ql", "main.py", "TwoDNO"])
            video_path = "media/videos/main/480p15/TwoDNO.mp4"

        # clear the placeholder at the end
        placeholder.empty()

        # st.write("Proyección sobre el plano XY")
        st.video(video_path)

        # clear the placeholder at the end
        placeholder.empty()
