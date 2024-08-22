import tkinter as tk
from tkinter import ttk
from componentes.stock_def import mostrar_categoria,on_item_selected, agregar_piezas

categoria = ["Aluminio", "Hierro", "Plastico", "Compra", "Chapa", "Tornilleria", "Fundidor"]

def stock(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="agregado de Piezas")
#____________________________________Pestania_______________________________________

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Agregado de Piezas").grid(row=0, column=0, sticky="nsew")


#____________________________________box categoria_______________________________________

    box_categoria = ttk.Frame(index)
    box_categoria.grid(row=1, column=0)

    tk.Label(box_categoria, text="Categorias").grid(row=0,column=0)
    tk.Label(box_categoria, text="Seleccione Una Categoria").grid(row=1,column=0)

    categoria_elejida = ttk.Combobox(box_categoria, values=categoria, state="readonly")
    categoria_elejida.grid(row=2, column=0)

    ttk.Button(box_categoria, text="Mostrar", command=lambda: mostrar_categoria(mostrar_piezas, categoria_elejida)).grid(row=3, column=0)

    btn_limpiar = ttk.Button(box_categoria, text="limpiar")
    btn_limpiar.grid(row=4, column=0)

#____________________________________tabla_______________________________________

    box_tabla = ttk.Frame(index)
    box_tabla.grid(row=1, column=1)

    mostrar_piezas = ttk.Treeview(box_tabla, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza",text="Pieza")
    mostrar_piezas.heading("Cantidad",text="Cantidad")
    mostrar_piezas.column("#0", width=5)
    mostrar_piezas.column("Pieza", width=250)
    mostrar_piezas.column("Cantidad", width=70)
    mostrar_piezas.config(height=12)
    mostrar_piezas.grid(row=0,column=0)

    mostrar_piezas.bind("<<TreeviewSelect>>", lambda event: on_item_selected(event, mostrar_piezas, pieza_seleccionada, detalles_pieazas))

#____________________________________acciones_______________________________________

    box_acciones = ttk.Frame(index)
    box_acciones.grid(row=1, column=2)


    tk.Label(box_acciones, text="Pieza Seleccionada").grid(row=0, column=0)

    pieza_seleccionada = tk.Label(box_acciones, text="...")
    pieza_seleccionada.grid(row=1, column=0)

    entry_cantidad_piezas = tk.Entry(box_acciones)
    entry_cantidad_piezas.grid(row=2, column=0)

    box_btn = tk.Frame(box_acciones)
    box_btn.grid(row=3, column=0)

    btn_agregar = ttk.Button(box_btn, text="Agregar", command=lambda: agregar_piezas(pieza_seleccionada, entry_cantidad_piezas, mostrar_piezas, acciones_realizada))
    btn_agregar.grid(row=0, column=1)

    tk.Label(box_acciones, text="Detalles De las Piezas").grid(row=4, column=0)

    detalles_pieazas = tk.Label(box_acciones, text="")
    detalles_pieazas.grid(row=5, column=0)

    tk.Label(box_acciones, text="accion").grid(row=6, column=0)

    acciones_realizada = tk.Label(box_acciones, text="")
    acciones_realizada.grid(row=7, column=0)
    

