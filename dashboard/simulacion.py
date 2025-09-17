import streamlit as st
from PIL import Image

def mostrar_simulacion():
    st.header("Chronos: Visión Estratégica 2040")

    st.subheader("Selector de Estrategia")
    estrategia = st.radio(
        "Elige la visión estratégica:",
        ["Fortaleza Verde", "Búnker Tecnológico"],
        key="estrategia_radio"
    )

    st.subheader("Visualizador de Futuros")
    if estrategia == "Fortaleza Verde":
        imagen_path = "dashboard/fortaleza_verde.png"
        texto = (
            "Fortaleza Verde representa un futuro sostenible y resiliente para ChronoLogistics y Madrid. "
            "Priorizamos la integración ecológica, infraestructuras verdes y la adaptación climática. "
            "Esta visión garantiza la protección de activos y la confianza de inversores en un entorno cambiante."
        )
    else:
        imagen_path = "dashboard/bunker_tecnologico.png"
        texto = (
            "Búnker Tecnológico apuesta por la máxima seguridad y digitalización. "
            "ChronoLogistics se convierte en el núcleo logístico más avanzado de Europa, "
            "blindando operaciones y datos ante cualquier amenaza. Es la opción preferida para inversores tecnológicos."
        )

    try:
        imagen = Image.open(imagen_path)
        st.image(imagen, caption=estrategia, use_container_width=True)
    except Exception:
        st.warning(f"No se encontró la imagen para '{estrategia}'. Añade '{imagen_path}' en la carpeta 'dashboard'.")

    st.markdown(f"**Defensa estratégica:** {texto}")
