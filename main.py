import streamlit as st
import pandas as pd

def clean_column_names(df):
    df.columns = (df.columns.str.strip().str.rstrip().str.lower().str.replace(" ","_").str.replace(".","")
                  .str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    return df

# Limpia contenido en columnas de tipo string, eliminando espacios y pasando texto a minúscula
def clean_column_text(df):
    for col in df.columns:
        if (df[col].dtypes== "O") & ("fecha" not in str(col)):
            df[col] = (df[col].astype(str).str.strip().str.rstrip().str.lower()
                     #.str.replace(".","")
                     .str.replace("Ã\x91","N")
                     .str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    return df

def clean_all_text(df):
    df = clean_column_names(df)
    df = clean_column_text(df)
    return df
  
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
  datos_peliculas_det = clean_column_names(datos_peliculas_det)
  datos_peliculas_det.rename(columns={'itconst': 'tconst'}, inplace=True)
  return datos_peliculas_det

def consultar_datos_pelicula(idpelicula):
  st.write("Información de la película seleccionada : ", idpelicula)
  tmp = idpelicula.split('-')
  tconst = tmp[0]
  #st.write("Película a buscar: ", tconst)
  pelicula_filtrada = peliculas_det[peliculas_det['tconst']==tconst.strip()]
  #st.write("Tamaño de peliculas_det : ", pelicula_filtrada.head())
  return pelicula_filtrada

def pintar_datos_pelicula_sel(pelicula_seleccionada):
  info_pelicula_sel = pelicula_seleccionada[['startyear','runtimeminutes','genres', 'categoria', 'primaryname','total_peliculas','rating_promedio_peliculas']]  
  info_pelicula_sel['rating_promedio_peliculas'] = info_pelicula_sel['rating_promedio_peliculas'].round(1)
  st.write("Detalles : ", info_pelicula_sel)
  

def pintar_datos_pelicula_sel1(pelicula_seleccionada):
  directores = pelicula_seleccionada[pelicula_seleccionada['categoria']=='director']  
  for index, row in directores.iterrows():
    st.write("Director de la película: ", row['primaryname'])
  actores = pelicula_seleccionada[pelicula_seleccionada['categoria'].isin(['actress', 'actor'])]
  for index, row in actores.iterrows():
    st.write("Actor de la película: ", row['primaryname'])

def predecir_rating(pelicula_seleccionada):
    rating = 80
    st.write("El rating de la película será de: ", rating)

def consultar_pelicula(peli_sel):
    st.write("Usted va a consultar: ", peli_sel)
    #pelicula_seleccionada = consultar_datos_pelicula(peli_sel)
    #pintar_datos_pelicula_sel(pelicula_seleccionada)
    
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

st.write("Película seleccionadaa: ", opcion_seleccionada)

if len(input_usuario)>0:
  pelicula_seleccionada = consultar_datos_pelicula(opcion_seleccionada)
  pintar_datos_pelicula_sel(pelicula_seleccionada)

pred = st.button("Predecir rating de la película") # Botón para predecir
if pred:
    predecir_rating(opcion_seleccionada)
