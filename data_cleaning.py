
import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_receipts_data.csv')

# 1. Handling Missing Values
# Check for missing values in the dataset
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values in 'store' with 'Unknown' (or you can use another placeholder)
df['store'].fillna('Unknown', inplace=True)

# Fill missing values in 'date' with '2023-01-01' (or you can use a reasonable date)
df['date'].fillna('2023-01-01', inplace=True)

# Fill missing values in 'total_amount' with the mean value of the column
df['total_amount'].fillna(df['total_amount'].mean(), inplace=True)

# 2. Standardizing Date Format
# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# 3. Removing Duplicates
# Remove any duplicate rows
df.drop_duplicates(inplace=True)

# 4. Correct Data Types
# Ensure 'total_amount' is numeric (it should already be, but we'll check and convert if needed)
df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')

# Verify the changes
print("\nData after cleaning:")
print(df.head())

# Save the cleaned data to a new CSV file (or overwrite the original one)
df.to_csv('cleaned_receipts_data_cleaned.csv', index=False)

print("\nData cleaning complete. The cleaned dataset is saved as 'cleaned_receipts_data_cleaned.csv'.")
=======
import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_receipts_data.csv')

# 1. Handling Missing Values
# Check for missing values in the dataset
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values in 'store' with 'Unknown' (or you can use another placeholder)
df['store'].fillna('Unknown', inplace=True)

# Fill missing values in 'date' with '2023-01-01' (or you can use a reasonable date)
df['date'].fillna('2023-01-01', inplace=True)

# Fill missing values in 'total_amount' with the mean value of the column
df['total_amount'].fillna(df['total_amount'].mean(), inplace=True)

# 2. Standardizing Date Format
# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# 3. Removing Duplicates
# Remove any duplicate rows
df.drop_duplicates(inplace=True)

# 4. Correct Data Types
# Ensure 'total_amount' is numeric (it should already be, but we'll check and convert if needed)
df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')

# Verify the changes
print("\nData after cleaning:")
print(df.head())

# Save the cleaned data to a new CSV file (or overwrite the original one)
df.to_csv('cleaned_receipts_data_cleaned.csv', index=False)

print("\nData cleaning complete. The cleaned dataset is saved as 'cleaned_receipts_data_cleaned.csv'.")

