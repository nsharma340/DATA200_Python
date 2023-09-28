#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = pd.read_csv('retail_sales_dataset.csv')
df = pd.DataFrame(data)
st.title("Product category where most sales happened")
attribute_counts = data['Product Category'].value_counts().reset_index()
attribute_counts.columns = ['Product Category','Count']

c = alt.Chart(attribute_counts).mark_bar().encode(
    x = 'Product Category:O',
    y = 'Count:Q',
    tooltip = ['Product Category', 'Count']
)
st.altair_chart(c, use_container_width = True)

st.title("Shoppers according to Age")
attribute_age = data['Age'].value_counts().reset_index()
attribute_age.columns = ['Age','Count']

d = alt.Chart(attribute_age).mark_bar().encode(
    x = 'Age:O',
    y = 'Count:Q',
    tooltip = ['Age', 'Count']
)
st.altair_chart(d, use_container_width = True)


 
