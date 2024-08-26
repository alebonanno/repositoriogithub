'''a. Escribir una función suma(numero) que resuelva la 
siguiente suma, asumiendo
que numero = 10:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
En el programa que invoque dicha función:
i. El usuario debe poder ingresar el valor del parámetro 
numero.
ii. Debe validarse que el dato ingresado por el usuario 
corresponda a
un dígito, y no a otro tipo de dato como un carácter.
iii. El cálculo debe realizarse utilizando algún tipo de 
bucle (ej: for,
while).
BONUS: Luego, codificar una función equivalente que utilice 
recursividad.'''
#Función que suma todos los numeros desde el valor ingresado hasta 0 admite enteros negativos y positivos 
def suma(numero):
    signo = -1 if numero < 0 else 1
    sumatoria = 0
    for i in range(abs(numero)+1):
        sumatoria += i
    return sumatoria * signo

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
print(f'La sumatoria del tipo 1+2+3+4+5+6+7+8+9+10 para el número {numero} es {suma(numero)}')
print(f' y usando la función recursiva da: {suma_recursiva(numero)}')