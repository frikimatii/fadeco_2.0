import tkinter as tk
from tkinter import ttk
import sqlite3
import ttkbootstrap as ttk




def modificar_datosterminados(parent):
    frame = ttk.Frame(parent)

    # Contenedor principal
    caja = ttk.Frame(frame)
    caja.grid(row=0, column=0, padx=10, pady=10)

    # Título
    tk.Label(caja, text="Modificar Piezas Terminadas", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="n", pady=3)

    
    return frame
