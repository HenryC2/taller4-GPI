# Este codigo es el que toma la base consolidada y genera un grafico descriptivo de los datos a analizar
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

# Obtener la ruta actual del archivo
ruta_actual = os.getcwd()


# Coneccion con Zenodo
zenodo_api = "https://zenodo.org/api/records/"  # The base API URL
zenodo_id = "15033729"
api_url = zenodo_api + zenodo_id  # The complete URL to access our data

print(f"Preparing to download data from: {api_url}")
 

# Folder temporal
temp_folder = "temp_data"
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)
    print(f"Created temporary folder: {temp_folder}")

# Descarga
print("Downloading metadata...")
response = requests.get(api_url)



# Verificar descarga
if response.status_code == 200:  
    print("Successfully downloaded metadata")
    
    # Save the metadata as a JSON file for reference
    metadata_file = os.path.join(temp_folder, "metadata.json")
    with open(metadata_file, 'w') as f:
        f.write(response.text)
    
    # Parse the JSON data
    metadata = json.loads(response.text)
    

    if 'files' in metadata and len(metadata['files']) > 0:
        # Get the download link for the first file (assuming it's our data)
        file_url = metadata['files'][0]['links']['self']
        
        print(f"Found data file at: {file_url}")
        
        # Step 6: Download the actual data file
        print("Downloading data file...")
        data_response = requests.get(file_url)
        
        if data_response.status_code == 200:
            # Save the downloaded file
            data_file = os.path.join(temp_folder, "survey_data.csv")
            with open(data_file, 'wb') as f:
                f.write(data_response.content)
            
            print(f"Data saved to: {data_file}")
            
            # Step 7: Load the data into a pandas DataFrame for analysis
            print("Loading data for analysis...")
            Proyectos_completo = pd.read_csv(data_file)
            
            # Step 8: Clean column names (convert to lowercase, replace spaces with underscores)
            Proyectos_completo.columns = [col.lower().replace(' ', '_') for col in Proyectos_completo.columns]
            
            
            print("\nData acquisition complete and ready for analysis!")
        else:
            print(f"Error downloading data file. Status code: {data_response.status_code}")
    else:
        print("No files found in the metadata")
else:
    print(f"Error downloading metadata. Status code: {response.status_code}")


print(Proyectos_completo.head())

# Crear un gráfico
conteo_partido = Proyectos_completo['partido'].value_counts()
conteo_partido.plot(kind='bar', color='orange')

plt.xlabel('Partido')
plt.ylabel('Total')
plt.title('Cantidad de proyectos por partido')

plt.savefig(f'{ruta_actual}\\results\\figures\\Proyectos_por_Partido.png')