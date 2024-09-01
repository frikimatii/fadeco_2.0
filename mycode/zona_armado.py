import tkinter as tk
from tkinter import ttk
import sqlite3

from mycode.funciones.zona_armado_funcion import limpiar_tabla, mostrar_piezas_tablas, mostrar_piezas_motor, manejar_inventario


caja_330 = ["corona_330", "cajas_torneadas_330", "eje", "manchon", "ruleman_6005",  "ruleman_6205", "seguer", "sinfin", "motor_220w", "oring", "ruleman6000"]

caja_300 = ["corona_300", "cajas_torneadas_300", "eje", "manchon", "ruleman_6005",  "ruleman_6205", "seguer", "sinfin", "motor_220w", "oring", "ruleman6000"]

caja_250 = ["corona_250", "cajas_torneadas_250", "eje_250", "manchon_250", "ruleman_6004",  "ruleman_6204", "seguer", "sinfin", "motor250_200w", "oring", "rulemanR6"]



quety_motores = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'motores'"
quety_cajas_330 = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'armado_caja' AND MODELO = 330"

quety_cajas_terminadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'torno_caja'"
quety_cajas_para_tornear = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'torno_caja'"


def zona_armado(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Zona De Armado")

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Armado").grid(row=0,columnspan=3, sticky="nsew")

    box1 = tk.Frame(index)
    box1.grid(row=1, column=0)

    tk.Label(box1, text="Tabla de piezas para el armado").grid(row=0,column=0)

    tabla_principal = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    tabla_principal.heading("Pieza", text="Pieza")
    tabla_principal.heading("Cantidad", text="Cantidad")
    tabla_principal.column("#0", width=0,stretch=tk.NO)
    tabla_principal.column("Pieza", width=200)
    tabla_principal.column("Cantidad", width=70)
    tabla_principal.config(height=20)
    tabla_principal.grid(row=2, column=0)

    tk.Label(box1, text="Limpiar tabla").grid(row=3, column=0)
    ttk.Button(box1, text="Limpiar", command=lambda: limpiar_tabla(tabla_principal)).grid(row=4, column=0)
    tk.Label(box1, text="Historial").grid(row=5, column=0)

    historial = tk.Listbox(box1, width=50)
    historial.grid(row=6,column=0)


    box2 = tk.Frame(index)
    box2.grid(row=1, column=1)

    tk.Label(box2, text="ZOna de armado").grid(row=0, columnspan=4)

    

    cajas = tk.Frame(box2)
    cajas.grid(row=1, column=1)
    tk.Label(cajas, text="armado de Cajas").grid(row=0, column=0)
    
    tk.Button(cajas, text="motores", command= lambda: mostrar_piezas_tablas(tabla_principal, quety_motores)).grid(row=1, column=0)
    
    tk.Label(cajas, text="mostrar piezas por modelo").grid(row=2, column=0)

    box_btn = tk.Frame(cajas)
    box_btn.grid(row=3, columnspan=2)

    tk.Button(box_btn, text="330", command= lambda: mostrar_piezas_motor(tabla_principal, caja_330)).grid(row=0, column=0)
    tk.Button(box_btn, text="300", command= lambda: mostrar_piezas_motor(tabla_principal, caja_300)).grid(row=0, column=1)
    tk.Button(box_btn, text="250", command= lambda: mostrar_piezas_motor(tabla_principal, caja_250)).grid(row=1, column=0)
    tk.Button(box_btn, text="ECO").grid(row=1, column=1)

    checkbox = ttk.Frame(cajas, style='Color.TFrame')
    checkbox.grid(row=4, column=0, columnspan=2)

    modelo = tk.IntVar()
    ttk.Label(checkbox, text="Modelo", style="WhiteOnRed.TLabel").grid(row=0, column=0, columnspan=3)
    tk.Radiobutton(checkbox, text="330", variable=modelo,selectcolor='#2f3542',
                   value=1, background='#192965', foreground='#fff',borderwidth=3, relief="raised").grid(row=1, column=0, padx=2, pady=2)
    tk.Radiobutton(checkbox, text="300", variable=modelo,selectcolor='#2f3542',
                   value=2, background='#192965', foreground='#fff',borderwidth=3, relief="raised").grid(row=1, column=1, padx=2, pady=2)
    tk.Radiobutton(checkbox, text="250", variable=modelo,selectcolor='#2f3542',
                   value=3, background='#192965', foreground='#fff',borderwidth=3, relief="raised").grid(row=1, column=2, padx=2, pady=2)
    tk.Radiobutton(checkbox, text="Eco", variable=modelo, selectcolor='#2f3542',
                   value=4, background='#192965', foreground='#fff',borderwidth=3, relief="raised").grid(row=1, column=3, padx=2, pady=2)


    ttk.Label(cajas, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=5, column=0,columnspan=2)
    cantidad_motores = tk.Entry(cajas, width=10)
    cantidad_motores.grid(row=6, column=0, columnspan=2, pady=3, padx=3)
    
    def enviar():
        selected_modelo = modelo.get()
        cantidad = int(cantidad_motores.get())
        manejar_inventario(selected_modelo, cantidad, historial)

    tk.Button(
    cajas,
    text="Motores Terminado",
    background="green",
    foreground="white",
    padx=4,
    pady=1,
    font=('Helvetica', 8, "bold"),
    command=enviar  # Asocia la función 'enviar' al botón
).grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    ttk.Separator(cajas, orient="horizontal", style="Separador2.TSeparator").grid(
        row=8, column=0, sticky="ew", columnspan=2, pady=3, padx=3)


    tk.Button(cajas, text="Consula de Motores para Tornear", command= lambda: mostrar_piezas_tablas(tabla_principal, quety_cajas_para_tornear)).grid(row=9, column=0)
    tk.Button(cajas, text="Consula de Motores Para Armar", command= lambda: mostrar_piezas_tablas(tabla_principal, quety_cajas_terminadas)).grid(row=9, column=1)


    pre_armado = tk.Frame(box2)
    pre_armado.grid(row=1, column=2)
    tk.Label(pre_armado, text="ZOna de armado").grid(row=0, column=0)


    armado_final = tk.Frame(box2)
    armado_final.grid(row=1, column=3)
    tk.Label(armado_final, text="ZOna de armado").grid(row=0, column=0)
