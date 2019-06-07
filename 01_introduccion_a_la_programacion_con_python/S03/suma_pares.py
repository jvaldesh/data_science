n = int(input("Ingrese un número\n"))
suma = 0

for i in range(n+1):
    if i % 2 == 0:
        suma += i

print(suma)