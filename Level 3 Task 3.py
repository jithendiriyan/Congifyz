#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[9]:


#the average ratings of different cuisines or cities using appropriate visualizations
# Bar plot for Average Rating of Different city
plt.figure(figsize=(12, 8))
average_ratings_by_cuisine = data.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=average_ratings_by_cuisine.values, y=average_ratings_by_cuisine.index, palette='viridis')
plt.title('Top 10 cities by Average Aggregate Rating')
plt.xlabel('Average Aggregate Rating')
plt.ylabel('Cuisines')
plt.show()


# In[14]:


# Bar plot for Average Rating of Different Cuisines
plt.figure(figsize=(12, 8))
average_ratings_by_cuisine = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=average_ratings_by_cuisine.values, y=average_ratings_by_cuisine.index, palette='viridis')
plt.title('Top 10 Cuisines by Average Aggregate Rating')
plt.xlabel('Average Aggregate Rating')
plt.ylabel('Cuisines')
plt.show()


# In[6]:


# Histogram for Aggregate Rating
plt.figure(figsize=(10, 6))
sns.histplot(data['Aggregate rating'], bins=20, kde=True)
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()


# In[12]:


# Scatter plot for Votes vs. Aggregate Rating
plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x='Votes', y='Aggregate rating', hue='Rating text', palette='deep')
plt.title('Votes vs. Aggregate Rating')
plt.xlabel('Votes')
plt.ylabel('Aggregate Rating')
plt.show()


# In[17]:


# Box plot for Price Range vs. Aggregate Rating
plt.figure(figsize=(10, 6))
sns.boxplot(x='Price range', y='Aggregate rating', data=data, palette='dark')
plt.title('Price Range vs. Aggregate Rating')
plt.xlabel('Price Range')
plt.ylabel('Aggregate Rating')
plt.show()


# In[ ]:




