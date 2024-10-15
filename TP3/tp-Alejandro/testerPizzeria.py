from pizzaVariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo
from auxiliar import *

class TesterPizzeria: 
    def main(self): 
    # Solución 7.a. Crear objetos de tipo PizzaVariedad, Pizza, Orden, MaestroPizzero y Mozo. 
        muzza = PizzaVariedad("Muzzarella",7000)
        fugazetta = PizzaVariedad("Fugazetta", 7500)
        napo = PizzaVariedad("Napolitana", 7500)
        calabresa = PizzaVariedad("Calabresa", 8100)
        roque = PizzaVariedad("Roquefort y Nuez", 9000)
        jamon = PizzaVariedad("Rúcula y Crudo", 9000)
        provo = PizzaVariedad("Provolone", 8500)
        pizzaMuza1 = Pizza(muzza)
        pizzaFugazetta1 = Pizza(fugazetta) 
        pizzaFugazetta2 = Pizza(fugazetta) 
        pizzaJamon1 = Pizza(jamon)
        pizzaNapo1 = Pizza(napo)
        pizzaNapo2 = Pizza(napo)
        pizzaJamon2 = Pizza(jamon)
        pizzaJamon3 = Pizza(jamon)
        pizzaProvo1 = Pizza(provo)
        pizzaCalabresa1 = Pizza(calabresa)
        pizzaProvo2 = Pizza(provo)
        pizzaRoque1 = Pizza(roque)
        pizzaMuza2 = Pizza(muzza)
        pizzaFugazetta3 = Pizza(fugazetta) 
        pizzaProvo3 = Pizza(provo)
        pizzaCalabresa2 = Pizza(calabresa)
        orden1 = Orden(1, [pizzaMuza1, pizzaFugazetta1])
        orden2 = Orden(2, [pizzaFugazetta2, pizzaJamon1])
        orden3 = Orden(3, [pizzaNapo1,pizzaNapo2, pizzaJamon2])
        orden4 = Orden(4, [pizzaJamon3, pizzaProvo1])
        orden5 = Orden(5, [pizzaCalabresa1, pizzaProvo2, pizzaRoque1])
        orden6 = Orden(6, [pizzaMuza2, pizzaFugazetta3, pizzaProvo3, pizzaCalabresa2])
        mP = MaestroPizzero("Pipo")
        print(f"Maestro Pizzero: {mP.obtenerNombre()}")
        mozo1 = Mozo("Nico")
        print(f"Mozo 1: {mozo1.obtenerNombre()}, tiene pizzas: {mozo1.obtenerPizzas()}")
        mozo2 = Mozo("Juan")
        print(f"Mozo 2: {mozo2.obtenerNombre()}, tiene pizzas: {mozo2.obtenerPizzas()}")
    #Solución 7.b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.     
        mP.tomarPedido(orden1)
        mP.tomarPedido(orden2)
        mP.tomarPedido(orden3)
        mP.tomarPedido(orden4)
        mP.tomarPedido(orden5)
        mP.tomarPedido(orden6)
        aux = Auxiliar()
        aux.imprimir_estado_ordenes(aux.status(mP))
        mP.cocinar()
        print("Cocinando pedidos...")
        aux.imprimir_estado_ordenes(aux.status(mP))
    #Solución 7.c. Enviar los mensajes tomarPizzas y servirPizzas a los objetos de la clase Mozo creados en el punto a.    
        mozo1.tomarPizzas(mP.entregar())
        mozo2.tomarPizzas(mP.entregar())
        mozo1.servirPizzas()
        mozo2.servirPizzas()
        aux.imprimir_estado_ordenes(aux.status(mP))
    #Solución 7.d. Mostrar la transición de estados de los objetos de las clases Orden y Pizza.
        mozo1.tomarPizzas(mP.entregar())
        mozo2.tomarPizzas(mP.entregar())
        aux.imprimir_estado_ordenes(aux.status(mP))
        mozo1.servirPizzas()
        mozo2.servirPizzas()
        aux.imprimir_estado_ordenes(aux.status(mP))
        mozo1.tomarPizzas(mP.entregar())
        mozo2.tomarPizzas(mP.entregar())
        aux.imprimir_estado_ordenes(aux.status(mP))
        mozo1.servirPizzas()
        mozo2.servirPizzas()
        aux.imprimir_estado_ordenes(aux.status(mP))
        
    
    #Solución 7.e. Calcular y mostrar el costo total de las órdenes creadas. 
        print(f"El costo total de todas las ordenes es: ${aux.totalCostoEntregadas(mP)}")
    
    
    
        
if __name__ == '__main__': 
    testerPizzeria = TesterPizzeria() 
    testerPizzeria.main()