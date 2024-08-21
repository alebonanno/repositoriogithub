"""e. Escribir un procedimiento numeros_par_impar(entrada) que, 
dada una lista de números, eleve cada elemento impar en ella al 
cuadrado y los mueva a otra lista e imprima ambas. La lista de 
números la ingresa el usuario en forma de números separados por 
coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81"""
entrada = input("Ingrese una lista de números separados por comas: ")
#entrada_string = '1,2,3,4,5,6,7,8,9'
entrada_sin_espacios = entrada_string.replace(" ", "")
lista_strings = entrada_sin_espacios.split(",")
lista_numeros = [int(num) for num in lista_strings]

def numeros_par_impar(lista_numeros):
  lista_pares = []
  lista_impares_cuadrados = []
  for n in lista_numeros:
    if n % 2 != 0:
      lista_impares_cuadrados.append(n**2)
    else:
      lista_pares.append(n)
  return lista_pares, lista_impares_cuadrados

print("Números ingresados:", lista_numeros)
print("Números pares:", numeros_par_impar(lista_numeros)[0])
print("Números impares al cuadrado:", numeros_par_impar(lista_numeros)[1])