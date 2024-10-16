import tkinter as tk
from tkinter import ttk
from pizzaVariedad import PizzaVariedad
#from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo
from auxiliar import *


def entregar():
    if mozo1.obtenerEstadoLibre(): 
        mozo1.tomarPizzas(mp.entregar())
        print("Entregando pizzas")
        refrescar_ordenes()
        actualizar_etiqueta_tomar(mozo1)
    if mozo2.obtenerEstadoLibre(): 
        mozo2.tomarPizzas(mp.entregar())
        print("Entregando pizzas")
        refrescar_ordenes()
        actualizar_etiqueta_tomar(mozo2)
# Instancias de PizzaVariedad
variedades = [
    PizzaVariedad("Muzzarella", 11000),
    PizzaVariedad("Margarita", 11430),
    PizzaVariedad("Napolitana", 13010),
    PizzaVariedad("Putanesca", 13550),
    PizzaVariedad("Jamón Cocido", 13550),
    PizzaVariedad("Americana", 19070),
    PizzaVariedad("Pepperoni", 19260),
    PizzaVariedad("Especial", 18030),
    PizzaVariedad("4 Quesos", 18330),
    PizzaVariedad("Provolone", 18330)
]

# Función para calcular el total
def calcular_total(event=None):
    total = 0
    for i in range(10):
        try:
            cantidad = int(cantidades[i].get())
            precio = float(variedades[i].obtenerPrecio())
            total += cantidad * precio
        except ValueError:
            pass
    total_label.config(text=f"Total: {total}")
    

# Función para obtener el número de órdenes
def obtener_numero_orden():
    return len(mp.obtenerOrdenes()) + 1

# Función para actualizar la etiqueta de número de orden
def actualizar_numero_orden():
    numero_orden = obtener_numero_orden()
    nOrden.config(text=f"N°: {numero_orden}")

def hacerOrden():
    # Crear una lista para almacenar las instancias de PizzaVariedad
    pizzas_pedidas = []
    pedido = generar_diccionario()
    # Recorrer el diccionario pedido
    for variedad, cantidad in pedido.items():
        # Buscar el precio de la variedad en la lista de variedades
        for var in variedades:
            if var.obtenerNombreVariedad() == variedad:
                # Crear las instancias según la cantidad
                for _ in range(cantidad):
                    pizza = Pizza(PizzaVariedad(variedad, var.obtenerPrecio()))
                    pizzas_pedidas.append(pizza)
    # Mostrar las pizzas pedidas
    for pizza in pizzas_pedidas:
        print(f"Variedad: {pizza.obtenerVariedad().obtenerNombreVariedad()}, Precio: {pizza.obtenerVariedad().obtenerPrecio()}")
        
    #print(orden)
    for cant in cantidades:
        cant.delete(0, tk.END)
        cant.insert(0, "0")
    if len(pizzas_pedidas) != 0:
        orden = Orden(len(mp.obtenerOrdenes())+1,pizzas_pedidas)    
        mp.tomarPedido(orden)
        actualizar_numero_orden()
    refrescar_ordenes()

cantidades = []

def generar_diccionario():
    pedido = {}
    for i, cantidad in enumerate(cantidades):
        try:
            cantidad_valor = int(cantidad.get())
            if cantidad_valor != 0:
                pedido[variedades[i].obtenerNombreVariedad()] = cantidad_valor
        except ValueError:
            pass
    return pedido
    

# Función para obtener el color de fondo según el estado
def obtener_color_estado(estado):
    colores = {1: "lightpink", 2: "lightgreen", 3: "lightgrey"}
    return colores.get(estado, "white")


# Función para refrescar el frame de órdenes
def refrescar_ordenes():
    # Limpiar el frame de órdenes
    for widget in ordenes_frame.winfo_children():
        widget.destroy()
    
    # Obtener las órdenes
    ordenesDirecta = mp.obtenerOrdenes()
    
    # Ordenar las órdenes en forma descendente por número de orden
    ordenes = ordenesDirecta[::-1]
    
    # Mostrar las órdenes en el frame
    for orden in ordenes:
        nro_orden = orden.obtenerNroOrden()
        estado = orden.obtenerEstadoOrden()
        precio = orden.calcularTotal()
        
        # Crear frame para cada orden
        orden_frame = tk.Frame(ordenes_frame, bg="white")
        orden_frame.pack(fill='x', pady=2)
      
        # Crear botón para el número de orden
        boton_orden = tk.Button(orden_frame, text=f"Orden {nro_orden}", command=lambda nro=nro_orden: [mostrarOrden(nro), print(f"Orden {nro} seleccionada")])
        boton_orden.pack(side="left", padx=5)
        
        # Crear etiqueta para el estado
        etiqueta_estado = tk.Label(orden_frame, text=f"Estado: {estado}", bg=obtener_color_estado(estado))
        etiqueta_estado.pack(side="left", padx=5, fill='x', expand=True)
        
        # Crear etiqueta para el precio
        etiqueta_precio = tk.Label(orden_frame, text=f"Precio: ${precio}")
        etiqueta_precio.pack(side="left", padx=5)
        
    # Asegurarse de que el Canvas se actualice con el tamaño del contenido
    ordenes_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Funciones para actualizar la etiqueta
def actualizar_etiqueta_tomar(mozo: Mozo):
    pizzas = mozo.obtenerPizzas()
    variedades = ", ".join([pizza.obtenerVariedad().obtenerNombreVariedad() for pizza in pizzas])
    mostrarOrden()
    if mozo1 == mozo:
        textoMozo1.set(f"{mozo.obtenerNombre()} tiene: {variedades}")
    else:
        textoMozo2.set(f"{mozo.obtenerNombre()} tiene: {variedades}")
        
def actualizar_etiqueta_servir(mozo: Mozo):
    mostrarOrden()
    if mozo1 == mozo:
        textoMozo1.set(mozo.obtenerNombre())
    else:
        textoMozo2.set(mozo.obtenerNombre())

#Muestra la orden seleccionada al hacer click en el boton Orden N° en la lista central de ordenes tomadas
ordenActual = 1
def mostrarOrden(num: int = None):
        global ordenActual
        if num is not None:  
            ordenActual = num
        else: 
            num = ordenActual
        # Obtener una orden
        ordenes = mp.obtenerOrdenes()
        for orden in ordenes:
            if num == orden.obtenerNroOrden():
                ordenFijada = orden
                break
            else:
                print(f"No se encontró ninguna orden con el número {num}")
        # Limpia el frame existente
        for widget in detalleOrden.winfo_children():
            widget.destroy()

        # Crear el nuevo contenido
        encabezado = tk.Label(detalleOrden, text=f"Orden N°: {ordenFijada.obtenerNroOrden()}", bg="darkgray", fg="white")
        encabezado.pack(fill='x')

        # Contar las cantidades y acumular precios por variedad
        contador_pizzas = {}
        for pizza in ordenFijada.obtenerPizzas():
            nombre_variedad = pizza.obtenerVariedad().obtenerNombreVariedad()
            if nombre_variedad in contador_pizzas:
                contador_pizzas[nombre_variedad]['cantidad'] += 1
                contador_pizzas[nombre_variedad]['precio'] += pizza.obtenerVariedad().obtenerPrecio()
            else:
                contador_pizzas[nombre_variedad] = {
                    'cantidad': 1,
                    'precio': pizza.obtenerVariedad().obtenerPrecio(),
                    'estado': pizza.obtenerEstado()
                }

        # Mostrar el detalle de las pizzas
        for nombre_variedad, datos in contador_pizzas.items():
            detalle = tk.Label(detalleOrden, text=f"{datos['cantidad']} x {nombre_variedad} ({datos['estado']}): ${datos['precio']}", bg=obtener_color_estado(datos['estado']))
            detalle.pack(fill='x', padx=5, pady=2)

        # Crear un frame para alinear el total a la derecha
        total_frame = tk.Frame(detalleOrden)
        total_frame.pack(fill='x', padx=5, pady=10, anchor='e')

        total = tk.Label(total_frame, text=f"Total: ${ordenFijada.calcularTotal()}")
        total.pack(side='right')
   
        
        
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Pizzeria Don Pipo")
ventana.geometry("840x440")

# Crear el maestro pizzero
mp = MaestroPizzero("Mario")

# Crear los mozos
mozo1 = Mozo("Alfredo")
mozo2 = Mozo("Guillermo")

# Primera columna
col1 = tk.Frame(ventana)
col1.grid(row=0, column=0, padx=10, pady=10, sticky="n")

tk.Label(col1, text="Maestro Pizzero", bg="lightgrey").grid(row=0, column=0, columnspan=3, sticky="ew")
tk.Label(col1, text=mp.obtenerNombre()).grid(row=1, column=0, columnspan=3, sticky="ew")
tk.Button(col1, text="Cocinar", command=lambda: [mp.cocinar(), refrescar_ordenes()]).grid(row=2, column=0, columnspan=3, sticky="ew")
tk.Button(col1, text="Entregar", command = lambda: entregar()).grid(row=3, column=0, columnspan=3, sticky="ew")

# Contenedor de orden
orden_frame = tk.Frame(col1,highlightbackground="darkgrey", highlightthickness=2)
orden_frame.grid(row=4, column=0, columnspan=3, pady=10, sticky="ew")
tk.Label(orden_frame, text="Orden").grid(row=0, column=0)
nOrden = tk.Label(orden_frame, text=f"N°: {len(mp.obtenerOrdenes())+1}")
nOrden.grid(row=0, column=1)

tk.Label(col1, text="Cantidad").grid(row=5, column=0)
tk.Label(col1, text="Pizza Variedad").grid(row=5, column=1)
tk.Label(col1, text="Precio").grid(row=5, column=2)

for i in range(10):
    cant = tk.Entry(col1, width=5)
    cant.grid(row=i+6, column=0)
    cant.insert(0, "0")
    cant.bind("<KeyRelease>", calcular_total)
    cantidades.append(cant)
    tk.Label(col1, text=variedades[i].obtenerNombreVariedad()).grid(row=i+6, column=1)
    tk.Label(col1, text="$ " + str(variedades[i].obtenerPrecio())).grid(row=i+6, column=2)

tk.Button(col1, text="Tomar Pedido", command=lambda: hacerOrden()).grid(row=16, column=0, sticky="w")
total_label = tk.Label(col1, text="Total $: 000000")
total_label.grid(row=16, column=1, columnspan=2, sticky="e")

# Segunda columna
col2 = tk.Frame(ventana)
col2.grid(row=0, column=1, padx=10, pady=10, sticky="n")
col2.grid_columnconfigure(1, minsize=270)

# Variable para el texto de la etiqueta nombre del mozo1
textoMozo1 = tk.StringVar()
textoMozo1.set(mozo1.obtenerNombre())

tk.Label(col2, text="Mozo 1", bg="lightgrey").grid(row=0, column=0, columnspan=3, sticky="ew")
tk.Label(col2, textvariable=textoMozo1).grid(row=1, column=0, columnspan=3, sticky="ew")
tk.Button(col2, text="Tomar Pizzas", command=lambda: [mozo1.tomarPizzas(mp.entregar()), refrescar_ordenes(),actualizar_etiqueta_tomar(mozo1)]).grid(row=2, column=0, columnspan=3, sticky="ew")
tk.Button(col2, text="Servir Pizzas", command=lambda: [mozo1.servirPizzas(), actualizar_etiqueta_servir(mozo1)]).grid(row=3, column=0, columnspan=3, sticky="ew")

# Área para órdenes
# Crear un Frame para contener el Canvas y el Scrollbar para el Área para órdenes
container = tk.Frame(col2)
container.grid(row=4, column=1, pady=10, sticky="nsew")

# Configurar el grid para que el container se expanda
col2.grid_rowconfigure(0, weight=1)
col2.grid_columnconfigure(0, weight=1)

# Crear un Canvas dentro del Frame para el Área para órdenes
canvas = tk.Canvas(container, bg="white", width=250, height=300)
canvas.grid(row=0, column=0, sticky="nsew")

# Crear un Scrollbar vertical y asociarlo con el Canvas para el Área para órdenes
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)

# Crear un Frame dentro del Canvas para el contenido de las órdenes
ordenes_frame = tk.Frame(canvas, bg="white", width=250, height=300)
orden_frame.grid(sticky="ew")
canvas.create_window((0, 0), window=ordenes_frame, anchor="nw")

# Tercera columna
col3 = tk.Frame(ventana)
col3.grid(row=0, column=2, padx=10, pady=10, sticky="n")
col3.grid_columnconfigure(1, minsize=270)

# Variable para el texto de la etiqueta nombre del mozo2
textoMozo2 = tk.StringVar()
textoMozo2.set(mozo2.obtenerNombre())

tk.Label(col3, text="Mozo 2", bg="lightgrey").grid(row=0, column=0, columnspan=3, sticky="ew")
tk.Label(col3, textvariable=textoMozo2).grid(row=1, column=0, columnspan=3, sticky="ew")
tk.Button(col3, text="Tomar Pizzas", command=lambda: [mozo2.tomarPizzas(mp.entregar()), refrescar_ordenes(),actualizar_etiqueta_tomar(mozo2)]).grid(row=2, column=0, columnspan=3, sticky="ew")
tk.Button(col3, text="Servir Pizzas", command=lambda: [mozo2.servirPizzas(), actualizar_etiqueta_servir(mozo2)]).grid(row=3, column=0, columnspan=3, sticky="ew")

# Área para detalle de orden
detalleOrden  = tk.Frame(col3, bg="white", width=270, height=300)
detalleOrden.grid(row=4, column=0, columnspan=3, pady=10, sticky="ew")

        
ventana.mainloop()


#TODO revisar los estados de pizza


