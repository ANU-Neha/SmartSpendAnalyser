import pandas as pd

# Existing data (or load from CSV if needed)
data = {
    'receipt_id': [1, 2, 3, 4, 5],
    'store': ['Store A', 'Store B', 'Store C', 'Store A', 'Store D'],
    'date': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05'],
    'total_amount': [150, 100, 200, 50, 120]
}

# Create DataFrame with initial data
df = pd.DataFrame(data)

# Additional data to append (10 new entries)
new_data = {
    'receipt_id': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'store': ['Store B', 'Store A', 'Store D', 'Store C', 'Store E', 'Store F', 'Store G', 'Store H', 'Store I', 'Store J'],
    'date': ['2023-05-06', '2023-05-07', '2023-05-08', '2023-05-09', '2023-05-10', 
             '2023-05-11', '2023-05-12', '2023-05-13', '2023-05-14', '2023-05-15'],
    'total_amount': [180, 160, 90, 220, 300, 210, 250, 190, 170, 260]
}

# Convert new data to DataFrame
new_df = pd.DataFrame(new_data)

# Append new data to the existing DataFrame
df = pd.concat([df, new_df], ignore_index=True)

# Save the updated DataFrame to CSV
df.to_csv('cleaned_receipts_data.csv', index=False)

print("New data added and saved to 'cleaned_receipts_data.csv' successfully!")
