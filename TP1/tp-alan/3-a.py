# 3. Sección C: Funciones matemáticas
# Resolver cada ejercicio en un archivo diferente.
# a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo
# que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a
# un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
# while).
# BONUS: Luego, codificar una función equivalente que utilice recursividad.




while True:
    numero = input("Ingrese un número entero: ")
    
    try:
        numero = int(numero)
        break  
    except ValueError:
        print("Ingrese un número válido, unicamente puede ser de tipo númerico") 


def suma(numero):
    resultado = 0  

    for index in range(1, numero + 1):
        resultado += index
    return resultado



resultado = suma(numero)

print(f"La suma del número 1 hasta {numero} es: {resultado}")
