import streamlit as st
from PIL import Image
import os
from precog.modelo import predecir_riesgo
from chronos.estrategias import estrategias_texto, get_estrategia_img
from klang.protocolos import protocolos_info, protocolo_activo

def run():
    st.set_page_config(page_title="Tormenta Dashboard", layout="wide")
    st.title("Panel de Mando - ChronoLogistics (by chavales)")
    tabs = st.tabs([
        "Precog: Riesgo Táctico",
        "Chronos: Visión 2040",
        "K-Lang: Manual Batalla"
    ])

    with tabs[0]:
        st.header("Mapa de Calor de Riesgo")
        mapa_path = os.path.join("precog", "mapa_calor.png")
        if os.path.exists(mapa_path):
            st.image(Image.open(mapa_path), caption="Mapa de Calor - Triángulo del Peligro", use_column_width=True)
        else:
            st.warning("No hay mapa, sorry.")

        st.header("Simulador de Riesgo (toquetea los sliders)")
        velocidad_media = st.slider("Viento (km/h)", 0, 150, 60)
        intensidad_lluvia = st.slider("Lluvia (mm/h)", 0, 100, 20)
        resultado = predecir_riesgo(velocidad_media, intensidad_lluvia)
        st.metric(label="Nivel de Riesgo", value=resultado)

    with tabs[1]:
        st.header("Elige tu estrategia favorita")
        estrategia = st.selectbox("¿Cuál te mola más?", ["Fortaleza Verde", "Búnker Tecnológico"])
        st.header("Futuro épico")
        img_path = get_estrategia_img(estrategia)
        if os.path.exists(img_path):
            st.image(Image.open(img_path), caption=estrategia, use_column_width=True)
        else:
            st.warning("No hay imagen, ups.")
        st.write(estrategias_texto[estrategia])

    with tabs[2]:
        st.header("Protocolos (elige uno y mira qué pasa)")
        protocolo = st.selectbox("Protocolo:", ["VÍSPERA", "CÓDIGO ROJO", "RENACIMIENTO"])
        info = protocolos_info[protocolo]
        st.subheader("Ficha Técnica")
        st.write(f"Disparador: {info['disparador']}")
        st.write("Acciones:")
        for accion in info['acciones']:
            st.write(f"- {accion}")

        st.header("Simulador de Protocolos (prueba los sliders)")
        viento = st.slider("Viento (km/h)", 0, 150, 30)
        inundacion = st.slider("Inundación (cm)", 0, 100, 10)
        activo = protocolo_activo(viento, inundacion)
        color = "red" if activo == "CÓDIGO ROJO" else ("orange" if activo == "VÍSPERA" else "green")
        st.markdown(f"<h2 style='color:{color};'>Protocolo que toca: {activo}</h2>", unsafe_allow_html=True)
