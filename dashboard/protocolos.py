import streamlit as st

PROTOCOLOS = {
    "VÍSPERA": {
        "disparador": "Alerta temprana por condiciones meteorológicas adversas.",
        "acciones": [
            "Activar monitoreo intensivo.",
            "Preparar equipos de respuesta.",
            "Notificar a la dirección."
        ]
    },
    "CÓDIGO ROJO": {
        "disparador": "Viento > 90 km/h o Inundación > 50 cm.",
        "acciones": [
            "Evacuar zonas críticas.",
            "Activar protocolo TITÁN.",
            "Desplegar recursos de emergencia."
        ]
    },
    "RENACIMIENTO": {
        "disparador": "Condiciones estabilizadas tras la crisis.",
        "acciones": [
            "Iniciar recuperación de activos.",
            "Restablecer operaciones.",
            "Evaluar daños y reportar."
        ]
    }
}

def mostrar_protocolos():
    st.header("K-Lang: Manual de Batalla Interactivo")

    st.subheader("Selector de protocolos")
    protocolo = st.selectbox("Selecciona un protocolo:", list(PROTOCOLOS.keys()))
    ficha = PROTOCOLOS[protocolo]
    st.markdown(f"**Disparador:** {ficha['disparador']}")
    st.markdown("**Secuencia de acciones:**")
    for accion in ficha["acciones"]:
        st.markdown(f"- {accion}")

    st.markdown("---")

    st.subheader("Simulador de protocolos")
    viento = st.slider("Velocidad del viento (km/h)", min_value=0, max_value=150, value=30)
    inundacion = st.slider("Nivel de inundación (cm)", min_value=0, max_value=100, value=10)
    temperatura = st.slider("Temperatura (°C)", min_value=-10, max_value=50, value=20)

    # Evaluar riesgo considerando temperatura
    riesgo_extremo = viento > 90 or inundacion > 50 or temperatura < -5 or temperatura > 45
    riesgo_medio = (viento > 30 or inundacion > 10 or temperatura < 0 or temperatura > 35) and not riesgo_extremo

    if riesgo_extremo:
        protocolo_activo = "CÓDIGO ROJO: TITÁN"
        color = "red"
    elif riesgo_medio:
        protocolo_activo = "VÍSPERA"
        color = "orange"
    else:
        protocolo_activo = "RENACIMIENTO"
        color = "green"

    st.markdown(f"<h2 style='color:{color};'>PROTOCOLO ACTIVO: {protocolo_activo}</h2>", unsafe_allow_html=True)
