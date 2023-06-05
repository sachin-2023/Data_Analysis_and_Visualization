#!/usr/bin/env python
# coding: utf-8

# # Dimentionality Reduction with Principal Component Analysis

# In[ ]:


import pandas as pd
from sklearn.decomposition import PCA

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Perform PCA
pca = PCA(n_components=2)
transformed_data = pca.fit_transform(data)

# Print explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

