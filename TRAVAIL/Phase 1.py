import pandas as pd
import json
import os

# Define the base directory path for 'data/final' relative to the 'TRAVAIL' directory
base_dir = '../data/final/'

# Function to read data from a file based on its extension
def read_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return pd.DataFrame(json.load(file))
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

# Function to read all files in a given directory and combine them
def read_data_from_directory(directory_path):
    all_data_frames = []
    for filename in os.listdir(directory_path):
        if filename.endswith(('.csv', '.xlsx', '.json')):
            file_path = os.path.join(directory_path, filename)
            df = read_file(file_path)
            all_data_frames.append(df)
    if all_data_frames:
        return pd.concat(all_data_frames, ignore_index=True)
    else:
        return pd.DataFrame()  # Return an empty DataFrame if there are no files

# Reading data from all categories and storing in a dictionary
data_categories = ['clients', 'conseillers', 'portfolios', 'produits', 'titres']
data_frames = {}

for category in data_categories:
    directory_path = os.path.join(base_dir, category)
    data_frames[category] = read_data_from_directory(directory_path)

# Combine all DataFrames from the data_frames dictionary into a single DataFrame
combined_data = pd.concat(data_frames.values(), ignore_index=True)

# Write the combined DataFrame to a new output file (Excel format)
output_file_path = os.path.join(base_dir, 'combined_data.xlsx')
combined_data.to_excel(output_file_path, index=False)

print(f"Data combined and written to {output_file_path}")
