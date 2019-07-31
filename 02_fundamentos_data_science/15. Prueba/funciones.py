import pandas as pd
import matplotlib.pyplot as plt

def estadisticas(df):
    for column, serie in df.iteritems():
        print("Columna {}".format(column))
        if serie.dtype == 'float64':
            # columna es continua, calcula medidas descriptivas
            print(serie.describe())
        else:
            # columna es discreta, calcula frecuencia
            print(serie.value_counts())

def observaciones_perdidas(dataframe, var, print_list = False):
    """
    observaciones_perdidas: Retorna la cantidad de casos perdidos y el porcentaje correspondiente.
    @param dataframe: La función debe ingresar un objeto DataFrame
    @param var: Variable a inspeccionar
    @param print_list: Opción para imprimir la lista de observaciones perdidas en la variable
    @return Cuando print_list == True, retorna la lista de casos considerando el codigo del pais (ccodealp). Sino retorna la cantidad de casos perdidos y el porcentaje correspondiente
    """
    cantidad = dataframe[var].isna().value_counts().get(True)
    porcentaje = dataframe[var].isna().value_counts(normalize = True).get(True)

    if print_list == True:
        return dataframe[dataframe[var].isna()]['ccodealp']

    return cantidad, porcentaje
