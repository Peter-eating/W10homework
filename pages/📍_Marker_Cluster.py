import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np
import geopandas as gpd


markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")
with col2:

    basemap = st.selectbox("Select a basemap:", options, index)

TW_fishing=gpd.read_file('https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv')

with st.expander("See source code"):
    
    with st.echo():
        with col1:

            m = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
            )
            m.add_basemap(basemap)
            m.add_points_from_xy(TW_fishing,
                          x="經度",
                          y="緯度",
                          spin=True,
                          add_legend=True,
                          layer_name='全台開放釣點')
            m.to_streamlit(height=700)
st.dataframe(TW_fishing)
