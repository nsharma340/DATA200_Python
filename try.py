#!/usr/bin/env python
# coding: utf-8

# In[48]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[49]:


data = pd.read_csv("Netflix Userbase.csv")


# In[50]:


data.head()


# In[51]:


data.info()


# In[52]:


data.shape


# In[53]:


data.describe()


# In[54]:


data.describe(include = 'all')


# In[60]:


sns.histplot(x= data.Device).set(title='Type of Device used by people')


# In[65]:


device = data['Device'].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Type of Device used by people")
device.set_xlabel("Device")
device.set_ylabel("Frequency")


# In[64]:


ax = data['Country'].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Users of Netflix in different countries")
ax.set_xlabel("Country")
ax.set_ylabel("Frequency")


# In[69]:


st.title("Type of Device used by people")
attribute_counts = data['Device'].value_counts()
st.bar_chart(attribute_counts)

