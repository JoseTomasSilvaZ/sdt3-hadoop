import pandas as pd

# Cargar el dataset
file_path = 'dataset4.csv'
df = pd.read_csv(file_path)

# Verificar y eliminar filas con valores nulos
df_cleaned = df.dropna()

# Convertir las columnas a los tipos de datos adecuados si es necesario
df_cleaned['taken'] = df_cleaned['taken'].astype(int)

# Guardar el dataset limpio
cleaned_file_path = 'cleaned_branch_traces4.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)
