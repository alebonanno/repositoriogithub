class Pizza:
  #constructor
  def __init__(self, var):
    self.__var = var

  #comandos
  def establecerVariedad(self, var):
    self.__var = var

  #consultas
  def obtenerVariedad(self):
    return self.__var