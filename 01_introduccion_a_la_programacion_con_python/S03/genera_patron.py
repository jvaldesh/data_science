n = int(input("Ingrese un número\n"))

for i in range(n+1):
    patron = ""
    if i > 0:
        for j in range(i+1):
            if j > 0:
                patron += str(j)

        print(patron)