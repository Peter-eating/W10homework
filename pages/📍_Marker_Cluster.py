import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv"

        m.add_points_from_xy(
            cities,
            x="緯度",
            y="經度",
            spin=True,
            layer_name='金門防空避難設施'
        )

m.to_streamlit(height=700)
