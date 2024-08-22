# BONUS: Luego, codificar una función equivalente que utilice recursividad.


while True:
    numero = input("Ingrese un número entero: ")
    
    try:
        numero = int(numero)
        break  
    except ValueError:
        print("Ingrese un número válido, unicamente puede ser de tipo númerico") 


def suma_recursiva(numero):
 
    if numero == 1:
        return 1
    else:
        return numero + suma_recursiva(numero - 1)




resultado = suma_recursiva(numero)
print(f"La suma del número 1 hasta {numero} es: {resultado}")