# Importamos librerias
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargamos datos
car_data = pd.read_csv('vehicles_us.csv')

# Agregamos un encabezado
st.header("Venta de autos")

# Creamos un boton que cree un histograma al clickearlo
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un histograma para la columna precio')
    # crear un histograma
    fig = px.histogram(car_data, x="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Creamos un boton que cree un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión') # crear un botón
     
if scatter_button: # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para la columna odómetro en relación al precio')
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)

# Usando el código anterior, lo mostraremos ahora como casillas de selección en vez de botones
hist_checkbox = st.checkbox("Construir un histograma")
scatter_checkbox = st.checkbox("Construir un gráfico de dispersión")

if hist_checkbox: # Al hacer clic en esta cassilla
    st.write("Creación de un gráfico de dispersión para la columna precio")
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox: # Al hacer clic en esta casilla
    st.write('Creación de un gráfico de dispersión para la columna odómetro en relación al precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)
