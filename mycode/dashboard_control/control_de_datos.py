import tkinter as tk
from tkinter import ttk
import sqlite3
import ttkbootstrap as ttk 

from mycode.dashboard_control.botones_datos.modificar_datosbrutos import modificar_datosbrutos
from mycode.dashboard_control.botones_datos.modificar_datosterminados import modificar_datosterminados
from mycode.dashboard_control.botones_datos.modificar_datosRetocados import modificar_datos_retocados
from mycode.dashboard_control.botones_datos.modificar_datospulidos import modificar_datospulidos

def control_datos(parent):
    frame = ttk.Frame(parent)

    # Encabezado
    header_frame = ttk.Frame(frame)
    header_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=5, columnspan=2)
    ttk.Label(header_frame, text="Modificar Datos", font=("Arial", 18, "bold")).grid(row=0, column=0, sticky="w")

    # Caja de botones
    caja_botones = ttk.Frame(header_frame)
    caja_botones.grid(row=1, column=0, columnspan=5)

    # Contenedor para contenido dinámico
    contenido_frame = ttk.Frame(frame)
    contenido_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    # Configuración del layout para redimensionamiento
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(0, weight=1)
    contenido_frame.rowconfigure(0, weight=1)
    contenido_frame.columnconfigure(0, weight=1)

    # Botones con sus respectivos comandos
    brutas = ttk.Button(caja_botones, text="Piezas Brutas", padding=10,command=lambda: mostrar_contenido(contenido_frame, "Piezas_brutas"))
    brutas.grid(row=0, column=1, pady=5, padx=10)

    piezas_retocadas = ttk.Button(caja_botones, text="Piezas Retocadas", padding=10,command=lambda: mostrar_contenido(contenido_frame, "piezas_retocadas"))
    piezas_retocadas.grid(row=0, column=2, pady=5, padx=10)

    terminadas = ttk.Button(caja_botones, text="Piezas Terminadas", padding=10, command=lambda: mostrar_contenido(contenido_frame, "piezas_terminada"))
    terminadas.grid(row=0, column=3, pady=5, padx=10)

    afilador_roman = ttk.Button(caja_botones, text="Piezas Pulidas", padding=10,command=lambda: mostrar_contenido(contenido_frame, "piezas_pulidas"))
    afilador_roman.grid(row=0, column=4, pady=5, padx=10)



    # Función para cambiar el contenido dinámico
    def mostrar_contenido(contenido_frame, tipo_dato):
        # Limpiar el contenido actual
        for widget in contenido_frame.winfo_children():
            widget.destroy()

        # Frame para el contenido específico
        frame = ttk.Frame(contenido_frame)
        frame.grid(row=0, column=0, sticky="nsew")


        # Mostrar contenido según el tipo de dato
        if tipo_dato == "Piezas_brutas":
            contenido = modificar_datosbrutos(frame)
            contenido.grid(row=1, column=0, sticky="nsew")
        elif tipo_dato == "piezas_retocadas":
            contenido = modificar_datos_retocados(frame)
            contenido.grid(row=1, column=0, sticky="nsew")
        elif tipo_dato == "piezas_terminada":
            contenido = modificar_datosterminados(frame)
            contenido.grid(row=1, column=0, sticky="nsew")
        elif tipo_dato == "piezas_pulidas":
            contenido = modificar_datospulidos(frame)
            contenido.grid(row=1, column=0, sticky="nsew")
        
    return frame