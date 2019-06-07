import sys

limite = int(sys.argv[1])

i = 0
suma = 0

while i < limite:
    i += 1
    if i % 2 == 0:
        suma += i

print(suma)