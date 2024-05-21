import streamlit as st
import pandas as pd
import plotly.express as px
import connections

# Get Connection with Database
con = connections.get_connection()

# Create DataFrame
df = pd.read_sql('''
select * from hostelworld_hostel hh  where country = 'Brazil' 
''', con)


# Streamlit Commands
st.title('Search Hostel')

# Testing SelectBox
city = st.selectbox(
    "How would you like to be contacted?",
    (df['city'].unique())
)

st.text(city)

df_map = df[df['city']==city]

# Create Map
#st.map(data=df_map, latitude='latitude', longitude='longitude', color=None, size=15, zoom=None, use_container_width=True)

px.set_mapbox_access_token(open(".mapbox_token").read())

# fig = px.scatter_mapbox(df_map, ,
#                             lat='latitude', lon='longitude',
#                             color='type', size=None,
#                             color_continuous_scale=px.colors.cyclical.IceFire,
#                             zoom = 2
#                             )
# fig.update_traces(textposition='top center')

fig = px.scatter_mapbox(df_map,
                        lat='latitude',
                        lon='longitude',
                        hover_name="name",
                        color='type',
                     #   zoom=2
                       )


st.plotly_chart(fig)
