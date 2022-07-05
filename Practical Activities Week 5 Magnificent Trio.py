#!/usr/bin/env python
# coding: utf-8

# ### Week 5 Practical Activities

# # 5.3.1 Practical activity: The magnificent trio

# ## 1. Prepare Notebook

# In[3]:


# Import necessary libraries. 
import numpy as np
import pandas as pd

# Load the database and create the DataFrame.
transport_costs = pd.read_excel('transport_costs.xlsx')
print(f'transport_costs has {transport_costs.shape[1]} columns, and {transport_costs.shape[0]} rows.')
print(f'It has the following columns: \n{transport_costs.columns}')


# In[4]:


transport_costs.head()


# In[7]:


# Subset to drop currency and distance unit. 
transport = transport_costs[['region', 'country', 'port', 
                             'sea freight cost',
                             'road transport cost per km']]
transport


# ## 2. Calculations

# In[8]:


# Create two functions to calculate:
#total_sea_freight_costs
def tsfc(x):
    """Calculates the total_sea_freight_cost as =
    sea freight cost x 2 x 4 """
    y = x * 8
    return y

# total_road_transport_cost. 
def trtc(x):
    """Calculates the total_road_transport_cost = 
    road transport cost x 10000 """
    y = x * 10000
    return y


# In[12]:


transport['total_sea_freight_cost'] = tsfc(transport['sea freight cost'])
transport['total_road_transport_cost'] = trtc(transport['road transport cost per km'])

# View the DataFrame.
transport


# In[16]:


#  Calculate the total_export_costs.  
transport['total_export_costs'] = transport['total_sea_freight_cost'] + transport['total_road_transport_cost']


# In[18]:


# Reorder transport DataFrame and add columns.  

transport = transport[['region', 'country', 'port', 'sea freight cost',
                             'road transport cost per km', 'total_sea_freight_cost',
                             'total_road_transport_cost', 'total_export_costs']]
transport.head()


# In[21]:


# Save output as csv file. 
transport.to_csv('python_transport.csv', index=False)


# ## 3. Cost of Exports per Region

# In[20]:


# Cost of exports per Region
region_export_cost = transport.groupby(['region'])['total_export_costs'].sum()
region_export_cost


# ----
