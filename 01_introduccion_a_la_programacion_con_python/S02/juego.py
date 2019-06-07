import sys
import random

jugada_usuario = sys.argv[1]
jugada_pc_int = random.randint(1, 3)

if jugada_pc_int == 1:
    jugada_pc = "piedra"
elif jugada_pc_int == 2:
    jugada_pc = "papel"
else:
    jugada_pc = "tijera"

if jugada_usuario == "piedra":
    if jugada_pc == "piedra":
        print("Computador juega piedra")
        print("Empataste")
    elif jugada_pc == "papel":
        print("Computador juega papel")
        print("Perdiste")
    elif jugada_pc == "tijera":
        print("Computador juega tijera")
        print("Ganaste")
elif jugada_usuario == "papel":
    if jugada_pc == "piedra":
        print("Computador juega piedra")
        print("Ganaste")
    elif jugada_pc == "papel":
        print("Computador juega papel")
        print("Empataste")
    elif jugada_pc == "tijera":
        print("Computador juega tijera")
        print("Perdiste")
elif jugada_usuario == "tijera":
    if jugada_pc == "piedra":
        print("Computador juega piedra")
        print("Perdiste")
    elif jugada_pc == "papel":
        print("Computador juega papel")
        print("Ganaste")
    elif jugada_pc == "tijera":
        print("Computador juega tijera")
        print("Empataste")
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera")