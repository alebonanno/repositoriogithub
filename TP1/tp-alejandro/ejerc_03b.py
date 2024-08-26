'''b. Escribir un programa que resuelva la secuencia de 
Fibonacci a pedido del usuario. Deberá codificar una función 
fibonacci(numero), cuyo parámetro numero debe ser ingresado 
por el usuario y su tipo, al igual que en el ejercicio
anterior, validado. La función debe encargarse de calcular la
 secuencia para dicho número. A continuación, una descripción
   matemática de la famosa secuencia:
   '''
#Función que suma todos los numeros desde el valor ingresado hasta 0 admite enteros negativos y positivos 
def sumaFibonacci(numero):
    signo = -1 if numero < 0 else 1
    sumatoria = 0
    if numero == 0: 
        return 0
    elif numero == 1: 
        return 1 * signo
    else:
        return sumaFibonacci(numero-(1*signo)) + numero

#Función que suma al igual que la anterior pero en forma recursiva
def suma_recursiva(numero):

    if numero > 0:
        return numero + suma_recursiva(numero - 1)
    elif numero < 0:
        return numero + suma_recursiva(numero + 1)
    else:
        return 0
#Ingreso y validación de datos, entero positivo o negativo y 0    
while True:
    numero = input("Ingrese un número entero: ")
    try:
        numero = int(numero)
        break  
    except ValueError:
        print("Eso no es un número entero. Inténtalo de nuevo.")

print(f"El número ingresado es: {numero}")
print(f'La sumatoria de fibonacci para el número {numero} es {sumaFibonacci(numero)}')