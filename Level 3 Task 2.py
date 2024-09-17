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


# In[4]:


#Analyze the Relationship Between Cuisine and Rating
cuisine_ratings = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)


# In[5]:


print(cuisine_ratings.head(10))


# In[8]:


# Plot average rating by cuisine (top 10)
plt.figure(figsize=(12, 8))
top_cuisines_by_rating = cuisine_ratings.head(10)
sns.barplot(x=top_cuisines_by_rating.values, y=top_cuisines_by_rating.index, palette='mako')
plt.title('Top 10 Cuisines by Average Rating')
plt.xlabel('Average Aggregate Rating')
plt.ylabel('Cuisine')
plt.show()


# In[9]:


#Identify Most Popular Cuisines Based on Votes
cuisine_votes = data.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)


# In[10]:


print(cuisine_votes.head(10))


# In[11]:


# Plot total votes by cuisine (top 10)
plt.figure(figsize=(12, 8))
top_cuisines_by_votes = cuisine_votes.head(10)
sns.barplot(x=top_cuisines_by_votes.values, y=top_cuisines_by_votes.index, palette='viridis')
plt.title('Top 10 Cuisines by Total Votes')
plt.xlabel('Total Votes')
plt.ylabel('Cuisine')
plt.show()


# In[15]:


# Combine rating and votes data for top cuisines
data= pd.DataFrame({
    'Average Rating': cuisine_ratings.head(10),
    'Total Votes': cuisine_votes.head(10)
}).reset_index()

# Plot average rating vs. total votes
plt.figure(figsize=(14, 8))
sns.scatterplot(x='Total Votes', y='Average Rating', data=data, hue='Cuisines', s=100, palette='Set2')
plt.title('Cuisine Analysis: Average Rating vs. Total Votes')
plt.xlabel('Total Votes')
plt.ylabel('Average Rating')
plt.legend(title='Cuisines', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# In[ ]:




