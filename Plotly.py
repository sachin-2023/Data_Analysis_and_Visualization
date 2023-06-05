#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly.express as px

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Create an interactive scatter plot
fig = px.scatter(data, x='x', y='y', color='category', hover_data=['label'])
fig.show()

