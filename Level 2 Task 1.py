#!/usr/bin/env python
# coding: utf-8

# In[9]:


#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[11]:


# the percentage of restaurants that offer table booking.
table_booking_percentage = data['Has Table booking'].value_counts(normalize=True) * 100
print("Table Booking Availability (Percentage):\n", table_booking_percentage)


# In[12]:


#the percentage of restaurants that offeronline delivery
online_delivery_percentage = data['Has Online delivery'].value_counts(normalize=True) * 100
print("\nOnline Delivery Availability (Percentage):\n", online_delivery_percentage)


# In[13]:


#Compare the average ratings of restaurants with table booking and those without.
avg_table_booking = data.groupby('Has Table booking')['Aggregate rating'].mean()
print("\nAverage Rating Comparison (With vs Without Table Booking):\n", avg_table_booking)


# In[14]:


# Analyze the availability of online delivery among restaurants with different price ranges
online_delivery_price_range = data.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100
print("\nOnline Delivery Availability by Price Range (Percentage):\n", online_delivery_price_range)

# Optional: Visualize the results with a bar plot
online_delivery_price_range.plot(kind='bar', stacked=True, color=['lightblue', 'lightgreen'])
plt.title('Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage')
plt.legend(title='Online Delivery', labels=['No', 'Yes'])
plt.xticks(rotation=0)
plt.show()


# In[ ]:




