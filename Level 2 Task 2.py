#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[6]:


# the most common price range among all the restaurants
common_price_range = data['Price range'].value_counts().idxmax()
print("Most Common Price Range:",common_price_range)


# In[8]:


# the average rating for each price range.
avg_price_range = data.groupby('Price range')['Aggregate rating'].mean()
print("\nAverage Rating for Each Price Range:\n", avg_price_range)


# In[10]:


# Identify the price range with the highest average rating
highest_avg_rating_price_range = avg_price_range.idxmax()
highest_avg_rating = avg_price_range.max()


# In[13]:


# Find the corresponding rating color for the highest average rating price range
highest_rating_color = data[data['Price range'] == highest_avg_rating_price_range]['Rating color'].mode()[0]

print("\nPrice Range with the Highest Average Rating:", highest_avg_rating_price_range)
print("Highest Average Rating:", highest_avg_rating)
print("Color Representing the Highest Rating:", highest_rating_color)



# In[ ]:




