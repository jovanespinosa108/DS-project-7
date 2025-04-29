import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis de Vehiculos Usados en USA')

hist_button = st.checkbox('Crea Histograma del Tipo de Vehiculos')

if hist_button:
    st.subheader('Distribucion de tipos de vehiculos')
    st.write('Este Histograma mustra cuantos vehiculos hay de cada typo.')

    # Crear histograma
    fig = px.histogram(car_data, x='type')

    # Muestra grafico
    st.plotly_chart(fig, use_container_width=True)

# Crea un boton para un grafico de dispersion usando checkbox
scatter_plot_button = st.checkbox('Mostrar grafico de dispersion por año y modelo')

if scatter_plot_button:
    st.subheader('Condicion de los vehiculos segun su año de modelo')
    st.write('Creacion de grafico de dispersion para ver la condicion de los autos en base a su año de modelo')

    # Crea Grafico de dispersion
    fig_2 = px.scatter(
        car_data,
        x='model_year',
        y='condition',
        color='condition',
        hover_name='model'
        )

    # Muestra el grafico
    st.plotly_chart(fig_2, use_container_width=True)

if st.checkbox('Crea pie plot de'):
    st.write("Este grafico de pastel muestra los autos Automaticos, Manuales, etc.")

    fig = px.pie(car_data, names='transmission', title='Tipos de transmision de vehiculos')
    st.plotly_chart(fig)

if st.checkbox('Crea grafico de barras de combustible'):
    st.write('Muestra que combustibles son mas usados (gasolina, diesel, electrico, etc)')

    fig = px.bar(
        car_data['fuel'].value_counts().reset_index(),
        x='count',
        y='fuel',
        labels={'index': 'Tipo de Combustible', 'fuel': 'Cantidad'},
        title='Distribucion de tipo de combustible'
    )

    st.plotly_chart(fig)


if st.checkbox('Crea Boxplot de precio en base a condicion'):
    st.write('Muestra la variacion de precio de los autos en base a su condicion')

    fig = px.box(car_data,
                 x='condition',
                 y='price',
                 title='Distribucion de precios segun condicion')
    
    st.plotly_chart(fig)
