import pandas as pd

# Load the CSV file using a raw string for the file path
df = pd.read_csv(
    r'assignment_data_set_old.csv')

# Split the 'genus species' column into two separate columns
df[['genus', 'species']] = df['genus species'].str.split(' ', n=1, expand=True)

# Drop the original 'genus species' column
df = df.drop('genus species', axis=1)

# Save the dataframe back to CSV using a raw string for the file path
df.to_csv(r'assignment_data_set.csv', index=False)
