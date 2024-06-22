import pandas as pd
import matplotlib.pyplot as plt
import os

output_dir = 'outputs/output_final'

def get_all_part_file_paths(directory):
    files = []
    for file in os.listdir(directory):
        if not file.endswith('.crc'):
            files.append(os.path.join(directory, file))
    return files

def read_and_concatenate_part_files(files, column_names):
    dataframes = [pd.read_csv(file, header=None, names=column_names) for file in files]
    return pd.concat(dataframes, ignore_index=True)

sample_data_files = get_all_part_file_paths(os.path.join(output_dir, 'sample_data'))
acc_frequency_files = get_all_part_file_paths(os.path.join(output_dir, 'acc_frequency_branch_type'))
count_data_taken_files = get_all_part_file_paths(os.path.join(output_dir, 'count_data_taken'))
proportion_files = get_all_part_file_paths(os.path.join(output_dir, 'proportion'))
average_taken_files = get_all_part_file_paths(os.path.join(output_dir, 'average_taken'))
unique_targets_files = get_all_part_file_paths(os.path.join(output_dir, 'unique_targets'))
count_never_taken_files = get_all_part_file_paths(os.path.join(output_dir, 'count_never_taken'))
target_analysis_files = get_all_part_file_paths(os.path.join(output_dir, 'target_analysis'))
unique_branch_addr_files = get_all_part_file_paths(os.path.join(output_dir, 'unique_branch_addr'))
frequency_by_target_files = get_all_part_file_paths(os.path.join(output_dir, 'frequency_by_target'))

sample_data = read_and_concatenate_part_files(sample_data_files, ['branch_addr', 'branch_type', 'taken', 'target']) if sample_data_files else pd.DataFrame()
acc_frequency = read_and_concatenate_part_files(acc_frequency_files, ['branch_type', 'frequency']) if acc_frequency_files else pd.DataFrame()
count_data_taken = read_and_concatenate_part_files(count_data_taken_files, ['branch_type', 'taken', 'count']) if count_data_taken_files else pd.DataFrame()
proportion = read_and_concatenate_part_files(proportion_files, ['branch_type', 'proportion_of_taken']) if proportion_files else pd.DataFrame()
average_taken = read_and_concatenate_part_files(average_taken_files, ['branch_type', 'avg_taken']) if average_taken_files else pd.DataFrame()
unique_targets = read_and_concatenate_part_files(unique_targets_files, ['branch_type', 'unique_target_count']) if unique_targets_files else pd.DataFrame()
count_never_taken = read_and_concatenate_part_files(count_never_taken_files, ['branch_type', 'count_never_taken']) if count_never_taken_files else pd.DataFrame()
target_analysis = read_and_concatenate_part_files(target_analysis_files, ['target', 'count']) if target_analysis_files else pd.DataFrame()
unique_branch_addr = read_and_concatenate_part_files(unique_branch_addr_files, ['branch_addr', 'count']) if unique_branch_addr_files else pd.DataFrame()
frequency_by_target = read_and_concatenate_part_files(frequency_by_target_files, ['target', 'frequency']) if frequency_by_target_files else pd.DataFrame()

if not acc_frequency.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(acc_frequency['branch_type'], acc_frequency['frequency'], color='skyblue')
    plt.xlabel('Branch Type')
    plt.ylabel('Frequency')
    plt.title('Frequency by Branch Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('frequency_by_branch_type.png')
    plt.show()

if not count_data_taken.empty:
    plt.figure(figsize=(12, 8))
    branch_types = count_data_taken['branch_type'].unique()
    taken_values = [0, 1]
    
    bar_width = 0.35
    index = range(len(branch_types))
    
    taken_0_counts = [count_data_taken[(count_data_taken['branch_type'] == bt) & (count_data_taken['taken'] == 0)]['count'].sum() for bt in branch_types]
    taken_1_counts = [count_data_taken[(count_data_taken['branch_type'] == bt) & (count_data_taken['taken'] == 1)]['count'].sum() for bt in branch_types]

    plt.bar(index, taken_0_counts, bar_width, label='Taken = 0')
    plt.bar([i + bar_width for i in index], taken_1_counts, bar_width, label='Taken = 1')
    
    plt.xlabel('Branch Type')
    plt.ylabel('Count')
    plt.title('Count Data by Branch Type and Taken Value')
    plt.xticks([i + bar_width / 2 for i in index], branch_types, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('count_data_taken.png')
    plt.show()

if not proportion.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(proportion['branch_type'], proportion['proportion_of_taken'], color='lightgreen')
    plt.xlabel('Branch Type')
    plt.ylabel('Proportion of Taken')
    plt.title('Proportion of Times Branch was Taken')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('proportion_of_taken.png')
    plt.show()

if not average_taken.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(average_taken['branch_type'], average_taken['avg_taken'], color='lightcoral')
    plt.xlabel('Branch Type')
    plt.ylabel('Average Taken')
    plt.title('Average Taken Value per Branch Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('average_taken.png')
    plt.show()

if not unique_targets.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(unique_targets['branch_type'], unique_targets['unique_target_count'], color='orange')
    plt.xlabel('Branch Type')
    plt.ylabel('Unique Target Count')
    plt.title('Unique Target Addresses per Branch Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('unique_target_count.png')
    plt.show()

if not count_never_taken.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(count_never_taken['branch_type'], count_never_taken['count_never_taken'], color='purple')
    plt.xlabel('Branch Type')
    plt.ylabel('Count Never Taken')
    plt.title('Count of Branches Never Taken')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('count_never_taken.png')
    plt.show()

if not target_analysis.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(target_analysis['target'], target_analysis['count'], color='cyan')
    plt.xlabel('Target Address')
    plt.ylabel('Count')
    plt.title('Target Address Analysis')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('target_analysis.png')
    plt.show()

if not unique_branch_addr.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(unique_branch_addr['branch_addr'], unique_branch_addr['count'], color='brown')
    plt.xlabel('Branch Address')
    plt.ylabel('Count')
    plt.title('Unique Branch Addresses')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('unique_branch_addr.png')
    plt.show()

if not frequency_by_target.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(frequency_by_target['target'], frequency_by_target['frequency'], color='magenta')
    plt.xlabel('Target Address')
    plt.ylabel('Frequency')
    plt.title('Frequency by Target Address')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('frequency_by_target.png')
    plt.show()
