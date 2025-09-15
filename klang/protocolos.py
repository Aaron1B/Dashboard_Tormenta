protocolos_info = {
    "VÍSPERA": {
        "disparador": "Viento fuerte o lluvia que flipas",
        "acciones": ["Avisar a la peña", "Preparar cosas por si acaso"]
    },
    "CÓDIGO ROJO": {
        "disparador": "Viento brutal o inundación heavy",
        "acciones": ["Salir corriendo", "Activar modo TITÁN"]
    },
    "RENACIMIENTO": {
        "disparador": "Todo calmado después del lío",
        "acciones": ["Ver qué se ha roto", "Volver a la normalidad"]
    }
}

def protocolo_activo(viento, inundacion):
    if viento > 90 or inundacion > 50:
        return "CÓDIGO ROJO"
    elif viento > 50 or inundacion > 20:
        return "VÍSPERA"
    else:
        return "RENACIMIENTO"
