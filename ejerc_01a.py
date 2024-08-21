"""Escribir una función de nombre palabra_no_tiene_letras(palabra,
 letras_prohibidas), la cual retorne True si es que los 
 caracteres que componen una palabra no se encuentran en una 
 lista de caracteres prohibidos."""




letras_prohibidas = []

while True:
    letra = input("Ingresa una letra (escribe 'exit' para salir): ")
    if letra.lower() == 'exit':
        break
    letras_prohibidas.append(letra)
    print(f"Has ingresado: {letra}")

print("Letras prohibidas:", letras_prohibidas)

# Ingresar una palabra
palabra = input("Ingresa una palabra: ")

# Definir la función
def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

# Llamar a la función
resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
# Usando expresión ternaria
print(f"La palabra '{palabra}' {'no contiene' if resultado else 'contiene'} letras prohibidas.")