# mozo.py
from pizza import Pizza

class Mozo:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []  # Inicializar como una lista vacía

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPizzas(self, pizzas: list):
        if len(self.pizzas) < 2:  # Solo puede llevar hasta 2 pizzas
            # Añadir las pizzas, pero no más de 2
            for pizza in pizzas:
                if len(self.pizzas) < 2:
                    self.pizzas.append(pizza)
                else:
                    break

    def servirPizzas(self):
        # Limpiar la lista de pizzas después de servirlas
        self.pizzas = []

    def obtenerNombre(self) -> str:
        return self.nombre

    def obtenerPizzas(self) -> list:
        return self.pizzas

    def obtenerEstadoLibre(self) -> bool:
        # Retorna True si el mozo puede llevar más pizzas (es decir, lleva 0 o 1 pizza)
        return len(self.pizzas) < 2
