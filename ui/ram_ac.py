import streamlit as st


def init_state():
    # required for preparing context switching
    st.session_state.current = 'ramac'
    st.session_state.ramac = True
    ##########################################

    # Variable initializations
    st.session_state.cycles = 500
    st.session_state.stroke = 0.5
    st.session_state.variables_size = 2


def ramac():
    st.title("Introduzca los datos necesarios para su computo")

    if not "ramac" in st.session_state:
        init_state()

    sz, *var_sections = st.columns(st.session_state['variables_size'] + 1)

    with sz:
        st.number_input(
            "Cantidad de variables", 
            value=st.session_state.variables_size, 
            key="variables_size",
            min_value=2, 
            max_value=3, 
            step=1, 
            help="varaiables de su ecuación no lineal"
        )

        var_names = [section.text_input("", key=f"x{i}") for i, section in enumerate(var_sections)]

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

    st.latex(r"\text{Punto inicial:}")
    initial = st.columns(2)
    x0 = initial[0].number_input("X", help="Coordenada X del punto inicial")
    y0 = initial[1].number_input("Y", help="Coordenada Y del punto inicial")

    st.latex(r"\text{Intervalo a graficar en el eje X:}")
    x_axis = st.columns(2)
    u0 = x_axis[0].number_input("inicio", key="keyx0")
    u1 = x_axis[1].number_input("fin", key="keyx1")

    st.latex(r"\text{Intervalo a graficar en el eje Y:}")
    y_axis = st.columns(2)
    v0 = y_axis[0].number_input("inicio", key="keyy0")
    v1 = y_axis[1].number_input("inicio", key="keyy1")

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
