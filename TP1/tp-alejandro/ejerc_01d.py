"""d. Dadas dos listas, lista1 y lista2, escribir un método
 listas_diferencia(lista1, lista2) que tome ambas como
  parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'e', 'd']"""


def listas_diferencia(lista1, lista2):
    # Inicializar listas para elementos comunes y no comunes
    comunes = []
    no_comunes = []

    # Encontrar elementos comunes
    for elemento in lista1:
        if elemento in lista2 and elemento not in comunes:
            comunes.append(elemento)

    for elemento in lista2:
        if elemento in lista1 and elemento not in comunes:
            comunes.append(elemento)

    # Encontrar elementos no comunes
    for elemento in lista1:
        if elemento not in lista2 and elemento not in no_comunes:
            no_comunes.append(elemento)

    for elemento in lista2:
        if elemento not in lista1 and elemento not in no_comunes:
            no_comunes.append(elemento)

    # Ordenar las listas según lo solicitado
    comunes.sort(reverse=True)
    no_comunes.sort()

    # Imprimir los resultados
    print(comunes)
    print(no_comunes)


listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])