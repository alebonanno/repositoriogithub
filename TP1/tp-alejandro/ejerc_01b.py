"""Escribir una función de nombre es_abc(palabra) la cual retorne
 True siempre y cuando las letras que componen dicha palabra 
 estén en orden alfabético, y False en caso contrario."""


# Ingresar una palabra
palabra = input("Ingresa una palabra: ")

def es_abc(palabra):
    return list(palabra.lower()) == sorted(palabra.lower())

# Llamar a la función
resultado = es_abc(palabra)
print(f"La palabra '{palabra}' {'Está ordenada alfabeticamente' if resultado else 'No está ordenada alfabeticamente'} ")