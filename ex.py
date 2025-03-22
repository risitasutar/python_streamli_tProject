import streamlit as st
import pandas as pd
from click import option
from streamlit import button

df=pd.read_csv('startup_cleaned.csv')

def load_investor_details(investor):
    st.title(investor)


st.sidebar.title('Startup Funding Analysis')

options =st.sidebar.selectbox('Select one',['Overall Analysis','StartUp','Investor'])

if options== 'Overall Analysis':
    st.title('Overall Analysis')
elif options=='StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    btn1= st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')

else:
    selected_investor=st.sidebar.selectbox('Select StartUp',sorted(set(df['investors'].str.split(',').sum())))
    btn2= st.sidebar.button('Find Investors Details')
    if btn2:
        load_investor_details(selected_investor)
    st.title('Investor Analysis')