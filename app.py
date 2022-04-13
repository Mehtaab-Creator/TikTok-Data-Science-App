#importing streamlit
import streamlit as st
#importing pandas to load data
import pandas as pd
#importing subprocess call method will allow us to run tiktokdata.py from commandline
from subprocess import call
#import plotly for viz
import plotly.express as px
import time

#input
hashtag = st.text_input('Search for a hashtag here', value="")

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

#button

if st.button('Get Data'):
    #run get data function here
    st.write(hashtag)
    call(['python3', 'tiktokdata.py', hashtag])
    st.success('This is a success message!')
    #load in existing data
        
    df = pd.read_csv('hashtag_data.csv')

    #visulisation

    fig = px.histogram(df, x='desc', y='stats_diggCount')
    st.plotly_chart(fig, use_container_width=True)

    #show tabular df in streamlit
    st.dataframe(df)