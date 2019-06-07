import sys

limite = int(sys.argv[1])

i = 0
suma = 0

while i < limite:
    i += 1
    numero = int(input("Ingrese numero: "))
    suma += numero

print(suma/limite)