import streamlit as st
from .datos import mostrar_datos
from .simulacion import mostrar_simulacion
from .protocolos import mostrar_protocolos

def run():
    st.set_page_config(page_title="Dashboard Tormenta", layout="wide")
    st.sidebar.title("Navegación")
    pestaña = st.sidebar.radio(
        "Ir a:",
        [
            "Precog: Monitor de Riesgo Táctico",
            "Chronos: Visión Estratégica 2040",
            "K-Lang: Manual de Batalla Interactivo"
        ]
    )
    if pestaña == "Precog: Monitor de Riesgo Táctico":
        mostrar_datos()
    elif pestaña == "Chronos: Visión Estratégica 2040":
        mostrar_simulacion()
    elif pestaña == "K-Lang: Manual de Batalla Interactivo":
        mostrar_protocolos()
