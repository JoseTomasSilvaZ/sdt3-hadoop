import pandas as pd

def process_chunk(chunk):
    # Realiza la limpieza necesaria en el chunk
    chunk_cleaned = chunk.dropna(subset=['branch_addr', 'branch_type', 'taken', 'target'], how='all')
    return chunk_cleaned

def clean_large_csv(file_path, chunk_size=100000):
    # Inicializar variables
    total_rows_deleted = 0
    initial_row_count = 0
    
    output_file_path = 'cleaned_' + file_path
    
    # Procesar el archivo en chunks
    with pd.read_csv(file_path, chunksize=chunk_size) as reader:
        for i, chunk in enumerate(reader):
            initial_row_count += len(chunk)
            cleaned_chunk = process_chunk(chunk)
            total_rows_deleted += len(chunk) - len(cleaned_chunk)
            
            # Guardar el chunk limpio en el archivo de salida
            if i == 0:
                cleaned_chunk.to_csv(output_file_path, mode='w', index=False)
            else:
                cleaned_chunk.to_csv(output_file_path, mode='a', index=False, header=False)
    
    return total_rows_deleted, initial_row_count

file_path = 'dataset4.csv'
deleted_rows, initial_rows = clean_large_csv(file_path)

print(f'Initial row count: {initial_rows}')
print(f'Rows deleted: {deleted_rows}')
print(f'Final row count: {initial_rows - deleted_rows}')
