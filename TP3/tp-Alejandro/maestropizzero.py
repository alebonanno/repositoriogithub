from pizza import Pizza
from orden import Orden

class MaestroPizzero:

    def __init__(self, nom: str):
        self.__nombre = nom
        self.__ordenes = []
        
    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, orden: Orden): 
        #Requiere orden ligado y orden.estado = Orden.__Estado_Inicial = 1
        if orden not in self.__ordenes: 
            self.__ordenes.append(orden)
        
    def cocinar(self):
        for orden in self.__ordenes:
            orden.establecerEstadoOrden(2)
            for pizza in orden.obtenerPizzas():
                pizza.establecerEstado(2)
            #    print(self.__nombre + ": cocinando una pizza de " + pizza.obtenerVariedad())
        
    def entregar(self, orden: Orden = None) -> list[Pizza]:
        #Requiere orden ligado y orden.estado = Orden.__Estado_Para_Entregar
        pizzasAEntregar = []
        contador = 0
        if orden is None:
            for orden in self.__ordenes:
                if orden.obtenerEstadoOrden() == 2:
                    entregadas = 0
                    
                    for pizza in orden.obtenerPizzas():
                        if pizza.obtenerEstado() == 2 and contador < 2:
                            pizza.establecerEstado(3)
                            pizzasAEntregar.append(pizza)
                            contador += 1
                        if pizza.obtenerEstado() == 3:
                            entregadas += 1
                    if entregadas == len(orden.obtenerPizzas()):
                        orden.establecerEstadoOrden(3)
                    if contador >= 2:
                        break
        else:
            if orden not in self.__ordenes: 
                return pizzasAEntregar
            if orden in self.__ordenes and orden.obtenerEstadoOrden() == 2: # __estado_para_entregar = 2
                entregadas = 0
                for pizza in orden.obtenerPizzas(): #Recorre las pizzas dentro de la orden
                    
                    if pizza.obtenerEstado() == 2 and contador < 2: #__estado_cocinada = 2
                        pizza.establecerEstado(3)
                        pizzasAEntregar.append(pizza)
                        contador += 1
                    if pizza.obtenerEstado() == 3: 
                        entregadas += 1 #revisa si aun quedan pizzas cocidas sin entregar, si han sido entregadas todas cambiar el estado de la orden
                if entregadas == len(orden.obtenerPizzas()): 
                    orden.establecerEstadoOrden(3)
        return pizzasAEntregar

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerOrdenes(self) -> list[Orden]:
        return self.__ordenes
  