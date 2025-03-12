Write-Output "El codigo empezo a correr"

Write-Output "Con base en el entorno computacional que se va a crear a partir del archivo .yaml, dentro de la carpeta del proyecto se va a llamar el path de python para correr el codigo completo"

conda env create -f Infraestructura\environment.yml
conda activate Taller2_GPI_environment


$PythonScriptpath = (Get-Command python).Path


Write-Output "El path utilizado en esta ejecución es : $PythonScriptpath , cambie esta ruta a la correspondiente al path de python.exe en su equipo"

& $PythonScriptpath Simulacion/Extraccion.py
& $PythonScriptpath Analisis/Limpieza.py
& $PythonScriptpath Analisis/Transformaciones_y_calculos.py
& $PythonScriptpath Visualizacion/Graficos.py
& $PythonScriptpath Analisis/Cargue_Automatizacion.py

Write-Output "El proceso finalizo"
