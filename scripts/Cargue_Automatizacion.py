# En este ultima proceso, una vez se tienen los datos consolidados con la informacion más importante y que a su vez nos sirven para responder el objetivo del proyecto, se realiza el cargue de los datos a una base de datos consolidada en la que se pueda realizar una rapida consulta de estos desde cualquier equipo y por parte de cualquier miembro del grupo. De igual forma, de ser posible se realiza la base para poder automatizar el proceso de actualizacion de estos datos y que estos puedan estar con la ultima información posible.


import pandas as pd
import os

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()
directorio_superior = os.path.dirname(ruta_actual)

Proyectos_completo = pd.read_csv(f'{directorio_superior}\\Simulacion\\data\\Datos_proyectos_procesado.csv')

# En este csao, solo es necesarios guardar la tabla final en la carpete de los resultados
Proyectos_completo.to_csv(f'{directorio_superior}\\Resultados\\Proyectos_completo.csv', index=False)


print("Los resultados fueron guardados finalmente")