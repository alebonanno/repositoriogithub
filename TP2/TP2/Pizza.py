

class Pizza():
    #<<Atributos de clase>> 
    #<<Atributos de instancia>> 
    def __init__(self, var): 
        self.__variedad = var #: string 
        #<<Constructores>> 
        #Variedad(var: string) 
    #<<Comandos>> 
    def establecerVariedad(self, var): #string) 
        self.__variedad = var
    #<<Consultas>> 
    def obtenerVariedad(self): #string
        return self.__variedad
    
