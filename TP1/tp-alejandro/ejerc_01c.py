"""c. Escriba un procedimiento procesar_palabras(entrada) que acepte
 una secuencia de palabras separadas por coma, las ordene y las
  imprima. Suponiendo que la entrada provista al programa es la
   siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te"""

def procesar_palabras(entrada):
    # Eliminar todos los espacios de la entrada y pasa a minúsculas
    entrada_sin_espacios = entrada.replace(" ", "").lower()
    # Dividir la entrada en palabras usando la coma como separador
    lista_palabras = entrada_sin_espacios.split(",")
    # Ordenar la lista de palabras alfabéticamente
    lista_palabras.sort()
    # Unir las palabras en un string separado por comas
    resultado = ",".join(lista_palabras)
    return resultado

# Ejemplo de uso
frase = "Te,felicito,que,bien,actuas"
resultado = procesar_palabras(frase)
print(resultado)  # 'actuas,bien,felicito,que,te'
