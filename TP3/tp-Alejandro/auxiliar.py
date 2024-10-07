from pizzaVariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo


estPizza = {
    1: "Cruda",
    2: "Cocida",
    3: "Despachada de cocina"
}

estOrden = {
    1: "Tomando orden",
    2: "Salió del horno",
    3: "Fue entregada"
}
class Auxiliar():
    
    
    def mostrarPizzasMaestro(self, nombre: MaestroPizzero, orden: Orden = None) -> str:
        mensaje = "Pizzas: "
        partes = []  # Lista para almacenar las partes del mensaje
        if orden not in nombre.obtenerOrdenes() and orden != None: return "Esa orden no la tiene el maestro pizzero"
        
        if orden is not None:
            # Mostrar solo las pizzas de la orden específica
            for pizza in orden.obtenerPizzas():
                parte = pizza.obtenerVariedad().obtenerNombreVariedad() + ", estado: " + estPizza[pizza.obtenerEstado()]
                partes.append(parte)
        else:
            
            # Mostrar todas las pizzas de todas las órdenes
            for orden in nombre.obtenerOrdenes():
                for pizza in orden.obtenerPizzas():
                    parte = pizza.obtenerVariedad().obtenerNombreVariedad() + ", estado: " + estPizza[pizza.obtenerEstado()]
                    partes.append(parte)

        mensaje += ", ".join(partes)  # Unir las partes con una coma
        return mensaje
    
    def mostrarPizzasMozo(self, nombre: Mozo) -> str:
        mensaje = "Pizzas: "
        partes = []  # Lista para almacenar las partes del mensaje
        for pizza in nombre.obtenerPizzas():
            parte = pizza.obtenerVariedad().obtenerNombreVariedad() + ", estado: " + estPizza[pizza.obtenerEstado()]
            partes.append(parte)

        mensaje += ", ".join(partes)  # Unir las partes con una coma
        return mensaje
 
    def status(self, mP: MaestroPizzero) -> dict:
        estado_ordenes = {}
        
        for orden in mP.obtenerOrdenes():
            numOrden = orden.obtenerNroOrden()
            estadoOrden = orden.obtenerEstadoOrden()
            estadoOrdenTexto = estOrden.get(estadoOrden, "Estado desconocido")
            totalOrden = orden.calcularTotal()
            
            for pizza in orden.obtenerPizzas():
                nombre_variedad = pizza.obtenerVariedad().obtenerNombreVariedad()
                estado_pizza = pizza.obtenerEstado()
                estadoPizzaTexto = estPizza.get(estado_pizza, "Estado desconocido")
                precioPizza = pizza.obtenerVariedad().obtenerPrecio()
                
                if numOrden not in estado_ordenes:
                    estado_ordenes[numOrden] = {
                        'estado de la orden': f"{estadoOrden} - {estadoOrdenTexto}",
                        'total de la orden': totalOrden,
                        'pizzas': []
                    }
                
                estado_ordenes[numOrden]['pizzas'].append({
                    'nombre variedad': nombre_variedad,
                    'estado de la pizza': f"{estado_pizza} - {estadoPizzaTexto}",
                    'precio': precioPizza
                })
        
        return estado_ordenes
    
    def imprimir_estado_ordenes(self, estado_ordenes: dict):
        for numOrden, detalles in estado_ordenes.items():
            print(f"Orden Número: {numOrden}")
            print(f"  Estado de la Orden: {detalles['estado de la orden']}")
            print(f"  Total de la Orden: {detalles['total de la orden']}")
            print("  Pizzas:")
            for pizza in detalles['pizzas']:
                print(f"    - Variedad: {pizza['nombre variedad']}, Estado: {pizza['estado de la pizza']}, Precio: {pizza['precio']}")
            print()  # Línea en blanco para separar órdenes

    def totalCostoEntregadas(self, mP: MaestroPizzero):
        total = 0
        for orden in mP.obtenerOrdenes():
            for pizza in orden.obtenerPizzas():
                total += pizza.obtenerVariedad().obtenerPrecio()
        return total
    
 