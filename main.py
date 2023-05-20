import streamlit as st
import pandas as pd
import read_files as rf

# Carga los datos
peliculas = rf.cargar_datos()
peliculas_det = rf.cargar_datos_peliculas_det()

# Crear un título
st.title("¡Bienvenidos a nuestra aplicación web - Movies Predictor!")

# Crear un campo de texto para el nombre de la película
#nombre_pelicula = st.text_input("Ingrese el nombre de la película:")
#selected_items = st.selectbox("Selecciona elementos", peliculas)


# Obtener la entrada del usuario
input_usuario = st.text_input("Buscar una película por nombre")

# Filtrar las opciones basadas en la entrada del usuario
opciones_filtradas = [opcion for opcion in peliculas if input_usuario.lower() in opcion.lower()]

# Mostrar las opciones filtradas en el selectbox
opcion_seleccionada = st.selectbox("Selecciona una película", opciones_filtradas)

st.write("Película seleccionada: ", opcion_seleccionada)

#pelicula_seleccionada = consultar_datos_pelicula(opcion_seleccionada)
consultar_datos_pelicula(opcion_seleccionada)
#for index, row in pelicula_seleccionada.iterrows():
#    st.write("Nombre:", row['PRIMARYTITLE'])

pred = st.button("Predict") # Botón para predecir
