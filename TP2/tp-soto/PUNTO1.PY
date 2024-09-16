# PROBLEMA:La pizzería de Don Pipo cuenta con tres empleados, un maestro pizzero y dos mozos que
# se encargan de entregar los pedidos a los clientes. Cada mozo puede cargar hasta dos pizzas al
# mismo tiempo. El maestro pizzero puede cocinar todas las pizzas que se necesiten al mismo
# tiempo, pues las masas ya están estiradas desde temprano, los ingredientes listos en las
# heladeras y las instalaciones de la cocina así lo permiten. Este último no necesita descansar,
# aunque solo puede tomar un único pedido a la vez. 

class Pizza:
    def __init__(self, variedad):
        self.variedad = variedad

class MaestroPizzero:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nom):
        self.nombre = nom

    def tomarPedido(self, var):
        if var:  
            pizza = Pizza(var)
            self.pizzasPorCocinar.append(pizza)

    def cocinar(self):
        self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
        self.pizzasPorCocinar.clear()

    def entregar(self):
        pizzas_a_entregar = self.pizzasPorEntregar[:2]  
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]  
        return pizzas_a_entregar

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar
