import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the output directory
output_dir = 'outputs/output_3'

# Load the datasets
sample_data = pd.read_csv(os.path.join(output_dir, 'sample_data/part-r-00000'), header=None, names=['branch_addr', 'branch_type', 'taken', 'target'])
acc_frequency = pd.read_csv(os.path.join(output_dir, 'acc_frequency/part-r-00000'), header=None, names=['branch_type', 'frequency'])
count_data_taken = pd.read_csv(os.path.join(output_dir, 'count_data_taken/part-r-00000'), header=None, names=['branch_type', 'taken', 'count'])
proportion = pd.read_csv(os.path.join(output_dir, 'proportion/part-r-00000'), header=None, names=['branch_type', 'proportion_of_taken'])
average_taken = pd.read_csv(os.path.join(output_dir, 'average_taken/part-r-00000'), header=None, names=['branch_type', 'avg_taken'])
unique_targets = pd.read_csv(os.path.join(output_dir, 'unique_targets/part-r-00000'), header=None, names=['branch_type', 'unique_target_count'])
count_never_taken = pd.read_csv(os.path.join(output_dir, 'count_never_taken/part-r-00000'), header=None, names=['branch_type', 'count_never_taken'])
target_analysis = pd.read_csv(os.path.join(output_dir, 'target_analysis/part-r-00000'), header=None, names=['target', 'count'])

# Plot frequency by branch type
plt.figure(figsize=(10, 6))
plt.bar(acc_frequency['branch_type'], acc_frequency['frequency'], color='skyblue')
plt.xlabel('Branch Type')
plt.ylabel('Frequency')
plt.title('Frequency by Branch Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('frequency_by_branch_type.png')
plt.show()

# Plot count data taken
plt.figure(figsize=(10, 6))
for branch_type in count_data_taken['branch_type'].unique():
    subset = count_data_taken[count_data_taken['branch_type'] == branch_type]
    plt.bar(subset['taken'] + (0.1 if branch_type == 'conditional_jump' else -0.1), subset['count'], width=0.2, label=branch_type)

plt.xlabel('Taken')
plt.ylabel('Count')
plt.title('Count Data by Branch Type and Taken Value')
plt.legend()
plt.tight_layout()
plt.savefig('count_data_taken.png')
plt.show()

# Plot proportion of taken
plt.figure(figsize=(10, 6))
plt.bar(proportion['branch_type'], proportion['proportion_of_taken'], color='lightgreen')
plt.xlabel('Branch Type')
plt.ylabel('Proportion of Taken')
plt.title('Proportion of Times Branch was Taken')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('proportion_of_taken.png')
plt.show()

# Plot average taken value per branch type
plt.figure(figsize=(10, 6))
plt.bar(average_taken['branch_type'], average_taken['avg_taken'], color='lightcoral')
plt.xlabel('Branch Type')
plt.ylabel('Average Taken')
plt.title('Average Taken Value per Branch Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('average_taken.png')
plt.show()

# Plot unique target addresses per branch type
plt.figure(figsize=(10, 6))
plt.bar(unique_targets['branch_type'], unique_targets['unique_target_count'], color='orange')
plt.xlabel('Branch Type')
plt.ylabel('Unique Target Count')
plt.title('Unique Target Addresses per Branch Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('unique_target_count.png')
plt.show()

# Plot count of branches never taken
plt.figure(figsize=(10, 6))
plt.bar(count_never_taken['branch_type'], count_never_taken['count_never_taken'], color='purple')
plt.xlabel('Branch Type')
plt.ylabel('Count Never Taken')
plt.title('Count of Branches Never Taken')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('count_never_taken.png')
plt.show()

# Plot target address analysis
plt.figure(figsize=(10, 6))
plt.bar(target_analysis['target'], target_analysis['count'], color='cyan')
plt.xlabel('Target Address')
plt.ylabel('Count')
plt.title('Target Address Analysis')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('target_analysis.png')
plt.show()
