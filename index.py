import tkinter as tk
from tkinter import ttk
from mycode.mecanizado import mecanizado
from mycode.porvedores import provedores
from mycode.agregado_piezas import agregado_piezas

root = tk.Tk()
root.title("FadeCo Stok")
root.geometry("1600x800")  # wxh

# Crear el Notebook para manejar las pestañas
ventana = ttk.Notebook(root)
ventana.grid(row=0, column=0, sticky="nsew")

# Agregar pestañas al Notebook

agregado_piezas(ventana)
mecanizado(ventana)
provedores(ventana)


root.mainloop()