import sys

precio = float(sys.argv[1])
num_usuarios = float(sys.argv[2])
num_usuarios_premium = float(sys.argv[3])
num_usuarios_free = float(sys.argv[4])
gastos = float(sys.argv[5])
num_usuarios_normales = num_usuarios - num_usuarios_premium - num_usuarios_free

utilidades = precio * num_usuarios_normales + 2 * precio * num_usuarios_premium - gastos

if utilidades > 0:
    utilidades = 0.65 * utilidades

print("Las utilidades son: {} dólares".format(utilidades))