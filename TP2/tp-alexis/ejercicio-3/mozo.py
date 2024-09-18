"""
Habiendo analizado el diagrama, genere la clase Mozo con los atributos y servicios
mencionados en dicho diagrama.
  a. El atributo pizzas se inicializa como una lista vacía.
  b. El comando tomarPizzas agrega los objetos de la clase Pizza referenciados por
  el parámetro formal pizzas. El mozo puede tomar hasta un máximo de 2 pizzas.
  c. servirPizzas limpia la lista pizzas, haciendo entrega de los pedidos a los clientes.
  d. obtenerEstadoLibre debe retornar True si es que la lista referenciada por el
  atributo pizzastiene una longitud de entre 0 y 1. Así mismo, debe retornar False
  si su tamaño es igual a 2.
"""

class Mozo:
  def __init__(self, nom):
    self.__nombre = nom
    self.__pizzas = []
  
  #comandos
  def establecerNombre(self, nom):
    self.__nombre = nom

  def tomarPizzas(self, pizzas):
    if len(self.__pizzas) == 1 or len(pizzas) == 1:
      self.__pizzas.append(pizzas.pop(0))
      print(f"El mozo {self.__nombre} tomo 1 pizza para entregar.")
    elif len(self.__pizzas) == 0:
      self.__pizzas.extend(pizzas[:2]) 
      del pizzas[:2]
      print(f"El mozo {self.__nombre} tomó 2 pizzas para entregar.")
    else:
      print("El mozo solo puede llevar como máximo 2 pizzas")

  def servirPizzas(self):
    if len(self.__pizzas) > 0:
      pizzasServidas = len(self.__pizzas)
      self.__pizzas.clear()
      print(f"El mozo {self.__nombre} sirvio {pizzasServidas} pizza{"s" if pizzasServidas > 1 else ""}.")
    else:
      print("Este mozo no tiene más pizzas por servir.")
  
  #consultas
  def obtenerNombre(self):
    return self.__nombre
  
  def obtenerPizzas(self):
    return self.__pizzas
  
  def obtenerEstadoLibre(self):
    return len(self.__pizzas) < 2