def predecir_riesgo(velocidad_media, intensidad_lluvia):
    riesgo = min(velocidad_media * 0.5 + intensidad_lluvia * 0.5, 100)
    if riesgo > 80:
        nivel = "MUY CHUNGO"
    elif riesgo > 50:
        nivel = "CUIDADO"
    else:
        nivel = "TRANQUI"
    return f"{int(riesgo)}% - {nivel}"
