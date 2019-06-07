def letra_i(n):
    letra = ""

    header = "*" * n
    letra = header

    for i in range(n-2):
        line = "\n"

        if(n%2 == 0):
            mitad = int(n/2) - 1
        else:
            mitad = int(n/2)
        
        line += " " * mitad 
        
        if(n%2 == 0):
            line += "**"
        else:
            line += "*"

        letra += line

    letra += "\n" + header

    return letra