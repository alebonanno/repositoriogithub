# c. Tal como sucede con la lógica proposicional, en Python muchas veces las
# expresiones booleanas pueden ser simplificadas manteniendo el valor de
# verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
# a a and b. A continuación, intente simplificar las siguientes expresiones y
# escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
# valor de verdad de las expresiones ya simplificadas:


# i. (a or b) or (b and c)
# ii. b and c or False
# iii. a and b or c or (b and a)
# iv. a == True or b == False



def procesar_sentencias(a, b, c):
  
    resultado_1 = a or b                   
    resultado_2 = b and c                  
    resultado_3 = a and b or c               
    resultado_4 = a or not b                 
    
    return resultado_1, resultado_2, resultado_3, resultado_4

a = True
b = False
c = True

resultados = procesar_sentencias(a, b, c)
print(resultados)