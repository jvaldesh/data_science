import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
import pickle

df_test = pd.read_csv('test_delivery_data.csv')
df_test.columns = ['deliverer_id', 'delivery_zone', 'monthly_app_usage', 'subscription_type', 'paid_price', 
'customer_size', 'menu', 'delay_time']
df = df_test.copy()
# Implemente el preprocesamiento de los datos que realizo en el conjunto de entrenamiento.
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

# Con el mejor modelo entrenado, genere las predicciones de los datos y genere las siguientes evaluaciones:
pickle_in = open("best_model.pickle","rb")
best_model = pickle.load(pickle_in)
y_test = df['delay_time']
X_test = df.drop(['delay_time'], axis = 1)
pred_pr = best_model.predict_proba(X_test)

# Evalue cual es la probabilidad que un pedido se atrase por sobre la media, para cada
# una de las zonas de envio
df_predict = df_test.copy()
df_predict['delay_proba'] = pred_pr[:, 1]
print("-- Probabilidad que un pedido se atrase por sobre la media, para cada una de las zonas de envio --")
print(df_predict.groupby(['delivery_zone']).mean().reset_index()[['delivery_zone', 'delay_proba']])

# Evalue cual es la probabilidad que un pedido se atrase por sobre la media, para cada
# uno de los repartidores
print("-- Probabilidad que un pedido se atrase por sobre la media, para cada uno de los repartidores --")
print(df_predict.groupby(['deliverer_id']).mean().reset_index()[['deliverer_id', 'delay_proba']])

# Evalue cual es la probabilidad que un pedido se atrase por sobre la media, para cada
# uno de los menus
print("-- Probabilidad que un pedido se atrase por sobre la media, para cada uno de los menus --")
print(df_predict.groupby(['menu']).mean().reset_index()[['menu', 'delay_proba']])

# Evalue cual es la probabilidad que un pedido se atrase por sobre la media, para cada
# una de las subscripciones
print("-- Probabilidad que un pedido se atrase por sobre la media, para cada una de las subscripciones --")
print(df_predict.groupby(['subscription_type']).mean().reset_index()[['subscription_type', 'delay_proba']])