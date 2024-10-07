from pizza import Pizza

class Mozo:

    def __init__(self, nom: str):
        self.__nombre = nom
        self.__pizzas = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPizzas(self, pizzas: list[Pizza]):
        if self.obtenerEstadoLibre(): 
            self.__pizzas = pizzas
        else:
            print("El mozo tiene pizzas para entregar antes de tomar otra")
            
    def servirPizzas(self):
        for pizza in self.__pizzas:
            print(self.__nombre + ": Sirviendo pizza de " + pizza.obtenerVariedad().obtenerNombreVariedad())
        self.__pizzas = []

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPizzas(self):
        return self.__pizzas
    
    def obtenerEstadoLibre(self):
        return len(self.__pizzas) == 0
  