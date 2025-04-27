import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("./vehicles_us.csv")
st.image('https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png', width=250)
st.image('https://cdn-icons-png.flaticon.com/512/3523/3523063.png', width=100)

st.divider()
st.header('Análisis de Datos de Vehículos en Venta')
st.write('¡Hola! 🚀 Usa los botones de abajo para construir gráficos y explorar los datos de los autos.')
st.divider()

option = st.selectbox('Selecciona la columna para el histograma', car_data.columns)

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Histograma para el conjunto de datos de anuncios de ventas de coches')
    fig = px.histogram(car_data, x=option)
    st.plotly_chart(fig, use_container_width=True)

# if hist_button:
#     st.write('Histograma para el conjunto de datos de anuncios de ventas de coches')
#     fig = px.histogram(car_data, x='odometer')

#     st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')
if disp_button:
    st.write('Gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

st.write('Autor: Heber Ramos (¡Emilio para los amigos! 🦖)')

