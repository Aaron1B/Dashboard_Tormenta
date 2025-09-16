def predecir_riesgo(velocidad_media, intensidad_lluvia, temperatura):
    if temperatura < 0:
        temp_riesgo = (abs(temperatura) * 1.5) + 10
    elif temperatura < 5:
        temp_riesgo = (5 - temperatura) * 1.2
    elif temperatura > 35:
        temp_riesgo = ((temperatura - 35) * 2)
    else:
        temp_riesgo = 0
    riesgo = int((velocidad_media * 0.35 + intensidad_lluvia * 0.5 + temp_riesgo))
    if riesgo > 70:
        nivel = "ALTO"
    elif riesgo > 40:
        nivel = "MEDIO"
    else:
        nivel = "BAJO"
    return f"{riesgo}% - {nivel}"
