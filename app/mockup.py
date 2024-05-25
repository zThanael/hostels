import streamlit as st
import folium
import pandas as pd
import numpy as np
from streamlit_folium import st_folium

import plotly.express as px
import plotly.graph_objects as go

from sqlalchemy import create_engine

# Internal Lib
#import connections

# Importação do DataFrame
# Get Connection with Database

# Ajustes do CSS

# Remover espaçamento no TOPO
st.markdown(" <style> div[class^='block-container'] { padding-top: 1rem; } </style> ", unsafe_allow_html=True)

# Remover espaçamento lateral
st.markdown('''
<style>
    section.main > div {max-width:75rem}
</style>
''', unsafe_allow_html=True)


# Set Color Map
colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred','lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 
'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

list_color = []
list_comprehension = [list_color.extend([color]*10) for color in colors]

nums = []
list_comprehension = [nums.extend(np.arange(0,10)) for i in range(len(colors))]

df_color = pd.DataFrame({'color': list_color, 'num_icon':nums})
df_color = df_color.reset_index()



@st.cache_data
def get_main_df():

    con = create_engine("postgresql+psycopg2://leitor:leitor123@personal.cxe0iuo8g20s.us-east-1.rds.amazonaws.com:5432/postgres")
    # Create DataFrame
    df_raw = pd.read_sql('''
    select * from hostelworld_hostel hh  where "type" = 'HOSTEL' --and country = 'Brazil'
    ''', con)
    con.dispose()

    return df_raw

# Get the DataFrame
df = get_main_df()

# SideBar
# with st.sidebar:
#     st.html('''
#     <ul>
#         <li> Newsletter </li>
#         <li> Linkedin </li>
#         <li> Instagram </li>
#         <li> GitHub </li>
#     </ul>
#     ''')


title1, title2 = st.columns([0.85, 0.15], gap = "large")
with title1:
    title1.title('Search Hostel')

with title2:
    title2.html('<br>')
    title2.link_button("Newsletter", "https://thanael.substack.com/", type='primary')
    title2.html('<br>')


col1, col2 = st.columns([0.25, 0.75], gap = "large")


with col1:
    st.html('<br><br>')
    # Select
    continent = col1.selectbox(
        label = "Selecione um Continente: ",
        options = (df['continent'].sort_values().unique()),
        index = None
    )

    if continent != None:
        df = df[df['continent'] == continent]

    st.html('<br>')
    # Select
    country = col1.selectbox(
        label = "Selecione um Pais: ",
        options = (df['country'].sort_values().unique()),
        index = None
    )

    if country != None:
        df = df[df['country'] == country]

    st.html('<br>')
    # Select
    city = col1.selectbox(
        label = "Selecione uma Cidade: ",
        options = (df['city'].sort_values().unique()),
        index = None
    )
    st.html('<br>')

    if city != None:
        df = df[df['city'] == city]

with col2: 

    if city == None or country == None:
        fig = px.scatter_mapbox(df,
                            lat='latitude',
                            lon='longitude',
                            hover_name="name",
                            zoom = 12 if city else 2.2
        )


        fig.update_layout(height=500, width= 800)

        st.plotly_chart(fig, use_container_width=True)

    else:

        # Criar colunas de cores.
        df = df.sort_values(by = 'qtd_rating', ascending = False)
        df = df.reset_index()
        df = df.merge(df_color[['color','num_icon']], how='left', left_index=True, right_index=True)

        # FOLIUM
        lat_avg = df['latitude'].mean()
        lon_avg = df['longitude'].mean()

        m = folium.Map(
            location = [lat_avg, lon_avg],
            zoom_start = 10 if city else 3.3
        )

        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred','lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

        for _, row in df.iterrows():
            folium.Marker(
                [row['latitude'], row['longitude']],
                tooltip = row['name'],
                icon=folium.Icon(icon=f"{row['num_icon']}", prefix='fa', color=f"{row['color']}")
            ).add_to(m)

        events = st_folium(m,  width=800, height = 500)

        px.set_mapbox_access_token(open(".mapbox_token").read())



if city != None :
    st.title("Hostel List")
    df_view = df[['name','city','country','qtd_rating','color','num_icon','url']].sort_values(by = 'qtd_rating', ascending = False)

    st.data_editor(
        df_view,
        column_config={
            "url": st.column_config.LinkColumn(
                "HostelWorld", display_text="Link"
            ),
        },
        hide_index=True,
    )