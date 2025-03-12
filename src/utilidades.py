


import pandas as pd
import os

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()
Proyectos_completo = pd.read_csv(f'{ruta_actual}\\data\\processed\\Datos_proyectos_procesado.csv')

conteo = Proyectos_completo['NOMBRE'].value_counts()

def calcular_media_conteo(conteo):
    return conteo.mean()

def calcular_mediana_conteo(conteo):
    return conteo.median()

def calcular_desviacion_conteo(conteo):
    return conteo.std()


