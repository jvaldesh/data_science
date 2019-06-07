def letra_o(n):
    letra = ""

    header = "*" * n 
    letra = header

    for i in range(n-2):
        line = "\n"
        line += "*"
        line += " " * (n-2)
        line += "*"
        letra += line

    letra += "\n" + header

    return letra

print(letra_o(5))
