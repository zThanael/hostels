import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

import plotly.express as px
import plotly.graph_objects as go

# Internal Lib
import connections

# Importação do DataFrame
# Get Connection with Database

# Remover espaçamento no TOPO
st.markdown(" <style> div[class^='block-container'] { padding-top: 1rem; } </style> ", unsafe_allow_html=True)


st.markdown('''
<style>
    section.main > div {max-width:75rem}
</style>
''', unsafe_allow_html=True)


@st.cache_data
def get_main_df():
    con = connections.get_connection()
    # Create DataFrame
    df_raw = pd.read_sql('''
    select * from hostelworld_hostel hh  where "type" = 'HOSTEL' and country = 'Brazil'
    ''', con)
    con.dispose()

    return df_raw

# Get the DataFrame
df = get_main_df()


with st.sidebar:
    st.html('''
    <ul>
        <li> Newsletter </li>
        <li> Linkedin </li>
        <li> Instagram </li>
        <li> GitHub </li>
    </ul>
    ''')



st.title('Search Hostel')

col1, col2 = st.columns([0.25, 0.75], gap = "medium")


with col1:
    st.html('<br><br>')
    # Select
    country = col1.selectbox(
        label = "Selecione um Pais: ",
        options = (df['country'].sort_values().unique()),
        index = None
    )

    st.html('<br>')
    # Select
    state = col1.selectbox(
        label = "Selecione um Estado: ",
        options = ('Santa Catarina','Paraná','Ceara'),
        index = None
    )
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

    # FOLIUM 
    # col2.text('# Mapa')

    # lat_avg = df['latitude'].mean()
    # lon_avg = df['longitude'].mean()

    # m = folium.Map(
    #     location = [lat_avg, lon_avg],
    #     zoom_start = 10 if city else 3.3
    # )

    # for _, row in df.iterrows():
    #     folium.Marker(
    #         [row['latitude'], row['longitude']],
    #         popup = row['name']
    #     ).add_to(m)

    # events = st_folium(m,  width=725)
    px.set_mapbox_access_token(open(".mapbox_token").read())

    fig = px.scatter_mapbox(df,
                            lat='latitude',
                            lon='longitude',
                            hover_name="name",
                            zoom = 12 if city else 2.2
    )


    fig.update_layout(height=500, width= 800)

    st.plotly_chart(fig, use_container_width=True)


st.title("Hostel List")

df_view = df[['name','city','country','qtd_rating','url']].sort_values(by = 'qtd_rating', ascending = False)
st.dataframe(df_view)