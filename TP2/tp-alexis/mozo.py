from pizza import Pizza

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
      print(f"El mozo {self.__nombre} tomo {len(pizzas)} pizza/s para entregar.")
    else:
      print("El mozo solo puede llevar como máximo 2 pizzas")

  def servirPizzas(self):
    if len(self.__pizzas) > 0:
      print(f"El mozo {self.__nombre} sirvio {len(self.__pizzas)} pizza/s")
      self.__pizzas.clear()
    else:
      print("Este mozo no tiene más pizzas por servir")
  
  #consultas
  def obtenerNombre(self):
    return self.__nombre
  
  def obtenerPizzas(self):
    return self.__pizzas
  
  def obtenerEstadoLibre(self):
    return len(self.__pizzas) < 2