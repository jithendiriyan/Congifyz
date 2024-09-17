#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the libraries
import pandas as pd


# In[6]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
df=data


# In[14]:


# Length of the restaurant name
df['Name Length'] = df['Restaurant Name'].apply(len)


# In[12]:


# Length of the address
df['Address Length'] = df['Address'].apply(len)
print("Sample of new features:\n", df[['Restaurant Name', 'Name Length', 'Address', 'Address Length']].head())


# In[10]:


# Encode 'Has Table booking' as binary
df['Has Table Booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)


# In[8]:


# Encode 'Has Online delivery' as binary
df['Has Online Delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)
print("\nSample of encoded features:\n", df[['Has Table booking', 'Has Table Booking', 'Has Online delivery', 'Has Online Delivery']].head())


# In[ ]:


# Encode 'Has Table booking' as binary
df['Has Table Booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)

