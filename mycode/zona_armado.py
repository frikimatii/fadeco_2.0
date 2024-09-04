import tkinter as tk
from tkinter import ttk
import sqlite3

from mycode.funciones.zona_armado_funcion import limpiar_tabla, mostrar_piezas_tablas, mostrar_piezas_motor, manejar_inventario, pre_armado_, armado_final_final


caja_330 = ["corona_330", "cajas_torneadas_330", "eje", "manchon", "ruleman_6005",  "ruleman_6205", "seguer", "sinfin", "motor_220w", "oring", "ruleman6000"]

caja_300 = ["corona_300", "cajas_torneadas_300", "eje", "manchon", "ruleman_6005",  "ruleman_6205", "seguer", "sinfin", "motor_220w", "oring", "ruleman6000"]

caja_250 = ["corona_250", "cajas_torneadas_250", "eje_250", "manchon_250", "ruleman_6004",  "ruleman_6204", "seguer", "sinfin", "motor250_200w", "oring", "rulemanR6"]

eco = [ "polea_grande", "polea_chica", "tornillo_teletubi_eco", "teclas", "capacitores_eco", "conector_hembra", "cable_corto_eco", "motores_eco", "caja_soldada_eco", "tapa_correa_eco", "correa_eco", "capuchon_motor_dodo", "buje_eje_eco", "rectangulo_plastico_eco"]



piezas_inox_armada330 = [ "BaseInox_330", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_330", "carros", "rueditas", "resorte_carro", "caja_330_armada", "capacitores"]

piezas_inox_armada300 = [ "BaseInox_300", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_300", "carros", "rueditas", "resorte_carro", "caja_300_armada", "capacitores"]

piezas_inox_armada250 = [ "BaseInox_250", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_250", "carros", "rueditas", "caja_250_armada", "capacitores_250" ]

piezas_pintada_armada330 = [ "BasePintada_330", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_330", "carros", "rueditas", "resorte_carro", "caja_330_armada", "capacitores", "bandeja_330"]

piezas_pintada_armada300 = [ "BasePintada_300", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_300", "carros", "rueditas", "resorte_carro", "caja_300_armada", "capacitores", "bandeja_300"]

piezas_inox_armadaeco = [ "BaseECO", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "cable_eco_220w", "varilla_330", "carros", "resorte_carro", "caja_eco_armada", "rueditas" ]

tipos_de_maquinas = ["inox_330", "inox_300", "inox_250", "pintada_330", "pintada_300", "eco"]


i330_piezas = [
    "brazo_330",
    "cubrecuchilla_330",
    "velero",
    "perilla_brazo",
    "cabezal_inox",
    "teletubi_330",
    "cuchilla_330",
    "cuadrado_regulador",
    "vela_final_330",
    "cubre_motor_rectangulo",
    "cubre_motor_cuadrado",
    "planchada_final_330",
    "varilla_brazo_330",
    "resorte_brazo",
    "tapa_afilador",
    "pipas",
    "tubo_manija",
    "afilador_final",
    "perilla_cubrecuchilla",
    "perilla_afilador",
    "base_afilador_330",
    "Base_Pre_armado_i330", 
    "piedra_afilador"
    "pinche_frontal",
    "pinche_lateral",
]


i300_piezas = [
    "brazo_300",
    "cubre_300",
    "velero",
    "perilla_brazo",
    "cabezal_inox",
    "teletu_300",
    "cuchilla_300",
    "cuadrado_regulador",
    "vela_final_300",
    "cubre_motor_rectangulo",
    "cubre_motor_cuadrado",
    "planchada_final_300",
    "varilla_brazo_300",
    "resorte_brazo",
    "tapa_afilador",
    "pipas",
    "tubo_manija",
    "afilador_final",
    "perilla_cubrecuchilla",
    "perilla_afilador",
    "base_afilador_300",
    "Base_Pre_armado_i300",
    "piedra_afilador",
    "pinche_frontal",
    "pinche_lateral",
]

i250_piezas = [
    "brazo_250",
    "cubrecuchilla_250",
    "velero",
    "perilla_brazo",
    "cabezal_250",
    "teletubi_250",
    "cuchilla_250",
    "cuadrado_regulador",
    "vela_final_250",
    "cubre_motor_rectangulo",
    "planchada_final_250",
    "varilla_brazo_250",
    "resorte_brazo",
    "tapa_afilador_250",
    "pipas",
    "tubo_manija_250",
    "afilador_final",
    "perilla_cubrecuchilla",
    "perilla_afilador",
    "base_afilador_250",
    "Base_Pre_armado_i250",
    "piedra_afilador",
    "capuchon_250",
    "pinche_frontal_250",
    "pinche_lateral_250",
]

p330_piezas = [
    "brazo_330",
    "cubrecuchilla_330",
    "velero",
    "perilla_brazo",
    "cabezal_pintada",
    "teletubi_330",
    "cuchilla_330",
    "cuadrado_regulador",
    "vela_final_330",
    "cubre_motor_rectangulo",
    "cubre_motor_cuadrado",
    "planchada_final_330",
    "varilla_brazo_330",
    "resorte_brazo",
    "tapa_afilador",
    "pipas",
    "tubo_manija",
    "afilador_final",
    "perilla_cubrecuchilla",
    "perilla_afilador",
    "base_afilador_330",
    "Base_Pre_armado_p330",
    "piedra_afilador",
    "pinche_frontal",
    "pinche_lateral",
]

p300_piezas = [
    "brazo_300",
    "cubre_300",
    "velero",
    "perilla_brazo",
    "cabezal_pintada",
    "teletu_300",
    "cuchilla_300",
    "cuadrado_regulador",
    "vela_final_300",
    "cubre_motor_rectangulo",
    "cubre_motor_cuadrado",
    "planchada_final_300",
    "varilla_brazo_300",
    "resorte_brazo",
    "tapa_afilador",
    "pipas",
    "tubo_manija",
    "afilador_final",
    "perilla_cubrecuchilla",
    "perilla_afilador",
    "base_afilador_300",
    "Base_Pre_armado_p300",
    "piedra_afilador",
    "pinche_frontal",
    "pinche_lateral",
]

iEco_piezas = [
    "brazo_330",
    "cubrecuchilla_330",
    "velero",
    "perilla_brazo",
    "cabezal_inox",
    "teletubi_doblado_eco",
    "cuchilla_330",
    "vela_final_330",
    "cuadrado_regulador",
    "planchada_final_330",
    "varilla_brazo_330",
    "resorte_brazo",
    "tapa_afilador_eco",
    "pitito_teletubi_eco",
    "pipas",
    "tubo_manija",
    "afilador_final",
    "perilla_cubrecuchilla",
    "perilla_afilador",
    "base_afilador_250",
    "Base_Pre_armado_ECO",
    "piedra_afilador",
    "pinche_lateral",
    "pinche_frontal",
]


calco_i330 = ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_330_4estrella"]
calco_i300 = ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_300_4estrella"]
calco_i250 = ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_250_2estrella"]
calco_p330 = ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_330_3estrella"]
calco_p300 = ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_300_3estrella"]
calco_eco = ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_330_4estrella", "calco_tensor_correa", "calco_verde_eco"]


quety_bases_pre_armadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'Pre_AR' "

quety_motores = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'motores'"
quety_cajas_330 = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'armado_caja' AND MODELO = 330"

quety_cajas_terminadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'torno_caja'"
quety_cajas_para_tornear = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'torno_caja'"


maquinas_terminadas = ["inox_330", "inox_300", "inox_250", "pintada_330", "pintada_300", "eco"]


query_maquinas_teminadas = "SELECT MAQUINA, CANTIDAD FROM maquinas"

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
    tk.Button(box_btn, text="ECO", command= lambda: mostrar_piezas_motor(tabla_principal, eco)).grid(row=1, column=1)

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


    tk.Button(cajas, text=" Motores para Tornear", command= lambda: mostrar_piezas_tablas(tabla_principal, quety_cajas_para_tornear)).grid(row=9, column=0)
    tk.Button(cajas, text="Motores Para Armar", command= lambda: mostrar_piezas_tablas(tabla_principal, quety_cajas_terminadas)).grid(row=9, column=1)


    pre_armado = tk.Frame(box2)
    pre_armado.grid(row=1, column=2)
    tk.Label(pre_armado, text="ZOna de PRE armado").grid(row=0, columnspan=2)

    box_boton_pre_armado = tk.Frame(pre_armado)
    box_boton_pre_armado.grid(row=1, columnspan=2)

    tk.Label(box_boton_pre_armado, text="Consulta de piezas del pre_armado").grid(row=0, columnspan=3)

    tk.Button(box_boton_pre_armado, text="Inox 330", command= lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armada330)).grid(row=1, column=0)
    tk.Button(box_boton_pre_armado, text="Inox 300", command= lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armada300)).grid(row=1, column=1)
    tk.Button(box_boton_pre_armado, text="Inox 250", command= lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armada250)).grid(row=1, column=2)
    tk.Button(box_boton_pre_armado, text="ECO", command= lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armadaeco)).grid(row=2, column=1)
    tk.Button(box_boton_pre_armado, text="Pintada 330", command= lambda: mostrar_piezas_motor(tabla_principal, piezas_pintada_armada330)).grid(row=2, column=0)
    tk.Button(box_boton_pre_armado, text="Pintada 300", command= lambda: mostrar_piezas_motor(tabla_principal, piezas_pintada_armada300)).grid(row=2, column=2)




    ttk.Separator(pre_armado, orient="horizontal", style="Separador2.TSeparator").grid(
        row=2, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    ttk.Label(pre_armado, text="Maquinas pre-armadas", style="WhiteOnRed.TLabel", font=("Arial", 14, "bold")).grid(row=3, column=0, columnspan=2)

    ttk.Label(pre_armado, text="Modelo de Maquina", style="WhiteOnRed.TLabel").grid(row=4, column=0)
    tipo_prearmada = ttk.Combobox(pre_armado, values=tipos_de_maquinas, state="readonly", width=16)
    tipo_prearmada.grid(row=4, column=1)

    ttk.Label(pre_armado, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=5, column=0)
    cantidad_prearmada = tk.Entry(pre_armado, width=10)
    cantidad_prearmada.grid(row=5, column=1, pady=4, padx=4)

    def enviar_():
        tipo_= tipo_prearmada.get()
        cantidad = int(cantidad_prearmada.get())
        pre_armado_(tipo_, cantidad, historial)


    tk.Button(
        pre_armado, 
        text="Pre Armado", 
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command= enviar_
    ).grid(row=6, column=1)

    ttk.Separator(pre_armado, orient="horizontal", style="Separador2.TSeparator").grid(
        row=7, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    ttk.Label(pre_armado, text="Consulta", style="WhiteOnRed.TLabel", font=("Arial", 14, "bold")).grid(row=8, column=0, columnspan=2)
    ttk.Label(pre_armado, text="Pre Armado Terminados ", style="WhiteOnRed.TLabel").grid(row=9, column=0, columnspan=2)
    tk.Button(
        pre_armado,
        text="Terminados", 
        font=('Arial', 8, "italic"),
        background= "gray", 
        foreground= "white",
        padx=4,
        pady=1,
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_bases_pre_armadas)).grid(row=10, columnspan=2)
    
    ttk.Separator(pre_armado, orient="horizontal", style="Separador2.TSeparator").grid(
        row=12, column=0, sticky="ew", columnspan=2, pady=3, padx=3)





    armado_final = tk.Frame(box2)
    armado_final.grid(row=1, column=3)
    tk.Label(armado_final, text="ZOna de armado").grid(row=0, column=0)

    botonera_armadofinal = ttk.Frame(armado_final, style='Color.TFrame')
    botonera_armadofinal.grid(row=1, column=0 , columnspan=2)

    ttk.Label(botonera_armadofinal, style="WhiteOnRed.TLabel",font=("Arial",12,"bold"), text="Piezas por modelo").grid(row=0, column=0, columnspan=3)
    
    ttk.Button(botonera_armadofinal, text="Inox 330", command= lambda: mostrar_piezas_motor(tabla_principal, i330_piezas)).grid(row=1, column=0, pady=5, padx=5)
    ttk.Button(botonera_armadofinal, text="Inox 300", command= lambda: mostrar_piezas_motor(tabla_principal, i300_piezas)).grid(row=1, column=1, pady=5, padx=5)
    ttk.Button(botonera_armadofinal, text="Inox 250", command= lambda: mostrar_piezas_motor(tabla_principal, i250_piezas)).grid(row=1, column=2, pady=5, padx=5)

    ttk.Button(botonera_armadofinal, text="Pintada 330", command= lambda: mostrar_piezas_motor(tabla_principal, p330_piezas)).grid(row=2, column=0, pady=5, padx=5)
    ttk.Button(botonera_armadofinal, text="Pintada 300", command= lambda: mostrar_piezas_motor(tabla_principal, p300_piezas)).grid(row=2, column=1, pady=5, padx=5)
    ttk.Button(botonera_armadofinal, text="ECO", command= lambda: mostrar_piezas_motor(tabla_principal, iEco_piezas)).grid(row=2, column=2, pady=5, padx=5)

    ttk.Separator(botonera_armadofinal, orient="horizontal", style="Separador2.TSeparator").grid(
        row=3, column=0, sticky="ew", columnspan=4, pady=1, padx=1)

    ttk.Label(armado_final, style="WhiteOnRed.TLabel", text="Maquinas Teminadas", font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2)

    ttk.Label(armado_final, text="Modelo", style="WhiteOnRed.TLabel").grid(row=7, column=0)
    modele_final = ttk.Combobox(armado_final, values=maquinas_terminadas, state="readonly", width=16)
    modele_final.grid(row=7, column=1)

    ttk.Label(armado_final, style="WhiteOnRed.TLabel", text="Cantidad").grid(row=8, column=0)
    cantidad_final = tk.Entry(armado_final, width=10)
    cantidad_final.grid(row=8, column=1, pady=5, padx=5)

    def armar():
        tipo = modele_final.get()
        cantiada = int(cantidad_final.get())
        armado_final_final(tipo, cantiada, historial)

    tk.Button(
        armado_final, 
        text="Confirmar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command= armar ).grid(row=9, column=1)

    ttk.Separator(armado_final, orient="horizontal", style="Separador2.TSeparator").grid(
        row=10, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    tk.Label(armado_final, text="Mostrar maquinas terminadas").grid(row=11, column=0)

    tk.Button(
        armado_final, 
        text="Mostrar Maquinas terminadas",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command= lambda: mostrar_piezas_tablas(tabla_principal, query_maquinas_teminadas)).grid(row=12, column=0)

    ttk.Separator(armado_final, orient="horizontal", style="Separador2.TSeparator").grid(
        row=13, column=0, sticky="ew", columnspan=2, pady=3, padx=3)