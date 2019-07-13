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
    
def histograma(dataframe, var, true_mean, sample_mean = False):
    """
    histograma: Grafique un histograma en conjunto y señala las medias
    @param dataframe:  La base de datos donde se encuentran los datos específicos.
    @param var:  La variable a graficar
    @param sample_mean: Si es verdadero, genera una recta vertical indicando la media de la variable en la selección muestral
    @param true_mean: Si es verdadero, genera una recta vertical indicando la media de variable en la base de datos completa
    """
    
    var_dropna_sub = dataframe[var].dropna()
    plt.figure(figsize = (15, 5))
    plt.hist(var_dropna_sub, color='gray', alpha=.4)
    if true_mean is not False:
        plt.axvline(true_mean, color='dodgerblue', linestyle='--', lw=2)
        
    if sample_mean is not False:
        plt.axvline(sample_mean, color='tomato', linestyle='--', lw=2)

def dotplot(dataframe, plot_var, plot_by, global_stat = False, statistic = 'mean'):
    """
    dotplot: Devuelve un dotplot
    @param dataframe: La tabla de datos donde buscar las variables.
    @param plot_var: La variable a analizar y extraer las medias.
    @param plot_by: La variable agrupadora.
    @param global_stat: Booleano. Si es True debe graficar la media global de la variable. Por defecto debe ser False.
    @param statistic: Debe presentar dos opciones. mean para la media y median para la mediana. Por defecto debe ser mean.
    """
    if statistic == 'mean':
        group_statistic = df_sub.groupby(plot_by)[plot_var].mean()
    else:
        group_statistic = df_sub.groupby(plot_by)[plot_var].median()
    
    plt.figure(figsize = (15, 5))
    plt.title('Posición de distintas zonas geográficas en cuanto a {} de {}'.format(statistic, plot_var))
    plt.plot(group_statistic.values, group_statistic.index, 'o', color = 'blue')
    
    if global_stat != False:
        plt.axvline(global_stat, color = 'tomato', linestyle = '--')
