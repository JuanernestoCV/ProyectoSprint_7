# Importamos librerias
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargamos datos
car_data = pd.read_csv('vehicles_us.csv')

# Agregamos un titulo
st.title("Venta de autos")

# Agregamos un encabezado
st.header("Visualizar los datos")
# Creamos una casilla de selección que permita ver los datos
if st.checkbox("Mostrar datos"):
    st.write("Datos sobre los vehiculo")
    st.dataframe(car_data)

# Creamos un separador
st.markdown("---")

# Agregamos un encabezado
st.header("Botones para generar gráficos")

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
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)

# Creamos un boton que cree un gráfico de barras
bar_button = st.button('Construir gráfico de barras') # crear un botón
     
if bar_button: # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un gráfico de barras para la columna type mostrando el precio promedio')
    # Creamos el gráfico de barras
    fig = px.bar(car_data.groupby(by="type")["price"].mean().sort_values(ascending=False))
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)

# Creamos un boton que cree un gráfico de caja
box_button = st.button('Construir gráfico de caja') 
     
if box_button: # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un gráfico de caja para la distribución del kilometraje por condición')
    # Creamos el gráfico de caja
    fig = px.box(car_data, x="condition", y="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)

#Creamos un encabezado
st.header("Marca las casillas para crear gráficas")
# Usando el código anterior, lo mostraremos ahora como casillas de selección en vez de botones
hist_checkbox = st.checkbox("Construir un histograma")
scatter_checkbox = st.checkbox("Construir un gráfico de dispersión")
bar_checkbox = st.checkbox('Construir gráfico de barras')
box_checkbox = st.checkbox('Construir gráfico de caja') 

if hist_checkbox: # Al hacer clic en esta cassilla
    st.write("Creación de un gráfico de dispersión para la columna precio")
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox: # Al hacer clic en esta casilla
    st.write('Creación de un gráfico de dispersión para la columna odómetro en relación al precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)

if bar_checkbox: # Al hacer clic en esta casilla
    st.write('Creación de un gráfico de barras para la columna type mostrando el precio promedio')
    fig = px.bar(car_data.groupby(by="type")["price"].mean().sort_values(ascending=False))
    st.plotly_chart(fig)

if box_checkbox: # Al hacer clic en esta casilla
    st.write('Creación de un gráfico de dispersión para la distribución del kilometraje por condición')
    fig = px.box(car_data, x="condition", y="odometer")
    st.plotly_chart(fig)
