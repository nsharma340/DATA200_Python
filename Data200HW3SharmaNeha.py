import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("Netflix Userbase.csv")

st.markdown("# Dataset Top 5")
#st.write("Dataset Top 5")
st.write(data.head())

st.title("Type of Device used by Netflix Users")
attribute_counts = data['Device'].value_counts()
st.bar_chart(attribute_counts)

st.title("Netflix Users across Countries")
country_counts = data['Country'].value_counts()
st.line_chart(country_counts, color = ['#FF0000'])


# Create a multiselect widget to select countries
st.markdown("## Select Country")
selected_countries = st.multiselect("Select countries", data['Country'])

# Filter the DataFrame based on the selected countries
filtered_data = data[data['Country'].isin(selected_countries)]

# Display the filtered data
st.write("Selected Data", filtered_data)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Plot value counts in a bar chart
if not filtered_data.empty:
    st.write("# Number of Netflix users by country")
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=filtered_data['Country'].value_counts().index, y=filtered_data['Country'].value_counts().values, data=filtered_data)
    #plt.xticks(rotation=45)
    st.pyplot()


if not filtered_data.empty:
    st.markdown("## Type of Device used by users filtered by Country")
    device_counts = filtered_data.groupby('Country')['Device'].value_counts().unstack(fill_value=0)
    st.bar_chart(device_counts, use_container_width=True)
