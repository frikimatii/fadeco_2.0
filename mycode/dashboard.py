import tkinter as tk
from tkinter import ttk
import sqlite3
import ttkbootstrap as ttk  # Asegúrate de tener importado ttkbootstrap

# Importa tus funciones desde el código de cada ventana
from mycode.dashboard_control.pieza_brutas import ventana_piezas_brutas
from mycode.dashboard_control.piezas_termindas import ventana_piezas_terminadas 
#from mycode.dashboard_control.control_de_datos import control_datos

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
    
    bruto = ttk.Button(vertical_frame, text="Piezas Brutas", padding=20, width=20, command=lambda: mostrar_contenido(conteniado_frame, "brutas"))
    bruto.grid(row=3, column=0, pady=10)
    
    datos_modificar = ttk.Button(vertical_frame, text="Modificar Datos", padding=20, width=20, command= lambda: mostrar_contenido(conteniado_frame, "datos"))
    datos_modificar.grid(row=4, column=0, pady=10)

    def mostrar_contenido(conteniado_frame, tipo_pieza):
        # Limpiar el contenido actual
        for widget in conteniado_frame.winfo_children():
            widget.destroy()
        
        # Mostrar contenido según el tipo de pieza
        if tipo_pieza == "terminadas":
            frame = ventana_piezas_terminadas(conteniado_frame)
        elif tipo_pieza == "brutas":
            frame = ventana_piezas_brutas(conteniado_frame)
        elif tipo_pieza == "datos":
            pass
            #pedir_pass(conteniado_frame)
        else:
            frame = ttk.Frame(conteniado_frame)  # Frame vacío como fallback
            frame.grid(row=0, column=0, sticky="nsew")



    def pedir_pass(conteniado_frame):
        ventana = tk.Toplevel()
        ventana.title("Autenticación Requerida")
        ventana.geometry("300x200")
        ventana.transient()
        ventana.grab_set()
        ventana.resizable(False, False)

        ttk.Label(ventana, text="Ingrese la Contraseña:", font=("Helvetica", 12)).pack  (pady=10)

        contrasena_var = tk.StringVar()
        entrada_contrasena = ttk.Entry(ventana, textvariable=contrasena_var, show="*")
        entrada_contrasena.pack(pady=5)

        # Mensaje de error dinámico
        mensaje_error = ttk.Label(ventana, text="", foreground="red")
        mensaje_error.pack()

        def verificar_pass():
            contrasena_correcta = "123"
            if contrasena_var.get() == contrasena_correcta:
                ventana.destroy()
                frame = control_datos(conteniado_frame)
                frame.grid(row=0, column=0, sticky="nsew")
            else:
                mensaje_error.config(text="Contraseña Incorrecta")

        ttk.Button(ventana, text="Aceptar", style="success.TButton", command=verificar_pass).pack(pady=10)
        ttk.Button(ventana, text="Cancelar", style="danger.TButton", command=ventana.destroy).  pack()
       
        
        
    # Mostrar por defecto las piezas terminadas
    mostrar_contenido(conteniado_frame, "datos")
