# Este codigo es el que toma la base consolidada y genera un grafico descriptivo de los datos a analizar

import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()
directorio_superior = os.path.dirname(ruta_actual)

Proyectos_completo = pd.read_csv(f'{directorio_superior}\\Simulacion\\data\\Datos_proyectos_procesado.csv')

# Crear un gráfico
conteo_partido = Proyectos_completo['PARTIDO'].value_counts()
conteo_partido.plot(kind='bar', color='skyblue')
plt.xlabel('Partido')
plt.ylabel('Total')
plt.title('Cantidad de proyectos por partido')

plt.savefig(f'{directorio_superior}\\Resultados\\Proyectos_por_Partido.png')