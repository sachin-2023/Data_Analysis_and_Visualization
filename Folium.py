import pandas as pd
import folium

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Create a map with markers
map = folium.Map(location=[latitude, longitude], zoom_start=10)
for index, row in data.iterrows():
    folium.Marker(location=[row['lat'], row['lon']], popup=row['name']).add_to(map)
map.save('map.html')
