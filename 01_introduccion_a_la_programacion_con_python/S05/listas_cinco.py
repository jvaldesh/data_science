import velocidad as vc
import listas_uno as lu

indice1 = []
for auto in lu.autos:
    indice1.append(auto[1])

promedio1 = vc.promedio(indice1)
lista = filter(lambda x: x > promedio1, indice1)

print(list(lista))