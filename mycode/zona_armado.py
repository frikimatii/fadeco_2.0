import tkinter as tk
from tkinter import ttk
import sqlite3
from ttkbootstrap import ttk

from mycode.funciones.zona_armado_funcion import limpiar_tabla, mostrar_piezas_tablas, mostrar_piezas_motor, manejar_inventario, pre_armado_, armado_final_final, actualizar_cantidad_a_cero, grafica_mes, grafico_maquinas, cierre_anual
from mycode.funciones.add_funcion import ordenar_por


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


caja_330 = ["corona_330", "cajas_torneadas_330", "eje", "manchon", "ruleman_6005",  "ruleman_6205", "seguer", "sinfin", "motor_220v", "oring", "ruleman6000"]

caja_300 = ["corona_300", "cajas_torneadas_300", "eje", "manchon", "ruleman_6005",  "ruleman_6205", "seguer", "sinfin", "motor_220v", "oring", "ruleman6000"]

caja_250 = ["corona_250", "cajas_torneadas_250", "eje_250", "manchon_250", "ruleman_6004",  "ruleman_6204", "seguer", "sinfin", "motor250_220v", "oring", "rulemanR6"]

eco = [ "polea_grande", "polea_chica", "tornillo_teletubi_eco", "teclas", "capacitores", "conector_hembra", "cable_corto_eco", "motor_eco", "caja_soldada_eco", "tapa_correa_eco", "correa_eco", "capuchon_motor_dodo", "buje_eje_eco", "rectangulo_plastico_eco"]



piezas_inox_armada330 = [ "BaseInox_330", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_330", "carros", "rueditas", "resorte_carro", "caja_330_armada", "capacitores"]

piezas_inox_armada300 = [ "BaseInox_300", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_300", "carros", "rueditas", "resorte_carro", "caja_300_armada", "capacitores"]

piezas_inox_armada250 = [ "BaseInox_250", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_250", "carros_250", "rueditas", "caja_250_armada", "capacitores_250" ]

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
    "cubre_300_torneado",
    "velero",
    "perilla_brazo",
    "cabezal_inox",
    "teletubi_300_torneado",
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
    "cubre_300_torneado",
    "velero",
    "perilla_brazo",
    "cabezal_pintada",
    "teletubi_300_torneado",
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
query_maquinas_teminadas = "SELECT MAQUINAS, CANTIDAD FROM maquinas_mes "

maquinas_terminadas = ["inox_330", "inox_300", "inox_250", "pintada_330", "pintada_300", "eco"]





def zona_armado(ventana):
    
    def colores():
        num = int(spin_num.get())  # Obtener el valor del Spinbox
        for item in tabla_principal.get_children():
            # Obtener el valor de la columna "Cantidad" de la fila actual
            cantidad = int(tabla_principal.item(item, 'values')[1])

            # Comparar la cantidad con el valor del Spinbox
            if cantidad < num:
                # Si es menor, poner la fila en rojo
                tabla_principal.tag_configure('coral', background='coral')
                tabla_principal.item(item, tags=('coral',))
            else:
                # Si es mayor o igual, poner la fila en verde
                tabla_principal.tag_configure('lightgreen', background='lightgreen')
                tabla_principal.item(item, tags=('lightgreen',))

        
        # Repetir la comprobación después de 500ms
        tabla_principal.after(500, colores)
    
    # Crear la pestaña dentro de la ventana principal
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Zona De Armado")

    # Crear el contenedor principal
    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    # Crear el cuadro (box1)
    box1 = ttk.Frame(index, padding=3)
    box1.grid(row=1, column=0)

    # Etiqueta para el título de la tabla
    ttk.Label(box1, text="Tabla de piezas para el armado", font=("Arial", 15, "bold")).grid(row=0, column=0)

    # Crear la tabla principal
    tabla_principal = ttk.Treeview(box1, columns=("Pieza", "Cantidad"), show='headings')
    tabla_principal.heading("Pieza", text="Pieza", command= lambda: ordenar_por(tabla_principal,"Pieza", False))
    tabla_principal.heading("Cantidad", text="Cant", command= lambda: ordenar_por(tabla_principal, "Cantidad", False))
    tabla_principal.column("#0", width=0, stretch=tk.NO)
    tabla_principal.column("Pieza", width=250)
    tabla_principal.column("Cantidad", width=70)
    tabla_principal.config(height=17)
    tabla_principal.grid(row=2, column=0, padx=7)

    # Botón para limpiar la tabla
    box_limpiar = ttk.Frame(box1)
    box_limpiar.grid(row=5, column=0, pady=5)
    ttk.Button(box_limpiar, text="Limpiar", command=lambda: limpiar_tabla(tabla_principal)).grid(row=0, column=0, pady=3)

    # Spinbox para seleccionar el límite de cantidad
    spin_num = ttk.Spinbox(box_limpiar, width=10, from_=0, to=100, state="readonly")
    spin_num.grid(row=0, column=1, padx=3)
    spin_num.set(10)  # Asignar un valor inicial al Spinbox

    # Etiqueta de historial
    ttk.Label(box1, text="Historial").grid(row=6, column=0, sticky="nw", pady=5)

    # Listbox para mostrar historial
    historial = tk.Listbox(box1, width=50)
    historial.grid(row=7, column=0)

    # Iniciar la función de colores
    colores()


    box2 = ttk.Frame(index, padding=3)
    box2.grid(row=1, column=1)

    ttk.Label(box2, text="Zona de armado", font=("Arial", 28, "bold")).grid(row=0, columnspan=4)

    


    cajas = ttk.Frame(box2,bootstyle="light", padding=5)
    cajas.grid(row=1, column=1, padx=5, pady=5)

    # Labelframe para Armado de Cajas
    lf_armado_cajas = ttk.Labelframe(cajas, text="stock de motores", padding=(10, 10))
    lf_armado_cajas.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    
    # Configura la columna para que tome todo el espacio disponible y alinee el botón al centro
    lf_armado_cajas.grid_columnconfigure(0, weight=1)
    
    # Botón para mostrar motores, centrado en la columna
    ttk.Button(lf_armado_cajas, text="Motores", bootstyle="warning-outline", command=lambda: mostrar_piezas_tablas(tabla_principal, quety_motores)).grid(row=0, column=0, sticky="ew")

        # Labelframe para seleccionar modelo
    lf_modelo = ttk.Labelframe(cajas, text="Seleccionar Modelo De Cajas", padding=(10, 10))
    lf_modelo.grid(row=1, column=0, sticky="ew", padx=5, pady=5)    

    # Frame para contener los botones
    box_btn = tk.Frame(lf_modelo)
    box_btn.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")    

    # Configura el Frame para que los botones se centren
    box_btn.grid_columnconfigure(0, weight=1)
    box_btn.grid_columnconfigure(1, weight=1)
    box_btn.grid_rowconfigure(0, weight=1)
    box_btn.grid_rowconfigure(1, weight=1)  

    # Botones para mostrar piezas por modelo
    ttk.Button(box_btn, text="Caja 330", bootstyle="primary-outline",command=lambda: mostrar_piezas_motor(tabla_principal, caja_330)).grid(row=0, column=0, padx=10, pady=10, sticky="nsew" )
    ttk.Button(box_btn, text="Caja 300", bootstyle="primary-outline",command=lambda: mostrar_piezas_motor(tabla_principal, caja_300)).grid(row=0, column=1, padx=10, pady=10, sticky="nsew" )
    ttk.Button(box_btn, text="Caja 250", bootstyle="primary-outline",command=lambda: mostrar_piezas_motor(tabla_principal, caja_250)).grid(row=1, column=0, padx=10, pady=10 , sticky="nsew")
    ttk.Button(box_btn, text="Caja ECO", bootstyle="primary-outline",command=lambda: mostrar_piezas_motor(tabla_principal, eco)).grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    # Labelframe para seleccionar modelo con Radiobuttons
    # Labelframe unificado
    lf_unificado = ttk.Labelframe(cajas, text="Modelo y Cantidad de Motores", padding=(40, 20))
    lf_unificado.grid(row=2, column=0, sticky="ns", padx=5, pady=5)

    # Variable para el modelo seleccionado
    modelo = tk.IntVar()

    # Botones de selección de modelo
    ttk.Radiobutton(lf_unificado, text="330", variable=modelo, value=1, bootstyle="success").grid(row=0, column=0, padx=5, pady=5)
    ttk.Radiobutton(lf_unificado, text="300", variable=modelo, value=2, bootstyle="success").grid(row=0, column=1, padx=5, pady=5)
    ttk.Radiobutton(lf_unificado, text="250", variable=modelo, value=3, bootstyle="success").grid(row=1, column=0, padx=5, pady=5)
    ttk.Radiobutton(lf_unificado, text="ECO", variable=modelo, value=4, bootstyle="success").grid(row=1, column=1, padx=5, pady=5)

    
    ttk.Separator(cajas, orient="horizontal").grid(row=2, column=0, sticky="ew", pady=5)

    # Campo de entrada para la cantidad de motores
    ttk.Label(lf_unificado, text="Cantidad de Motores:" ).grid(row=3, column=0, padx=5, pady=5, columnspan=2)
    cantidad_motores = tk.Entry(lf_unificado, width=10)
    cantidad_motores.grid(row=4, column=0,columnspan=2, padx=5, pady=5)

    # Función para manejar el inventario
    def enviar():
        selected_modelo = modelo.get()
        cantidad = int(cantidad_motores.get())
        manejar_inventario(selected_modelo, cantidad, historial)

    # Botón para enviar datos
    ttk.Button(lf_unificado, text="Motores Terminados",bootstyle="success", command=enviar, padding=7).grid(row=5, column=0, columnspan=2, pady=10)


    # Labelframe para opciones adicionales
    lf_opciones = ttk.Labelframe(cajas, text="Opciones Adicionales", padding=(10, 10))
    lf_opciones.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

    # Configura las columnas del Labelframe para que los botones se centren
    lf_opciones.grid_columnconfigure(0, weight=1)
    lf_opciones.grid_columnconfigure(1, weight=1)

    # Botones adicionales centrados
    ttk.Button(lf_opciones, text="Motores\Tornear",bootstyle="warning", command=lambda: mostrar_piezas_tablas(tabla_principal, quety_cajas_para_tornear)).grid(row=0, column=0, padx=5, sticky="ew")
    ttk.Button(lf_opciones, text="Motores\Armar", bootstyle="success", command=lambda: mostrar_piezas_tablas(tabla_principal, quety_cajas_terminadas)).grid(row=0, column=1, padx=5, sticky="ew")








    pre_armado = ttk.Frame(box2,bootstyle="light", padding=5)
    pre_armado.grid(row=1, column=2, padx=4)


    lf_pre_armado = ttk.Labelframe(pre_armado, text="Zona de Pre Armado", padding=(10, 10))
    lf_pre_armado.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    # Labelframe para la consulta de piezas del pre-armado
    lf_consulta_piezas = ttk.Labelframe(lf_pre_armado, text="Consulta de Piezas del Pre-Armado", padding=(10, 10))
    lf_consulta_piezas.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    # Botones para mostrar piezas según el tipo de pre-armado
    ttk.Button(lf_consulta_piezas, text="Inox 330",bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armada330)).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Button(lf_consulta_piezas, text="Inox 300",bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armada300)).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    ttk.Button(lf_consulta_piezas, text="Inox 250",bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armada250)).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
    ttk.Button(lf_consulta_piezas, text="ECO",bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, piezas_inox_armadaeco)).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    ttk.Button(lf_consulta_piezas, text="Pintada 330",bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, piezas_pintada_armada330)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Button(lf_consulta_piezas, text="Pintada 300", bootstyle="primary-outline",command=lambda: mostrar_piezas_motor(tabla_principal, piezas_pintada_armada300)).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    # Separador
    ttk.Separator(lf_pre_armado, orient="horizontal",bootstyle="light").grid(
        row=1, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    # Labelframe para la selección del modelo y cantidad
    lf_seleccion_modelo = ttk.Labelframe(lf_pre_armado, text="Maquinas Pre-Armadas", padding=(10, 10), style="Bold9.TLabelframe")
    lf_seleccion_modelo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    # Selección del modelo de la máquina
    ttk.Label(lf_seleccion_modelo, text="Modelo de Maquina", style="WhiteOnRed.TLabel").grid(row=0, column=0, padx=5, pady=5)
    tipo_prearmada = ttk.Combobox(lf_seleccion_modelo, values=tipos_de_maquinas, state="readonly", width=10, font=("Arial", 12, "bold"))
    tipo_prearmada.grid(row=0, column=1, padx=5, pady=5)

    # Ingreso de cantidad
    ttk.Label(lf_seleccion_modelo, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=0, padx=5, pady=5)
    cantidad_prearmada = tk.Entry(lf_seleccion_modelo, width=10)
    cantidad_prearmada.grid(row=1, column=1, padx=5, pady=5)


    def enviar_():
        tipo_= tipo_prearmada.get()
        cantidad = int(cantidad_prearmada.get())
        pre_armado_(tipo_, cantidad, historial)


    # Botón para enviar la información de pre-armado
    ttk.Button(
        lf_seleccion_modelo, 
        text="Pre Armado", bootstyle="success",padding=7,
        command=enviar_
    ).grid(row=2, column=1, pady=5)

    # Separador
    ttk.Separator(lf_pre_armado, orient="horizontal", bootstyle="light").grid(
        row=3, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    # Labelframe para la consulta de pre-armado terminados
    lf_consulta_terminados = ttk.Labelframe(lf_pre_armado, text="Consulta de Pre Armado Terminados", padding=(10, 10), style="Bold9.TLabelframe")
    lf_consulta_terminados.grid(row=4, column=0, padx=5, pady=5)

    ttk.Label(lf_consulta_terminados, text="Pre Armado Terminado", style="WhiteOnRed.TLabel", font=("Arial", 14, "bold")).grid(row=0, column=0,  padx=5, pady=5)
    ttk.Button(
        lf_consulta_terminados,
        text="Terminados", bootstyle="warning-outline",padding=10,
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_bases_pre_armadas)).grid(row=1, column=0, padx=5, pady=5)




    armado_final = ttk.Frame(box2,bootstyle="light", padding=3)
    armado_final.grid(row=1, column=3, padx=5, pady=5)

   # Labelframe principal donde anidaremos las demás secciones
    lf_principal = ttk.Labelframe(armado_final, text="Armado final",  padding=(5, 5))
    lf_principal.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    # Sección de Botonera dentro del Labelframe principal
    lf_botonera = ttk.Labelframe(lf_principal, text="Piezas por modelo",  padding=(5, 5))
    lf_botonera.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    ttk.Button(lf_botonera, text="Inox 330", bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, i330_piezas)).grid(row=0, column=0, pady=5, padx=5, sticky="nsew")
    ttk.Button(lf_botonera, text="Inox 300", bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, i300_piezas)).grid(row=0, column=1, pady=5, padx=5, sticky="nsew")
    ttk.Button(lf_botonera, text="Inox 250", bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, i250_piezas)).grid(row=0, column=2, pady=5, padx=5, sticky="nsew")

    ttk.Button(lf_botonera, text="Pintada 330", bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, p330_piezas)).grid(row=1, column=0, pady=5, padx=5, sticky="nsew")
    ttk.Button(lf_botonera, text="Pintada 300", bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, p300_piezas)).grid(row=1, column=1, pady=5, padx=5, sticky="nsew")
    ttk.Button(lf_botonera, text="ECO", bootstyle="primary-outline", command=lambda: mostrar_piezas_motor(tabla_principal, iEco_piezas)).grid(row=1, column=2, pady=5, padx=5, sticky="nsew")

    ttk.Separator(lf_principal, orient="horizontal",bootstyle="light").grid(row=1, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    # Sección de Máquinas Terminadas dentro del Labelframe principal
    lf_terminadas = ttk.Labelframe(lf_principal, text="Máquinas Terminadas", padding=5)
    lf_terminadas.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    ttk.Label(lf_terminadas, text="Modelo").grid(row=0, column=0)
    modele_final = ttk.Combobox(lf_terminadas, values=maquinas_terminadas, state="readonly", width=10, font=("Arial", 12, "bold"))
    modele_final.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(lf_terminadas, text="Cantidad").grid(row=1, column=0)
    cantidad_final = tk.Entry(lf_terminadas, width=10)
    cantidad_final.grid(row=1, column=1, pady=5, padx=5)

    def armar():
        tipo = modele_final.get()
        cantidad = int(cantidad_final.get())
        armado_final_final(tipo, cantidad, historial)

    ttk.Button(lf_terminadas, text="Confirmar", bootstyle="success", command=armar, padding=7).grid(row=2, column=1, pady=5, padx=5)

    ttk.Separator(lf_principal, orient="horizontal",bootstyle="light").grid(row=3, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    # Sección de Mostrar Máquinas Terminadas dentro del Labelframe principal
    lf_mostrar_terminadas = ttk.Labelframe(lf_principal, text="Mostrar Máquinas Terminadas", style="Bold9.TLabelframe")
    lf_mostrar_terminadas.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    ttk.Button(lf_mostrar_terminadas, text="Máquinas Terminadas", bootstyle="warning", command=lambda: mostrar_piezas_tablas(tabla_principal, query_maquinas_teminadas)).grid(row=0, column=0, pady=5, padx=3)
    ttk.Button(lf_mostrar_terminadas, text="Grafico de Maquinas",bootstyle="danger",command=lambda: grafico_maquinas()).grid(row=0, column=1, pady=5, padx=3)



    findemes = ttk.Frame(armado_final)
    findemes.grid(row=6, column=0, columnspan=3)
    
    # Agrupación en un LabelFrame para el cierre del mes
    lf_finde_mes = ttk.LabelFrame(findemes, text="Cierre Del Mes")
    lf_finde_mes.grid(row=1, column=0, padx=10, pady=10, columnspan=3,sticky="nsew")

    # Etiqueta y combobox para seleccionar el mes
    ttk.Label(lf_finde_mes, text="Mes", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=2, pady=2)
    meses_opcional = ttk.Combobox(lf_finde_mes, values=meses, state="readonly", width=12, font=("Arial", 12, "bold"))
    meses_opcional.grid(row=0, column=1, padx=2, pady=2)

    # Botón para terminar el mes
    cierre_mes = ttk.Button(
        lf_finde_mes,
        text="Terminar El Mes",bootstyle="success",
        command=lambda: actualizar_cantidad_a_cero(total, meses_opcional, historial)
    )
    cierre_mes.grid(row=1, column=0, columnspan=2, padx=3, pady=3)
    # Etiqueta para mostrar el total
    total = ttk.Label(lf_finde_mes, text="", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold"))
    total.grid(row=2, column=0, columnspan=2, padx=3, pady=3)

    # Botón para mostrar el registro
    mostrar_registro = ttk.Button(
        lf_finde_mes,
        text="Mostrar Grafica del Año",bootstyle="danger",
        command=lambda: grafica_mes()
    )
    mostrar_registro.grid(row=3, column=0, columnspan=2)
    
    fin_anual = ttk.Button(
        lf_finde_mes,
        text="Cerra el Año",bootstyle="secondary",
        command= lambda: cierre_anual(info_fin)
    )
    fin_anual.grid(row=4, column=0, columnspan=2, pady=10)

    info_fin = tk.Label(lf_finde_mes, text=".")
    info_fin.grid(row=5, column=0)
    
    