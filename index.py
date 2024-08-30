import tkinter as tk 
from tkinter import ttk

from mycode.add import add_piezas
from mycode.mecanizado import mecanizado
from mycode.porvedores import provedores
root = tk.Tk()
root.title("FadeCo Stok")
root.geometry("1600x800") #wxh

ventana = ttk.Notebook(root)
ventana.grid(row=0, column=0)

add_piezas(ventana)
mecanizado(ventana)
provedores(ventana)

root.mainloop() 