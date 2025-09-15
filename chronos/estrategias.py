estrategias_texto = {
    "Fortaleza Verde": "La Fortaleza Verde es rollo naturaleza, todo verde y bonito, así no nos ahogamos y mola más vivir.",
    "Búnker Tecnológico": "El Búnker Tecnológico es como vivir en Matrix, todo seguro y lleno de robots, nadie se moja pero igual te aburres."
}

def get_estrategia_img(estrategia):
    if estrategia == "Fortaleza Verde":
        return "chronos/fortaleza_verde.png"
    else:
        return "chronos/bunker_tecnologico.png"
