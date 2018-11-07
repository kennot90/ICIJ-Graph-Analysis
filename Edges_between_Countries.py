
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


# In[2]:


home_dir = os.getcwd()
data_folder = '//all_data//'
entities = 'Entities.csv'


# In[3]:


dir = home_dir + data_folder + entities
print(dir)
df = pd.read_csv(dir, dtype = str)


# In[4]:


df.shape


# # This is on the Entities as stated in the Panama Papers.

# In[5]:


df.head()


# # Deciding which columns to choose
# 
# To do an inital exploration, I have only chosen the Jurisdiction_description as well as country.
# Jurisdiction_description means 'the official power to make legal decisions and judgements.'
# With this, I assume that the company lies in the particular country
# "Country" means where the country operates.

# In[6]:


df_edges = df[['name','jurisdiction_description', 'countries', 'incorporation_date','inactivation_date', 'address']]


# # Check for Duplicate Records

# In[7]:


df_2 = df_edges[df_edges.duplicated(subset = ['name','jurisdiction_description', 'countries', 'incorporation_date','inactivation_date', 'address'], 
                        keep = False)]


# In[8]:


df_edges = df_edges.drop_duplicates(subset = ['name','jurisdiction_description', 'countries', 'incorporation_date','inactivation_date', 'address']
                        ,keep = 'first')


# In[9]:


df_edges


# In[10]:


df_edges = df_edges[['jurisdiction_description', 'countries']]


# In[11]:


df_edges.jurisdiction_description.unique()


# In[12]:


df_edges.countries.unique()


# # Identifying the weird values in the columns itself.
# 
# From this, we identified that 
# 
# Under Jurid, we have weird values such as 
# -  'Recorded in leaked files as "fund"'
# -   'Undetermined'
# 
# Under countries, we have 
# 
# - A lot of values with the ';' which is a combination of countries
# - 'Not identified'
# - NaN
# 
# 
# We will remove all these

# In[13]:


df_edges = df_edges.dropna()
df_edges = df_edges[ df_edges['jurisdiction_description'] != 'Undetermined']
df_edges = df_edges[ df_edges['jurisdiction_description'] !=  'Recorded in leaked files as "fund"']
df_edges = df_edges[~df_edges['countries'].str.contains(';')]
df_edges = df_edges[ df_edges['countries'] != 'Not identified']


# # Grouping them into countries together

# In[15]:


df_edges


# In[17]:


df_edges_overall = df_edges.groupby(['jurisdiction_description', 'countries']).size().reset_index(name = 'Freq')


# In[21]:


df_edges_overall.columns = ['target', 'source', 'weight']
#jurisdiction_description = target
#countries = source


# In[19]:


df_edges_overall


# # It is interesting to note that there are sizeable amount of self loops
# 
# Eg. Bahamas to Bahamas 400 records 

# In[23]:


df_edges_overall.to_csv('edgesbetweencountries_no_same_count.csv', index = False)

