# maestro_pizzero.py
from pizza import Pizza

class MaestroPizzero:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPedido(self, var: str) -> None:
        if var:  # Verifica que var no sea una cadena vacía
            pizza = Pizza(var)
            self.pizzasPorCocinar.append(pizza)

    def cocinar(self) -> None:
        # Mover pizzas de pizzasPorCocinar a pizzasPorEntregar
        self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
        self.pizzasPorCocinar = []

    def entregar(self) -> list:
        # Retorna hasta 2 pizzas y las elimina de pizzasPorEntregar
        pizzas_a_entregar = self.pizzasPorEntregar[:2]
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]
        return pizzas_a_entregar

    def obtenerNombre(self) -> str:
        return self.nombre

    def obtenerPizzasPorCocinar(self) -> list:
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self) -> list:
        return self.pizzasPorEntregar
