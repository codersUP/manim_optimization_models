import streamlit as st
from cutting_edge import cutedge
from geometric import geo
from ideas_geo import ideasgeo
from line_search import linesearch
from penalty import penalty
from plineal import plineal
from ram_ac import ramac
from simplex import simplex
from welcome import welcome


options = [
    "Decidiendo...",
    "Solución geométrica para problemas de programación lineal",
    "Método Simplex",
    "Planos cortantes",
    "Ramificación y acotación",
    "Ideas geométricas de demostración de teoremas",
    "Métodos numéricos para la optimización no lineal",
    "Búsqueda en línea",
    "Penalización",
]

router = [
    welcome,
    geo,
    simplex,
    cutedge,
    ramac,
    ideasgeo,
    plineal,
    linesearch,
    penalty,
]


def callback():
    if "current" in st.session_state:
        del st.session_state[st.session_state.current]


def sidebar():
    with st.sidebar:
        st.header("Qué desea computar?")
        opt = st.radio("", options, on_change=callback)

        idx = options.index(opt)

        return router[idx]
