import streamlit as st
from PIL import Image
import precog

def mostrar_datos():
    st.header("Precog: Monitor de Riesgo Táctico")

    st.subheader("Mapa de Clústeres de Riesgo (3D)")
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    np.random.seed(42)
    viento_cluster = np.random.uniform(0, 200, 100)
    lluvia_cluster = np.random.uniform(0, 100, 100)
    temp_cluster = np.random.uniform(-10, 50, 100)

    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111, projection='3d')

    velocidad_media = st.slider("Velocidad media (km/h)", min_value=0, max_value=200, value=80)
    intensidad_lluvia = st.slider("Intensidad de lluvia (mm/h)", min_value=0, max_value=100, value=20)
    temperatura = st.slider("Temperatura (°C)", min_value=-10, max_value=50, value=20)

    riesgo = precog.predecir_riesgo(velocidad_media, intensidad_lluvia, temperatura)
    riesgo_valor = int(riesgo.split('%')[0])
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('risk', ['blue', 'red'])
    cruz_color = cmap(riesgo_valor / 100)

    # Dibujar cruz en el punto simulado
    ax.scatter([velocidad_media], [intensidad_lluvia], [temperatura], marker='x', s=100, c=[cruz_color])
    ax.set_xlabel('Velocidad (km/h)')
    ax.set_ylabel('Lluvia (mm/h)')
    ax.set_zlabel('Temperatura (°C)')
    ax.set_title('Mapa de Clústeres de Riesgo')

    # Ajustar ticks para abarcar todo el rango
    ax.set_xticks([0, 50, 100, 150, 200])
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_zticks([-10, 0, 10, 20, 30, 40, 50])

    # Mostrar valores mínimos y máximos en las esquinas
    ax.text(0, 0, -10, 'Min', color='black', fontsize=8)
    ax.text(200, 100, 50, 'Max', color='black', fontsize=8)

    # Barra de color para riesgo
    import matplotlib as mpl
    norm = mpl.colors.Normalize(vmin=0, vmax=100)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, pad=0.15, shrink=0.7)
    cbar.set_label('Riesgo (%)', rotation=270, labelpad=15)

    st.pyplot(fig)

    st.subheader("Simulador de Riesgo Interactivo")
    st.success(f"Nivel de riesgo en cascada: {riesgo}")
