from maestroPizzero import MaestroPizzero
from mozo import Mozo

class TesterPizzeria:
    def main(self):
        mozo1 = Mozo("Alejandro")
        mozo2 = Mozo("Alexis")
        maestroPizzero = MaestroPizzero("Alan")
        
        maestroPizzero.tomarPedido("Napolitana")
        maestroPizzero.tomarPedido("Fugazzeta")
        maestroPizzero.tomarPedido("Margarita")
        maestroPizzero.tomarPedido("Napolitana")
        maestroPizzero.tomarPedido("Margarita")
        maestroPizzero.tomarPedido("Fugazzeta")
        maestroPizzero.tomarPedido("Margarita")
        maestroPizzero.cocinar()

        pizzasPorEntregar = maestroPizzero.entregar()
        while len(pizzasPorEntregar) > 0:
          if mozo1.obtenerEstadoLibre():
            mozo1.tomarPizzas(pizzasPorEntregar)
            mozo1.servirPizzas()
            pizzasPorEntregar.extend(maestroPizzero.entregar())
          if mozo2.obtenerEstadoLibre():
            mozo2.tomarPizzas(pizzasPorEntregar)
            mozo2.servirPizzas()
            pizzasPorEntregar.extend(maestroPizzero.entregar())

if __name__ == '__main__':
  testerPizzeria = TesterPizzeria()
  testerPizzeria.main()