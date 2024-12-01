import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)
        cities = "https://raw.githubusercontent.com/Peter-eating/W10homework/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv"
        regions = "https://github.com/8048-kh/test/raw/refs/heads/main/REGION.shp"

        m.add_shp(regions, layer_name="Aboriginal Tribes")
        m.add_points_from_xy(
            cities,
            x="緯度",
            y="經度",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
