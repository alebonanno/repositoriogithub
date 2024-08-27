# calcular si es un año bisiesto
def anio_bisiesto(anio):
  return isleap(anio)

# calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
  if mes in (1, 3, 5, 7, 8, 10, 12):
    return 31
  elif mes in (4, 6, 9, 11):
    return 30
  elif mes == 2 and anio_bisiesto:
    return 29
  else:
    return 28
  
# calcular edad equivalente en días
def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
  dias = 0

  # calcular los dias
  for a in range(anio_comienzo, anio_fin):
    if (anio_bisiesto(a)): dias = dias + 366
    else: dias = dias + 365

  # agregar los días transcurridos en este año
  for m in range(1, hora_local.tm_mon):
    dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

  # agregar los días transcurridos en este mes
  dias = dias + hora_local.tm_mday

  return dias

# verifica que el string se puede castear a entero y devuelve el valor casteado
def intentar_castear_a_entero(cadena):
  try:
    return int(cadena), True
  except:
    return cadena, False