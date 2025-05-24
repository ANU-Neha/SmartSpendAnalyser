import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_receipts_data.csv')

# Display the first few rows of the DataFrame to see the contents
print("First few rows of the dataset:")
print(df.head())
