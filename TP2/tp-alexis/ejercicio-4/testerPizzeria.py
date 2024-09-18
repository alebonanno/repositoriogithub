"""
Una vez codificadas en Python las Clases de los puntos anteriores, instancie los objetos
tal como sucede en las siguientes instrucciones:

  mozo1 = Mozo(‘Alfredo’)
  mozo2 = Mozo(‘Alfredo’)

Luego, responda lo siguiente:
  i. ¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto?
  ii. ¿Son objetos equivalentes? Explique que significa que dos objetos lo sean.
  iii. ¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria?
"""
from mozo import Mozo

class TesterPizzeria:
  def main(self):
      mozo1 = Mozo("Alfredo")
      mozo2 = Mozo("Alfredo")

      print("i. ¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto?")
      print("Los identificadores mozo1 y mozo2 hacen referencia a objectos distintos ya que le asignamos un nuevo objecto a cada uno.")
      if mozo1 is mozo2:
        print("Son el mismo objeto")
      else:
        print("No son el mismo objeto")
      print()
      
      print("ii. ¿Son objetos equivalentes? Explique que significa que dos objetos lo sean.");
      print("Podemos decir que son equivalentes ya que por definición si dos objectos tienen el mismo estado interno decimos que son equivalente, en este caso tienen el mismo estado interno, ambos mozos tienen el mismo nombre y la lista de pizzas esta vacía")
      print()
      
      print("iii. ¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria?")
      idMozo1 = id(mozo1)
      idMozo2 = id(mozo2)
      print("ID en memoria mozo1: " + str(idMozo1))
      print("ID en memoria mozo2: " + str(idMozo2))
      if idMozo1 == idMozo2:
        print("mozo1 y mozo2 tienen misma dirección de memoria")
      else:
        print("mozo1 y mozo2 tienen distinta dirección de memoria")
      print("Utilizando la función ""id(object)"" obtenemos la dirección de memoria, en cada mozo vemos tienen diferente dirección memoria")
      print()
        

if __name__ == '__main__':
  testerPizzeria = TesterPizzeria()
  testerPizzeria.main()