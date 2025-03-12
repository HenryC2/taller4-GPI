# En esta tercera etapa se realiza el proceso de transformacion de los datos tomando en cuenta el objetivo del trabajo y el contexto teorico. En este sentido se realizan los calculos de las medidas y variables necesarias para solucionar el problema de interes.

import pandas as pd
import os

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()
directorio_superior = os.path.dirname(ruta_actual)

Proyectos_completo = pd.read_csv(f'{ruta_actual}\\data\\processed\\Datos_proyectos_procesado.csv')

# Se dejan los nombres en un mismo formato y se crea la nueva columna
Proyectos_completo['NOMBRE'] = Proyectos_completo['NOMBRE'].str.title()

tipo_dict = {'A': 'Orgánica', 'B': 'Estatutaria', 'C': 'Ordinaria'}
Proyectos_completo['TIPO_NOMBRE'] = Proyectos_completo['TIPO'].map(tipo_dict)


Proyectos_completo.to_csv(f'{ruta_actual}\\data\\processed\\Datos_proyectos_procesado.csv', index=False)