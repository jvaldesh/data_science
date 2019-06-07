cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

tmp = cuenta_regresiva
while tmp > 0:
    print("Iteración {}".format(tmp))
    tmp -= 1