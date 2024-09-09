from Pizza import *

class MaestroPizzero():
    # método de inicialización
    def __init__(self, nombre):
        #<<Atributos de clase>>
        #<<Atributos de instancia>>
        self.__nombre = nombre #string
        self.__pizzasPorCocinar = [] # Pizza[]
        self.__pizzasPorEntregar = [] # Pizza[]
        #<<Constructores>>
        #MaestroPizzero(nom: string)
    #<<Comandos>>
    def establecerNombre(self, nombre): # string
        self.__nombre = nombre
    def tomarPedido(self, var): #var: str): Pizza
        #Requiere var no vacío
        pizza = Pizza(var)
        print(f'Tomando pedido {pizza.obtenerVariedad()}')
        self.__pizzasPorCocinar.append(pizza)
        pizzasCrudas = [pizza.obtenerVariedad() for pizza in self.__pizzasPorCocinar]
        print(f'       Pizzas para cocinar: {pizzasCrudas}')
    def cocinar(self):
        if self.__pizzasPorCocinar:
            print('Cocinando pizzas' )
            print(f'      Cocinando: {self.obtenerNombrePizzasPorCocinar()}')
            self.__pizzasPorEntregar.extend(self.__pizzasPorCocinar)
            self.__pizzasPorCocinar = []
            print(f'Pizzas para entregar: {self.obtenerNombrePizzasPorEntregar()}')
            
        else: print('    No hay pizzas pedidas para cocinar')
    def entregar(self): # Pizza[]
        entregando = []
        if len(self.__pizzasPorEntregar) > 0:
            entregando.extend(self.__pizzasPorEntregar[:1])
            del self.__pizzasPorEntregar[0]
            entrega = [pizza.obtenerVariedad() for pizza in entregando]
            print(f'      Tomando: {entrega}')
        return entregando
    #<<Consultas>>
    def obtenerNombre(self): #string
        return self.__nombre
    def obtenerPizzasPorCocinar(self): #Pizza[]
        return self.__pizzasPorCocinar
    def obtenerPizzasPorEntregar(self): #Pizza[]
        return self.__pizzasPorEntregar
    

    def obtenerNombrePizzasPorCocinar(self):
        return [pizza.obtenerVariedad() for pizza in self.__pizzasPorCocinar]
    def obtenerNombrePizzasPorEntregar(self):
        return [pizza.obtenerVariedad() for pizza in self.__pizzasPorEntregar]