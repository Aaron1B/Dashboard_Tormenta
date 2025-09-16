import streamlit as st
from PIL import Image
import precog

def mostrar_datos():
    st.header("Precog: Monitor de Riesgo Táctico")

    st.subheader("Mapa de Calor de Riesgo")
    mapa_path = "dashboard/mapa_de_calor.png"
    try:
        image = Image.open(mapa_path)
        st.image(image, caption="Mapa de clústeres con Triángulo del Peligro", use_column_width=True)
    except Exception:
        st.warning("No se encontró el mapa de clústeres. Añade 'mapa_de_calor.png' en la carpeta 'dashboard'.")

    st.subheader("Simulador de Riesgo Interactivo")
    velocidad_media = st.slider("Velocidad media (km/h)", min_value=0, max_value=200, value=80)
    intensidad_lluvia = st.slider("Intensidad de lluvia (mm/h)", min_value=0, max_value=100, value=20)

    if st.button("Calcular nivel de riesgo en cascada"):
        riesgo = precog.predecir_riesgo(velocidad_media, intensidad_lluvia)
        st.success(f"Nivel de riesgo en cascada: {riesgo}")
    else:
        st.info("Ajusta los parámetros y pulsa 'Calcular nivel de riesgo en cascada'.")
