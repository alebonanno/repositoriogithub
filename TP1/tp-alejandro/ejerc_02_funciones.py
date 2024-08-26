'''ejerc_02_funciones.py'''
import time
from calendar import isleap
# calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)
# calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2 and anio_bisiesto == True:
        return 29
    elif mes == 2 and anio_bisiesto == False:
        return 28
# función que pasa la edad en años a su equivalente en días
def edad_a_dias(edad, hora_local, anio_comienzo, anio_fin):

    dias = 0
# calcular los dias
    for a in range(anio_comienzo, anio_fin):
        if (anio_bisiesto(a)): dias = dias + 366
        else: dias = dias + 365
# agregar los días transcurridos en este año
    for m in range(1, hora_local.tm_mon):
        dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
# agregar los días transcurridos en este mes
    return  dias + hora_local.tm_mday