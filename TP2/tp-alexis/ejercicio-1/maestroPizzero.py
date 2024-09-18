from pizza import Pizza

"""
Genere la clase MaestroPizzero, conteniendo los atributos y servicios mencionados en
el diagrama de clases anterior.
  i. El comando tomarPedido debe crear un nuevo objeto de la clase Pizza,
  de la variedad indicada en el parámetro formal var. Una vez inicializado
  dicho objeto, debe este agregarse a la lista referenciada por el atributo
  pizzasPorCocinar.
  ii. El comando cocinar debe tomar todos los objetos de la clase Pizza de la
  lista pizzasPorCocinar y depositarlos en una segunda lista,
  pizzasPorEntregar. Si no hay pizzas por ser cocinadas, el comando no
  tiene efecto sobre el estado interno del objeto.
  iii. El comando entregar retorna hasta un máximo de 2 objetos de la clase
  Pizza de la lista pizzasPorEntregar, removiéndolos de ella. Si no hay
  pizzas para ser entregadas, se debe retornar una lista vacía.
"""

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
  