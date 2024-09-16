class Pizza:
    def __init__(self, var):
        self.variedad = var

    def establecerVariedad(self, var):
        self.variedad = var

    def obtenerVariedad(self):
        return self.variedad

if __name__ == "__main__":
 
    pizza = Pizza("Margarita")

    print(f"Variedad inicial de la pizza: {pizza.obtenerVariedad()}") 

    pizza.establecerVariedad("Pepperoni")


    print(f"Variedad actual de la pizza: {pizza.obtenerVariedad()}")

