import tkinter as tk  # Importar tkinter como tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from mycode.mecanizado import mecanizado
from mycode.agregado_piezas import agregado_piezas
from mycode.zona_armado import zona_armado
from mycode.seccion_provedores import def_provedor
from mycode.control import control
from mycode.inicio import inicio
from mycode.dashboard import dashboard

# Crear ventana principal con ttkbootstrap
root = ttk.Window(themename="darkly")  # Tema inicial: Darkly
root.title("Fadeco Stock")
root.geometry("1335x720")  # wxh
root.iconbitmap("C:/Fadeco_stock/img/FLogo.ico")  # Ruta del icono

# Crear el Notebook para manejar las pestañas
ventana = ttk.Notebook(root)
ventana.grid(row=0, column=0, sticky="nsew")

# Agregar las pestañas
inicio(ventana)
agregado_piezas(ventana)
mecanizado(ventana)
def_provedor(ventana)
zona_armado(ventana)
control(ventana)
dashboard(ventana)

# Variable para almacenar el estado del tema


root.mainloop()
