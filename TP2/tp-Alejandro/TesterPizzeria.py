from Pizza import *
from MaestroPizzero import *
from Mozo import *         
from Ventana1 import *      
import os
import time

class TesterPizzeria: 
  def main(self):
     ventana = Ventana1()
     def ejercicio4():            
          print('\nCreando mozo 1')
          mozo1 = Mozo("Alfredo")
          print('   Mozo 1 creado y se llama :' + str(mozo1.obtenerNombre()))
          mozo2 = Mozo("Alfredo")
          print('   Mozo 2 creado y se llama :' + str(mozo2.obtenerNombre()))
          mozo1.servirPizzas()
          print('i. ¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto? ')
          print('     ID mozo1: ' + str(id(mozo1)) + ' ID mozo2: ' + str(id(mozo2)) + '       ' 
               + str(" SI HACEN REFERENCIA AL MISMO OBJETO" 
                    if (id(mozo1)) == (id(mozo2)) else " NO HACEN REFERENCIA AL MISMO OBJETO"))
          print('ii. ¿Son objetos equivalentes? Explique que significa que dos objetos lo sean. ')
          print('     En este caso no son equivalentes pero podrian serlo')
          print('     La equivalencia de objetos depende de cómo se define el método')
          print('     __eq__ en la clase Mozo. Si __eq__ está implementado para comparar ')
          print('     los atributos relevantes (por ejemplo, el nombre), entonces mozo1 ')
          print('     y mozo2 podrían considerarse equivalentes si tienen los mismos valores ')
          print('     para esos atributos.')
          print('     class Mozo:')
          print('     def __init__(self, nombre):')
          print('     self.nombre = nombre\n')

          print('     def __eq__(self, other):')
          print('        return self.nombre == other.nombre\n')

          print('     mozo1 = Mozo("Alfredo")')
          print('     mozo2 = Mozo("Alfredo")')
          print('     print(mozo1 == mozo2)  # Esto devolverá True si __eq__ está definido como arriba\n')

          print('     En este caso, mozo1 y mozo2 serían considerados equivalentes porque tienen el mismo nombre.')

          print('iii. ¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria? \n' + 
               '      No comparten la misma posición de memoria')
          print('     ID mozo1: ' + str(id(mozo1)) + ' != ID mozo2: ' + str(id(mozo2)))
     def menu():
          opcion = 100
          while opcion:
               print('Elija una opción: ')
               print(f'Maestro Pizzero: {maestroPizzero.obtenerNombre()}           Mozo1: {mozo1.obtenerNombre()}            Mozo2: {mozo2.obtenerNombre()}        0] SALIR')
               print('1] Tomar pedido: Muzza           10] Tomar pizzas        20] Tomar pizzas      33] Ejercicio 4 del Tp2')
               print('2] Tomar pedido: Especial        11] Servir pizzas       21] Servir pizzas     34] GUI')      
               print('3] Tomar pedido: Palmitos        12] Pizzas para servir  22] Pizzas para servir')
               print('4] Tomar pedido: Rúcula y Jamón')
               print('5] Cocinar')
               print(f'6] Entregar al mozo1 {mozo1.obtenerNombre()}')
               print(f'7] Entregar al mozo2 {mozo2.obtenerNombre()}')
               print('8] Lista de pizzas a cocinar')
               print('9] Lista de pizzas cocinadas')
               try: 
                    opcion = input('Opcion: ')
                    match int(opcion):
                         case 0:
                              break
                         case 1:
                              maestroPizzero.tomarPedido("Muzza")
                         case 2:
                              maestroPizzero.tomarPedido("Especial")
                         case 3:
                              maestroPizzero.tomarPedido("Rúcula con Jamón")
                         case 4:
                              maestroPizzero.tomarPedido("Palmitos")
                         case 5:
                              maestroPizzero.cocinar()
                         case 6 | 10: 
                              mozo1.tomarPizzas(maestroPizzero.entregar(mozo1.manosLibres()))
                              print(f'El mozo1 {mozo1.obtenerNombre()} tomo las pizzas: {mozo1.obtenerNombrePizzasPorEntregar()}')
                         case 7 | 20:
                              mozo2.tomarPizzas(maestroPizzero.entregar(mozo2.manosLibres()))
                              print(f'El mozo2 {mozo2.obtenerNombre()} tomo las pizzas: {mozo2.obtenerNombrePizzasPorEntregar()}')
                         case 8:
                              print(maestroPizzero.obtenerNombrePizzasPorCocinar())
                         case 9:
                              print(maestroPizzero.obtenerNombrePizzasPorEntregar())
                         case 11:
                              mozo1.servirPizzas()
                         case 12:
                              print(f'{mozo1.obtenerNombre()} tiene {mozo1.obtenerNombrePizzasPorEntregar()}')
                         case 21:
                              mozo2.servirPizzas()
                         case 22:
                              print(f'{mozo2.obtenerNombre()} tiene {mozo2.obtenerNombrePizzasPorEntregar()}')
                         case 33:
                              ejercicio4()
                         case 34:
                              ventana.main()
                         case _ :
                              print('OPCION NO VALIDA')
                    time.sleep(2)

               except:
                    print('OPCION NO VALIDA')
                    time.sleep(2)
      
     #Crea al maestro pizzero Mario 
     print('\nCreando a maestro pizzero')
     maestroPizzero = MaestroPizzero("Mario")
     print('  El maestro pizzero ' + str(maestroPizzero.obtenerNombre()) + ' ha sido creado')
     #Creando Mozos
     print('\nCreando mozo 1')
     mozo1 = Mozo("Luigi")
     print('   Mozo 1 creado y se llama :' + str(mozo1.obtenerNombre()))
     mozo2 = Mozo("Alfredo")
     print('   Mozo 2 creado y se llama :' + str(mozo2.obtenerNombre()))

     #b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero. 
     maestroPizzero.tomarPedido("Muzza")                 #Maestro pizzero toma pedido de muzza
     maestroPizzero.tomarPedido("Especial")              #Maestro pizzero toma pedido de Especial
     maestroPizzero.tomarPedido("Rúcula con Jamón")      #Maestro pizzero toma pedido de Rucúla y Jamón
     maestroPizzero.cocinar()                            #Maestro pizzero cocina las pizzas 
     mozo1.tomarPizzas(maestroPizzero.entregar(mozo1.manosLibres()))
     print(f'El mozo1 {mozo1.obtenerNombre()} tomo las pizzas? {not mozo1.obtenerEstadoLibre()} {mozo1.obtenerNombrePizzasPorEntregar()}')
     print('Mozo sirviendo las pizzas', end='')
     mozo1.servirPizzas()
     print(f'El mozo1 {mozo1.obtenerNombre()} tiene las pizzas? {not mozo1.obtenerEstadoLibre()}  {mozo1.obtenerNombrePizzasPorEntregar()}')
     
     #maestroPizzero.cocinar()
     maestroPizzero.tomarPedido("Palmitos")
     #print(maestroPizzero.obtenerNombrePizzasPorEntregar())
     maestroPizzero.cocinar()
     #print(maestroPizzero.obtenerNombrePizzasPorEntregar())
     mozo2.tomarPizzas(maestroPizzero.entregar(mozo2.manosLibres()))
     print(f'El mozo2 {mozo2.obtenerNombre()} tomo las pizzas? {not mozo2.obtenerEstadoLibre()}')
     print(f'El mozo2 {mozo2.obtenerNombre()} tiene las pizzas: {mozo2.obtenerNombrePizzasPorEntregar()}')
     mozo2.servirPizzas()
     
     menu()  
if __name__ == '__main__':
    testerPizzeria = TesterPizzeria() 
    testerPizzeria.main()