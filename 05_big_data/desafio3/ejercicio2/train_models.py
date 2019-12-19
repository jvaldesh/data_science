import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB
import pickle

df = pd.read_csv('train_delivery_data.csv')
df.columns = ['deliverer_id', 'delivery_zone', 'monthly_app_usage', 'subscription_type', 'paid_price', 
'customer_size', 'menu', 'delay_time']

# Recodifique el vector objetivo delay_time entre 1 y 0, identificando como 1 aquellos
# casos donde hubo una demora superior al promedio
df['delay_time'] = np.where(df['delay_time'] > df['delay_time'].mean(), 1, 0)

# Para aquellos atributos string, recodifiquelos en K-1 columnas, manteniendo la primera
# categoria como referencia. Elimine el atributo original. Puede utilizar pd.get_dummies
# para eso.
df = pd.concat([df, pd.get_dummies(df['delivery_zone'], prefix = 'delivery_zone', drop_first = True)], 1)
df = pd.concat([df, pd.get_dummies(df['subscription_type'], prefix = 'subscription_type', drop_first = True)], 1)
df = pd.concat([df, pd.get_dummies(df['menu'], prefix = 'menu', drop_first = True)], 1)
df = df.drop(['delivery_zone', 'subscription_type', 'menu'], axis = 1)

# Genere conjuntos de entrenamiento y validacion con los atributos y el vector objetivo,
# preservando un .33 para test y un random state de 11238.
y = df['delay_time']
X = df.drop(['delay_time'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11238, test_size = 0.33)

# Entrene los siguientes modelos LogisticRegression , DecisionTreeClassifier ,
# RandomForestClassifier , GradientBoostingClassifier y BernoulliNB sin modificar hiperparametros.
# Genere un print para cada modelo donde presente el classification_report .
lr_model = LogisticRegression().fit(X_train, y_train)
print("-- Modelo LogisticRegression --")
print(classification_report(y_test, lr_model.predict(X_test)))

dtc_model = DecisionTreeClassifier().fit(X_train, y_train)
print("-- Modelo DecisionTreeClassifier --")
print(classification_report(y_test, dtc_model.predict(X_test)))

rfc_model = RandomForestClassifier().fit(X_train, y_train)
print("-- Modelo RandomForestClassifier --")
print(classification_report(y_test, rfc_model.predict(X_test)))

gbc_model = GradientBoostingClassifier().fit(X_train, y_train)
print("-- Modelo GradientBoostingClassifier --")
print(classification_report(y_test, gbc_model.predict(X_test)))

bnb_model = BernoulliNB().fit(X_train, y_train)
print("-- Modelo BernoulliNB --")
print(classification_report(y_test, bnb_model.predict(X_test)))

print("El mejor modelo obtenido es con algoritmo GradientBoostingClassifier")
pickle_out = open("best_model.pickle","wb")
pickle.dump(gbc_model, pickle_out)
pickle_out.close()