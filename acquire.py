#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
from env import host, user, password


# In[2]:


def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[3]:


# Titanic    
    
def get_titanic_data():
    sql_query = 'SELECT * FROM passengers'
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    return df


# In[6]:


titanic = get_titanic_data()
titanic.head()


# In[7]:


titanic.to_csv('titanic_df.csv')


# In[12]:


def get_iris_data():
    sql_query = """
               SELECT species_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species
                USING(species_id)
                """
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    return df


# In[13]:


iris = get_iris_data()
iris.head()


# In[14]:


iris.to_csv('iris_df.csv')


# In[18]:


def get_telco_data():
    sql_query = """
                SELECT * FROM customers
                JOIN contract_types
                USING(contract_type_id)
                JOIN  internet_service_types
                USING(internet_service_type_id)
                JOIN payment_types
                USING(payment_type_id)
                """
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df


# In[19]:


telco = get_telco_data()
telco.head()


# In[20]:


telco.to_csv('telco_df.csv')


# In[ ]:




