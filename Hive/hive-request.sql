-- Crea la tabla del dataset
CREATE TABLE IF NOT EXISTS dataset (
    branch_addr STRING,
    branch_type STRING,
    taken INT,
    target STRING
);

-- Crear tabla para almacenar el número total de registros
CREATE TABLE IF NOT EXISTS total_records (
    total_records INT
);

-- Crear tabla para almacenar la frecuencia de cada tipo de branch
CREATE TABLE IF NOT EXISTS branch_frequency (
    branch_type STRING,
    frequency INT
);

-- Crear tabla para almacenar la relación entre tipos de branch y taken
CREATE TABLE IF NOT EXISTS branch_taken_relationship (
    branch_type STRING,
    taken INT,
    count INT
);

-- Crear tabla para almacenar la proporción de registros con taken igual a 1
CREATE TABLE IF NOT EXISTS branch_taken_proportion (
    branch_type STRING,
    proportion_taken_1 DOUBLE
);

-------------------------------------------------------------------
-- Consultas
-------------------------------------------------------------------

-- Para obtener el número total de registros en el dataset:
-- Inserción de datos
INSERT INTO total_records
SELECT COUNT(*) AS total_records FROM dataset;

-- Para contar la frecuencia de cada tipo de branch:
-- Inserción de datos
INSERT INTO branch_frequency
SELECT branch_type, COUNT(*) AS frequency
FROM dataset
GROUP BY branch_type;

-- Para analizar la relación entre los tipos de branch y el valor de taken:
-- Inserción de datos
INSERT INTO branch_taken_relationship
SELECT branch_type, taken, COUNT(*) AS count
FROM dataset
GROUP BY branch_type, taken;

-- Para calcular la proporción de registros con taken igual a 1 para cada tipo de branch:
-- Inserción de datos
INSERT INTO branch_taken_proportion
SELECT branch_type, 
       SUM(CASE WHEN taken = 1 THEN 1 ELSE 0 END) / COUNT(*) AS proportion_taken_1
FROM dataset
GROUP BY branch_type;