from pizza import Pizza

class Orden:
    
    #Atributos de clase
    __estado_inicial = 1
    __estado_para_entregar = 2
    __estado_entregada = 3
    
    #Atributos de instancia
    def __init__(self, nro: int, pizzas: list):
        self.__nroOrden = nro
        self.__pizzas = pizzas
        self.__estadoOrden = Orden.__estado_inicial

    # Comandos
    def establecerNroOrden(self, nro: int):
        self.__nroOrden = nro

    def establecerPizzas(self, pizzas: list):
        self.__pizzas = pizzas

    def establecerEstadoOrden(self, est: int):
        if self.__estadoOrden + 1 == est:
            self.__estadoOrden = est

    # Consultas
    def obtenerNroOrden(self) -> int:
        return self.__nroOrden

    def obtenerPizzas(self) -> list[Pizza]:
        return self.__pizzas

    def obtenerEstadoOrden(self) -> int: 
        return self.__estadoOrden

    def calcularTotal(self) -> float:
        return sum(pizza.obtenerVariedad().obtenerPrecio() for pizza in self.__pizzas) 

