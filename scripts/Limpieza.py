# Corresponde a la segunda etapa en la cual se analizan los datos y se limpia la informacion de los valores nulos o con problemas para dejar una base limpia y con la mayor informacion completa posible. Asi mismo se realiza algunas estadisticas basicas para observar el comportamiento basico de los datos y filtrar unicamente la informacion util.

import pandas as pd
import os

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()
directorio_superior = os.path.dirname(ruta_actual)

Proyectos_completo = pd.read_csv(f'{directorio_superior}\\Simulacion\\data\\Datos_proyectos_procesado.csv')

# Eliminar el carácter "_" de la columna NOMBRE
Proyectos_completo['NOMBRE'] = Proyectos_completo['NOMBRE'].str.replace('_', ' ')


Proyectos_completo.to_csv(f'{directorio_superior}\\Simulacion\\data\\Datos_proyectos_procesado.csv', index=False)
