import streamlit as st
import os
import json
import subprocess

def init_state():
    # required for preparing context switching
    st.session_state.current = 'geo'
    st.session_state.geo = True
    ##########################################

    # Variable initializations
    st.session_state.form = "10000*x + 6000*y"
    st.session_state.example = ["20*x+50*y <= 3000", "x+y <= 90", "y >= 10", "y >= 0", "x >= 0"]
    st.session_state.contr_cant = 5


def geo():
    st.title("Introduzca los datos necesarios para su cómputo")

    if not "geo" in st.session_state:
        init_state()

    form = st.text_input("Fórmula", help=
        'Una expresión matemática.'
        'Los operadores soportados son:'
        '+, -, *, **, \\, ^, &, ...',
        value = st.session_state.form
    )

    contr_cant = st.number_input(
        "Cantidad de restricciones", 
        value=st.session_state.contr_cant, 
        min_value=0, 
        step=1, 
        help="restricciones que cumple su problema lineal"
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
        path = os.path.abspath(
            os.path.join(__file__, "../../src/Geometric/geometric_aproach.json")
        )
        with open(path, 'r') as settings:
            data = json.load(settings)
        data["func"] = form
        data["constraints"] = contrains
        
        json_object = json.dumps(data, indent = 4)
        with open(path, 'w') as settings:
            settings.write(json_object)
            
        # Execute Manim graphics
        subprocess.run(["manim", "-ql", "main.py", "TwoDGeo_Manim"])
        video_path = "media/videos/main/480p15/TwoDGeo_Manim.mp4"
        
        # clear the placeholder at the end
        placeholder.empty()

        st.video(video_path)
