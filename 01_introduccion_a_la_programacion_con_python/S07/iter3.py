def filter(diccionario, elemento):
    diccionario_new = {}
    for key, value in diccionario.items():
        if value > elemento:
            diccionario_new[key] = value

    return diccionario_new