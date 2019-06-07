import velocidad as vc
import listas_uno as lu

indice1 = []
indice2 = []
indice4 = []
for auto in lu.autos:
    indice1.append(auto[1])
    indice2.append(auto[2])
    indice4.append(auto[4])

promedio1 = vc.promedio(indice1)
promedio2 = vc.promedio(indice2)
promedio4 = vc.promedio(indice4)

print(promedio1)
print(promedio2)
print(promedio4)