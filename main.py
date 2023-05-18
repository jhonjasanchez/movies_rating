import streamlit as st

# Crear un título
st.title("¡Bienvenidos a nuestra aplicación web - Movies Predictor!")

# Crear un campo de texto para el nombre de la película
nombre_pelicula = st.text_input("Ingrese el nombre de la película:")

# Crear una lista de opciones con selección múltiple
opciones_seleccionadas = st.multiselect("Seleccione los actores", ["Opción 1", "Opción 2", "Opción 3"])

pred = st.button("Predict") # Botón para predecir
