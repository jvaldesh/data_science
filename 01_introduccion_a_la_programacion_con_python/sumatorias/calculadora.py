import sys

operacion = int(sys.argv[1])

numero1 = float(input("Ingrese numero 1: "))
numero2 = float(input("Ingrese numero 2: "))

if operacion == 1:
    print("La suma de {} y {} es: {}".format(numero1, numero2, numero1 + numero2))
elif operacion == 2:
    print("La resta de {} y {} es: {}".format(numero1, numero2, numero1 - numero2))
elif operacion == 3:
    print("La multiplicacion de {} y {} es: {}".format(numero1, numero2, numero1 * numero2))
elif operacion == 4:
    print("La division de {} y {} es: {}".format(numero1, numero2, numero1 / numero2))
else:
    print("Debe ingresar una operacion del 1 al 4")
