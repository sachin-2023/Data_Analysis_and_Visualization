import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Perform data cleaning and preprocessing
# Example: Handle missing values
data = data.dropna()

# Example: Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data)
