"""
1.e Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista e imprima ambas. La lista de números la ingresa el usuario en forma de números separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81
"""

def numeros_par_impar(entrada): 
  lista_impar_al_cuadrado = []
  for num in entrada:
    if num % 2 == 1:
      lista_impar_al_cuadrado.append(num*num)
      entrada.remove(num)
  print(entrada)
  print(lista_impar_al_cuadrado)

numeros_par_impar([1,2,3,4,5,6,7,8,9])