import streamlit as st
import pandas as pd 
import plotly_express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide', page_title='Indicadores OC')

st.subheader('Unidade: São Francisco')
st.header('Score da Unidade')
fig = go.Figure(go.Indicator(
    mode='gauge+number',
    value=95,
    title={'text':'Score'},
    gauge={
        'axis':{'range':[0,100]}
    }
))

st.plotly_chart(fig)

st.header('Financeiro')
st.subheader('Faturamento')
c1, c2 = st.columns(2)
with c1:
    st.metric('Atual', value='63.000')
with c2:
    st.metric('Meta', value='150.000', delta="-87.000")