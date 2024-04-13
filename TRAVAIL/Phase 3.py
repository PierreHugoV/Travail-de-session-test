# Import necessary libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt

# Placeholder for data loading function, assuming data is already loaded and cleaned
def load_data():
    # This would normally load data from files or a database
    # Here we simulate it with a small dataset as an example
    data = {
        'Conseillers': pd.DataFrame({
            'Conseiller_ID': ['C1', 'C2', 'C3'],
            'Valeur_Gestion': [1000000, 1500000, 1200000],
            'Type_Portefeuille': ['Risque', 'Balancé', 'Sécurité']
        }),
        'Produits': pd.DataFrame({
            'Produit_ID': ['P1', 'P2', 'P3', 'P4'],
            'Clients': [100, 150, 200, 120],
            'Industrie': ['Finance', 'Tech', 'Finance', 'Santé']
        }),
        'Titres': pd.DataFrame({
            'Titre_ID': ['T1', 'T2', 'T3', 'T4', 'T5'],
            'Popularité': [50, 60, 70, 80, 90]
        })
    }
    return data

def plot_adviser_performance(data):
    plt.figure(figsize=(8, 5))
    plt.bar(data['Conseillers']['Conseiller_ID'], data['Conseillers']['Valeur_Gestion'], color='blue')
    plt.xlabel('Conseiller ID')
    plt.ylabel('Valeur Totale Sous Gestion')
    plt.title('Performance des Conseillers Financiers')
    plt.grid(True)
    plt.show()  # This ensures the plot will be displayed

def plot_portfolio_distribution(data):
    portfolio_counts = data['Conseillers']['Type_Portefeuille'].value_counts()
    plt.figure(figsize=(8, 5))
    portfolio_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution des Types de Portefeuilles')
    plt.ylabel('')
    plt.show()  # This ensures the plot will be displayed

# Assuming data is loaded
data = load_data()
# Uncomment below to see plots
# plot_adviser_performance(data)
# plot_portfolio_distribution(data)
