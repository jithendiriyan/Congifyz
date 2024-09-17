#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


# In[2]:


#load the dataset
data=pd.read_csv(r"E:\Congifyz\Dataset .csv")
data


# In[3]:


# Handle missing values
data = data.dropna(subset=['Cuisines'])


# In[5]:


# Encode categorical variables
categorical_columns = ['City', 'Cuisines', 'Currency', 'Has Table booking','Has Online delivery', 'Is delivering now', 'Switch to order menu', 'Rating color', 'Rating text']
label_encoders = {}
for column in categorical_columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le


# In[6]:


# Split the data into features and target variable
X = data.drop(columns=['Restaurant ID', 'Restaurant Name', 'Address', 'Locality', 'Locality Verbose', 'Aggregate rating'])
y = data['Aggregate rating']


# In[7]:


# Normalize/Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# In[8]:


# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# In[9]:


# Train and evaluate models
def evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


# In[10]:


# Linear Regression
linear_reg = LinearRegression()
mse_linear, r2_linear = evaluate_model(linear_reg, X_train, y_train, X_test, y_test)
print(f"Linear Regression - MSE: {mse_linear}, R²: {r2_linear}")


# In[11]:


# Decision Tree Regressor
tree_reg = DecisionTreeRegressor(random_state=42)
mse_tree, r2_tree = evaluate_model(tree_reg, X_train, y_train, X_test, y_test)
print(f"Decision Tree - MSE: {mse_tree}, R²: {r2_tree}")


# In[12]:


# Compare model performances
print("\nModel Comparison:")
print(f"Linear Regression - MSE: {mse_linear}, R²: {r2_linear}")
print(f"Decision Tree - MSE: {mse_tree}, R²: {r2_tree}")
print(f"Random Forest - MSE: {mse_forest}, R²: {r2_forest}")


# In[ ]:




