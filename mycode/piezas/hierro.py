import tkinter as tk
from tkinter import ttk

def hierro(parent):
    frame = ttk.Frame(parent)
    
    # Crear un Frame para la tabla de piezas
    box2 = ttk.Frame(frame)
    box2.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box2, text="Tabla de piezas").grid(row=0, column=0, sticky="w")

    mostrar_piezas = ttk.Treeview(box2, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza")
    mostrar_piezas.heading("Cantidad", text="Cantidad")
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=200)
    mostrar_piezas.column("Cantidad", width=70)
    mostrar_piezas.config(height=20)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")

    # Configurar el peso para que el contenido se expanda
    box2.grid_rowconfigure(1, weight=1)
    box2.grid_columnconfigure(0, weight=1)

    return frame