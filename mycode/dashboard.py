import tkinter as tk
from tkinter import ttk
import sqlite3
import ttkbootstrap as ttk  # Asegúrate de tener importado ttkbootstrap

# Importa tus funciones desde el código de cada ventana
from mycode.dashboard_control.pieza_brutas import ventana_piezas_brutas
from mycode.dashboard_control.piezas_termindas import ventana_piezas_terminadas 

def dashboard(notebook_principal):
    # Frame de la pestaña principal
    pestania_principal = ttk.Frame(notebook_principal)
    notebook_principal.add(pestania_principal, text="Panel De Control")
    
    # Frame principal donde se mostrarán las piezas
    conteniado_frame = ttk.Frame(pestania_principal)
    conteniado_frame.grid(row=0, column=2, sticky="nsew")
    
    # Frame lateral izquierdo para los botones
    vertical_frame = ttk.Frame(pestania_principal, width=200)
    vertical_frame.grid(row=0, column=1, padx=30)
    
    # Botón para mostrar piezas terminadas
    terminadas = ttk.Button(vertical_frame, text="Piezas Terminadas", padding=20, width=20, command=lambda: mostrar_contenido(conteniado_frame, "terminadas"))
    terminadas.grid(row=2, column=0, pady=10)
    
    # Botón para mostrar piezas brutas
    bruto = ttk.Button(vertical_frame, text="Piezas Brutas", padding=20, width=20, command=lambda: mostrar_contenido(conteniado_frame, "brutas"))
    bruto.grid(row=3, column=0, pady=10)

    def mostrar_contenido(conteniado_frame, tipo_pieza):
        # Limpiar el contenido actual
        for widget in conteniado_frame.winfo_children():
            widget.destroy()
        
        # Mostrar contenido según el tipo de pieza
        if tipo_pieza == "terminadas":
            frame = ventana_piezas_terminadas(conteniado_frame)
        elif tipo_pieza == "brutas":
            frame = ventana_piezas_brutas(conteniado_frame)
        
        frame.grid(row=0, column=0, sticky="nsew")

    # Mostrar por defecto las piezas terminadas
    mostrar_contenido(conteniado_frame, "terminadas")
