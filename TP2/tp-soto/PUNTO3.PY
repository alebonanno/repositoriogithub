class Pizza:
    def __init__(self, var):
        self.variedad = var

    def establecerVariedad(self, var):
        self.variedad = var

    def obtenerVariedad(self):
        return self.variedad

class Mozo:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom):
        self.nombre = nom

    def tomarPizzas(self, pizzas):
        if isinstance(pizzas, list) and len(pizzas) > 0:
            pizzas_a_tomar = pizzas[:2]
            self.pizzas.extend(pizzas_a_tomar)

    def servirPizzas(self):
        self.pizzas.clear()

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzas(self):
        return self.pizzas

    def obtenerEstadoLibre(self):
      
        return len(self.pizzas) <= 1

if __name__ == "__main__":
    pizza1 = Pizza("Margarita")
    pizza2 = Pizza("Pepperoni")
    pizza3 = Pizza("Cuatro Quesos")

 
    mozo = Mozo("Juan")
 
    mozo.tomarPizzas([pizza1, pizza2, pizza3])
  
    print(f"Pizzas tomadas: {[pizza.obtenerVariedad() for pizza in mozo.obtenerPizzas()]}")  

    print(f"Estado libre del mozo: {mozo.obtenerEstadoLibre()}")

    mozo.servirPizzas()
  
    print(f"Pizzas después de servir: {[pizza.obtenerVariedad() for pizza in mozo.obtenerPizzas()]}")  
  
    print(f"Estado libre del mozo: {mozo.obtenerEstadoLibre()}") 