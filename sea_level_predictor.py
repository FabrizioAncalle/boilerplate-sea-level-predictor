import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer datos
    df = pd.read_csv('epa-sea-level.csv')

    # Crear scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Primera línea de mejor ajuste (todos los datos)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r')

    # Segunda línea de mejor ajuste (desde el año 2000)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = res_2000.intercept + res_2000.slope * x_pred_2000
    plt.plot(x_pred_2000, y_pred_2000, 'green')

    # Etiquetas y título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Guardar imagen
    plt.savefig('sea_level_plot.png')

    return plt.gca()