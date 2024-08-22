# b. Escribir un programa que resuelva la secuencia de Fibonacci a pedido del
# usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro
# numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio
# anterior, validado. La función debe encargarse de calcular la secuencia para
# dicho número. A continuación, una descripción matemática de la famosa
# secuencia:


def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero para calcular la secuencia fibonacci: "))
            if numero < 0:
                print("El número debe ser positivo")
            else:
                return numero
        except ValueError:
            print("Debes ingresar un número de tipo numerico")


def fibonacci(numero):
  
    if numero < 0:
         return print("El número debe ser un entero no negativo.")
    

    resultado_fibonacci = []
    
    a = 0
    b = 1
    

    for i in range(numero):
        resultado_fibonacci.append(a)
        proximo_numero = a + b
        a = b
        b = proximo_numero
    
    return resultado_fibonacci




numero = pedir_numero()

resultado = fibonacci(numero)

print("La secuencia fibonacci es:")
print(resultado)
