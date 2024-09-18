from pizza import Pizza

class MaestroPizzero:
  def __init__(self, nombre):
    self.__nombre = nombre
    self.__pizzasPorCocinar = []
    self.__pizzasPorEntregar = []

  #comandos
  def establecerNombre(self, nom):
    self.__nombre = nom

  def tomarPedido(self, var):
    if len(var) > 0:
      nuevaPizza = Pizza(var)
      self.__pizzasPorCocinar.append(nuevaPizza)
      print(f"Se tomo el pedido de la pizza {var}")
    else:
      print("Nombre de pizza incorrecto")

  def cocinar(self):
    if len(self.__pizzasPorCocinar) > 0:
      self.__pizzasPorEntregar.extend(self.__pizzasPorCocinar)
      pizzasCocinadas = len(self.__pizzasPorCocinar)
      self.__pizzasPorCocinar.clear()
      print(f"El maestro pizzero cocino {pizzasCocinadas} pizza{"s" if pizzasCocinadas > 1 else ""}")
    else:
      print("No quedan pizzas por cocinar")

  def entregar(self):
    if len(self.__pizzasPorEntregar) > 0:
      pizzas = self.__pizzasPorEntregar[:2]
      self.__pizzasPorEntregar = self.__pizzasPorEntregar[2:]
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
  