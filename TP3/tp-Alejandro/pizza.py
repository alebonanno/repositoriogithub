from pizzaVariedad import PizzaVariedad

class Pizza:
    __estado_por_cocinar = 1
    __estado_cocinada = 2
    __estado_entregada = 3
    
    def __init__(self, var: PizzaVariedad):
        self.__variedad = var
        self.__estado = self.__estado_por_cocinar

    def establecerVariedad(self, var: PizzaVariedad):
        self.__variedad = var
    
    def establecerEstado(self, est: int):
        if self.__estado + 1 == est:
            self.__estado = est
    #Consultas        
    def obtenerVariedad(self) -> PizzaVariedad:
        return self.__variedad
    
    def obtenerEstado(self) -> int:
        return self.__estado
            
    def __repr__(self) -> str:
        return self.__variedad.obtenerNombreVariedad()
    
