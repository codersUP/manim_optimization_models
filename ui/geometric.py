import streamlit as st


def init_state():
    # required for preparing context switching
    st.session_state.current = 'geo'
    st.session_state.geo = True
    ##########################################

    # Variable initializations


def geo():
    st.title("Introduzca los datos necesarios para su computo")

    if not "geo" in st.session_state:
        init_state()

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
        contrains = []
        for i, section in enumerate(var_sections):
            with section:
                st.latex(r"r_{%d}\\[-100pt]" % (i))
                contrains.append(st.text_input("", key=f"key_r{i}"))


    run = st.button("Computar")
    if run:
        placeholder = st.empty() # For displaying messages
        placeholder.success("Ejecutando...")
        
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
