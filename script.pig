-- Load the data from HDFS
data = LOAD '/user/root/data/cleaned_branch_traces.csv' USING PigStorage(',') AS (branch_addr:chararray, branch_type:chararray, taken:int, target:chararray);

-- Sample of data
sample_data = LIMIT data 10;
STORE sample_data INTO 'file:///home/output/sample_data' USING PigStorage(',');

-- Filter branches that were never taken
never_taken = FILTER data BY taken == 0;
grouped_never_taken = GROUP never_taken BY branch_type;
count_never_taken = FOREACH grouped_never_taken GENERATE group AS branch_type, COUNT(never_taken) AS count_never_taken;
STORE count_never_taken INTO 'file:///home/output/count_never_taken' USING PigStorage(',');

-- Analysis on target addresses
grouped_by_target = GROUP data BY target;
target_analysis = FOREACH grouped_by_target GENERATE group AS target, COUNT(data) AS count;
STORE target_analysis INTO 'file:///home/output/target_analysis' USING PigStorage(',');
