<<<<<<< HEAD
'''c. Tal como sucede con la lógica proposicional, en Python
 muchas veces las expresiones booleanas pueden ser 
 simplificadas manteniendo el valor de verdad de la expresión.
   Así, por ejemplo, (a and b) or (b and a) es equivalente 
a a and b. A continuación, intente simplificar las siguientes
 expresiones y escriba un procedimiento 
 procesar_sentencias(a, b, c) que permita evaluar el 
valor de verdad de las expresiones ya simplificadas:
i. (a or b) or (b and c) 
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == True or b == False

Cortocicuito lógico:
x or y Si x es falso, entonces y; de otro modo, x
x and y Si x es falso, entonces x; de otro modo, y
not x Si x es falson entronces True, de otro modo, False

a   b   c   i   ii  iii iv
0   0   0   0   0   0   1
0   0   1   0   0   1   1
0   1   0   1   0   0   0
0   1   1   1   1   1   0
1   0   0   1   0   0   1
1   0   1   1   0   1   1
1   1   0   1   0   1   1
1   1   1   1   1   1   1


Ecuaciones simplificadas:
i. a or b 
ii. b and c
iii. a and b or c
iv. a or not b
'''
print('i.(a or b) or (b and c)    simplificada a or b ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           {(a or b) or (b and c)}                  {a or b}')

print('ii. b and c or False    simplificada b and c ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           {b and c or False}                  {b and c}')

print('iii. a and b or c or (b and a)    simplificada a and b or c ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           {a and b or c or (b and a)}                  {a and b or c}')

print('iv. a == True or b == False    simplificada a or not b ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           { a == True or b == False}                  {a or not b}')

=======
'''c. Tal como sucede con la lógica proposicional, en Python
 muchas veces las expresiones booleanas pueden ser 
 simplificadas manteniendo el valor de verdad de la expresión.
   Así, por ejemplo, (a and b) or (b and a) es equivalente 
a a and b. A continuación, intente simplificar las siguientes
 expresiones y escriba un procedimiento 
 procesar_sentencias(a, b, c) que permita evaluar el 
valor de verdad de las expresiones ya simplificadas:
i. (a or b) or (b and c) 
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == True or b == False

Cortocicuito lógico:
x or y Si x es falso, entonces y; de otro modo, x
x and y Si x es falso, entonces x; de otro modo, y
not x Si x es falson entronces True, de otro modo, False

a   b   c   i   ii  iii iv
0   0   0   0   0   0   1
0   0   1   0   0   1   1
0   1   0   1   0   0   0
0   1   1   1   1   1   0
1   0   0   1   0   0   1
1   0   1   1   0   1   1
1   1   0   1   0   1   1
1   1   1   1   1   1   1


Ecuaciones simplificadas:
i. a or b 
ii. b and c
iii. a and b or c
iv. a or not b
'''
print('i.(a or b) or (b and c)    simplificada a or b ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           {(a or b) or (b and c)}                  {a or b}')

print('ii. b and c or False    simplificada b and c ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           {b and c or False}                  {b and c}')

print('iii. a and b or c or (b and a)    simplificada a and b or c ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           {a and b or c or (b and a)}                  {a and b or c}')

print('iv. a == True or b == False    simplificada a or not b ')
            
for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
            print(f'           { a == True or b == False}                  {a or not b}')

>>>>>>> a5b1d41688712504ffb252ba1031fcc4246d4181
