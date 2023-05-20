import streamlit as st
import pandas as pd
import numpy as np
import joblib

#Cambiar el tipo de las columnas
def cambiar_tipos(info_pelicula):
  info_pelicula['startyear'] = info_pelicula['startyear'].astype(str)
  info_pelicula['startyear'] = info_pelicula.startyear.replace({'\\N': np.nan})
  info_pelicula['startyear'] = info_pelicula.startyear.replace({',': ''})
  info_pelicula['startyear'] = info_pelicula['startyear'].astype(np.integer)
  info_pelicula['runtimeminutes'] = info_pelicula['runtimeminutes'].astype(str)
  info_pelicula['runtimeminutes'] = info_pelicula.runtimeminutes.replace({'\\N': '0'})
  info_pelicula['runtimeminutes'] = info_pelicula['runtimeminutes'].astype(np.integer)
  return info_pelicula

#Se dejan sólo las columnas que el modelo va a utilizar
def quitar_columnas(info_pelicula):
  info_pelicula_2 = info_pelicula[['startyear','runtimeminutes', 'genres','total_actores',
         'total_directores', 'total_escritores', 'total_otras_categorias',
         'prom_ponderado_rating_actores',
         'prom_ponderado_rating_directores',
         'prom_ponderado_rating_escritores',
         'prom_ponderado_rating_otras_cat']]
  return info_pelicula_2

#Se preparan los géneros de la película
def preparar_generos(info_pelicula):
  info_pelicula['genres']=info_pelicula['genres'].str.strip().str.replace(',', ' ')
  info_pelicula['genres']=info_pelicula.genres.replace({ "\\N": "otro"})
  unique_values = ['History','War','Comedy','Family','News','Short','Animation','Fantasy',
                     'Crime','Action','Thriller','Music','Horror','Reality-TV','Documentary',
                     'Sport','Biography','Adventure','Musical','Adult','Romance','Western',
                     'otro','Mystery','Drama','Sci-Fi','Talk-Show','Game-Show']
  for i in unique_values:
    info_pelicula[i]=np.where(info_pelicula.genres.str.contains(i),1,0)
  info_pelicula = info_pelicula.drop(['genres'], axis=1)
  return info_pelicula

# si hay promedios ponderados nulos, se deja con valor de cero (0)
def preparar_promedios_ponderados(info_pelicula):
  info_pelicula['prom_ponderado_rating_actores']= np.where(info_pelicula['prom_ponderado_rating_actores'].isna(),0,info_pelicula.prom_ponderado_rating_actores)
  info_pelicula['prom_ponderado_rating_directores']= np.where(info_pelicula['prom_ponderado_rating_directores'].isna(),0,info_pelicula.prom_ponderado_rating_directores)
  info_pelicula['prom_ponderado_rating_escritores']= np.where(info_pelicula['prom_ponderado_rating_escritores'].isna(),0,info_pelicula.prom_ponderado_rating_escritores)
  info_pelicula['prom_ponderado_rating_otras_cat']= np.where(info_pelicula['prom_ponderado_rating_otras_cat'].isna(),0,info_pelicula.prom_ponderado_rating_otras_cat)
  return info_pelicula

def preparar_pelicula(info_pelicula):
  info_pelicula = cambiar_tipos(info_pelicula)
  info_pelicula = quitar_columnas(info_pelicula)
  info_pelicula = preparar_generos(info_pelicula)
  info_pelicula = preparar_promedios_ponderados(info_pelicula)
  return info_pelicula

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

def consultar_pelicula_a_preparar(idpelicula):
  tmp = idpelicula.split('-')
  tconst = tmp[0]
  datos=pd.read_csv('DATASET_PELICULAS_SIN_PUNTAJE.csv',sep=";",encoding='latin-1', decimal=',')
  datos = clean_column_names(datos)
  datos.rename(columns={'itconst': 'tconst'}, inplace=True)
  pelicula_filtrada = datos[datos['tconst']==tconst.strip()]
  return pelicula_filtrada

def consultar_datos_pelicula(idpelicula):
  st.write("Información de la película seleccionada : ", idpelicula)
  tmp = idpelicula.split('-')
  tconst = tmp[0]
  #st.write("Película a buscar: ", tconst)
  st.write('<a href="https://www.imdb.com/title/'+tconst+'">Ir al sitio web oficiall en IMDB: '+tmp[1]+'</a>', unsafe_allow_html=True)
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
    pelicula_a_preparar=consultar_pelicula_a_preparar(pelicula_seleccionada)
    st.write("Pelicula a preparar: ", pelicula_a_preparar)
    pelicula_preparada=preparar_pelicula(pelicula_a_preparar)
    st.write("Pelicula preparada: ", pelicula_preparada)
    rating = modelo.predict(pelicula_preparada)
    st.write("El rating de la película será de: ", rating)

def consultar_pelicula(peli_sel):
    st.write("Usted va a consultar: ", peli_sel)
    #pelicula_seleccionada = consultar_datos_pelicula(peli_sel)
    #pintar_datos_pelicula_sel(pelicula_seleccionada)

  
    
# Carga los datos
peliculas = cargar_datos()
peliculas_det = cargar_datos_peliculas_det()
modelo = joblib.load('base_model_2000s.pkl')

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

pelicula_seleccionada = consultar_datos_pelicula(opcion_seleccionada)
pintar_datos_pelicula_sel(pelicula_seleccionada)

pred = st.button("Predecir rating de la película") # Botón para predecir
if pred:
    predecir_rating(opcion_seleccionada)
