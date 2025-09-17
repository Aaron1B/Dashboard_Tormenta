import streamlit as st

import streamlit as st
from PIL import Image
import precog

def mostrar_datos():
    st.header("Precog: Monitor de Riesgo Táctico")

    velocidad_media = st.slider("Velocidad media (km/h)", min_value=0, max_value=200, value=80)
    intensidad_lluvia = st.slider("Intensidad de lluvia (mm/h)", min_value=0, max_value=100, value=20)
    temperatura = st.slider("Temperatura (°C)", min_value=-10, max_value=50, value=20)

    riesgo = precog.predecir_riesgo(velocidad_media, intensidad_lluvia, temperatura)

    st.subheader("Mapa de Calor de Riesgo en Madrid")
    from streamlit_folium import st_folium
    import folium
    from folium.plugins import HeatMap

    madrid_coords = [40.4168, -3.7038]
    m = folium.Map(location=madrid_coords, zoom_start=11)

    puntos_riesgo = [
        [40.4200, -3.7050, 0.8],
        [40.4150, -3.7000, 0.6],
        [40.4300, -3.7100, 0.9],
        [40.4100, -3.6900, 0.7],
        [40.4250, -3.7150, 0.5],
        [40.4180, -3.7020, 1.0],
        [40.4120, -3.6990, 0.4],
        [40.4270, -3.7080, 0.3],
        [40.4190, -3.7040, 0.9],
        [40.4130, -3.7010, 0.7]
    ]
    HeatMap([[lat, lon, valor] for lat, lon, valor in puntos_riesgo], radius=18, blur=15, min_opacity=0.3, max_opacity=0.8).add_to(m)
    st_folium(m, width=600, height=400)

    st.subheader("Simulador de Riesgo Interactivo")

    st.success(f"Nivel de riesgo en cascada: {riesgo}")
