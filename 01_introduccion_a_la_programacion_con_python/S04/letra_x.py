def letra_x(n):
    letra = ""

    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                letra += "*"
            else:
                letra += " "

        letra += "\n"

    return letra