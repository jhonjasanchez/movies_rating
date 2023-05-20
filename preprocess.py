

def cambiar_tipos(info_pelicula):
  info_pelicula['startyear'] = info_pelicula['startyear'].astype(str)
  info_pelicula['startyear'] = info_pelicula.startyear.replace({'\\N': np.nan})
  info_pelicula['startyear'] = info_pelicula['startyear'].astype(np.float)
  info_pelicula['runtimeminutes'] = info_pelicula['runtimeminutes'].astype(str)
  info_pelicula['runtimeminutes'] = info_pelicula.runtimeminutes.replace({'\\N': np.nan})
  info_pelicula['runtimeminutes'] = info_pelicula['runtimeminutes'].astype(np.float)
  return info_pelicula

def preparar_pelicula(info_pelicula):
  info_pelicula = cambiar_tipos(info_pelicula)
  return info_pelicula
