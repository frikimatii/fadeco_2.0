import tkinter as tk 
from tkinter import ttk
from mycode.funciones.add_funcion import ordenar_por

from mycode.funciones.provedores_funcion import limpiar_tabla, mostrar_piezas_tablas, mostrar_por_modelo, enviar_a_soldar, resibir_bases, mandar_piezas_a, resicbir_piezas_de, armar_cabezales, mandar_a_niquelar, resibir_niquelado, mandar_a_pintar, resivir_de_pintura, mandar_a_roman, resibir_afiladores, mecanizar_carcaza

bases = ["BaseInox_330","BaseInox_300","BaseInox_250","BaseECO","BasePintada_330","BasePintada_300", "cabezal_pintado"]

query_mostrar_piezas_soldador = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'soldador' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'soldador' "

query_mostras_bases_ensoldador = "SELECT PIEZAS, CANTIDAD FROM provedores WHERE PROVEDOR = 'soldador'"

query_mostrar_base_enfabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'soldador'"


query_carmelo ="SELECT PIEZAS ,CANTIDAD FROM pulidor_carmelo"
query_maxi = "SELECT PIEZAS ,CANTIDAD FROM pulidor_maxi"

query_stock_fabrica_pulido = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pulidor' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'pulido' "


query_piezas_cabezal_250 = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROVEDOR = 'pulidor' AND MODELO = '250'"


query_piezas_cabezal_inox = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROVEDOR = 'pulidor' AND MODELO = 'inox'"

query_piezas_cabezal_pintada = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROVEDOR = 'pulidor' AND MODELO = 'pintada'"

niquelado = [
    "eje_rectificado",
    "varilla_brazo_330",
    "varilla_brazo_300",
    "varilla_brazo_250",
    "tubo_manija",
    "tubo_manija_250",
    "palanca_afilador"
]

lista_piezas_carmerlo = ["brazo_augeriado_250", "brazo_augeriado_300", "brazo_augeriado_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO", "tapa_afilador_eco"
]
lista_piezas_carmerlo_para_fabrica = ["brazo_250", "brazo_300", "brazo_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO", "tapa_afilador_eco"
]

lista_piezas_maxi = ["brazo_augeriado_250", "brazo_augeriado_300", "brazo_augeriado_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO","tapa_afilador_eco"
]

lista_piezas_maxi_para_fabrica = ["brazo_250", "brazo_300", "brazo_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO", "tapa_afilador_eco"
]


modelo_piezas = ["BasePintada_330", "BasePintada_300", "cabezal_pintada","caja_soldada_eco", "teletubi_doblado_eco"]

piezas_afilador = ["capuchon_afilador","carcaza_afilador","eje_corto","eje_largo","ruleman608","palanca_afilador","resorte_palanca","resorte_empuje"]


query_cabezales_inox = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MODELO = 'inox' AND SECTOR = 'cabezal'"
query_cabezales_pintada = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MODELO = 'pintada' AND SECTOR = 'cabezal'"
query_cabezales_250 = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MODELO = '250' AND SECTOR = 'cabezal' "


quety_niquelado_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'niquelar'"

quety_niquelado_en_niquelado = "SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'niqular'"

quety_niquelado_en_fabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'niquelar'"

quety_pintura_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pintura'"

quety_en_pintura = "SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'pintura'"

quety_pintura_terminada = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'pintura'"

query_piezas_afialador_fabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'pieza_afilador'"

query_piezas_afialador_en_roman = "SELECT PIEZAS, CANTIDAD FROM AFILADOR "

query_afialador_terminado = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = 'afilador_final' "

query_piezas_carcaza = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PIEZAS = 'carcaza_afilador' "



def provedores(ventana):

    style = ttk.Style()
    style.configure("Bold9.TLabelframe.Label", font=("Helvetica", 14, "bold"))

    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Porvedores")

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Provedores", font=("Arial", 30, "bold")).grid(row=0,columnspan=4, sticky="ns")

    box1 = tk.Frame(index)
    box1.grid(row=1, column=0, sticky="ns")
    tk.Label(box1, text="Tabla de piezas de provedores", font=("Arial", 12, "bold")).grid(row=0,column=0, sticky="w")

    tabla_principal = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    tabla_principal.heading("Pieza", text="Pieza", command= lambda: ordenar_por(tabla_principal, "Pieza", False))
    tabla_principal.heading("Cantidad", text="Cantidad", command= lambda: ordenar_por(tabla_principal, "Cantidad", False))
    tabla_principal.column("#0", width=0,stretch=tk.NO)
    tabla_principal.column("Pieza", width=270)
    tabla_principal.column("Cantidad", width=110)
    tabla_principal.config(height=20)
    tabla_principal.grid(row=2, column=0, padx=7)

    tk.Label(box1, text="Limpiar").grid(row=3, column=0)
    ttk.Button(box1, text="Limpiar", command=lambda: limpiar_tabla(tabla_principal)).grid(row=4, column=0)
    tk.Label(box1, text="Historial").grid(row=5, column=0)

    historial = tk.Listbox(box1, width=60, height=10, font=("Arial", 10, "bold"))
    historial.grid(row=6,column=0)

    



    box2 = tk.Frame(index)
    box2.grid(row=1, column=1)
    
    soldador = tk.Frame(box2)
    soldador.grid(row=0, column=0)
    
    # Sección de Stock
    stock_frame = ttk.LabelFrame(soldador, text="Stock Soldador", padding=7, relief="groove", style="Bold9.TLabelframe")
    stock_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    
    tk.Button(stock_frame, text="Stock en fábrica", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_soldador)).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(stock_frame, text="Stock en Soldador", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostras_bases_ensoldador)).grid(row=1, column=1, padx=5, pady=5)
    
    # Sección de Envíos y Recepciones
    envios_frame = ttk.LabelFrame(soldador, text="Envíos y Recepciones", padding=10, relief="groove", style="Bold9.TLabelframe")
    envios_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    
    tk.Label(envios_frame, text="Enviar a Soldar:").grid(row=1, column=0, pady=5, sticky="e")
    base_seleccionada_entrega = ttk.Combobox(envios_frame, values=bases, state="readonly", width=15, font= ("Arial", 12, "bold"))
    base_seleccionada_entrega.grid(row=1, column=1, pady=5, sticky="w")
    tk.Label(envios_frame, text="Cantidad:").grid(row=2, column=0, pady=5, sticky="e")
    cantidad_de_bases_entregada = tk.Entry(envios_frame)
    cantidad_de_bases_entregada.grid(row=2, column=1, pady=5, sticky="w")
    tk.Button(envios_frame, text="Enviar",bg="green" ,fg="white",command=lambda: enviar_a_soldar(base_seleccionada_entrega,   cantidad_de_bases_entregada, historial)).grid(row=3, column=0, columnspan=2, pady=10)
    
    tk.Label(envios_frame, text="Recibir de Soldador:").grid(row=4, column=0, pady=5, sticky="e")
    base_seleccionada_resivida = ttk.Combobox(envios_frame, values=bases, state="readonly", width=15, font= ("Arial", 12, "bold"))
    base_seleccionada_resivida.grid(row=4, column=1, pady=5, sticky="w")
    tk.Label(envios_frame, text="Cantidad:").grid(row=5, column=0, pady=5, sticky="e")
    cantidad_de_bases_resividas = tk.Entry(envios_frame)
    cantidad_de_bases_resividas.grid(row=5, column=1, pady=5, sticky="w")
    tk.Button(envios_frame, text="Recibir",bg="blue",fg="white", command=lambda: resibir_bases(base_seleccionada_resivida,   cantidad_de_bases_resividas, historial)).grid(row=6, column=0, columnspan=2, pady=10)
    
    # Sección de Acciones del Soldador
    acciones_frame = ttk.LabelFrame(soldador, text="Piezas para el Soldador", padding=10, relief="groove", style="Bold9.TLabelframe")
    acciones_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    tk.Button(acciones_frame, text="inox 330", command=lambda: mostrar_por_modelo("inox_330", tabla_principal)).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(acciones_frame, text="inox 300", command=lambda: mostrar_por_modelo("inox_300", tabla_principal)).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(acciones_frame, text="inox 250", command=lambda: mostrar_por_modelo("inox_250", tabla_principal)).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(acciones_frame, text="Pintada 330", command=lambda: mostrar_por_modelo("pintada_330", tabla_principal)).grid  (row=2, column=0, padx=5, pady=5)
    tk.Button(acciones_frame, text="Pintada 300", command=lambda: mostrar_por_modelo("pintada_330", tabla_principal)).grid  (row=2, column=1, padx=5, pady=5)
    tk.Button(acciones_frame, text="ECO", command=lambda: mostrar_por_modelo("ECO", tabla_principal)).grid(row=2, column=2, padx=5, pady=5)
    
    cabezales_terminados = ttk.Frame(box2, style='Pestania.TFrame', padding=5)
    cabezales_terminados.grid(row=1, column=0, pady=5)
    
    # Título con estilo
    ttk.Label(cabezales_terminados, text="Cabezales", font=("Arial", 14, "bold"), style='WhiteOnRed.TLabel').grid(row=0,    column=0, columnspan=3, pady=5)
    
    # Sección de stock de cabezales con bordes
    stock_cabezal = ttk.LabelFrame(cabezales_terminados, text="Piezas De Cabezales", padding=5, relief="solid",  style="Bold9.TLabelframe")
    stock_cabezal.grid(row=1, column=0, columnspan=3, pady=5)
    
    btn_agregar_cabezal_inox = ttk.Button(stock_cabezal, text="INOX", style="TButton", command=lambda: mostrar_piezas_tablas    (tabla_principal, query_cabezales_inox))
    btn_agregar_cabezal_inox.grid(row=1, column=0, padx=5, pady=5)
    
    btn_agregar_cabezal_pintada = ttk.Button(stock_cabezal, text="PINTADA", style="TButton", command=lambda:    mostrar_piezas_tablas(tabla_principal, query_cabezales_pintada))
    btn_agregar_cabezal_pintada.grid(row=1, column=1, padx=5, pady=5)
    
    btn_agregar_cabezal_250 = ttk.Button(stock_cabezal, text="250", style="TButton", command=lambda: mostrar_piezas_tablas  (tabla_principal, query_cabezales_250))
    btn_agregar_cabezal_250.grid(row=1, column=2, padx=5, pady=5)
    
    # Sección de entrada y botones de agregar
    botones = ttk.LabelFrame(cabezales_terminados, text="Cabezales Soldados", padding=3, relief="ridge", style="Bold9.TLabelframe")
    botones.grid(row=2, column=0, columnspan=3, pady=5)
    
    for i, (texto, comando) in enumerate([
        ("Acero INOX", lambda: armar_cabezales("cabezal_inox", entrada_cantida_inox, historial)),
        ("Pintada", lambda: armar_cabezales("cabezal_pintada", entrada_cantidad_pintada, historial)),
        ("250", lambda: armar_cabezales("cabezal_250", entrada_cantidad_250, historial))
    ]):
        ttk.Label(botones, style='WhiteOnRed.TLabel', text=texto, font=("Arial", 12)).grid(row=0, column=i, padx=10, pady=5)
    
        entrada = ttk.Entry(botones, width=12, style='WhiteOnRed.TEntry')
        entrada.grid(row=1, column=i, padx=10, pady=5)
    
        agregar_btn = ttk.Button(botones, text="Agregar", style="TButton", command=comando)
        agregar_btn.grid(row=2, column=i, padx=10, pady=5)
    
        # Asignando las entradas a variables
        if i == 0:
            entrada_cantida_inox = entrada
        elif i == 1:
            entrada_cantidad_pintada = entrada
        elif i == 2:
            entrada_cantidad_250 = entrada
    
    



    box3 = tk.Frame(index)
    box3.grid(row=1, column=2, sticky="ns")

    # Crear un Labelframe para Carmelo
    carmelo_frame = ttk.Labelframe(box3, text="Carmelo", padding="7", style="Bold9.TLabelframe")
    carmelo_frame.grid(row=0, column=0, padx=5, pady=5)

    # Envíos para Carmelo
    tk.Label(carmelo_frame, text="Enviar", font=("Arial", 9,"bold" ,"underline")).grid(row=0, column=0, columnspan=2, sticky="w")
    tk.Label(carmelo_frame, text="Seleccione la pieza").grid(row=1, column=0, sticky="w")
    piezas_seleccionada_c = ttk.Combobox(carmelo_frame,values=lista_piezas_carmerlo, state="readonly", width=20, font= ("Arial", 12, "bold"))
    piezas_seleccionada_c.grid(row=1, column=1, padx=5)
    tk.Label(carmelo_frame, text="Cantidad").grid(row=2, column=0, sticky="w")
    cantida_de_piezas_c = tk.Entry(carmelo_frame)
    cantida_de_piezas_c.grid(row=2, column=1, padx=5)
    tk.Button(carmelo_frame, text="Enviar", bg="blue",fg="white", command=lambda: mandar_piezas_a("pulidor_carmelo", cantida_de_piezas_c, piezas_seleccionada_c, tabla_principal, historial)).grid(row=3, column=0, columnspan=2, pady=5)

    # Entrega para Carmelo
    tk.Label(carmelo_frame, text="ENTREGA", font=("Arial", 9,"bold" ,"underline")).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))
    tk.Label(carmelo_frame, text="Seleccione la pieza").grid(row=5, column=0, sticky="w")
    piezas_resibida_c = ttk.Combobox(carmelo_frame, values=lista_piezas_carmerlo_para_fabrica, state="readonly", width=20, font= ("Arial", 12, "bold"))
    piezas_resibida_c.grid(row=5, column=1, padx=5)
    tk.Label(carmelo_frame, text="Cantidad").grid(row=6, column=0, sticky="w")
    cantida_de_resibida_c = tk.Entry(carmelo_frame)
    cantida_de_resibida_c.grid(row=6, column=1, padx=5)
    tk.Button(carmelo_frame, text="Recibir",bg="green",fg="white", command=lambda: resicbir_piezas_de("pulidor_carmelo", cantida_de_resibida_c, piezas_resibida_c, tabla_principal, historial)).grid(row=7, column=0, columnspan=2, pady=5)

    # Stock para Carmelo
    tk.Label(carmelo_frame, text="Stock Carmelo",font=("Arial", 8,"bold" ,"underline")).grid(row=8, column=0, pady=(10, 0))
    tk.Button(carmelo_frame, text="EN CARMELO", command=lambda: mostrar_piezas_tablas(tabla_principal, query_carmelo)).grid(row=9, column=0, pady=5)

    tk.Label(carmelo_frame, text="Stock bruto fabrica", font=("Arial", 8,"bold" ,"underline")).grid(row=8, column=1, pady=(10, 0))
    tk.Button(carmelo_frame, text="BRUTO FABRICA", command=lambda: mostrar_piezas_tablas(tabla_principal, query_stock_fabrica_pulido)).grid(row=9, column=1)


    # Crear un Labelframe para Maxi
    maxi_frame = ttk.Labelframe(box3, text="Maxi", padding="7", style="Bold9.TLabelframe")
    maxi_frame.grid(row=1, column=0, padx=5, pady=5)

    # Envíos para Maxi
    tk.Label(maxi_frame, text="Envios", font=("Arial", 9,"bold" ,"underline")).grid(row=0, column=0, columnspan=2, sticky="w")
    tk.Label(maxi_frame, text="Seleccione la pieza").grid(row=1, column=0, sticky="w")
    piezas_seleccionada_m = ttk.Combobox(maxi_frame, values=lista_piezas_maxi, state="readonly", width=20, font= ("Arial", 12, "bold"))
    piezas_seleccionada_m.grid(row=1, column=1, padx=5)
    tk.Label(maxi_frame, text="Cantidad").grid(row=2, column=0, sticky="w")
    cantida_de_piezas_m = tk.Entry(maxi_frame)
    cantida_de_piezas_m.grid(row=2, column=1, padx=5)
    tk.Button(maxi_frame, text="Enviar",bg="blue",fg="white", command=lambda: mandar_piezas_a("pulidor_maxi", cantida_de_piezas_m, piezas_seleccionada_m, tabla_principal, historial)).grid(row=3, column=0, columnspan=2, pady=5)

    # Entrega para Maxi
    tk.Label(maxi_frame, text="ENTREGA", font=("Arial", 9,"bold" ,"underline")).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))
    tk.Label(maxi_frame, text="Seleccione la pieza").grid(row=5, column=0, sticky="w")
    piezas_resibida_m = ttk.Combobox(maxi_frame,  values=lista_piezas_maxi_para_fabrica, state="readonly", width=20, font= ("Arial", 12, "bold"))
    piezas_resibida_m.grid(row=5, column=1, padx=5)
    tk.Label(maxi_frame, text="Cantidad").grid(row=6, column=0, sticky="w")
    cantida_de_resibida_m = tk.Entry(maxi_frame)
    cantida_de_resibida_m.grid(row=6, column=1, padx=5)
    tk.Button(maxi_frame, text="Recibir",bg="green",fg="white", command=lambda: resicbir_piezas_de("pulidor_maxi", cantida_de_resibida_m, piezas_resibida_m, tabla_principal, historial)).grid(row=7, column=0, columnspan=2, pady=5)

    # Stock para Maxi
    tk.Label(maxi_frame, text="Stock Maxi", font=("Arial", 8,"bold" ,"underline")).grid(row=8, column=0, pady=(10, 0))
    tk.Button(maxi_frame, text="EN MAXI", command=lambda: mostrar_piezas_tablas(tabla_principal, query_maxi)).grid(row=9, column=0, pady=5)
    tk.Label(maxi_frame, text="Stock en Fabrica bruto", font=("Arial", 8,"bold" ,"underline")).grid(row=8, column=1, pady=(10, 0))
    tk.Button(maxi_frame, text="BRUTO FABRICA", command=lambda: mostrar_piezas_tablas(tabla_principal, query_stock_fabrica_pulido)).grid(row=9, column=1)
    



    box4 = tk.Frame(index)
    box4.grid(row=1, column=3, sticky="ns")

    # Labelframe para Pintura
    labelframe_pintura = ttk.Labelframe(box4, text="Pintura", style="Bold9.TLabelframe", padding=7)
    labelframe_pintura.grid(row=0, column=0, columnspan=2)

    labelframe_stock = ttk.Labelframe(labelframe_pintura, text="Opciones de Stock", style="Bold9.TLabelframe")
    labelframe_stock.grid(row=1, column=0, columnspan=3)

    btn_group = tk.Frame(labelframe_stock)
    btn_group.grid(row=0, column=0, columnspan=3)

    ttk.Button(
        btn_group,
        text="Stock en fabrica",
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_pintura_bruto)
    ).grid(row=0, column=0)

    ttk.Button(
        btn_group,
        text="Stock Terminado",
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_pintura_terminada)
    ).grid(row=0, column=1)

    ttk.Button(
        btn_group,
        text="Stock en Pintura",
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_en_pintura)
    ).grid(row=1, columnspan=2)

    ttk.Separator(labelframe_pintura, orient="horizontal").grid(
        row=2, column=0, columnspan=3, padx=5, pady=5
    )

    # Envíos a Pintura
    labelframe_envios = ttk.Labelframe(labelframe_pintura, text="Envíos a Pintura", style="Bold9.TLabelframe" )
    labelframe_envios.grid(row=3, column=0, columnspan=3, pady=5)

    ttk.Label(labelframe_envios, text="Tipo").grid(row=0, column=0, sticky="w")
    modelo = ttk.Combobox(labelframe_envios, values=modelo_piezas, state="readonly", width=17, font= ("Arial", 12, "bold"))
    modelo.grid(row=0, column=1, sticky="w")

    ttk.Label(labelframe_envios, text="Cantidad").grid(row=1, column=0, sticky="w")
    enviar_a_pintura = ttk.Entry(labelframe_envios, width=10)
    enviar_a_pintura.grid(row=1, column=1, pady=2)

    tk.Button(
        labelframe_envios,
        text="Enviar Bases",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: mandar_a_pintar(modelo, enviar_a_pintura, tabla_principal, historial)
    ).grid(row=2, column=1, pady=5)

    # Bases Recibidas
    labelframe_recibidas = ttk.Labelframe(labelframe_pintura, text="Bases Recibidas", style="Bold9.TLabelframe")
    labelframe_recibidas.grid(row=4, column=0, columnspan=3, pady=5)

    ttk.Label(labelframe_recibidas, text="Tipo").grid(row=0, column=0, sticky="w")
    modelo_pintur = ttk.Combobox(labelframe_recibidas, values=modelo_piezas, state="readonly", width=17, font= ("Arial", 12, "bold"))
    modelo_pintur.grid(row=0, column=1)

    ttk.Label(labelframe_recibidas, text="Cantidad").grid(row=1, column=0, sticky="w")
    resibe_cantidad_pintura = ttk.Entry(labelframe_recibidas, width=10)
    resibe_cantidad_pintura.grid(row=1, column=1, pady=3)

    tk.Button(
        labelframe_recibidas,
        text="Cantidad Recibida",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: resivir_de_pintura(modelo_pintur, resibe_cantidad_pintura, tabla_principal, historial)
    ).grid(row=2, column=1, pady=5)



    # Labelframe para Niquelado/ Rectificado
    labelframe_niquelado = ttk.Labelframe(box4, text="Niquelado/ Rectificado",style="Bold9.TLabelframe" , padding=7)
    labelframe_niquelado.grid(row=3, column=0, columnspan=2, pady=5)

    # Opciones de Stock
    labelframe_stock = ttk.Labelframe(labelframe_niquelado, text="Opciones de Stock", style="Bold9.TLabelframe")
    labelframe_stock.grid(row=1, column=0, columnspan=3, pady=5)

    grupbtn = tk.Frame(labelframe_stock)
    grupbtn.grid(row=0, column=0, columnspan=3)

    ttk.Button(
        grupbtn,
        text="Stock en bruto",
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_niquelado_bruto)
    ).grid(row=0, column=0)

    ttk.Button(
        grupbtn,
        text="Stock en niquelado",
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_niquelado_en_niquelado)
    ).grid(row=0, column=1)

    ttk.Button(
        grupbtn,
        text="Stock en fabrica",
        command=lambda: mostrar_piezas_tablas(tabla_principal, quety_niquelado_en_fabrica)
    ).grid(row=1, columnspan=2)

    ttk.Separator(labelframe_stock, orient="horizontal").grid(
        row=2, column=0, columnspan=3, padx=5, pady=5
    )

    # Piezas a Niquelar/ Rectificar
    labelframe_piezas_niquelar = ttk.Labelframe(labelframe_niquelado, text="Piezas A Niquelar/ Rectificado", style="Bold9.TLabelframe" )
    labelframe_piezas_niquelar.grid(row=2, column=0, columnspan=3, pady=10)

    ttk.Label(labelframe_piezas_niquelar, text="Piezas", style="WhiteOnRed.TLabel").grid(row=0, column=0, sticky="w")
    lista_piezas = ttk.Combobox(labelframe_piezas_niquelar, values=niquelado, state="readonly", width=17, font= ("Arial", 12, "bold"))
    lista_piezas.grid(row=0, column=1, sticky="w")

    ttk.Label(labelframe_piezas_niquelar, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=0, sticky="w")
    cantidad_a_niquelar = ttk.Entry(labelframe_piezas_niquelar, style='WhiteOnRed.TEntry', width=10)
    cantidad_a_niquelar.grid(row=1, column=1, sticky="w", pady=1)

    tk.Button(
        labelframe_piezas_niquelar,
        text="Enviar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: mandar_a_niquelar(lista_piezas, cantidad_a_niquelar, tabla_principal, historial)
    ).grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky="w")

    # Piezas Terminadas
    labelframe_piezas_terminadas = ttk.Labelframe(labelframe_niquelado, text="Piezas Terminadas")
    labelframe_piezas_terminadas.grid(row=4, column=0, columnspan=3, pady=10)

    ttk.Label(labelframe_piezas_terminadas, text="Piezas", style="WhiteOnRed.TLabel").grid(row=0, column=0, sticky="w")
    lista_piezas_nique = ttk.Combobox(labelframe_piezas_terminadas, values=niquelado, state="readonly", width=17, font= ("Arial", 12, "bold"))
    lista_piezas_nique.grid(row=0, column=1, sticky="w")

    ttk.Label(labelframe_piezas_terminadas, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=0, sticky="w")
    cantidad_a_niquelado = ttk.Entry(labelframe_piezas_terminadas, style='WhiteOnRed.TEntry', width=10)
    cantidad_a_niquelado.grid(row=1, column=1, sticky="w", pady=1)

    tk.Button(
        labelframe_piezas_terminadas,
        text="Recibido",
        background="blue",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: resibir_niquelado(lista_piezas_nique, cantidad_a_niquelado, tabla_principal, historial)
    ).grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky="w")



    
    # Creación del marco principal
    box10 = tk.Frame(index)
    box10.grid(row=1, column=4)

    # Sección del Armado De Afilador
    box1 = ttk.Frame(box10, style='Color.TFrame')
    box1.grid(row=0, column=3, sticky="n", pady=3, padx=4, columnspan=2)

    # Título
    ttk.Label(box1, text="Armado De Afilador", style="WhiteOnRed.TLabel", font=("Arial", 18, "bold")).grid(row=0, column=0,     columnspan=2)

    # Mostrar Piezas
    ttk.Label(box1, text="Mostrar Piezas", style="WhiteOnRed.TLabel").grid(row=1, column=0, columnspan=2)
    tk.Button(box1, text="en Fabrica", font=('Arial', 8, "italic"), bg="gray", fg="white", command=lambda: mostrar_piezas_tablas    (tabla_principal, query_piezas_afialador_fabrica)).grid(row=2, column=1)
    tk.Button(box1, text="en Roman", font=('Arial', 8, "italic"), bg="gray", fg="white", command=lambda: mostrar_piezas_tablas  (tabla_principal, query_piezas_afialador_en_roman)).grid(row=2, column=0)

    # Separador
    ttk.Separator(box1, orient="horizontal", style="Separador2.TSeparator").grid(row=3, column=0, sticky="ew", columnspan=2,    pady=3, padx=3)

    # Afiladores Terminados
    ttk.Label(box1, text="Afiladores Terminadas", style="WhiteOnRed.TLabel").grid(row=4, column=0)
    tk.Button(box1, text="Mostrar", font=('Arial', 8, "italic"), bg="gray", fg="white", command=lambda: mostrar_piezas_tablas   (tabla_principal, query_afialador_terminado)).grid(row=4, column=1)

    # Separador
    ttk.Separator(box1, orient="horizontal", style="Separador2.TSeparator").grid(row=5, column=0, sticky="ew", columnspan=2,    pady=3, padx=3)

    # Sección de envíos de Afilador
    envios_afilador = ttk.Frame(box1, style='Color.TFrame')
    envios_afilador.grid(row=6, column=0, columnspan=2)

    # Carcaza mecanizadas
    carcaza = tk.Frame(envios_afilador)
    carcaza.grid(row=0, columnspan=2)

    tk.Label(carcaza, text="Carcaza mecanizadas").grid(row=4, columnspan=2)
    tk.Label(carcaza, text="Ingrese Cantidad de Carcaza.").grid(row=4, columnspan=2)
    cantidad_ingresada_carcaza = tk.Entry(carcaza)
    cantidad_ingresada_carcaza.grid(row=5, columnspan=2)

    tk.Button(carcaza, text="Cargar...", command=lambda: mecanizar_carcaza(cantidad_ingresada_carcaza, tabla_principal,     historial)).grid(row=6, column=0)
    tk.Button(carcaza, text="Consulta Carcaza", command=lambda: mostrar_piezas_tablas(tabla_principal, query_piezas_carcaza)).  grid(row=6, column=1)

    # Separador
    ttk.Separator(carcaza, orient="horizontal", style="Separador2.TSeparator").grid(row=7, column=0, sticky="ew", columnspan=2,     pady=3, padx=3)

    # Enviar piezas a Roman
    ttk.Label(envios_afilador, text="Enviar piezas a Roman", font=("Arial", 12, "bold"), style="WhiteOnRed.TLabel").grid(row=1,     column=0, columnspan=2)
    ttk.Label(envios_afilador, text="Piezas", style="WhiteOnRed.TLabel").grid(row=2, column=0)
    ttk.Label(envios_afilador, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=2, column=1)

    comboxboxafiladores = ttk.Combobox(envios_afilador, values=piezas_afilador, state="readonly", width=17, font= ("Arial", 12, "bold"))
    comboxboxafiladores.grid(row=3, column=0)

    entrycantidad1 = ttk.Entry(envios_afilador, width=7)
    entrycantidad1.grid(row=3, column=1)

    tk.Button(envios_afilador, text="Envios a Roman", bg="green", fg="white", command=lambda: mandar_a_roman    (comboxboxafiladores, entrycantidad1, tabla_principal, historial)).grid(row=4, column=1)

    # Separador
    ttk.Separator(envios_afilador, orient="horizontal", style="Separador2.TSeparator").grid(row=5, column=0, sticky="ew",   columnspan=2, pady=3, padx=3)

    # Entrega de Afiladores Terminados
    ttk.Label(envios_afilador, text="ENTREGA DE AFILADORES TERMINADOS", font=("Arial", 10, "bold"), style="WhiteOnRed.TLabel"). grid(row=6, column=0, columnspan=2)

    cantidad_terminada = ttk.Entry(envios_afilador, width=10)
    cantidad_terminada.grid(row=7, column=0, columnspan=2, pady=2)

    tk.Button(envios_afilador, text="Afiladores Terminados", bg="blue", fg="white", command=lambda: resibir_afiladores  (cantidad_terminada, historial)).grid(row=8, column=0, columnspan=2)

    # Separador final
    ttk.Separator(envios_afilador, orient="horizontal", style="Separador2.TSeparator").grid(row=9, column=0, sticky="ew",   columnspan=2, pady=3, padx=3)
