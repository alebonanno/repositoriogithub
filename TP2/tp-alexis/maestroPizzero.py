from pizza import Pizza

class MaestroPizzero:
  #constructor
  def __init__(self, nombre):
    self.__nombre = nombre
    self.__pizzasPorCocinar = []
    self.__pizzasPorEntregar = []

  #comandos
  def establecerNombre(self, nom):
    self.__nombre = nom

  def tomarPedido(self, var):
    nuevaPizza = Pizza(var)
    self.__pizzasPorCocinar.append(nuevaPizza)

  def cocinar(self):
    if len(self.__pizzasPorCocinar) > 0:
      self.__pizzasPorEntregar.extend(self.__pizzasPorCocinar)
      self.__pizzasPorCocinar.clear()
      print("Todas las pizzas fueron cocinadas")
    else:
      print("No quedan pizzas por cocinar")

  def entregar(self):
    if len(self.__pizzasPorEntregar) > 0:
      pizzas = self.__pizzasPorEntregar[:2]
      self.__pizzasPorEntregar = self.__pizzasPorEntregar[2:]
      print("Entregando pizzas")
      return pizzas
    else:
      print("No quedan pizzas por entregar")
      return []

  #consultas
  def obtenerNombre(self):
    return self.__nombre
  
  def obtenerPizzasPorCocinar(self):
    return self.__pizzasPorCocinar
  
  def obtenerPizzasPorEntregar(self):
    return self.__pizzasPorEntregar
  