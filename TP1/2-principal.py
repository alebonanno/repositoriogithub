import time
from funciones import Edad

def main():
    # Ingreso de datos del usuario
    nombre = input("Ingrese su nombre: ")

    while True:
        edad = input("Ingrese su edad: ")
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("Por favor, ingrese un número válido para la edad.")
    
    # Crear instancia de la clase Edad
    persona = Edad(nombre, edad)

    # Calcular los días y meses
    dias = persona.calcular_dias()
    meses = persona.calcular_meses()

    # Imprimir la edad del usuario
    print(f"La edad de {persona.nombre} es {persona.edad} años o {meses} meses o {dias} días")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
