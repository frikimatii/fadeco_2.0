import tkinter as tk
from tkinter import ttk

# Importar funciones para el contenido de cada pestaña
from mycode.piezas.aluminio import aluminio
from mycode.piezas.chapa import chapa
from mycode.piezas.acero_dulce import acero_dulce
from mycode.piezas.compra import shop
from mycode.piezas.plastico import plastico
from mycode.piezas.tornilleria import tornillo
from mycode.piezas.hierro import hierro

def agregado_piezas(notebook_principal):
    # Crear una nueva pestaña en el notebook principal
    pestania_principal = ttk.Frame(notebook_principal)
    notebook_principal.add(pestania_principal, text='Agregado de Piezas')

    # Crear un Frame para el contenido de las pestañas
    contenido_frame = ttk.Frame(pestania_principal)
    contenido_frame.grid(row=0, column=2, sticky="nsew")

    # Crear un Frame para contener las pestañas verticales
    vertical_frame = ttk.Frame(pestania_principal)
    vertical_frame.grid(row=0, column=1, sticky="ns")

    # Crear botones para las pestañas verticales
    boton1 = ttk.Button(vertical_frame, text='Acero Dulce', command=lambda: mostrar_contenido(contenido_frame, 'acero_dulce'))
    boton2 = ttk.Button(vertical_frame, text='Aluminio', command=lambda: mostrar_contenido(contenido_frame, 'aluminio'))
    boton3 = ttk.Button(vertical_frame, text='Chapa', command=lambda: mostrar_contenido(contenido_frame, 'chapa'))
    boton4 = ttk.Button(vertical_frame, text='Shop', command=lambda: mostrar_contenido(contenido_frame, 'shop'))
    boton5 = ttk.Button(vertical_frame, text='Plástico', command=lambda: mostrar_contenido(contenido_frame, 'plastico'))
    boton6 = ttk.Button(vertical_frame, text='Tornillo', command=lambda: mostrar_contenido(contenido_frame, 'tornillo'))
    boton7 = ttk.Button(vertical_frame, text='Fundicion hierro', command=lambda: mostrar_contenido(contenido_frame, 'hierro'))


    # Empacar los botones verticalmente en el vertical_frame
    boton1.grid(row=0, column=0, sticky="ew")
    boton2.grid(row=1, column=0, sticky="ew")
    boton3.grid(row=2, column=0, sticky="ew")
    boton4.grid(row=3, column=0, sticky="ew")
    boton5.grid(row=4, column=0, sticky="ew")
    boton6.grid(row=5, column=0, sticky="ew")
    boton7.grid(row=6, column=0, sticky="ew")

    # Función para mostrar el contenido de la pestaña seleccionada
    def mostrar_contenido(contenido_frame, texto):
        for widget in contenido_frame.winfo_children():
            widget.destroy()  # Elimina el contenido actual
        if texto == 'acero_dulce':
            frame = acero_dulce(contenido_frame)
        elif texto == 'aluminio':
            frame = aluminio(contenido_frame)
        elif texto == 'chapa':
            frame = chapa(contenido_frame)
        elif texto == 'shop':
            frame = shop(contenido_frame)
        elif texto == 'plastico':
            frame = plastico(contenido_frame)
        elif texto == 'tornillo':
            frame = tornillo(contenido_frame)
        elif texto == 'hierro':
            frame = hierro(contenido_frame)
        frame.grid(row=0, column=0, sticky="nsew")

    # Mostrar el contenido de la primera pestaña por defecto
    mostrar_contenido(contenido_frame, 'acero_dulce')

    # Configurar el peso de las filas y columnas para el contenido
    pestania_principal.grid_rowconfigure(0, weight=1)
    pestania_principal.grid_columnconfigure(1, weight=0)  # Columna de los botones
    pestania_principal.grid_columnconfigure(2, weight=1)  # Columna de contenido

    # Configurar el peso de las filas y columnas para los frames internos
    contenido_frame.grid_rowconfigure(0, weight=1)
    contenido_frame.grid_columnconfigure(0, weight=1)
