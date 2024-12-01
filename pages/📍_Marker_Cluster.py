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

        m = leafmap.Map(center=[24.445033, 118.375672], zoom=4)
        cities = "https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv"
        regions = "https://github.com/8048-kh/test/raw/refs/heads/main/REGION.shp"

        m.add_shp(regions, layer_name="Aboriginal Tribes")
        m.add_points_from_xy(
            cities,
            x="緯度",
            y="經度",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
        )

m.to_streamlit(height=700)
