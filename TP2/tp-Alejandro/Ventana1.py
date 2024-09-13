from tkinter import *
from Pizza import *
from MaestroPizzero import *
from Mozo import *  

class Ventana1():
    def main(self):
        def pedido(pizza):
            maestroPizzero.tomarPedido(pizza)
            pizzasCrudas()
            
        def cocinando():
            maestroPizzero.cocinar()
            etqPizzasCrudas.config(text=" ")
            pizzasCocidas()
            
        def pizzasCrudas():
            pizzas_por_cocinar=maestroPizzero.obtenerNombrePizzasPorCocinar()
            pizzas_por_cocinar_texto = ", ".join(pizzas_por_cocinar)
            etqPizzasCrudas.config(text=pizzas_por_cocinar_texto) 
            print(maestroPizzero.obtenerNombrePizzasPorCocinar())
            
        def pizzasCocidas():
            pizzas_cocidas = maestroPizzero.obtenerNombrePizzasPorEntregar()
            pizzas_cocidas_texto = ", ".join(pizzas_cocidas)
            etqPizzasCocidas.config(text=pizzas_cocidas_texto)
            print(maestroPizzero.obtenerNombrePizzasPorEntregar())
            
        def entregarMozo1():
            while mozo1.obtenerEstadoLibre() and len(maestroPizzero.obtenerPizzasPorEntregar()): 
                mozo1.tomarPizzas(maestroPizzero.entregar(mozo1.manosLibres()))
            print(f'El mozo1 {mozo1.obtenerNombre()} tomo las pizzas: {mozo1.obtenerNombrePizzasPorEntregar()}')
            pizzasCocidas()
            mostrarPizzas1()
        def entregarMozo2():
            mozo2.tomarPizzas(maestroPizzero.entregar(mozo2.manosLibres()))
            print(f'El mozo2 {mozo2.obtenerNombre()} tomo las pizzas: {mozo2.obtenerNombrePizzasPorEntregar()}')
            pizzasCocidas()
            mostrarPizzas2()
            
        def sirviendo1():
            mozo1.servirPizzas()
            etqPantallaMozo1.config(text="                       ")
            
        def sirviendo2():
            mozo2.servirPizzas()
            etqPantallaMozo2.config(text="                       ")
            
        def mostrarPizzas1():
            pizzas_mozo1 = mozo1.obtenerNombrePizzasPorEntregar()
            pizzas_mozo1_texto = ", ".join(pizzas_mozo1)
            etqPantallaMozo1.config(text=pizzas_mozo1_texto)
            print(f'{mozo1.obtenerNombre()} tiene {mozo1.obtenerNombrePizzasPorEntregar()}')
            
        def mostrarPizzas2():
            pizzas_mozo2 = mozo2.obtenerNombrePizzasPorEntregar()
            pizzas_mozo2_texto = ", ".join(pizzas_mozo2)
            etqPantallaMozo2.config(text=pizzas_mozo2_texto)
            print(f'{mozo2.obtenerNombre()} tiene {mozo2.obtenerNombrePizzasPorEntregar()}')
            
        vent = Tk()
        vent.title("Pizzería Don Pipo")
        vent.attributes('-topmost', True)

        #vent.geometry("500x280")
        vent.minsize(width=660, height=400) #tamaño de la ventana
        vent.config(padx=35, pady=35) #separa el interior del borde de la ventana
        #Creando Maestro Pizzero Mario:
        maestroPizzero = MaestroPizzero("Mario")
        #Creando Mozos
        mozo1 = Mozo("Luigi")
        mozo2 = Mozo("Alfredo")
        
        etiqPrint = Label(vent)
        etiqPrint.grid(row=1, column=0, pady=6)
        
        #Comandos Maestro Pizzero
        etiqMPizzero = Label(vent,width=15,text="Maestro Pizzero", bg="#fbb")
        etiqMPizzero.grid(row=2,column=0, pady=6, padx=6)
        etiqNomMPizzero = Label(vent, text= maestroPizzero.obtenerNombre(), fg="#fbb")
        etiqNomMPizzero.grid(row=3,column=0)
        btnPedidoMuzza = Button(vent, width=15, text="Muzza", command=lambda: pedido("Muzza"))
        btnPedidoMuzza.grid(row=4, column=0, pady=6)
        btnPedidoEspecial = Button(vent, width=15, text="Especial", command=lambda: pedido("Especial"))
        btnPedidoEspecial.grid(row=5, column=0, pady=6)
        btnPedidoRJ = Button(vent,width=15, text="Rúcula con Jamón", command=lambda: pedido("Rúcula_con_Jamón"))
        btnPedidoRJ.grid(row=6, column=0, pady=6)
        btnPedidoPalmitos = Button(vent,width=15, text="Palmitos", command=lambda: pedido("Palmitos"))
        btnPedidoPalmitos.grid(row=7, column=0, pady=6)


        btnCocinar =Button(vent,width=15, text="Cocinar Pizzas",command=lambda: cocinando())
        btnCocinar.grid(row=8, column=0, pady=6)
        btnEntregarMozo1 = Button(vent, width=15, text="Entregar a mozo1", command=lambda: entregarMozo1())
        btnEntregarMozo1.grid(row=9,column=0,pady=6)
        btnEntregarMozo2 = Button(vent, width=15, text="Entregar a mozo2", command=lambda: entregarMozo2())
        btnEntregarMozo2.grid(row=10,column=0,pady=6)
        btnPizzasACocinar = Button(vent,width=15, text="Pizzas a Cocinar",command=lambda: pizzasCrudas())
        btnPizzasACocinar.grid(row=11, column=0, pady=6)
        btnPizzasACocinar = Button(vent,width=15, text="Pizzas Cocinadas",command=lambda: pizzasCocidas())
        btnPizzasACocinar.grid(row=12, column=0, pady=6)

        etqPizzasCrudas = Label(vent, text="Pizzas a Cocinar", bg="#fbb")
        etqPizzasCrudas.grid(row=11, column=1, columnspan=2, sticky="ew")
        etqPizzasCocidas = Label(vent, text="Pizzas Cocidas", bg="#fbb")
        etqPizzasCocidas.grid(row=12, column=1, columnspan=2, sticky="ew")
        #Comandos Mozo1
        etiqMozo1 = Label(vent,width=30,text="Mozo1", bg="#bfb")
        etiqMozo1.grid(row=2,column=1, pady=6, padx=6)
        etiqNomMozo1 = Label(vent, text= mozo1.obtenerNombre(), fg="#787")
        etiqNomMozo1.grid(row=3,column=1)
        btnMozo1TomaPizzas = Button(vent, width=15, text="Mozo1 tomar pizzas", command=lambda: entregarMozo1())
        btnMozo1TomaPizzas.grid(row=4, column=1, pady=6)
        btnMozo1SirvePizzas = Button(vent, width=15, text="Mozo1 Sirve pizzas", command=lambda: sirviendo1())
        btnMozo1SirvePizzas.grid(row=5, column=1, pady=6)
        btnMozo1TienePizzas = Button(vent, width=15, text="Pizzas de Mozo1", command=lambda: mostrarPizzas1())
        btnMozo1TienePizzas.grid(row=6, column=1, pady=6)
        etqPantallaMozo1 = Label(vent,text="Mozo1", bg="#bfb", pady=6)
        etqPantallaMozo1.grid(row=7, column=1, pady=6, sticky="ew")

        #Comandos Mozo2
        etiqMozo2 = Label(vent,width=30,text="Mozo2", bg="#bbf")
        etiqMozo2.grid(row=2,column=2, pady=6, padx=6)
        etiqNomMozo2 = Label(vent, text= mozo2.obtenerNombre(), fg="#bbf")
        etiqNomMozo2.grid(row=3,column=2)
        btnMozo2TomaPizzas = Button(vent, width=15, text="Mozo2 tomar pizzas", command=lambda: entregarMozo2())
        btnMozo2TomaPizzas.grid(row=4, column=2, pady=6)
        btnMozo2SirvePizzas = Button(vent, width=15, text="Mozo2 Sirve pizzas", command=lambda: sirviendo2())
        btnMozo2SirvePizzas.grid(row=5, column=2, pady=6)
        btnMozo2TienePizzas = Button(vent, width=15, text="Pizzas de Mozo2", command=lambda: mostrarPizzas2())
        btnMozo2TienePizzas.grid(row=6, column=2, pady=6)
        etqPantallaMozo2 = Label(vent,text="Mozo2", bg="#bbf", pady=6)
        etqPantallaMozo2.grid(row=7, column=2, pady=6, sticky="ew")

        vent.mainloop() #Es para que permanezca abierta

if __name__ == '__main__':
    vent = Ventana1() 
    vent.main()