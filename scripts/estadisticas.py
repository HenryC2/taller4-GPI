


import pandas as pd
import os

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()
Proyectos_completo = pd.read_csv(f'{ruta_actual}\\data\\processed\\Datos_proyectos_procesado.csv')

SUMA_NOMBRE = Proyectos_completo.groupby('NOMBRE').sum()
print(SUMA_NOMBRE)


