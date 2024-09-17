#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import imblearn
import sklearn
from imblearn.over_sampling import SMOTE


# In[ ]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[ ]:


#Explore the dataset and identify the number of rows and columns.

rows,columns=data.shape
print(f'Total Rows:{rows}\nTotal Columns:{columns}')


# In[ ]:


#Check for missing values in each column and handle them accordingly.
missing_values=data.isnull()
missing_values


# In[ ]:


missing_values_sum=data.isnull().sum()
print("Missing values in each column:\n",missing_values_sum)


# In[ ]:


#checking the data type
data.dtypes


# In[ ]:


#converting data types
data['Restaurant ID'] = data['Restaurant ID'].astype('object')
data['Country Code'] = data['Country Code'].astype('float')
data['Average Cost for two'] = data['Average Cost for two'].astype('float')
data['Price range'] = data['Price range'].astype('object')
data['Votes'] = data['Votes'].astype('float')


# In[ ]:


#checking the datatypes
data.dtypes


# In[ ]:


#create the countplot for aggregate_rating
sns.countplot(x='Aggregate rating', data=data)
plt.title('Distribution of Aggregate Rating')
plt.xticks(rotation=90)# Rotate x-axis labels for better visibility
plt.show()


# In[ ]:


# Check for class imbalances
class_counts = data['Aggregate rating'].value_counts()
print("Class distribution:\n", class_counts)


# In[ ]:


# Apply SMOTE to balance classes
smote = SMOTE()
X, y = smote.fit_resample(data.drop(columns=['Aggregate rating']), data['Aggregate rating'])


# In[ ]:





# In[ ]:




