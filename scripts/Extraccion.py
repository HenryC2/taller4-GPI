# Este corresponde al primer proceso en el cual se realiza la busqueda de la informacion, ya sea por coneccion a una base de datos o mediante otro proceso, y se extraen los datos en brutos para ser utilizados en procesos posteriores.

# Importacion de librerias
import pandas as pd
import os
ruta_actual = os.getcwd()

# Cargue de los archivos CSV y cruzarlos por la columna indicada
congresistas = pd.read_csv(f'{ruta_actual}\\data\\raw\\Congresistas_raw.csv', sep=';')
proyectos = pd.read_csv(f'{ruta_actual}\\data\\raw\\Proyectos_raw.csv', sep=';')
print(congresistas.head())
Proyectos_completo = pd.merge(congresistas, proyectos, on='ID_CONGRESISTA')

Proyectos_completo.to_csv(f'{ruta_actual}\\data\\processed\\Datos_proyectos_procesado.csv', index=False)
