import streamlit as st
import pandas as pd

# Carga tus datos desde una fuente (por ejemplo, un archivo CSV)
def cargar_datos():
  #datos=pd.read_csv('https://github.com/jhonjasanchez/movies_rating/blob/main/DATASET_PELICULAS_SIN_PUNTAJE.csv',sep=";",encoding='latin-1', decimal=',')
  datos=pd.read_csv('DATASET_PELICULAS_SIN_PUNTAJE.csv',sep=";",encoding='latin-1', decimal=',')
  columna = datos['TCONST']+' - '+datos['PRIMARYTITLE']
  lista_peliculas = columna.tolist()
  lista_peliculas.sort()
  return lista_peliculas


# Carga los datos
peliculas = cargar_datos()

# Crear un título
st.title("¡Bienvenidos a nuestra aplicación web - Movies Predictor!")

# Crear un campo de texto para el nombre de la película
nombre_pelicula = st.text_input("Ingrese el nombre de la película:")

selected_items = st.selectbox("Selecciona elementos", peliculas)


# Obtener la entrada del usuario
input_usuario = st.text_input("Buscar opción")

# Filtrar las opciones basadas en la entrada del usuario
opciones_filtradas = [opcion for opcion in peliculas if input_usuario.lower() in opcion.lower()]

# Mostrar las opciones filtradas en el selectbox
opcion_seleccionada = st.selectbox("Selecciona una opción", opciones_filtradas)

st.write("Opción seleccionada:", opcion_seleccionada)

pred = st.button("Predict") # Botón para predecir
