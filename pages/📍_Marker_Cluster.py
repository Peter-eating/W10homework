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

st.title("KINMEN Air-Raid Shelter")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[24.445748, 118.377391], zoom=4)
        cities = "https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN%20Air-Raid%20Shelter.csv"
        regions = "https://github.com/Peter-eating/W10homework/raw/refs/heads/main/KINMEN.shp"

        m.add_geojson(regions, layer_name="鄉鎮區界")
        m.add_points_from_xy(
            cities,
            x="經度",
            y="緯度",
            color_column="轄管分局",
            icon_names=["gear", "map"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
