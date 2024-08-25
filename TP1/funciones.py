from calendar import isleap

class Edad:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.hora_local = time.localtime(time.time())
        self.anio_comienzo = self.hora_local.tm_year - edad
        self.anio_fin = self.anio_comienzo + edad

    def anio_bisiesto(self, anio):
        return isleap(anio)

    def calcular_dias_mes(self, mes, anio):
        meses_31_dias = {1, 3, 5, 7, 8, 10, 12}
        meses_30_dias = {4, 6, 9, 11}
        if mes in meses_31_dias:
            return 31
        elif mes in meses_30_dias:
            return 30
        elif mes == 2:
            return 29 if self.anio_bisiesto(anio) else 28
        return 0

    def calcular_dias(self):
        dias = 0
        for a in range(self.anio_comienzo, self.anio_fin):
            dias += 366 if self.anio_bisiesto(a) else 365
        for m in range(1, self.hora_local.tm_mon):
            dias += self.calcular_dias_mes(m, self.hora_local.tm_year)
        dias += self.hora_local.tm_mday
        return dias

    def calcular_meses(self):
        return self.edad * 12 + self.hora_local.tm_mon

