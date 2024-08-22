import tkinter as tk
from tkinter import ttk

categoria = ["carmelo", "maxi", "pintor", "afilador", "niquelado", "soldador"]

def provedores(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="provedores")
#____________________________________Pestania_______________________________________

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Provedores").grid(row=0, column=0, sticky="nsew")
#____________________________________box categoria_______________________________________

    box_categoria = ttk.Frame(index)
    box_categoria.grid(row=1, column=0)

    tk.Label(box_categoria, text="Seleccione un Provedor").grid(row=0,column=0)
    tk.Label(box_categoria, text="Seleccione Un Provedor").grid(row=1,column=0)

    categoria_elejida = ttk.Combobox(box_categoria, values=categoria, state="readonly")
    categoria_elejida.grid(row=2, column=0)

    ttk.Button(box_categoria, text="Mostrar").grid(row=3, column=0)

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

#____________________________________acciones_______________________________________

    box_acciones = ttk.Frame(index)
    box_acciones.grid(row=1, column=2)

    tk.Label(box_acciones, text="Pieza Seleccionada").grid(row=0, column=0)

    pieza_seleccionada = tk.Label(box_acciones, text="...")
    pieza_seleccionada.grid(row=1, column=0)
