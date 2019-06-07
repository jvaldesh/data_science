import sys

precio = float(sys.argv[1])
num_usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])

utilidades = precio * num_usuarios - gastos

if utilidades > 0:
    utilidades = 0.65 * utilidades

print("Las utilidades son: {} dólares".format(utilidades))