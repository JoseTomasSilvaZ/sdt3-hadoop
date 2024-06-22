CREATE TABLE dataset (
    branch_addr STRING,
    branch_type STRING,
    taken INT,
    target STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

CREATE TABLE sample_data AS
SELECT * FROM dataset
LIMIT 10;


CREATE TABLE count_never_taken AS
SELECT branch_type, COUNT() AS count_never_taken
FROM dataset
WHERE taken = 0
GROUP BY branch_type;


CREATE TABLE target_analysis AS
SELECT target, COUNT() AS count
FROM dataset
GROUP BY target;


CREATE TABLE acc_frequency AS
SELECT branch_type, COUNT() AS frequency
FROM dataset
GROUP BY branch_type;


CREATE TABLE count_data_taken AS
SELECT branch_type, taken, COUNT() AS count
FROM dataset
GROUP BY branch_type, taken;


CREATE TABLE proportion AS
SELECT branch_type, CAST(SUM(taken) AS DOUBLE) / COUNT(*) AS proportion_of_taken
FROM dataset
GROUP BY branch_type;


CREATE TABLE average_taken AS
SELECT branch_type, AVG(taken) AS avg_taken
FROM dataset
GROUP BY branch_type;


CREATE TABLE unique_targets AS
SELECT branch_type, COUNT(DISTINCT target) AS unique_target_count
FROM dataset
GROUP BY branch_type;


CREATE TABLE unique_branch_addr AS
SELECT branch_addr, COUNT(*) AS count
FROM dataset
GROUP BY branch_addr;


CREATE TABLE frequency_by_target AS
SELECT target, COUNT(*) AS frequency
FROM dataset
GROUP BY target
ORDER BY frequency DESC;
