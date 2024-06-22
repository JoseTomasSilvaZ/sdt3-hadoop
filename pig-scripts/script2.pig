-- Load the data from HDFS
data = LOAD '/user/root/data/cleaned_dataset4.csv' USING PigStorage(',') AS (branch_addr:chararray, branch_type:chararray, taken:int, target:chararray);

-- Frequency by branch type
grouped_by_branch_type = GROUP data BY branch_type;
acc_frequency_branch_type = FOREACH grouped_by_branch_type GENERATE group AS branch_type, COUNT(data) AS frequency;
STORE acc_frequency_branch_type INTO 'file:///home/output/acc_frequency_branch_type' USING PigStorage(',');

-- Group by branch-type and taken value
grouped = GROUP data BY (branch_type, taken);
count_data_taken = FOREACH grouped GENERATE FLATTEN(group) AS (branch_type, taken), COUNT(data) AS count;
STORE count_data_taken INTO 'file:///home/output/count_data_taken' USING PigStorage(',');

-- Proportion of how many times that branch was taken (taken = 1)
proportion = FOREACH grouped_by_branch_type GENERATE group AS branch_type, (double)SUM(data.taken)/COUNT(data) AS proportion_of_taken;
STORE proportion INTO 'file:///home/output/proportion' USING PigStorage(',');

-- Average 'taken' value per branch type
average_taken = FOREACH grouped_by_branch_type GENERATE group AS branch_type, AVG(data.taken) AS avg_taken;
STORE average_taken INTO 'file:///home/output/average_taken' USING PigStorage(',');
---ES LO MISMO BASICAMENTE QUE EL ANTERIOR

-- Count unique target addresses per branch type
unique_targets = FOREACH grouped_by_branch_type {
    unique_targets_set = DISTINCT data.target;
    GENERATE group AS branch_type, COUNT(unique_targets_set) AS unique_target_count;
}
STORE unique_targets INTO 'file:///home/output/unique_targets' USING PigStorage(',');

-- UNIQUE BRANCH ADDR
unique_branch_addr = FOREACH (GROUP data BY branch_addr) GENERATE 
                      group AS branch_addr, 
                      COUNT(data) AS count;
STORE unique_branch_addr INTO 'file:///home/output/unique_branch_addr' USING PigStorage(',');


-- TARGET PATTERN
grouped_by_target = GROUP data BY target;
frequency_by_target = FOREACH grouped_by_target GENERATE 
                      group AS target, 
                      COUNT(data) AS frequency;
sorted_frequency_by_target = ORDER frequency_by_target BY frequency DESC;
STORE sorted_frequency_by_target INTO 'file:///home/output/frequency_by_target' USING PigStorage(',');
