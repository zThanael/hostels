import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import connections

# Get Connection with Database
con = connections.get_connection()

@st.cache_data
def get_main_df():
  # Create DataFrame
  df_raw = pd.read_sql('''
  select * from hostelworld_hostel hh  where "type" = 'HOSTEL' --and country = 'Brazil'
  ''', con)

  return df_raw

df_raw = get_main_df()

df = df_raw.copy()

# Streamlit Commands
st.text('# Search Hostel')

# Testing SelectBox
country = st.selectbox(
    label = "Selecione um Pais: ",
    options = (df['country'].sort_values().unique()),
    index = None
)

if country != None:
    df = df[df['country'] == country]


# Testing SelectBox
city = st.selectbox(
    label =  "Selecione uma cidade: ",
    options = (df['city'].sort_values().unique()),
    index = None
)

if city != None:
    df = df[df['city'] == city]


#df_map = df[df['city']==city]

# Create Map
#st.map(data=df_map, latitude='latitude', longitude='longitude', color=None, size=15, zoom=None, use_container_width=True)


px.set_mapbox_access_token(open(".mapbox_token").read())

fig = px.scatter_mapbox(df,
                        lat='latitude',
                        lon='longitude',
                        hover_name="name",
                        zoom = 10 if city else 2.2
)



#fig.show()

st.plotly_chart(fig)
