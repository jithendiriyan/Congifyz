#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[4]:


#Calculate basic statistical measures (mean,median, standard deviation, etc.) for numerical columns.
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
descriptive_stats = data[numerical_columns].describe()


# In[6]:


descriptive_stats


# In[7]:


categorical_columns = ['Country Code', 'City', 'Cuisines']
for col in categorical_columns:
    print(data[col].value_counts())


# In[10]:


# Top Cuisines
top_cuisines = data['Cuisines'].value_counts().head(10)
print("Top Cuisines:\n", top_cuisines)


# In[9]:


# Top Cities
top_cities = data['City'].value_counts().head(10)
print("Top Cities:\n", top_cities)


# In[19]:


sns.histplot(data['Aggregate rating'], kde=True)
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()


# In[20]:


# Bar plot for top cuisines
top_cuisines.plot(kind='bar', color='skyblue')
plt.title('Top 10 Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[21]:


# Bar plot for top cities
top_cities.plot(kind='bar', color='orange')
plt.title('Top 10 Cities with Most Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[ ]:




