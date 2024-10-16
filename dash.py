import streamlit as st
import pandas as pd 
import plotly_express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Indicadores OC')

st.write('Unidade: São Francisco')

st.header('Visão Geral')
fig = go.Figure(go.Indicator(
    mode='gauge+number',
    value=95,
    title={'text':'Score'},
    domain={'x': [0,1], 'y': [0,1]},
    gauge={
        'axis':{'range':[0,100]}
    }
))
cl1, cl2 = st.columns(2)
with cl1:
    st.plotly_chart(fig)


st.header('Financeiro')
st.subheader('Faturamento')

c1, c2 = st.columns(2)

with c1:
    st.metric('Atual', value='63.000')
with c2:
    st.metric('Meta', value='150.000', delta="-87.000")

st.subheader('Venda/Dia')
c1, c2 = st.columns(2)
with c1:
    st.metric('Atual', value='5.250')
with c2:
    st.metric('Meta', value='7.250', delta='-2.000')

st.subheader('Ticket médio')
c1, c2 = st.columns(2)
with c1:
    st.metric('Atual', value='650')
with c2:
    st.metric('Meta', value='500', delta='100')

st.subheader('Conversão Valor')
c1, c2 = st.columns(2)
with c1:
    st.metric('Atual', value='25%')
with c2:
    st.metric('Meta', value='30%', delta='-10%')

st.subheader('Conversão Qauntidade')
c1, c2 = st.columns(2)
with c1:
    st.metric('Atual', value='70%')
with c2:
    st.metric('Meta', value='50%', delta='20%')

st.subheader('Projeção de venda')
c1, c2 = st.columns(2)
with c1:
    st.metric('Atual', value='126.000')
with c2:
    st.metric('Meta', value='150.000', delta='-24.000')