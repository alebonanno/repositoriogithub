# mozo1 = Mozo('Alfredo')
# mozo2 = Mozo('Alfredo')

#i. ¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto?
# No.

# En Python, cuando creas dos objetos con el mismo constructor, como Mozo('Alfredo'), cada llamada al constructor crea un nuevo objeto en memoria, incluso si los atributos iniciales son idénticos. Por lo tanto, mozo1 y mozo2 son dos instancias diferentes de la clase Mozo que tienen el mismo nombre, pero son objetos distintos.

# Para comprobar esto, puedes usar el operador is que verifica si dos identificadores hacen referencia al mismo objeto en memoria:

#print(mozo1 is mozo2)  # Output: False

#Este código imprimirá False, confirmando que mozo1 y mozo2 no son el mismo objeto

# ii. ¿Son objetos equivalentes? Explique qué significa que dos objetos lo sean.
#Sí, los objetos son equivalentes.

#En Python, dos objetos son equivalentes si tienen el mismo valor para sus atributos, aunque sean instancias diferentes. En este caso, ambos objetos mozo1 y mozo2 tienen el atributo nombre igual a 'Alfredo'.

#Para comprobar si dos objetos son equivalentes, puedes definir un método especial __eq__ en la clase Mozo, que compara los valores de los atributos de dos instancias:

class Mozo:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom):
        self.nombre = nom

    def tomarPizzas(self, pizzas):
        if isinstance(pizzas, list) and len(pizzas) > 0:
            pizzas_a_tomar = pizzas[:2]
            self.pizzas.extend(pizzas_a_tomar)

    def servirPizzas(self):
        self.pizzas.clear()

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzas(self):
        return self.pizzas

    def obtenerEstadoLibre(self):
        return len(self.pizzas) <= 1

    def __eq__(self, other):
        if isinstance(other, Mozo):
            return self.nombre == other.nombre
        return False

#Con este método, puedes verificar la equivalencia de los objetos:

# print(mozo1 == mozo2)  # Output: True
#Este código imprimirá True, indicando que los objetos son equivalentes.

#iii. ¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria?
#No.

#Cada instancia de la clase Mozo se crea en una posición de memoria diferente. Aunque mozo1 y mozo2 pueden tener los mismos valores para sus atributos, ocupan lugares distintos en la memoria. Puedes verificar esto usando el método id() para obtener el identificador único de cada objeto:
#print(id(mozo1))  # Muestra la dirección de memoria de mozo1
#print(id(mozo2))  # Muestra la dirección de memoria de mozo2

#Cada llamada a id() retornará un valor diferente, confirmando que mozo1 y mozo2 están en diferentes posiciones de memoria.


