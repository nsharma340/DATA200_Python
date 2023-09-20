#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
toy = pd.read_csv('toy_dataset.csv')
df = pd.DataFrame(toy)
X = list(df.iloc[:, 2])
Y = list(df.iloc[:, 4])
#Plot the data using bar() method
plt.bar(X, Y, color = 'b')
plt.title("Gender vs illness variation")
plt.xlabel("Gender")
plt.ylabel("illness")

#show the plot
plt.show()

