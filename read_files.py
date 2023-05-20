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
  datos_peliculas_det1=pd.read_csv('DATASET_PELICULAS_FINAL_2023.csv',sep=";",encoding='latin-1', decimal=',')
  datos_peliculas_det1 = clean_column_names(datos_peliculas_det1)
  datos_peliculas_det1.rename(columns={'itconst': 'tconst'}, inplace=True)

  return datos_peliculas_det1

def consultar_datos_pelicula(idpelicula):
  tmp = idpelicula.split('-')
  tconst = tmp[0]
  st.write("Película a buscar: ", tconst)
  st.write("Tamaño de peliculas_det : ", peliculas_det1.head())
  #pelicula_filtrada = peliculas_det[peliculas_det['TCONST']==tconst]
  #return pelicula_filtrada

datos_peliculas_det = cargar_datos_peliculas_det()