class Pizza:
    def __init__(self, var):
        self.variedad = var

    def establecerVariedad(self, var):
        self.variedad = var

    def obtenerVariedad(self):
        return self.variedad


class MaestroPizzero:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nom):
        self.nombre = nom

    def tomarPedido(self, var):
        if var:  # Asegura que var no esté vacío
            pizza = Pizza(var)
            self.pizzasPorCocinar.append(pizza)

    def cocinar(self):
        self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
        self.pizzasPorCocinar.clear()

    def entregar(self):
        pizzas_a_entregar = self.pizzasPorEntregar[:2]  # Obtiene hasta 2 pizzas
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]  # Elimina las entregadas
        return pizzas_a_entregar

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar


class Mozo:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom):
        self.nombre = nom

    def tomarPizzas(self, pizzas):
        if isinstance(pizzas, list) and len(pizzas) > 0:
            pizzas_a_tomar = pizzas[:2]  # Tomar hasta 2 pizzas
            self.pizzas.extend(pizzas_a_tomar)

    def servirPizzas(self):
        self.pizzas.clear()

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzas(self):
        return self.pizzas

    def obtenerEstadoLibre(self):
        return len(self.pizzas) <= 1


class TesterPizzeria:
    def main(self):
        # Crear un objeto de tipo MaestroPizzero
        maestro = MaestroPizzero("Don Pipo")

        # Crear dos objetos de tipo Mozo
        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Beatriz")

        # Crear algunos objetos de tipo Pizza
        pizza1 = Pizza("Margarita")
        pizza2 = Pizza("Pepperoni")
        pizza3 = Pizza("Cuatro Quesos")

        # 1. Enviar mensajes tomarPedido al MaestroPizzero
        maestro.tomarPedido(pizza1.obtenerVariedad())
        maestro.tomarPedido(pizza2.obtenerVariedad())
        maestro.tomarPedido(pizza3.obtenerVariedad())

        # 2. Enviar mensaje cocinar al MaestroPizzero
        maestro.cocinar()

        # 3. Enviar mensaje entregar al MaestroPizzero
        pizzas_entregadas = maestro.entregar()
        print(f"Pizzas entregadas: {[pizza.obtenerVariedad() for pizza in pizzas_entregadas]}")

        # 4. Enviar mensaje tomarPizzas a los mozos
        mozo1.tomarPizzas(maestro.obtenerPizzasPorEntregar())
        mozo2.tomarPizzas(maestro.obtenerPizzasPorEntregar())

        # 5. Mostrar estado de los mozos
        print(f"Pizzas en mozo1: {[pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()]}")
        print(f"Pizzas en mozo2: {[pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()]}")

        # 6. Enviar mensaje servirPizzas a los mozos
        mozo1.servirPizzas()
        mozo2.servirPizzas()

        # 7. Mostrar el estado de las listas de pizzas de los mozos después de servir
        print(f"Pizzas en mozo1 después de servir: {[pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()]}")
        print(f"Pizzas en mozo2 después de servir: {[pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()]}")

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
