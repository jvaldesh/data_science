#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


## Helpers


def infer_datatype(df, datatype, drop_none=True):
    """ A partir de un dataset y un tipo de datos entregado, devuelve los nombres de las columnas
        del dataset que tienen el correspondiente tipo de dato.
        
        Argumentos:
           - df: Dataframe de pandas.
           - datatype: String con el tipo de dato que se desea consultar a las columnas del dataframe.
           - drop_none: Filtra las columnas cuyo tipo de dato no esté especificado. default = True.
    """
    tmp_list = [i if df[i].dtype == datatype else None for i in df.columns]
    if drop_none is True:
        tmp_list = list(filter(lambda x: x != None, tmp_list))

    return tmp_list

def return_time_string(var, date_format='%m%d%Y'):
    return var.apply(lambda x: datetime.strptime(str(x), date_format))

def count_freq(df, selected_columns):
    """ Cuenta la cantidad de valores únicos y la frecuencia de dichos valores en las columnas
        entregadas por `selected_columns`.
        
        Argumentos:
            - df: dataframe que contiene las columnas en cuestión.
            - selected_columns: Columnas del dataframe de las que se quiere saber la frecuencia de valores.
    """
    return {i: df[i].unique().shape[0] for i in selected_columns}


def create_suitable_dataframe(df):
    """TODO: Crea un dataframe apto para entrenamiento de acuerdo a normas básicas de limpieza de datos faltantes,
        transformación de etiquetas nulas en variables categóricas y crea atributos sinteticos de edad del sospechoso
         y conversión de distancia a sistema metrico.
    Argumentos:
        - df: Un objeto pandas.DataFrame 
    returns: 
    """
    ### Obtener columnas por tipo de dato
    object_data_type = infer_datatype(df, 'object')
    integer_data_type = infer_datatype(df, 'int')
    float_data_type = infer_datatype(df, 'float')
    
    # Quiero recuperar la lista de valores numericos tambien
    suitable_numerical_attributes = list(integer_data_type) + list(float_data_type)
    #print(suitable_numerical_attributes)

    ### Contar la cantidad de clases en el caso de las var. categóricas y frecuencia de valores para las numéricas
    object_unique_vals = count_freq(df, object_data_type)
    int_unique_vals = count_freq(df, integer_data_type)
    float_unique_vals = count_freq(df, float_data_type)
    
    ### Selección de atributos categoricos que cumplen con características deseadas
    suitable_categorical_attributes = dict(filter(lambda x: x[1] < 100 and x[1] >= 2, object_unique_vals.items()))
    suitable_categorical_attributes = list(suitable_categorical_attributes.keys())

  #
    
    meters = df['ht_feet'].astype(str) + '.' + df['ht_inch'].astype(str)
    df['meters'] = meters.apply(lambda x: float(x) * 0.3048) # Conversión de distanca a sistema metrico (non retarded)
    df['month'] = return_time_string(df['datestop']).apply(lambda x: x.month) # Agregación a solo meses
    
    ### Calculo de la edad del suspechoso
    age_individual = return_time_string(df['dob']).apply(lambda x: 2009 - x.year)
    # Filtrar solo mayores de 18 años y menores de 100
    df['age_individual'] = np.where(np.logical_and(df['age'] > 18, df['age'] < 100), df['age'], np.nan)
    #df.replace(r'^\s*$', np.nan, regex=True)
    proc_df = df
    preserve_vars = suitable_categorical_attributes + ['month', 'meters']
    proc_df = proc_df.loc[:, preserve_vars] # Agregar los atributos sintéticos al df
    return proc_df

def typeData(df):

    ### Obtener columnas por tipo de dato
    object_data_type = infer_datatype(df, 'object')
    integer_data_type = infer_datatype(df, 'int')
    float_data_type = infer_datatype(df, 'float')
    
    # Quiero recuperar la lista de valores numericos tambien
    suitable_numerical_attributes = list(integer_data_type) + list(float_data_type)
    #print(suitable_numerical_attributes)

    ### Contar la cantidad de clases en el caso de las var. categóricas y frecuencia de valores para las numéricas
    return object_data_type,suitable_numerical_attributes

def df_get_dummies(df):
    Lista_Atrib_elim=[]
    frames = []
    frames.append(df)
    for index,colname in enumerate(df):
        if(df[colname].dtype=='object'):
            Lista_Atrib_elim.append(colname)
            frames.append(pd.get_dummies(df[colname],prefix=colname, drop_first=True))
    df=pd.concat(frames,axis=1).drop(columns=Lista_Atrib_elim)
    return df

def plot_importance(fit_model, feat_names):
    tmp_importance = fit_model.feature_importances_
    sort_importance = np.argsort(tmp_importance)[::-1][:10]
    names = [feat_names[i] for i in sort_importance]
    plt.title("Feature importance")
    plt.barh(range(len(names)), tmp_importance[sort_importance])
    plt.yticks(range(len(names)), names, rotation=0)



