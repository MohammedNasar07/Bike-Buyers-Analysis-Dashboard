import pandas as pd

# Load the data
file_path = '../Bike_Buyers_Analysis.xlsx'  # Adjust the path if necessary
bike_buyers_df = pd.read_excel(file_path, sheet_name='bike_buyers')

# Data cleaning steps
# 1. Handle missing values by dropping rows with any missing values
bike_buyers_df.dropna(inplace=True)

# 2. Convert Income to float
bike_buyers_df['Income'] = bike_buyers_df['Income'].astype(float)

# 3. Create Age Brackets
bins = [0, 18, 35, 50, 65, 100]
labels = ['<18', '18-35', '35-50', '50-65', '65+']
bike_buyers_df['Age Bracket'] = pd.cut(bike_buyers_df['Age'], bins=bins, labels=labels, right=False)

# Save the cleaned data to a new sheet
with pd.ExcelWriter(file_path, mode='a') as writer:
    bike_buyers_df.to_excel(writer, sheet_name='Cleaned Data', index=False)

# Display the first few rows of the cleaned dataframe
print(bike_buyers_df.head())
