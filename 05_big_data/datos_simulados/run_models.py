# run_models.py

# realizamos los imports necesarios
from sklearn.metrics import classification_report 
from sklearn.linear_model import LogisticRegression 
import pandas as pd
import glob, os

print("Training model on first dataset")

# ingestamos los datos, declaramos que no tenemos etiquetas de columna en el csv.
# para efectos prácticos, vamos a entrenar con el primer batch de datos.
df = pd.read_csv('simulate_churn_1.csv', header=None)
# separamos nuestro vector objetivo
y = df.iloc[:, 3]
# de nuestros atributos 
X = df.drop(columns=[3])

# entrenamos el modelo (ojo, sin dividir datos)
clf = LogisticRegression().fit(X, y)

# para cada csv existente
for i in glob.glob(os.getcwd() + '/*.csv'): 
    # imprimimos el log.
    print("Validating on :", i)
    # separamos nuestro vector objetivo
    y = df.iloc[:, 3]
    # de nuestros atributos
    X = df.drop(columns=[3])
    # # generamos un reporte con el clasificador entrenado. 
    print(classification_report(y, clf.predict(X)), '\n')