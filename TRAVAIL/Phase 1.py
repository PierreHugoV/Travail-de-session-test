import openpyxl
import pandas as pd
import json
import glob
import pip
import openpyxl
import os

# Fonction pour charger les fichiers depuis un sous-dossier spécifique
def load_files_from_subfolder(subfolder_path):
    data = {}
    file_found = False
    for file_path in glob.glob(f"{subfolder_path}/*"):
        file_found = True
        if file_path.endswith('.xlsx'):
            data[os.path.basename(file_path)] = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            data[os.path.basename(file_path)] = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            data[os.path.basename(file_path)] = pd.DataFrame(json_data)

    if not file_found:
        print(f"No data files found in {subfolder_path}. Check the directory path and file extensions.")

    return data


# Fonction principale pour charger toutes les données
def load_all_data(base_dir):
    all_data = {}
    total_files_loaded = 0
    for subfolder in ['clients', 'conseillers', 'portfolios', 'produits', 'titres']:
        subfolder_path = os.path.join(base_dir, subfolder)
        subfolder_data = load_files_from_subfolder(subfolder_path)
        if subfolder_data:
            all_data[subfolder] = subfolder_data
            total_files_loaded += len(subfolder_data)
        else:
            print(f"No files loaded from subfolder: {subfolder}")

    # Return the total number of files loaded and the data dictionary
    return total_files_loaded, all_data


def main():
    # Le chemin de base pour le dossier 'data' dans PyCharm
    base_data_dir = '../data/final'  # Ajuster le chemin vers le dossier 'data'
    total_files_loaded, loaded_data = load_all_data(base_data_dir)

    # Afficher le total de fichiers chargés
    print(f"Total number of data files loaded: {total_files_loaded}")

    # Affichage des données chargées pour vérification
    for category, data_files in loaded_data.items():
        print(f"Category: {category}")
        for file_name, data_frame in data_files.items():
            print(f"Data from {file_name}:")
            print(data_frame.head(), '\\n')  # Afficher seulement les premières lignes

if __name__ == "__main__":
    main()
