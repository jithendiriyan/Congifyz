#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install folium


# In[5]:


#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap


# In[6]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[7]:


# Create a base map
map_restaurants = folium.Map(location=[20, 0], zoom_start=2)


# In[10]:


# Add restaurant locations as points on the map
for _, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name'],
    ).add_to(map_restaurants)


# In[12]:


map_restaurants


# In[16]:


# Distribution of restaurants by country
country_distribution = data['Country Code'].value_counts()
country_distribution.plot(kind='bar', color='red')
plt.title('Distribution of Restaurants by Country')
plt.xlabel('Country Code')
plt.ylabel('Number of Restaurants')
plt.show()


# In[18]:


# Distribution of restaurants by city
city_distribution = data['City'].value_counts().head(20)
city_distribution.plot(kind='bar', color='brown')
plt.title('Top 20 Cities with Most Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[20]:


# Scatter plot to visualize the relationship between Latitude/Longitude and Rating
# Latitude vs Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Latitude'], y=data['Aggregate rating'])
plt.title('Latitude vs Aggregate Rating')
plt.xlabel('Latitude')
plt.ylabel('Aggregate Rating')
plt.show()


# In[22]:


# Longitude vs Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Longitude'], y=data['Aggregate rating'])
plt.title('Longitude vs Aggregate Rating')
plt.xlabel('Longitude')
plt.ylabel('Aggregate Rating')
plt.show()


# In[24]:


# Calculate correlation
correlation_latitude = data['Latitude'].corr(data['Aggregate rating'])
correlation_longitude = data['Longitude'].corr(data['Aggregate rating'])

print(f"Correlation between Latitude and Rating: {correlation_latitude}")
print(f"Correlation between Longitude and Rating: {correlation_longitude}")


# In[ ]:




