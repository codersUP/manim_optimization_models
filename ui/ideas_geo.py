import streamlit as st
import subprocess

def init_state():
    # required for preparing context switching
    st.session_state.current = 'ideasgeo'
    st.session_state.ideasgeo = True
    ##########################################


def ideasgeo():
    st.title("Ideas geométricas empleadas en demostración de teoremas y algoritmos.")

    if not "ideasgeo" in st.session_state:
        init_state()

    with st.expander("Algoritmo Simplex"):
        st.write("""
            Para resolver un problema de programación lineal solo es necesario considerar los vértices
            del poliedro S como candidatos a solución óptima del problema, donde S representa el conjunto 
            de soluciones factibles de dicho problema. Si se considera un número grande de variables y 
            restricciones, la cantidad de vértices puede ser enorme.
        """)
        st.write("""
            El método Simplex tiene su base en una idea geométrica muy simple: primero encuentra una 
            base factible (un vértice de S). Luego el método se mueve de vértice en vértice, a través de 
            las aristas de S que sean direcciones de descenso para la función objetivo, lo que genera una 
            sucesión de vértices cuyos valores por f son estrictamente decrecientes, con lo que se asegura 
            que un mismo vértice no es visitado dos veces. Así, como el número de vértices es finito, el 
            algoritmo converge en tiempo finito; esto significa que encuentra una solución óptima, o una 
            arista a lo largo de la cual la función objetivo es no acotada.
        """)
        st.write("Véase este procedimiento en el siguiente ejemplo:")
        
        subprocess.run(["manim", "-ql", "main.py", "GeoSimplex"])
        video_path = "media/videos/main/480p15/GeoSimplex.mp4"
        st.video(video_path)

        st.write( """
            El video mostrado anteriormente responde al modelo de optimización lineal que 
            se muestra a continuación:
        """)
        st.latex(r"""
            \begin{align*}
                min \, z           = &-2x - 3y \\
                s.a \, \, \, x + y &\leq 3 \\
                    x + 2y         &\leq 4 \\
                    -x + y         &\leq 1 \\
                    x, y           &\ge 0
            \end{align*}
        """)

        st.write( """
            Las rectas aparecen en el mismo orden que se encuentran las restricciones. En
            el caso de este ejemplo, se obtiene una respuesta óptima en solo 4 iteraciones, 
            en el punto (2,1). Si desea hacer uso de esta herramienta, puede hacerlo 
            a través de la opción en la barra lateral que declara **Método Simplex**.
        """)