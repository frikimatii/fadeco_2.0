import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk 
from mycode.dashboard_control.botones_datos.botones_mecanizado.plegadora import modificar_plegadora

def modificar_datos_retocados(parent):
    frame = ttk.Frame(parent)

    # Contenedor principal
    caja = ttk.Frame(frame)
    caja.grid(row=0, column=0, padx=10, pady=10)

    # Frame para contenido dinámico
    contenido_frame = ttk.Frame(caja)
    contenido_frame.grid(row=1, column=0, sticky="nsew")
    caja.rowconfigure(1, weight=1)
    caja.columnconfigure(0, weight=1)

    # Botones de herramientas
    botones_acciones = ttk.Frame(caja)
    botones_acciones.grid(row=0, column=0, sticky="n")

    herramientas = {
        "Plegadora": lambda: mostrar_contenido(contenido_frame, "PLEGADORA"),
        "Plasma": lambda: mostrar_contenido(contenido_frame, "PLASMA"),
        "Corte": lambda: mostrar_contenido(contenido_frame, "CORTE"),
        "Augeriado": lambda: mostrar_contenido(contenido_frame, "AUGERIADO"),
        "Torno": lambda: mostrar_contenido(contenido_frame, "TORNO"),
        "Fresa": lambda: mostrar_contenido(contenido_frame, "FRESA"),
        "Soldador": lambda: mostrar_contenido(contenido_frame, "SOLDADOR"),
        "Pulido": lambda: mostrar_contenido(contenido_frame, "PULIDO"),
        "Balancin": lambda: mostrar_contenido(contenido_frame, "BALANCIN"),
    }

    for idx, (nombre, comando) in enumerate(herramientas.items()):
        ttk.Button(botones_acciones, text=nombre, command=comando).grid(row=0, column=idx, padx=5, pady=5)

    def mostrar_contenido(contenido_frame, tipo_dato):
        for widget in contenido_frame.winfo_children():
            widget.destroy()

        frame = ttk.Frame(contenido_frame)
        frame.grid(row=0, column=0, sticky="nsew")

        if tipo_dato == "PLEGADORA":
            contenido = modificar_plegadora(frame)
            contenido.grid(row=0, column=0, sticky="nsew")

    return frame
