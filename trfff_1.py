import streamlit as st
import pandas as pd
import seaborn as sns
data = pd.read_csv("Netflix Userbase.csv")

st.title("Type of Device used by people")
attribute_counts = data['Device'].value_counts()
st.bar_chart(attribute_counts)

st.title("Type of Device used by people")
country_counts = data['Country'].value_counts()
st.line_chart(country_counts, color = ['#FF0000'])
