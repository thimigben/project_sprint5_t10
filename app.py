import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles.csv')

st.header('Portal de Análise de Veículos')

# Checkbox para o Histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para o Gráfico de Dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão para preço vs quilometragem')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
