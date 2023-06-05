import pandas as pd
import seaborn as sns

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Perform EDA
# Example: Calculate descriptive statistics
statistics = data.describe()

# Example: Calculate correlation matrix
correlation_matrix = data.corr()

# Example: Visualize correlation matrix
sns.heatmap(correlation_matrix, annot=True)
