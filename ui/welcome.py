import streamlit as st


def welcome():
    st.title("Proyecto de Modelos de Optimización II")
    st.header("Graficar Conceptos y Algoritmos de Modelos de Optimización")

    st.subheader("Desarrollado por:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("- Carmen Irene Cabrera Rodríguez")
        st.markdown("- Enrique Martínez González")

    with col2:
        st.markdown("- Andy A. Castañeda Guerra")
        st.markdown("- Richard García De la Osa")

    st.markdown(
        "## Para comenzar seleccione que programa desea ejecutar en el menú lateral 👈"
    )
