import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

data = pd.read_csv("Netflix Userbase.csv")

st.markdown("# Dataset Top 5")
#st.write("Dataset Top 5")
st.write(data.head())

###2. using the altair charts
st.title("Type of Device used by Netflix Users")
attribute_counts = data['Device'].value_counts().reset_index()
attribute_counts.columns = ['Device', 'Count']

c = alt.Chart(attribute_counts).mark_bar().encode(
    x='Device:O',  # Use 'O' for ordinal data (text)
    y='Count:Q',   # Use 'Q' for quantitative data (numeric)
    tooltip=['Device', 'Count']  # Display tooltips on hover
)

st.altair_chart(c, use_container_width=True)



###5. using the altair charts
st.title("Netflix Users across Countries")
country_counts = data['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

c = alt.Chart(country_counts).mark_line().encode(
    x='Country:O',  # Use 'O' for ordinal data (text)
    y='Count:Q',   # Use 'Q' for quantitative data (numeric)
    tooltip=['Country', 'Count']  # Display tooltips on hover
    #color = ['#FF0000']
)

st.altair_chart(c, use_container_width=True)



###7. Multiselect widget creation
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
    
