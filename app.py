import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("./vehicles_us.csv")
st.header('Mi primera app web con python')
st.write('Esta app aún no es funcional. Está en construcción...')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')
if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

