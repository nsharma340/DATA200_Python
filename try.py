import streamlit as st
import pandas as pd
import seaborn as sns
data = pd.read_csv("Netflix Userbase.csv")
data.head()
data.info()
data.shape
data.describe()
data.describe(include = 'all')
sns.histplot(x= data.Device).set(title='Type of Device used by people')
device = data['Device'].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Type of Device used by people")
device.set_xlabel("Device")
device.set_ylabel("Frequency")
ax = data['Country'].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Users of Netflix in different countries")
ax.set_xlabel("Country")
ax.set_ylabel("Frequency")
st.title("Type of Device used by people")
attribute_counts = data['Device'].value_counts()
st.bar_chart(attribute_counts)




