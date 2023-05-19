import streamlit as st
import pandas as pd

def cargar_datos():
    # Carga tus datos desde una fuente (por ejemplo, un archivo CSV)
    datos = pd.read_csv('datos.csv')
    return datos

# Crear un título
st.title("¡Bienvenidos a nuestra aplicación web - Movies Predictor!")

# Crear un campo de texto para el nombre de la película
nombre_pelicula = st.text_input("Ingrese el nombre de la película:")

pred = st.button("Predict") # Botón para predecir
