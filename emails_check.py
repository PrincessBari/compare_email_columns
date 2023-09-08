import pandas as pd

# getcwd() 
# 

# Load csv file into pandas df
file_path = 'filepath'
df = pd.read_csv(file_path) 

# # Get column names
# column_names = df.columns

# # Print column names
# print(column_names)
# # Index(['Column A', 'Column B'], dtype='object')

# Create column "Emails found in both columns" w/ the email addresses that are same from first 2 columns
df['Emails found in both columns'] = df.apply(lambda row: row['Column A'] if row['Column A'] == row['Column B'] else None, axis=1)

# Create a "Emails in column B not in A" column with the email addresses that are found only in the 2nd column
df['Emails in column B not in A'] = df.apply(lambda row: row['Column B'] if row['Column A'] != row['Column B'] else None, axis=1)

# Create a "Emails in column A and not in B" column with the email addresses that are in the 1st column but not in the 2nd column
df['Emails in column A and not in B'] = df.apply(lambda row: row['Column A'] if row['Column A'] != row['Column B'] else None, axis=1)

# File path to save the updated df
file_path_to_save = 'filepath'

# Save updated df to the specified file path
df.to_csv(file_path_to_save, index=False)
