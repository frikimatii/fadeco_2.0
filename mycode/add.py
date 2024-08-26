import tkinter as tk
from tkinter import ttk
from mycode.funciones.add_funcion import mostrar_categoria, limpiar_tabla, agregar_piezas

categoria = ["Aluminio", "Hierro", "Plastico", "Compra", "Chapa", "Tornilleria", "Acero_dulce"]

def add_piezas(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Agregado de Piezas")
#____________________________________Pestania_______________________________________

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Agregar Piezas").grid(row=0, columnspan=3, sticky="nsew")

    box1 = tk.Frame(index)
    box1.grid(row=1, column=0)

    tk.Label(box1, text="Botones").grid(row=0, column=0, sticky="nsew")
    tk.Label(box1, text="Seleccione una opcion para agregar piezas segun su tipo !!! ").grid(row=0, column=0, sticky="nsew")

    box_btn = tk.Frame(box1)
    box_btn.grid(row=2,column=0)

    ttk.Button(box_btn, text=categoria[0], command=lambda:
        mostrar_categoria(mostrar_piezas, "Aluminio", "piezas_brutas", detalles_pieazas, pieza_seleccionada)).grid(row=1, column=0)
    ttk.Button(box_btn, text=categoria[1], command=lambda: mostrar_categoria(mostrar_piezas, "Hierro", "piezas_brutas", detalles_pieazas, pieza_seleccionada)).grid(row=1, column=1)
    ttk.Button(box_btn, text=categoria[2], command=lambda:mostrar_categoria(mostrar_piezas, "Plastico", "piezas_brutas", detalles_pieazas, pieza_seleccionada) ).grid(row=2, column=0)
    ttk.Button(box_btn, text=categoria[3]).grid(row=2, column=1)
    ttk.Button(box_btn, text=categoria[4], command=lambda: mostrar_categoria(mostrar_piezas, "Chapa", "piezas_brutas", detalles_pieazas, pieza_seleccionada)).grid(row=3, column=0)
    ttk.Button(box_btn, text=categoria[5], command=lambda:
        mostrar_categoria(mostrar_piezas, "Tornilleria", "piezas_brutas", detalles_pieazas, pieza_seleccionada)).grid(row=3, column=1)
    ttk.Button(box_btn, text=categoria[6], command=lambda:
        mostrar_categoria(mostrar_piezas, "Acero_dulce", "piezas_brutas", detalles_pieazas, pieza_seleccionada)).grid(row=4, columnspan=2)
    ttk.Button(box_btn, text="Limpiar Tabla", command=lambda: limpiar_tabla(mostrar_piezas)).grid(row=5, columnspan=2)

    box_btn2 = tk.Frame(box1)
    box_btn2.grid(row=3, column=0)

    ttk.Button(box_btn2, text="Plasma").grid(row=0, column=0)
    ttk.Button(box_btn2, text="Corte").grid(row=1, column=0)



    box2 = tk.Frame(index)
    box2.grid(row=1, column=1)

    tk.Label(box2, text="Tabla de piezas").grid(row=0, column=0, sticky="nsew")

    mostrar_piezas = ttk.Treeview(box2, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza",text="Pieza")
    mostrar_piezas.heading("Cantidad",text="Cantidad")
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=200)
    mostrar_piezas.column("Cantidad", width=70)
    mostrar_piezas.config(height=20)
    mostrar_piezas.grid(row=0,column=0)

    box_acciones = ttk.Frame(index)
    box_acciones.grid(row=1, column=2)


    tk.Label(box_acciones, text="Agregado").grid(row=0, column=0, sticky="nsew")


    tk.Label(box_acciones, text="Pieza Seleccionada").grid(row=0, column=0)

    pieza_seleccionada = tk.Label(box_acciones, text="...")
    pieza_seleccionada.grid(row=1, column=0)

    entry_cantidad_piezas = tk.Entry(box_acciones)
    entry_cantidad_piezas.grid(row=2, column=0)

    box_btn = tk.Frame(box_acciones)
    box_btn.grid(row=3, column=0)

    btn_agregar = ttk.Button(box_btn, text="Agregar", command=lambda: agregar_piezas(pieza_seleccionada, entry_cantidad_piezas, mostrar_piezas, hisotrial))
    btn_agregar.grid(row=0, column=1)

    tk.Label(box_acciones, text="Detalles De las Piezas").grid(row=4, column=0)

    detalles_pieazas = tk.Label(box_acciones, text="")
    detalles_pieazas.grid(row=5, column=0)

    tk.Label(box_acciones, text="Historial").grid(row=6, column=0)

    hisotrial = tk.Listbox(box_acciones, width=50)
    hisotrial.grid(row=7, column=0)

    acciones_realizada = tk.Label(box_acciones, text="")
    acciones_realizada.grid(row=7, column=0)
    