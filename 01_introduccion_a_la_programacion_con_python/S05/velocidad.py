from functools import reduce

def promedio(lista):
    total = reduce(lambda x, y : x + y, lista)
    return total / len(lista)