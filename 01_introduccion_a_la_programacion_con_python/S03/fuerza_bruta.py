import string

clave = input("Ingresa contraseña\n")

intentos = 0
for i in clave.lower():
    for j in string.ascii_lowercase:
        intentos += 1
        if i == j:
            break

print("{} intentos".format(intentos))