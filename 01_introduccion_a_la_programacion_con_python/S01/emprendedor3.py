import sys

precio = float(sys.argv[1])
num_usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])
utilidades_anterior = 1000

if len(sys.argv) > 4:
    utilidades_anterior = float(sys.argv[4])

utilidades = precio * num_usuarios - gastos

if utilidades > 0:
    utilidades = 0.65 * utilidades

utilidades_total = utilidades_anterior + utilidades
print("Las utilidades totales son: {} dólares".format(utilidades_total))