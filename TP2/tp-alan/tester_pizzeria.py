# tester_pizzeria.py
from MaestroPizzero import MaestroPizzero

from mozo import Mozo
from pizza import Pizza

class TesterPizzeria:
    def main(self):
        # Crear objetos de tipo MaestroPizzero, Mozo y Pizza
        maestro_pizzero = MaestroPizzero("Gonzalo")
        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Carlos")
        
        # Crear algunas pizzas
        pizza1 = Pizza("Margarita")
        pizza2 = Pizza("Pepperoni")
        pizza3 = Pizza("Cuatro Quesos")
        
        # Enviar los mensajes tomarPedido, cocinar y entregar al MaestroPizzero
        maestro_pizzero.tomarPedido("Margarita")
        maestro_pizzero.tomarPedido("Pepperoni")
        maestro_pizzero.cocinar()
        pizzas_entregadas = maestro_pizzero.entregar()
        
        # Mostrar las pizzas entregadas
        print("Pizzas entregadas:", [pizza.obtenerVariedad() for pizza in pizzas_entregadas])
        
        # Tomar las pizzas entregadas con los mozos
        mozo1.tomarPizzas(pizzas_entregadas[:1])  # Tomamos solo una pizza para mozo1
        mozo2.tomarPizzas(pizzas_entregadas[1:])  # Tomamos la otra pizza para mozo2
        
        # Mostrar el estado de las pizzas de cada mozo
        print("Pizzas que lleva mozo1:", [pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()])
        print("Pizzas que lleva mozo2:", [pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()])
        
        # Intentar añadir una pizza extra a mozo1
        mozo1.tomarPizzas([pizza3])
        
        # Mostrar el estado después de intentar añadir una pizza extra
        print("Pizzas que lleva mozo1 después de intentar añadir una más:", [pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()])
        
        # Servir pizzas
        mozo1.servirPizzas()
        mozo2.servirPizzas()
        
        # Mostrar el estado después de servir las pizzas
        print("Pizzas que lleva mozo1 después de servir:", [pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()])
        print("Pizzas que lleva mozo2 después de servir:", [pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()])

if __name__ == '__main__':
    tester_pizzeria = TesterPizzeria()
    tester_pizzeria.main()
