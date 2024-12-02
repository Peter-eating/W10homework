import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("csv")

csv_url = "https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv"
response = requests.get(csv_url)
csv_data = response.text  
df = pd.read_csv(StringIO(csv_data))
st.dataframe(df)
