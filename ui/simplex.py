import streamlit as st
import sys
import os
import json
import subprocess


def init_state():
    # required for preparing context switching
    st.session_state.current = 'simplex'
    st.session_state.simplex = True
    ##########################################

    # Variable initializations
    st.session_state.variables_size = 2
    


def simplex():
    st.title("Introduzca los datos necesarios para modelar su problema")

    if not "simplex" in st.session_state:
        init_state()

    sz, leq, eq = st.columns(3)

    var_cant = sz.number_input(
        "Cantidad de variables involucradas en el problema", 
        key="variables_size",
        min_value=2, 
        max_value=10, 
        step=1, 
        help="número de variables involucradas en su problema"
    )

    contr_cant = leq.number_input(
        "Cantidad de restricciones de desigualdad (<=)", 
        value=0, 
        min_value=0, 
        step=1, 
        help="restricciones de desigualdad que debe cumplir su problema"
    )

    contr_cant_eq = eq.number_input(
        "Cantidad de restricciones de igualdad (=)", 
        value=0, 
        min_value=0, 
        step=1, 
        help="restricciones de igualdad que debe cumplir su problema"
    )

    st.latex(r"\text{Intervalo a graficar en el eje X:}")
    x_axis = st.columns(2)
    u0 = x_axis[0].number_input("inicio", key="x0")
    u1 = x_axis[1].number_input("fin", key="x1")

    st.latex(r"\text{Intervalo a graficar en el eje Y:}")
    y_axis = st.columns(2)
    v0 = y_axis[0].number_input("inicio", key="y0")
    v1 = y_axis[1].number_input("fin", key="y1")

    if var_cant == 3:
        st.latex(r"\text{Intervalo a graficar en el eje Z:}")
        z_axis = st.columns(2)
        z0 = z_axis[0].number_input("inicio", key="z0")
        z1 = z_axis[1].number_input("fin", key="z1")


    A, B = [], []
    if contr_cant:
        st.latex(r"\text{Matriz de coeficientes (}a_{i,j}\text{) y términos independientes (}b_i\text{) (}\leq\text{)}")
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

    A_, B_ = [], []
    if contr_cant_eq:
        st.latex(r"\text{Matriz de coeficientes (}a_{i,j}\text{) y términos independientes (}b_i\text{) (}=\text{)}")
        for i in range(contr_cant_eq):
            A_.append([])
            items = st.columns(var_cant + 1)

            # populate columns
            for j in range(var_cant):
                with items[j]:
                    st.latex(r"a_{%d,%d}\\[-100pt]" % (i + contr_cant, j))
                    A_[-1].append(
                        st.number_input("", key=f"key'_a_{i + contr_cant},{j}")
                    ) 

            # A.append([item.number_input(f"a_{i},{j}") for j, item in enumerate(items[:-1])])
            with items[-1]:
                st.latex(r"b_{%d}\\[-100pt]" % (i + contr_cant))
                B_.append(st.number_input("", key=f"key'_b_{i + contr_cant}"))

    st.latex(r"\text{Coeficientes de la función objetivo (}c_j\text{)}")  
    C = []
    for j, col in enumerate(st.columns(var_cant)):
        with col:
            st.latex(r"c_{%d}\\[-100pt]" % (j))
            C.append(st.number_input("", key=f"key'_c_{j}"))

    st.latex(r"\text{Rangos de los coeficientes de la función objetivo (}c_j\text{)}") 

    lo, hi = [], []
    for i in range(var_cant):
        cols = st.columns(2)
        lo.append(cols[0].number_input(
            f"min{i}",
            value=-sys.float_info.max, 
            min_value=-sys.float_info.max, 
            max_value=sys.float_info.max,
        ))
        hi.append(cols[1].number_input(
            f"max{i}",
            value=sys.float_info.max, 
            min_value=-sys.float_info.max, 
            max_value=sys.float_info.max,
        ))


    st.write(
        "El archivo multimedia que se mostrará"
        " tras presionar el botón de Computar, representa"
        " la interpretación geométrica del área de puntos "
        "factibles del problema y de las soluciones factibles"
        " que genera Simplex en cada iteración. Dichas soluciones"
        " se mostrarán como puntos amarillos. En caso de obtener"
        " un óptimo del problema, el punto se mostrará rojo. Si "
        "el problema consta de solo 3 variables, también se "
        "realizará una graficación en 3D del mismo."
    )  

    run = st.button("Computar")
    if run:
        placeholder = st.empty() # For displaying messages
        placeholder.success("Ejecutando...")

        for i, item in enumerate(lo):
            if item == sys.float_info.max or item == -sys.float_info.max:
                lo[i] = None
        for i, item in enumerate(hi):
            if item == sys.float_info.max or item == -sys.float_info.max:
                hi[i] = None

        ranges = [[u0, u1], [v0, v1]]
        if var_cant == 3:
            ranges.append([z0, z1])

        # generate json for input data
        data = {
            "vars_c": C,
            "A_ineq": A if A else None,
            "b_ineq": B if B else None,
            "A_eq": A_ if A_ else None,
            "b_eq": B_ if B_ else None,
            "bounds": tuple([item for item in zip(lo, hi)]),
            "ranges": ranges
        }
        json_object = json.dumps(data, indent = 4)

        # Writing to input.json in simplex package
        path = os.path.abspath(os.path.join(__file__, "../../src/simplex/input.json"))
        with open(path, "w") as outfile:
            outfile.write(json_object)

        
        # Execute Manim graphics
        subprocess.run(["manim", "-ql", "main.py", "TwoDSimplex"])
        video_path = "media/videos/main/480p15/TwoDSimplex.mp4"
        with open(".temp", "r") as fp:
            msg = fp.read()

        video_path2 = None
        if var_cant == 3:
            subprocess.run(["manim", "-ql", "main.py", "ThreeDSimplex"])
            video_path2 = "media/videos/main/480p15/ThreeDSimplex.mp4"
        
        os.remove(".temp")
        
        # clear the placeholder at the end
        placeholder.empty()

        st.write("Proyección sobre el plano XY")
        st.video(video_path)
        st.write(msg)

        if not video_path2 is None:
            st.write("Superficie tridimensional")
            st.video(video_path2)

        placeholder.empty()
