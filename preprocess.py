from nltk.tokenize import word_tokenize

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
  listado_generos = info_pelicula['genres']
  lista=list()
  texto = ' '
  for val in listado_generos:
    tokens = val.split()
    texto += " ".join(tokens)+" "

  palabras = word_tokenize(texto)
  unique_values = list(set(palabras))
  
  return info_pelicula


def preparar_pelicula(info_pelicula):
  info_pelicula = cambiar_tipos(info_pelicula)
  info_pelicula = quitar_columnas(info_pelicula)
  return info_pelicula
