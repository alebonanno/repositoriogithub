"""
Genere la clase Pizza con los atributos y servicios mencionados en dicho diagrama.
"""

class Pizza:
  def __init__(self, var):
    self.__var = var

  #comandos
  def establecerVariedad(self, var):
    self.__var = var

  #consultas
  def obtenerVariedad(self):
    return self.__var