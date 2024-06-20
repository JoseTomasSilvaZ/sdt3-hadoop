import pandas as pd

# Cargar el dataset desde el archivo CSV
data = pd.read_csv('cleaned_branch_traces.csv')

# Filtrar las filas donde taken es 0
never_taken_data = data[data['taken'] == 0]

# Encontrar branch types que nunca han sido tomadas
never_taken_branch_types = never_taken_data['branch_type'].unique()

# Verificar si existen branch types que nunca han sido tomadas en el dataset completo
all_branch_types = data['branch_type'].unique()
never_taken_completely = [branch for branch in all_branch_types if branch not in data[data['taken'] == 1]['branch_type'].unique()]

# Mostrar los resultados
print("Branch types that have never been taken in any instance (taken = 0):")
print(never_taken_branch_types)

print("\nBranch types that are completely never taken in the entire dataset:")
print(never_taken_completely)