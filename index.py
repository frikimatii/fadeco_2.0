import tkinter as tk
from tkinter import ttk

from mycode.mecanizado import mecanizado
from mycode.porvedores import provedores
from mycode.agregado_piezas import agregado_piezas
from mycode.zona_armado import zona_armado

root = tk.Tk()
root.title("FadeCo Stok")
root.geometry("1500x850")  # wxh

# Crear el Notebook para manejar las pestañas
ventana = ttk.Notebook(root)
ventana.grid(row=0, column=0, sticky="nsew")

# Agregar pestañas al Notebook

mecanizado(ventana)
agregado_piezas(ventana)
provedores(ventana)
zona_armado(ventana)


root.mainloop()