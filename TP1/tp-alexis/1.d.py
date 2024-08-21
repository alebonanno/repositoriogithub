"""
1.d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
que tome ambas como parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'e', 'd']
"""

def listas_diferencia(lista1, lista2):
  elementos_en_comun = []
  elementos_no_comunes = [];

  for elem1 in lista1:
    if elem1 in lista2:
      elementos_en_comun.append(elem1)
    else: 
      elementos_no_comunes.append(elem1)

  for elem2 in lista2:
    if elem2 not in lista1:
      elementos_no_comunes.append(elem2)

  elementos_en_comun.sort()
  elementos_en_comun.reverse()
  elementos_no_comunes.sort()

  print(elementos_en_comun)
  print(elementos_no_comunes)

listas_diferencia(["b", "a", "c"], ["e", "b", "d", "c"])