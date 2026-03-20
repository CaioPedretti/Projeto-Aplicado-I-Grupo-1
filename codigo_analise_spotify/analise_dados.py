import pandas as pd

# Carregar dataset
df = pd.read_csv('dados_spotify/dataset_spotify.csv')

# Informações gerais
print("Informações do dataset:")
print(df.info())

# Primeiras linhas
print("\nPrimeiras linhas:")
print(df.head())
