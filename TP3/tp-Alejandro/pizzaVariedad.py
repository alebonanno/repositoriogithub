class PizzaVariedad:
    #Atributos de clase
    #Constructores
    def __init__(self, nomVar: str, pre: float):
        self.__nombreVariedad = nomVar
        self.__precio = pre
    #Comandos
    def establecerNombreVariedad(self, nomVar: str):
         self.__nombreVariedad = nomVar
    
    def establecerPrecio(self, pre: float):
         self.__precio = pre
         
    #Consultas
    def obtenerNombreVariedad(self) -> str:
        return self.__nombreVariedad 
    
    def obtenerPrecio(self) -> float:
        return self.__precio
   