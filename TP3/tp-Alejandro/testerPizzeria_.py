from pizzaVariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo
from auxiliar import *

class TesterPizzeria: 
    def main(self): 
    # Solución 7.a. Crear objetos de tipo PizzaVariedad, Pizza, Orden, MaestroPizzero y Mozo. 
        muzza = PizzaVariedad("Muzzarella",11000)
        marga = PizzaVariedad("Margarita",11430)
        fugazza = PizzaVariedad("Fugazza", 13010)
        napo = PizzaVariedad("Napolitana", 13010)
        putanesca = PizzaVariedad("Putanesca", 13550)
        jamon = PizzaVariedad("Jamón Cocido", 13550)
        ameri = PizzaVariedad("Americana", 19070)
        peppe = PizzaVariedad("Pepperoni", 19260)
        espec = PizzaVariedad("Especial", 18030)
        cuatro = PizzaVariedad("4 Quesos", 18330)
        provo = PizzaVariedad("Provolone", 18330)
        pizzaMuza = Pizza(muzza)
        pizzaMarga = Pizza(marga) 
        pizzaFugazza = Pizza(fugazza)
        pizzaNapo = Pizza(napo)
        pizzaPutanesca = Pizza(putanesca)
        pizzaJamon = Pizza(jamon)
        pizzaAmericana = Pizza(ameri)
        pizzaPepperoni = Pizza(peppe)
        pizzaEspec = Pizza(espec)
        pizzaCuatro = Pizza(cuatro)
        pizzaProvo = Pizza(provo)
        orden1 = Orden(1,[pizzaMuza])
        orden2 = Orden(2, [pizzaMarga, pizzaFugazza])
        orden3 = Orden(3, [pizzaNapo,pizzaPutanesca,pizzaJamon])
        orden4 = Orden(4, [pizzaAmericana,pizzaPepperoni,pizzaEspec])
        orden5 = Orden(5,[pizzaCuatro,pizzaProvo])
        mPMario = MaestroPizzero("Mario")
        alfredo = Mozo("Alfredo")
        guillermo = Mozo("Guillermo")
    #Solución 7.b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.     
        mPMario.tomarPedido(orden1)
        mPMario.cocinar()
        mPMario.tomarPedido(orden2)
        mPMario.tomarPedido(orden3)
        mPMario.cocinar()
    #Solución 7.c. Enviar los mensajes tomarPizzas y servirPizzas a los objetos de la clase Mozo creados en el punto a.    
        alfredo.tomarPizzas(mPMario.entregar())
        alfredo.servirPizzas()
        guillermo.tomarPizzas(mPMario.entregar())
        guillermo.servirPizzas()
        aux = Auxiliar()
        aux.imprimir_estado_ordenes(aux.status(mPMario))
    #Solución 7.d. Mostrar la transición de estados de los objetos de las clases Orden y Pizza.
        mPMario.tomarPedido(orden4)
        mPMario.tomarPedido(orden5)
        mPMario.cocinar()    
        alfredo.tomarPizzas(mPMario.entregar())
        alfredo.servirPizzas()
        guillermo.tomarPizzas(mPMario.entregar())
        aux.imprimir_estado_ordenes(aux.status(mPMario))
        guillermo.servirPizzas()
        alfredo.tomarPizzas(mPMario.entregar())
        alfredo.servirPizzas()
        guillermo.tomarPizzas(mPMario.entregar())
        guillermo.servirPizzas()
        aux.imprimir_estado_ordenes(aux.status(mPMario))
        
    
    #Solución 7.e. Calcular y mostrar el costo total de las órdenes creadas. 
        print(f"El costo total de todas las ordenes es: ${aux.totalCostoEntregadas(mPMario)}")
    
    
    
        
if __name__ == '__main__': 
    testerPizzeria = TesterPizzeria() 
    testerPizzeria.main()