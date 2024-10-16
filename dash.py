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
#st.subheader('Faturamento')

c1, c2, c3 = st.columns(3)

with c1:
    st.metric('Faturamento', value='63.000', delta="-87.000")
    st.metric('Conversão Valor', value='25%', delta='-10%')
with c2:
    st.metric('Vendas/Dia', value='5.250', delta='-2.000')
    st.metric('Conversão Quantidade', value='70%', delta='20%')
with c3:
    st.metric('Ticket Médio', value='650', delta='100')
    st.metric('Projeção de venda', value='126.000', delta='-24.000')

st.divider()
st.header('Boletos')
c1, c2 = st.columns(2)
with c1:
    labels = ['Boleto', 'Outros']
    values = [60,40]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig)

c1, c2, c3 = st.columns(3)
with c1:
    st.metric('Total a receber', value='500.000,00')
with c2:
    st.metric('Média Recebimentos', value='20.000,00')
with c3:
    st.metric('Prazo médio (meses)', value='25', delta='-17')

st.divider()

st.header('Marketing')
