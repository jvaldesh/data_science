import pandas as pd
import numpy as np

df = pd.read_csv("athlete_events.csv")

df_winter = df[df["Season"] == "Winter"]
df_summer = df[df["Season"] == "Summer"]
noc_series = df["NOC"].value_counts()
noc_series = noc_series.sort_values(ascending=False)

ejercicio_1 = df.shape
ejercicio_2 = df["Games"].value_counts().shape[0] 
ejercicio_3 = df["Season"].value_counts() / len(df)
ejercicio_4 = df_summer[df_summer["Year"] == df_summer["Year"].min()]["City"].unique()[0]
ejercicio_5 = df_winter[df_winter["Year"] == df_winter["Year"].min()]["City"].unique()[0]
ejercicio_6 = noc_series[:10]
ejercicio_7 = df["Medal"].value_counts() / (len(df) - df["Medal"].isnull().sum())
ejercicio_8 = df_summer[df_summer["Year"] == df_summer["Year"].min()]["NOC"].unique()