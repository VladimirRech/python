'''

total_grouping.py
Show how to group totals by one column in Python
Display the first value in a given column
10/12/2024

'''
import pandas as pd

col_group_tot = "depto"
csv_file = "transportation.csv"
col_first_value = "start"
sep_char = ';'

# read csv file
df = pd.read_csv(csv_file, sep=sep_char)

print(f"\nRead file: {csv_file}\n\nGrouping by {col_group_tot}:\n")

# create the totals
result = df.groupby(col_group_tot).agg(total_rows = (col_group_tot, 'size'),
         first_value_for_start = (col_first_value, "first")).reset_index()

# configure to print all rows in dataframe
with pd.option_context("display.max_rows", None, "display.max_columns", None):
    print(result)