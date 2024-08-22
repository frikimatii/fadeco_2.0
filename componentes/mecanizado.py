import tkinter as tk
from tkinter import ttk
from componentes.mecanizado_def import mostrar_datos, limpiar_tabla, on_item_selected, agregar_proceso

tipo_de_mecanizado = ["corte", "plegadora", "torno", "augeriado", "plasma", "soldar", "freza", "balancin"]

def mecanizado(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Mecanizado")
#____________________________________Pestania_______________________________________

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="MEcanizado").grid(row=0, column=0, sticky="nsew")

#____________________________________box categoria_______________________________________

    box_categoria = ttk.Frame(index)
    box_categoria.grid(row=1, column=0)

    tk.Label(box_categoria, text="sctok de piezas para mecanizar. ").grid(row=0,column=0)
    tk.Label(box_categoria, text="Elija una opcion").grid(row=1,column=0)

    box_btn = tk.Frame(box_categoria)
    box_btn.grid(row=2, column=0)

    tk.Button(box_btn, text="PLEGADORA", command=lambda: mostrar_datos(mostrar_tablapiezas, "plegadora")).grid(row=0, column=0)
    tk.Button(box_btn, text="PLASMA", command=lambda: mostrar_datos(mostrar_tablapiezas, "plasma")).grid(row=0, column=1)
    tk.Button(box_btn, text="SOLDAR", command=lambda: mostrar_datos(mostrar_tablapiezas, "soldar")).grid(row=1, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=1, column=1)

    tk.Button(box_btn, text="PLASMA").grid(row=2, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=2, column=1)
    tk.Button(box_btn, text="PLASMA").grid(row=3, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=3, column=1)


    btn_limpiar = ttk.Button(box_categoria, text="limpiar", command=lambda: limpiar_tabla(mostrar_tablapiezas))
    btn_limpiar.grid(row=3, columnspan=2)

#____________________________________tabla_______________________________________

    box_tabla = ttk.Frame(index)
    box_tabla.grid(row=1, column=1)

    mostrar_tablapiezas = ttk.Treeview(box_tabla, columns=("Pieza", "Cantidad"))
    mostrar_tablapiezas.heading("Pieza",text="Pieza")
    mostrar_tablapiezas.heading("Cantidad",text="Cantidad")
    mostrar_tablapiezas.column("#0", width=5)
    mostrar_tablapiezas.column("Pieza", width=250)
    mostrar_tablapiezas.column("Cantidad", width=70)
    mostrar_tablapiezas.config(height=12)
    mostrar_tablapiezas.grid(row=0,column=0)

    mostrar_tablapiezas.bind("<<TreeviewSelect>>", lambda event: on_item_selected(event , mostrar_tablapiezas, pieza_seleccionada))


#____________________________________info acciones_______________________________________

    box_acciones = ttk.Frame(index)
    box_acciones.grid(row=1, column=2)
    tk.Label(box_acciones, text="Acciones").grid(row=0, column=0)
    
    tk.Label(box_acciones, text="Pieza Seleccionada").grid(row=1, column=0) 
    pieza_seleccionada = tk.Label(box_acciones, text="....")
    pieza_seleccionada.grid(row=1, column=1)

    tk.Label(box_acciones ,text="Cantidad:").grid(row=2, column=0)
    cantidad_acciones = ttk.Entry(box_acciones)
    cantidad_acciones.grid(row=2, column=1)


    box_btn = tk.Frame(box_acciones)
    box_btn.grid(row=4, columnspan=2)

    tk.Button(box_btn, text="PLEGADORA", command=lambda: agregar_proceso(cantidad_acciones, pieza_seleccionada, "plegadora", "plegadora")).grid(row=0, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=0, column=1)
    tk.Button(box_btn, text="SOLDAR").grid(row=1, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=1, column=1)

    tk.Button(box_btn, text="PLASMA").grid(row=2, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=2, column=1)
    tk.Button(box_btn, text="PLASMA").grid(row=3, column=0)
    tk.Button(box_btn, text="PLASMA").grid(row=3, column=1)
