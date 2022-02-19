import streamlit as st
import sys
import os
import json
import subprocess

def init_state():
    # required for preparing context switching
    st.session_state.current = 'geo'
    st.session_state.geo = True
    st.session_state.form = "(x**2 + y - 11)+(x + y**2 - 7)**2"
    st.session_state.example = ["20*x+50*y <= 3000", "x+y <= 90", "y >= 10", "y >= 0", "x >= 0"]
    st.session_state.contr_cant = 4
    
    ##########################################

    # Variable initializations


def geo():
    st.title("Introduzca los datos necesarios para su computo")

    if not "geo" in st.session_state:
        init_state()

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
                contrains.append(st.text_input("", key=f"key_r{i}", value=st.session_state.example[i]))


    run = st.button("Computar")
    if run:
        placeholder = st.empty() # For displaying messages
        placeholder.success("Ejecutando...")
        with open('../src/Geometric/geometric_aproach.json', 'r') as settings:
            data = json.load(settings)
        data["func"] = form
        data["constraints"] = contrains
        
        with open('../src/Geometric/geometric_aproach.json', 'w') as settings:
            json.dump(data, settings)
            
        # Execute Manim graphics
        # subprocess.run(["manim", "-ql", "main.py", "TwoDGeo_Manim"])
        # video_path = "./media/videos/Geo_Manim/480p15/Geo_Manim_ManimCE_v0.14.0.mp4"
        # # with open(".temp", "r") as fp:
        # #     msg = fp.read()

        
        # # os.remove(".temp")
        # # clear the placeholder at the end
        # placeholder.empty()

        # st.write("Proyección sobre el plano XY")
        # st.video(video_path)
        # st.write(msg)

        # if not video_path2 is None:
        #     st.write("Superficie tridimensional")
        #     st.video(video_path2)
        # {
        # "func": "10000*x + 6000*y",
        # "constraints": ["20*x+50*y <= 3000", "x+y <= 90", "y >= 10", "y >= 0", "x >= 0"]
        # }

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
