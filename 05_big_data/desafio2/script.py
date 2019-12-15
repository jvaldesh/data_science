### Desafío - Introducción a Big Data
### Ejercicio 1: Ingesta de datos semiestructurados
import requests
import json

url = 'https://www.balldontlie.io/api/v1/games'

params = dict(
    per_page = 100
)

data = requests.get(url=url, params=params).json()

print(data['data'][0])
print("Cada juego tiene un identificador llamado 'id'. Cada home_team tiene un identificador llamado 'id'. \
Cada visitor_team tiene un identificador llamado 'id'")

### Ejercicio 2: Organización de los datos
import pandas as pd

get_row = lambda x: [x['season'], x['period'],
x['home_team']['full_name'], x['home_team']['conference'], x['home_team']['division'],
x['visitor_team']['full_name'], x['visitor_team']['conference'], x['visitor_team']['division'],
x['home_team_score'], x['visitor_team_score'],
x['home_team_score'] - x['visitor_team_score'], x['visitor_team_score'] - x['home_team_score']]
df_data = list(map(get_row, data['data']))
df = pd.DataFrame(df_data, columns = [
'season', 'period',
'home', 'home_conference', 'home_division',
'visitor', 'visitor_conference', 'visitor_division',
'home_score', 'visitor_score', 'home_differential', 'visitor_differential'])
print(df.head(5))

### Ejercicio 3: El efecto de jugar de local
import numpy as np
df['home_win'] = np.where(df['home_score'] > df['visitor_score'], 1, 0)
df['visitor_win'] = np.where(df['home_score'] < df['visitor_score'], 1, 0)

df_home_win = df.groupby(['home']).sum().reset_index()[['home', 'home_win']]
print("Los primeros 5 equipos en cuanto a desempeño por jugar de local son:")
print(df_home_win.sort_values(by = ['home_win', 'home'], ascending = [False, True]).head(5))
print("Los últimos 5 equipos en cuanto a desempeño por jugar de local son:")
print(df_home_win.sort_values(by = ['home_win', 'home'], ascending = [False, True]).tail(5))
df_visitor_win = df.groupby(['visitor']).sum().reset_index()[['visitor', 'visitor_win']]
print("Los primeros 5 equipos en cuanto a desempeño por jugar de visitante son:")
print(df_visitor_win.sort_values(by = ['visitor_win', 'visitor'], ascending = [False, True]).head(5))
print("Los últimos 5 equipos en cuanto a desempeño por jugar de visitante son:")
print(df_visitor_win.sort_values(by = ['visitor_win', 'visitor'], ascending = [False, True]).tail(5))

### Ejercicio 4: Obteniendo el porcentaje de ganar local y de visita
#### Genere un nuevo objeto que guarde el porcentaje de juegos ganados como local por equipo.
df_home_win['home_win_percent'] = df_home_win['home_win'].apply(lambda x: float(x/df.shape[0]))
#### Repita lo mismo para los juegos donde el equipo fue visitante.
df_visitor_win['visitor_win_percent'] = df_visitor_win['visitor_win'].apply(lambda x: float(x/df.shape[0]))
#### ¿Qué equipos tienen iguales chances de ganar como visitante o local?
df_win_percent = pd.merge(df_home_win, df_visitor_win, left_on = 'home', right_on = 'visitor')
print("¿Qué equipos tienen iguales chances de ganar como visitante o local?")
print(df_win_percent[df_win_percent['home_win_percent'] == df_win_percent['visitor_win_percent']])
