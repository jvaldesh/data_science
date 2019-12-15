#script_demo.py
"""
simula una cantidad n de observaciones que siguen una especificación:
age - Un número entero aleatorio entre 18 y 90
income - Un número entero aleatorio entre 10000 y 1000000.
employment_status - Un string entre Employed con probabilidad de ocurrencia .7 y Unemployed con probabilidad de ocurrencia .3.
debt_status - Un string entre Debt con probabilidad de ocurrencia .2 y No Debt con una probabilidad de ocurrencia de .8
churn_pr - Probabilidad predicha de churn para el usuario siguiendo una distribución BetaBinomial(alpha=600, beta=300).

uso:
python3.6 script_demo.py 1

donde 1 hace referencia a un número identificador. """
import random
import numpy as np
import csv
import sys

catch_number = sys.argv[1]
def create_random_row():
    age = random.randint(18, 90)
    income = random.randrange(10000, 1000000, step=1000)
    employment_status = np.random.choice(['Unemployed', 'Employed'], 1, [.3, .7])[0]
    debt_status = np.random.choice(['Debt', 'No Debt'], 1, [.2, .8])[0]
    churn_pr = np.random.beta(600, 300)
    return [age, income, employment_status, debt_status, churn_pr]

with open(f"simulate_churn_{catch_number}.csv", 'w') as csvfile: 
    file = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for _ in range(10000):
        file.writerow(create_random_row())
        
print("Script Listo!")