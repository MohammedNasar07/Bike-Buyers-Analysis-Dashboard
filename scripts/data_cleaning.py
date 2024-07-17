import pandas as pd

# Load the data
file_path = '../Bike_Buyers_Analysis.xlsx'  # Adjust the path if necessary
bike_buyers_df = pd.read_excel(file_path, sheet_name='bike_buyers')

# Display the first few rows of the dataframe
print(bike_buyers_df.head())
