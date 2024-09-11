import tkinter as tk
from tkinter import ttk

from mycode.mecanizado import mecanizado
from mycode.agregado_piezas import agregado_piezas
from mycode.zona_armado import zona_armado
from mycode.seccion_provedores import def_provedor

root = tk.Tk()
root.title("FadeCo Stok")
root.geometry("1300x750")  # wxh

# Crear el Notebook para manejar las pestañas
ventana = ttk.Notebook(root)
ventana.grid(row=0, column=0, sticky="nsew")

# Agregar pestañas al Notebook

agregado_piezas(ventana)
mecanizado(ventana)
def_provedor(ventana)
zona_armado(ventana)

root.mainloop()