import os
import pandas as pd
import json
import glob

# Fonction pour charger les fichiers depuis un sous-dossier spécifique
def load_files_from_subfolder(subfolder_path):
    all_data_frames = []
    for file_path in glob.glob(f"{subfolder_path}/*"):
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as file:
                df = pd.DataFrame(json.load(file))
        all_data_frames.append(df)
    return all_data_frames

# Fonction pour uniformiser les noms des colonnes et les types de données
def standardize_data(frames_list):
    # Supposons que vous avez une liste de noms de colonnes standards à utiliser
    # standard_columns = ['col1', 'col2', 'col3', ...]
    standardized_frames = []
    for df in frames_list:
        # Renommer les colonnes ici si nécessaire
        # df.rename(columns={'old_name1': 'standard_name1', 'old_name2': 'standard_name2'}, inplace=True)
        # Convertir les colonnes au bon type ici si nécessaire
        # df['some_column'] = df['some_column'].astype('float')
        standardized_frames.append(df)
    return standardized_frames

# Charger les données de tous les fichiers
clients_folder_path = os.path.join('..', 'data', 'final', 'clients')
all_clients_data = load_files_from_subfolder(clients_folder_path)

# Uniformiser les données
standardized_clients_data = standardize_data(all_clients_data)

# Concaténer toutes les données en un seul DataFrame
combined_clients_data = pd.concat(standardized_clients_data, ignore_index=True)

# Écrire le DataFrame combiné dans un fichier Excel
output_file_path = os.path.join('..', 'data', 'final', 'combined_clients_data.xlsx')
combined_clients_data.to_excel(output_file_path, index=False)

print(f"Les données combinées ont été écrites dans {output_file_path}")
