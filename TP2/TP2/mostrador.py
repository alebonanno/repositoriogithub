

class Mostrador():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__pizzas = []

    #Comandos
    def recibirPizzas(self, pizzas): #pizzas[0,1]
        self.__pizzas.extend(pizzas)
    def retirarPizza(self):
        pizzaSaliendo = []
        if self.__pizzas:
            pizzaSaliendo.extend(self.__pizzas[:1])
            del self.__pizzas[0]
        return pizzaSaliendo
    def nombreMostrador(self, nom): #nom stream
        self.__nombre = nom
    def hayPizzas(self):
        if len(self.obtenerNombrePizzas()):
            print(f'     Hay estas pizzas en el mostrador para que entreguen los mozos: {self.obtenerNombrePizzas()}') 
        else: print(f'     No hay pizzas en el mostrador para entregar')

    #Consultas
    def obtenerNombre(self):
        return self.__nombre
    def obtenerNombrePizzas(self):
        return [pizza.obtenerVariedad() for pizza in self.__pizzas]

if __name__ == '__main__':
    mostrador = Mostrador('mostrador')
    print(f'{id(mostrador)} Mostrador creado ')
    print(f'Pizzas en mostrador: {mostrador.obtenerNombrePizzas()}')
