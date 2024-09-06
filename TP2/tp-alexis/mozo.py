class Mozo:
  #constructor
  def __init__(self, nom):
    self.__nombre = nom
    self.__pizzas = []
  
  #comandos
  def establecerNombre(self, nom):
    self.__nombre = nom

  def tomarPizzas(self, pizzas):
    if len(pizzas) + len(self.__pizzas) <= 2:
      self.__pizzas.extend(pizzas)
    else:
      print("El mozo solo puede llevar como máximo 2 pizzas")

  def servirPizzas(self):
    if len(self.__pizzas) > 0:
      self.__pizzas.clear()
      print("Pizzas servidas")
    else:
      print("Este mozo no tiene más pizzas por servir")
  
  #consultas
  def obtenerNombre(self):
    return self.__nombre
  
  def obtenerPizzas(self):
    return self.__pizzas
  
  def obtenerEstadoLibre(self):
    return len(self.__pizzas) < 2