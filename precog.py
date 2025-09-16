def predecir_riesgo(velocidad_media, intensidad_lluvia):
    riesgo = int((velocidad_media * 0.4 + intensidad_lluvia * 0.6))
    if riesgo > 70:
        nivel = "ALTO"
    elif riesgo > 40:
        nivel = "MEDIO"
    else:
        nivel = "BAJO"
    return f"{riesgo}% - {nivel}"
