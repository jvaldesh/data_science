import velocidad as vc

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

vel_lt_prom = 0
vel_lt_prom_dis_gt_prom = 0
vel_gt_prom = 0
vel_gt_prom_dis_lt_prom = 0
vel_prom = vc.promedio(velocidad)
dis_prom = vc.promedio(distancia)

for i in zip(velocidad, distancia):
    if i[0] < vel_prom:
        vel_lt_prom += 1

        if i[1] > dis_prom:
            vel_lt_prom_dis_gt_prom += 1

    if i[0] > vel_prom:
        vel_gt_prom += 1

        if i[1] < dis_prom:
            vel_gt_prom_dis_lt_prom += 1

print(vel_lt_prom)
print(vel_lt_prom_dis_gt_prom)
print(vel_gt_prom)
print(vel_gt_prom_dis_lt_prom)