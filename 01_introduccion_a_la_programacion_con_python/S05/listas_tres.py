import listas_uno as lu
import velocidad as vc

indice1 = []
for auto in lu.autos:
    indice1.append(auto[1])

promedio1 = vc.promedio(indice1)

for auto in lu.autos:
    if auto[1] > promedio1:
        print(auto)