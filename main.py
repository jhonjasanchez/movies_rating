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

# Cargar la información detallada de las películas
def cargar_datos_peliculas_det():
  datos_peliculas_det=pd.read_csv('DATASET_PELICULAS_FINAL_2023.csv',sep=";",encoding='latin-1', decimal=',')
  return datos_peliculas_det

def consultar_datos_pelicula(idpelicula):
  tmp = idpelicula.split('-')
  st.write("Película a buscar: ", tmp)
  #tconst = tmp[0].str.strip()
  #pelicula_filtrada = datos_peliculas_det[datos_peliculas_det.tconst == idpelicula]
  #return pelicula_filtrada


# Carga los datos
peliculas = cargar_datos()
peliculas_det = cargar_datos_peliculas_det()

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
