import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("KINMEN Air-Raid Shelters")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[24.441831, 118.353515], zoom=4)
        cities = "https://raw.githubusercontent.com/Peter-eating/W10homework/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv"
        regions = "https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN.shp"

        m.add_shp(regions, layer_name="KINMEN")
        m.add_points_from_xy(
            cities,
            x="經度",
            y="緯度",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
            
        )

m.to_streamlit(height=700)
