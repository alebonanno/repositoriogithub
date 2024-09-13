
class Mozo():
    #<<Atributos de clase>>
    #<<Atributos de instancia>>
    def __init__(self, nombre): #string
        self.__nombre = nombre
        self.__pizzas = [] #Pizza[]
        #<<Constructores>>
        #Mozo(nom: string)
    #<<Comandos>>
    def establecerNombre(self, nom): #: string)
        self.__nombre = nom
    def tomarPizzas(self, pizzas): #Pizza[])          
        if not len(self.__pizzas): print('--Mozo: No hay pizzas para tomar')
        self.__pizzas.extend(pizzas)
    
        #Requiere pizzas ligado
    def servirPizzas(self):
        print(f'  {self.__nombre}: ', end='')
        if self.obtenerNombrePizzasPorEntregar():
            print(f'Sirviendo las pizzas de: {self.obtenerNombrePizzasPorEntregar()}')    
            self.__pizzas = []
        else:
            print('No tengo pizzas para entregar')
        
    #<<Consultas>>
    def obtenerNombre(self): #string
        return self.__nombre
    def obtenerPizzas(self): #Pizza[]
        return self.__pizzas
    def obtenerEstadoLibre(self): #boolean
        #return not bool(self.__pizzas)
        return True if len(self.__pizzas) < 2 else False
    def manosLibres(self):
        #print(self.__pizzas)
        if len(self.__pizzas) == 1:
            return 1
        elif self.obtenerEstadoLibre():
            return 2
        else: return 0
    def obtenerNombrePizzasPorEntregar(self):
        return [pizza.obtenerVariedad() for pizza in self.__pizzas]
    
    