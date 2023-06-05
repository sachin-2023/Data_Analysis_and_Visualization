#!/usr/bin/env python
# coding: utf-8

# # Clustering with K-means

# In[ ]:


import pandas as pd
from sklearn.cluster import KMeans

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(data)

# Print cluster labels
print("Cluster Labels:", clusters)

