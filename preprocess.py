import pandas as pd
import numpy as np

#Cambiar el tipo de las columnas
def cambiar_tipos(info_pelicula):
  info_pelicula['startyear'] = info_pelicula['startyear'].astype(str)
  info_pelicula['startyear'] = info_pelicula.startyear.replace({'\\N': np.nan})
  info_pelicula['startyear'] = info_pelicula['startyear'].astype(np.float)
  info_pelicula['runtimeminutes'] = info_pelicula['runtimeminutes'].astype(str)
  info_pelicula['runtimeminutes'] = info_pelicula.runtimeminutes.replace({'\\N': np.nan})
  info_pelicula['runtimeminutes'] = info_pelicula['runtimeminutes'].astype(np.float)
  return info_pelicula

#Se dejan sólo las columnas que el modelo va a utilizar
def quitar_columnas(info_pelicula)
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
