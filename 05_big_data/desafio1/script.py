import random

def create_random_row():
    # simulamos la columna edad
    age = random.randint(18, 90)
    # simulamos la columna ingreso
    income = random.randrange(10000, 1000000, step=1000)
    # simulamos la situación laboral
    employment_status = random.choice(['Unemployed', 'Employed'])
    # simulamos si es que tiene deuda o no
    debt_status = random.choice(['Debt', 'No Debt'])
    # simulamos si es que se cambió recientemente o no
    churn_status = random.choice(['Churn', 'No Churn'])

    return age, income, employment_status, debt_status, churn_status

### Ejercicio 1: Generación Artifical de Datos
data = []
[data.append(create_random_row()) for _ in range(10000000)]

### Ejercicio 2: mejorar la siguiente línea de código
employment_income_looped = 0
for i in data:
    if i[2] == 'Employed':
        employment_income_looped += i[1]

print("¿Qué retornará la variable employment_income_looped ?", "Retorna la suma de los sueldos de personas 'Employed'")
print("¿Cómo sería una implementación del código utilizando map y filter ?", "Implementación...")

income_employed_data = list(map(lambda r: r[1], filter(lambda x: x[2] == 'Employed', data)))
income_employed_sum = sum(income_employed_data)

print(employment_income_looped == income_employed_sum)
print("¿Son iguales los resultados?", "Si, son iguales.")

### Ejercicio 3: mejorar la siguiente línea de código
count_debts_looped = 0
for i in data:
    for j in i:
        if j == 'Debt':
            count_debts_looped += 1

print("¿Cuál será el retorno de la variable count_debts_looped ?", "Retorna la cantidad de clientes con deuda")
print("¿Cuál es la complejidad algorítmica del código?", "La complejidad algoritmica es de 'n2'")
print("¿Cómo sería una implementación del código utilizando map y filter ?", "Implementación...")

debt_data = list(filter(lambda r: r[3] == 'Debt', data))
debt_sum = len(debt_data)
print(count_debts_looped == debt_sum)
print("¿Son iguales los resultados?", "Si, son iguales.")

### Ejercicio 4: mejorar la siguiente línea de código
churn_subset, no_churn_subset = [], []
for i in data:
    for j in i:
        if i == 'Churn':
            churn_subset.append(i)
    for j in i:
        if i == 'No Churn':
            no_churn.append(i)

print("¿Cuál será el retorno de la variable churn_subset y no_churn_subset ?", "Las variables permaneceran como listas vacias dado que 'i' nunca tomará los valores 'Churn' y 'No Churn'. Además la variable 'no_churn' no está definida.")
print("¿Cuál es la complejidad algorítmica del código?", "La complejidad algoritmica es de 'n3'")
print("¿Cómo sería una implementación del código utilizando map y filter ?", "Implementación...")

churn_data = list(map(lambda x: x, filter(lambda r: r[4] == 'Churn', data)))
no_churn_data = list(map(lambda x: x, filter(lambda r: r[4] == 'No Churn', data)))

print("¿Son iguales los resultados de ambas operaciones?", "No son inguales")
print("Estime la media, la varianza, el mínimo y el máximo de la edad para ambos subsets, sin utilizar librerías externas.")

def get_age(row):
    return row[0]

def average(data):
    return sum(data) / len(data)

def variance(data):
    avg = average(data)
    return sum((x - avg) ** 2 for x in data) / len(data)

age_churn_data = list(map(get_age, churn_data))
age_no_churn_data = list(map(get_age, no_churn_data))

print("La media de age_churn_data es: {:.2f}".format(average(age_churn_data)))
print("La media de age_no_churn_data es: {:.2f}".format(average(age_no_churn_data)))

print("La varianza de age_churn_data es: {:.2f}".format(variance(age_churn_data)))
print("La varianza de age_no_churn_data es: {:.2f}".format(variance(age_no_churn_data)))

print("El mínimo de age_churn_data es: ", min(age_churn_data))
print("El mínimo de age_no_churn_data es: ", min(age_no_churn_data))

print("El máximo de age_churn_data es: ", max(age_churn_data))
print("El máximo de age_no_churn_data es: ", max(age_no_churn_data))

### Ejercicio 5: mejorar la siguiente línea de código
unemployed_debt_churn = 0
unemployed_nodebt_churn = 0
unemployed_debt_nochurn = 0
unemployed_nodebt_nochurn = 0
employed_debt_churn = 0
employed_nodebt_churn = 0
employed_debt_nochurn = 0
employed_nodebt_nochurn = 0
for i in data:
    if i[2] == 'Unemployed' and i[3] == 'Debt' and i[4] == 'Churn':
        unemployed_debt_churn += 1
    if i[2] == 'Unemployed' and i[3] == 'No Debt' and i[4] == 'Churn':
        unemployed_nodebt_churn += 1
    if i[2] == 'Unemployed' and i[3] == 'Debt' and i[4] == 'No Churn':
        unemployed_debt_nochurn += 1
    if i[2] == 'Unemployed' and i[3] == 'No Debt' and i[4] == 'No Churn':
        unemployed_nodebt_nochurn += 1
    if i[2] == 'Employed' and i[3] == 'Debt' and i[4] == 'Churn':
        employed_debt_churn += 1
    if i[2] == 'Employed' and i[3] == 'No Debt' and i[4] == 'Churn':
        employed_nodebt_churn += 1
    if i[2] == 'Employed' and i[3] == 'Debt' and i[4] == 'No Churn':
        employed_debt_nochurn += 1
    if i[2] == 'Employed' and i[3] == 'No Debt' and i[4] == 'No Churn':
        employed_nodebt_nochurn += 1

print("Unemployed, Debt, Churn: ", unemployed_debt_churn)
print("Unemployed, No Debt, Churn: ", unemployed_nodebt_churn)
print("Unemployed, Debt, No Churn: ", unemployed_debt_nochurn)
print("Unemployed, No Debt, No Churn: ", unemployed_nodebt_nochurn)
print("Employed, Debt, Churn: ", employed_debt_churn)
print("Employed, No Debt, Churn: ", employed_nodebt_churn)
print("Employed, Debt, No Churn: ", employed_debt_nochurn)
print("Employed, No Debt, No Churn: ", employed_nodebt_nochurn)

print("¿Cómo sería una implementación utilizando map ?", "Implementación...")
from collections import Counter
data_filtered = list(map(lambda x: (x[2], x[3], x[4]), data))
data_counter = Counter(data_filtered)
for key, value in sorted(data_counter.items()):
    print("{}: {}".format(key, value))

print("¿Son iguales los resultados de ambas operaciones?", "Si, son iguales.")
