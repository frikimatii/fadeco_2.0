import tkinter as tk
from tkinter import ttk

from mycode.funciones.add_funcion import on_item_selected, limpiar_tabla, mostrar_categoria, agregar_piezas, mostrar_datos

def shop(parent):
    frame = ttk.Frame(parent)
    
    box1 = ttk.Frame(frame)
    box1.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box1, text="Tabla de piezas").grid(row=0, column=0, sticky="w")


    mostrar_piezas = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza")
    mostrar_piezas.heading("Cantidad", text="Cantidad")
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=200)
    mostrar_piezas.column("Cantidad", width=70)
    mostrar_piezas.config(height=20)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")

    ttk.Button(box1, text="Limpiar Tabla", command= lambda: limpiar_tabla(mostrar_piezas)).grid(row=2, columnspan=2)


    box2 = ttk.Frame(frame)
    box2.grid(row=0, column=1)

    tk.Label(box2, text="Pieza q se Compra Afuera").grid(row=0, column=0)

    tk.Button(box2, text="Mostras Piezas de Compras", command= lambda: mostrar_categoria(mostrar_piezas, "shop", "piezas_brutas", detalles_pieazas, pieza_seleccionada)).grid(row=1, column=0)

    box_acciones = ttk.Frame(box2)
    box_acciones.grid(row=2, column=0)

    tk.Label(box_acciones, text="Agregado").grid(row=0, column=0, sticky="nsew")

    tk.Label(box_acciones, text="Pieza Seleccionada").grid(row=0, column=0)

    pieza_seleccionada = tk.Label(box_acciones, text="...")
    pieza_seleccionada.grid(row=1, column=0)

    entry_cantidad_piezas = tk.Entry(box_acciones)
    entry_cantidad_piezas.grid(row=2, column=0)

    box_btn = tk.Frame(box_acciones)
    box_btn.grid(row=3, column=0)

    btn_agregar = ttk.Button(box_btn, text="Agregar" ,command=lambda: agregar_piezas(pieza_seleccionada, entry_cantidad_piezas, mostrar_piezas, hisotrial, "shop", "piezas_brutas"))

    btn_agregar.grid(row=0, column=1)

    tk.Label(box_acciones, text="Detalles De las Piezas").grid(row=4, column=0)

    detalles_pieazas = tk.Label(box_acciones, text="")
    detalles_pieazas.grid(row=5, column=0)

    tk.Label(box_acciones, text="Historial").grid(row=6, column=0)

    hisotrial = tk.Listbox(box_acciones, width=50)
    hisotrial.grid(row=7, column=0)

    acciones_realizada = tk.Label(box_acciones, text="")
    acciones_realizada.grid(row=7, column=0)
    

    return frame
