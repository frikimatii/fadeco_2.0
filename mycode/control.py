import tkinter as tk
from tkinter import ttk
import sqlite3
from mycode.funciones.control_funciones import limpiar_tabla, mostrar_piezas_tablas, accion_embalar, accion_venta, consultar_piezas_sector_motor, consultar_piezas_sector, consultar_maquinas_final, verificar_disponibilidad_maquinas,  abrir_archivo_txt, drup_basurero
from mycode.funciones.add_funcion import ordenar_por

from mycode.funciones.chatbot_funcion import obtenerpiezas
pieza_a_eliminar = obtenerpiezas()

pieza_a_eliminar.sort()


tipo_maquina = ["inox_330","inox_300" ,"inox_250", "pintada_330", "pintada_300", "eco"]

tipo_enbalada = ["inox_330_embalada","inox_300_embalada" ,"inox_250_embalada", "pintada_330_embalada", "pintada_300", "eco_embalada"]

tipo_venta = ["inox_330_venta","inox_300_venta" ,"inox_250_venta", "pintada_330_venta", "pintada_300_venta", "eco_venta"]


query_maquinas_teminadas = "SELECT MAQUINA, CANTIDAD FROM maquinas WHERE CATEGORIA = 'terminadas' "

query_maquinas_enbaladas = "SELECT MAQUINA, CANTIDAD FROM maquinas WHERE CATEGORIA = 'embalada' "

query_maquinas_venta = "SELECT MAQUINA, CANTIDAD FROM maquinas WHERE CATEGORIA = 'venta' "

query_calcomanias = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'embalar'"


tipo_caja = ["330", "300", "250", "eco"]

tipo_prearmado = ("inoxidable 330", "inoxidable 300", "inoxidable 250", "pintada 330", "pintada 300", "inoxidable eco")


calco_eco = {
    "garantia": 1,
    "manual_instruciones": 1,
    "etiqueta_peligro": 1,
    "F_circulo": 1,
    "F_cuadrado": 1,
    "circulo_argentina": 1,
    "etiqueta_cable": 1,
    "fadeco_330_4estrella": 1,    
    "calco_tensor_correa":1,
    "calco_verde_eco":1
}
calco_pintada_300 = {
    "garantia": 1,
    "manual_instruciones": 1,
    "etiqueta_peligro": 1,
    "F_circulo": 1,
    "F_cuadrado": 1,
    "circulo_argentina": 1,
    "etiqueta_cable": 1,
    "fadeco_300_3estrella": 1
}
calco_pintada_330 = {
    "garantia": 1,
    "manual_instruciones": 1,
    "etiqueta_peligro": 1,
    "F_circulo": 1,
    "F_cuadrado": 1,
    "circulo_argentina": 1,
    "etiqueta_cable": 1,
    "fadeco_330_3estrella": 1
}
calco_inox_250 = {
    "garantia": 1,
    "manual_instruciones": 1,
    "etiqueta_peligro": 1,
    "F_circulo": 1,
    "F_cuadrado": 1,
    "circulo_argentina": 1,
    "etiqueta_cable": 1,
    "fadeco_250_2estrella": 1
}
calco_inox_300 = {
    "garantia": 1,
    "manual_instruciones": 1,
    "etiqueta_peligro": 1,
    "F_circulo": 1,
    "F_cuadrado": 1,
    "circulo_argentina": 1,
    "etiqueta_cable": 1,
    "fadeco_300_4estrella": 1
}
calco_inox_330 ={
    "garantia": 1,
    "manual_instruciones": 1,
    "etiqueta_peligro": 1,
    "F_circulo": 1,
    "F_cuadrado": 1,
    "circulo_argentina": 1,
    "etiqueta_cable": 1,
    "fadeco_330_4estrella": 1
}

calco_inox_330 =["garantia","manual_instruciones","etiqueta_peligro","F_circulo","F_cuadrado","circulo_argentina","etiqueta_cable","fadeco_330_4estrella"]

def control(ventana):

    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Control Calidad\Consulta")

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Control Calidad - Consultorio", font=("Arial", 23, "bold")).grid(row=0,columnspan=6 )

    box1 = tk.Frame(index)
    box1.grid(row=1, column=0, padx=15, sticky="nw")
    tk.Label(box1, text="Tabla de piezas", font=("Arial", 18, "bold"), background= '#192965', foreground='white').grid(row=0,column=0 , sticky="w")

    tabla_principal = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    tabla_principal.heading("Pieza", text="Pieza", command= lambda: ordenar_por(tabla_principal, "Pieza", False))
    tabla_principal.heading("Cantidad", text="Cantidad",command= lambda: ordenar_por(tabla_principal, "Cantidad", False))
    tabla_principal.column("#0", width=0,stretch=tk.NO)
    tabla_principal.column("Pieza", width=200)
    tabla_principal.column("Cantidad", width=70)
    tabla_principal.config(height=15)
    tabla_principal.grid(row=2, column=0, sticky="nsew")

    ttk.Button(box1, text="Limpiar", command=lambda: limpiar_tabla(tabla_principal)).grid(row=4, column=0, pady=5)

    tk.Label(box1, text="Historial", font=("Arial", 9, "bold")).grid(row=5, column=0, sticky="w")

    historial = tk.Listbox(box1, width=50, font=("Arial", 10, "bold"), height=9)
    historial.grid(row=6,column=0)
    
    
    # Creación del Frame principal box2
    box2 = ttk.Frame(index)
    box2.grid(row=1, column=1)  

    # Agrupación en un LabelFrame para mostrar máquinas terminadas
    lf_maquinas_terminadas = ttk.LabelFrame(box2, text="Maquinas para limpiar", style="", padding=(10, 5))
    lf_maquinas_terminadas.grid(row=0, column=0, padx=5, pady=5, columnspan=2)    

    # Botón para mostrar máquinas terminadas
    ttk.Button(lf_maquinas_terminadas, text="Mostrar máquinas terminadas", command=lambda: mostrar_piezas_tablas(tabla_principal, query_maquinas_teminadas),bootstyle="warning", padding=7).grid(row=0, column=0, padx=5, pady=5)   

    emabalaje = ttk.Frame(box2, style='Pestania.TFrame')
    emabalaje.grid(row=2, column=0)

    # Agrupación de widgets en un LabelFrame
    lf_maquinas_terminadas = ttk.LabelFrame(emabalaje, text="Maquinas embaladas", bootstyle="ligth", padding=(10, 5))
    lf_maquinas_terminadas.grid(row=0, column=0, sticky="n", padx=5, pady=5)

    # Etiqueta de descripción
    ttk.Label(lf_maquinas_terminadas, wraplength=250, text="Ingrese las máquinas que se limpiaron y embalaron. Aquí se descuentan las calcomanías", font=("Arial", 8, "bold")).grid(row=1, column=0, columnspan=2, padx=2, pady=2)

    # Etiqueta y combobox para seleccionar tipo de máquina
    ttk.Label(lf_maquinas_terminadas, text="Tipo De Maquina",font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="se")
    tipo_maquina_combox = ttk.Combobox(lf_maquinas_terminadas, values=tipo_maquina, state="readonly", width=14, font=("Arial", 12, "bold"))
    tipo_maquina_combox.grid(row=2, column=1, sticky="nw", pady=3)

    # Etiqueta y campo de entrada para cantidad
    ttk.Label(lf_maquinas_terminadas, text="Cantidad", font= ("Arial", 12, "bold")).grid(row=3, column=0, sticky="se")
    entry_cantidad = ttk.Entry(lf_maquinas_terminadas, width=10)
    entry_cantidad.grid(row=3, column=1, sticky="nw")

    # Botón para embalar
    ttk.Button(
        lf_maquinas_terminadas,
        text="Embalar", bootstyle="success",padding=3,
        command=lambda: accion_embalar(entry_cantidad, tipo_maquina_combox,     tabla_principal, historial)
    ).grid(row=4, column=0, columnspan=2, pady=4)

    # Etiqueta y botón para mostrar cantidad de máquinas terminadas
    tk.Label(lf_maquinas_terminadas, wraplength=200, text="Mostrar cantidad de máquinas     terminadas en fábrica").grid(row=5, column=0, columnspan=2)
    
    ttk.Button(lf_maquinas_terminadas, text="Stock Embalado",padding=5, bootstyle="info", command=lambda: mostrar_piezas_tablas (tabla_principal, query_maquinas_enbaladas)).grid(row=6, column=0,)

    ttk.Button(lf_maquinas_terminadas, text="Stock Calcomanias", padding=5, bootstyle="secondary", command=lambda: mostrar_piezas_tablas (tabla_principal, query_calcomanias)).grid(row=6, column=1)

    # Creación del Frame ventas
    ventas = ttk.Frame(box2)
    ventas.grid(row=3, column=0)
    
    # Agrupación de widgets en un LabelFrame para ventas
    lf_ventas = ttk.LabelFrame(ventas, text="Maquinas Vendidas",bootstyle="success",padding=(10, 5))
    lf_ventas.grid(row=0, column=0, sticky="n", padx=5, pady=5)
    
    # Etiqueta de descripción
    ttk.Label(lf_ventas, text="Ingrese máquinas vendidas", style="WhiteOnRed.TLabel", font= ("Arial", 8)).grid(row=1, column=0, columnspan=2, padx=2, pady=2)
    
    # Etiqueta y combobox para seleccionar tipo de máquina
    ttk.Label(lf_ventas, text="Tipo De Maquina", style="WhiteOnRed.TLabel", font=("Arial", 12,"bold")).grid(row=2, column=0, sticky="se")
    tipo_maquina_combox_venta = ttk.Combobox(lf_ventas, values=tipo_enbalada,   state="readonly", width=14, font=("Arial", 12, "bold"))
    tipo_maquina_combox_venta.grid(row=2, column=1, sticky="nw")
    
    # Etiqueta y campo de entrada para cantidad
    ttk.Label(lf_ventas, text="Cantidad", style="WhiteOnRed.TLabel", font=("Arial", 12,"bold")).grid(row=3, column=0, sticky="se")
    entry_cantidad_venta = ttk.Entry(lf_ventas, width=10)
    entry_cantidad_venta.grid(row=3, column=1, sticky="nw")
    
    # Botón para registrar venta
    ttk.Button(
        lf_ventas,
        text="Venta", bootstyle="danger",padding=7,
        command=lambda: accion_venta(entry_cantidad_venta, tipo_maquina_combox_venta,   tabla_principal, historial)
    ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
    
    ttk.Separator(lf_ventas, orient="horizontal", bootstyle="success").grid(row=5, column=0, columnspan=2, sticky="ew", padx=3, pady=3)
    
    # Etiqueta y botón para mostrar cantidad de máquinas vendidas
    tk.Label(lf_ventas, text="Mostrar cantidad que se Vendieron",  wraplength=200).grid(row=6, column=0, columnspan=2)
    
    ttk.Button(lf_ventas, text="Mostrar",bootstyle="light",padding=10, command=lambda: mostrar_piezas_tablas  (tabla_principal, query_maquinas_venta)).grid(row=7, column=0, columnspan=2, pady=5)
    






    # Creación del Frame principal "consultorio"
    consultorio = ttk.LabelFrame(index,text="CONSULTA POR SECTOR", bootstyle="warning")
    consultorio.grid(row=1, column=2, padx=10, pady=10)
    
    ttk.Label(consultorio, text="MOTORES", font=("Arial", 15, "bold"),bootstyle="inverse-secondary").grid(row=0, column=0, pady=3)

    # LabelFrame para la sección de Motores
    lf_motores = ttk.LabelFrame(consultorio, text="Se pueden Armar ... Motores ??", padding=10)
    lf_motores.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Etiqueta y combobox en la sección de Motores
    ttk.Label(lf_motores, text="Tipo De Motor", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="se")
    tipo_maquina_combox_motor = ttk.Combobox(lf_motores, values=tipo_caja, state="readonly", width=14, font=("Arial", 12, "bold"))
    tipo_maquina_combox_motor.grid(row=1, column=1, sticky="nw")

    # Cantidad y botón de consulta en la sección de Motores
    ttk.Label(lf_motores, text="Cantidad", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="se")
    entry_motores_cantidad = ttk.Entry(lf_motores, width=10)
    entry_motores_cantidad.grid(row=2, column=1, sticky="nw")
    ttk.Button(
        lf_motores,
        text="Consulta",bootstyle="warning",
        command=lambda: consultar_piezas_sector_motor(entry_motores_cantidad, tabla_principal, historial, tipo_maquina_combox_motor)
    ).grid(row=3, column=0, columnspan=2, pady=10)


    ttk.Label(consultorio, text="Bases PreArmadas", font=("Arial", 15, "bold"),bootstyle="inverse-secondary").grid(row=2, column=0)
    
    # LabelFrame para la sección de Prearmado
    lf_prearmado = ttk.LabelFrame(consultorio, text="Se Pueden armar ... Base PreArmadas?", padding=(10, 5))
    lf_prearmado.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    # Etiqueta y combobox en la sección de Prearmado
    ttk.Label(lf_prearmado, text="Tipo De Base", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="se")
    tipo_pre_combox = ttk.Combobox(lf_prearmado, values=tipo_prearmado, state="readonly", width=14, font=("Arial", 12, "bold"))
    tipo_pre_combox.grid(row=1, column=1, sticky="nw")

    # Cantidad y botón de consulta en la sección de Prearmado
    ttk.Label(lf_prearmado, text="Cantidad", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="se")
    entry_pre_cantidad = ttk.Entry(lf_prearmado, width=10)
    entry_pre_cantidad.grid(row=2, column=1, sticky="nw")
    ttk.Button(
        lf_prearmado,
        text="Consulta",bootstyle="warning",
        command=lambda: consultar_piezas_sector(entry_pre_cantidad, tabla_principal, historial, tipo_pre_combox)
    ).grid(row=3, column=0, columnspan=2, pady=10)


    ttk.Label(consultorio, text="Armado Final",font=("Arial", 15, "bold"),bootstyle="inverse-secondary").grid(row=4, column=0)

    # LabelFrame para la sección de Armado Final
    lf_armadofinal = ttk.LabelFrame(consultorio, text="Se Pueden Armar ... Maquinas ?", padding=(10, 5))
    lf_armadofinal.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    # Etiqueta y combobox en la sección de Armado Final
    ttk.Label(lf_armadofinal, text="Tipo Maquina",font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="se")
    tipo_maquina_combox_final = ttk.Combobox(lf_armadofinal, values=tipo_prearmado, state="readonly", width=14, font=("Arial", 12, "bold"))
    tipo_maquina_combox_final.grid(row=1, column=1, sticky="nw")

    # Cantidad y botón de consulta en la sección de Armado Final
    ttk.Label(lf_armadofinal, text="Cantidad", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="se")
    entry_cantidad_final = ttk.Entry(lf_armadofinal, width=10)
    entry_cantidad_final.grid(row=2, column=1, sticky="nw")
    ttk.Button(
        lf_armadofinal,
        text="Consulta",bootstyle="warning",
        command=lambda: consultar_maquinas_final(entry_cantidad_final, tabla_principal, historial, tipo_maquina_combox_final)
    ).grid(row=3, column=0, columnspan=2, pady=10)
    
    
    
    
    
    frame_principal = tk.Frame(index)
    frame_principal.grid(row=1, column=4, padx=3, pady=7)  # Ubicado en la columna 4

    # LabelFrame de Consulta de Pedido
    pedidos_frame = ttk.LabelFrame(frame_principal, text="Consulta de Pedido", padding=(5, 5), bootstyle="info")
    pedidos_frame.grid(row=0, column=0, padx=5, pady=7, sticky="ew")  # Primer LabelFrame dentro del frame principal

    # Títulos
    ttk.Label(pedidos_frame, text="Máquinas Pedidas", style="WhiteOnRed.TLabel", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2,    pady=(0, 5))

    # Etiquetas de las máquinas
    etiquetas_maquinas = [
        "Inoxidable 330",
        "Inoxidable 300",
        "Inoxidable 250",
        "Pintada 330",
        "Pintada 300",
        "Inoxidable Eco"
    ]

    for idx, etiqueta in enumerate(etiquetas_maquinas, start=2):
        ttk.Label(pedidos_frame, text=etiqueta, style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=idx, column=0, padx=1, pady=1,  sticky="se")

    # Entradas para las cantidades
    entradas_maquinas = []

    for idx in range(len(etiquetas_maquinas)):
        entry = ttk.Entry(pedidos_frame, width=7)
        entry.grid(row=idx + 2, column=1, sticky="nw")
        entradas_maquinas.append(entry)

    # Función para ejecutar la consulta
    def ejecutar_consulta():
        cantidades = {
            "inox330": int(entradas_maquinas[0].get() or 0),
            "inox300": int(entradas_maquinas[1].get() or 0),
            "inox250": int(entradas_maquinas[2].get() or 0),
            "pintada330": int(entradas_maquinas[3].get() or 0),
            "pintada300": int(entradas_maquinas[4].get() or 0),
            "ecoInox": int(entradas_maquinas[5].get() or 0)
        }
        verificar_disponibilidad_maquinas(cantidades, historial)

    # Botón para consultar
    resultado_final = ttk.Button(
        pedidos_frame,
        text="Averiguar",bootstyle="success",padding=10,
        command=ejecutar_consulta
    )
    resultado_final.grid(row=8, column=0, columnspan=2, padx=2, pady=5)

    # Botón para abrir el archivo de texto
    btn_abrir_archivo = ttk.Button(
        pedidos_frame,
        text="Abrir registro",bootstyle="info", padding=15,
        command=abrir_archivo_txt  # Llama a la función para abrir el archivo
    )
    btn_abrir_archivo.grid(row=9, column=0, columnspan=2, padx=5, pady=5)






    # LabelFrame de Gestión de Piezas
    drup = ttk.LabelFrame(frame_principal, text="Gestión de Piezas",padding=5, bootstyle="danger" )
    drup.grid(row=1, column=0, padx=5, pady=5)

    tk.Label(drup, text="Basurero", font=("Ariel", 15, "bold", "underline")).grid(row=0, column=0)
    
    tk.Label(drup, text="Seleccione una pieza para eliminar").grid(row=1, column=0, padx=5, pady=5)
    
    pieza_eliminar = ttk.Combobox(drup, values=pieza_a_eliminar, font=("Arial", 12, "bold"))
    pieza_eliminar.grid(row=2, column=0, padx=5, pady=5)

    cantidad_ingresada = tk.Entry(drup)
    cantidad_ingresada.grid(row=3, column=0, padx=5, pady=5)

    # Botón que llama a la función drup_basurero
    btn_drup = ttk.Button(drup, text="Descarte🗑️​", padding=12, bootstyle="danger",command=lambda: drup_basurero(pieza_eliminar, cantidad_ingresada, "piezas_terminadas", historial))
    btn_drup.grid(row=4, column=0)
