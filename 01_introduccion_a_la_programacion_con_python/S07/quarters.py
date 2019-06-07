ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000
}

quarters = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for mes, venta in ventas.items():
    if mes in ["Enero", "Febrero", "Marzo"]:
        quarters["Q1"] += venta
    elif mes in ["Abril", "Mayo", "Junio"]:
        quarters["Q2"] += venta
    elif mes in ["Julio", "Agosto", "Septiembre"]:
        quarters["Q3"] += venta
    elif mes in ["Octubre", "Noviembre", "Diciembre"]:
        quarters["Q4"] += venta

print(quarters)