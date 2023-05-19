import streamlit as st
import pandas as pd

# Carga tus datos desde una fuente (por ejemplo, un archivo CSV)

def cargar_datos():
  datos=pd.read_csv('https://drive.google.com/file/d/1aBm0vzwjuyLb6CzqO4G76cF8KyjeUCsF/view?usp=sharing',sep=";",encoding='latin-1', decimal=',')
  return datos

# Carga los datos
datos = cargar_datos()

# Crear un título
st.title("¡Bienvenidos a nuestra aplicación web - Movies Predictor!")

# Crear un campo de texto para el nombre de la película
nombre_pelicula = st.text_input("Ingrese el nombre de la película:")

pred = st.button("Predict") # Botón para predecir
