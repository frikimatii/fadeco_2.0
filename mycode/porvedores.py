import tkinter as tk 
from tkinter import ttk

from mycode.funciones.provedores_funcion import limpiar_tabla, mostrar_piezas_tablas, mostrar_por_modelo, enviar_a_soldar, resibir_bases, mandar_piezas_a, resicbir_piezas_de, armar_cabezales, mandar_a_niquelar, resibir_niquelado, mandar_a_pintar, resivir_de_pintura, mandar_a_roman, resibir_afiladores

bases = ["BaseInox_330","BaseInox_300","BaseInox_250","BaseECO","BasePintada_330","BasePintada_300", "cabezal_pintado"]

query_mostrar_piezas_soldador = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'soldador' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'soldador' "

query_mostras_bases_ensoldador = "SELECT PIEZAS, CANTIDAD FROM provedores WHERE PROVEDOR = 'soldador'"

query_mostrar_base_enfabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'soldador'"


query_carmelo ="SELECT PIEZAS ,CANTIDAD FROM pulidor_carmelo"
query_maxi = "SELECT PIEZAS ,CANTIDAD FROM pulidor_maxi"

query_stock_fabrica_pulido = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pulidor'"


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

lista_piezas_carmerlo = ["brazo_250","brazo_300","brazo_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO"
]

lista_piezas_maxi = ["brazo_250","brazo_300","brazo_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO"
]

modelo_piezas = ["BasePintada_330", "BasePintura_300", "cabezal_pintada","caja_soldada_eco", "teletubi_doblado_eco"]
piezas_afilador = ["capuchon_afilador","carcaza_afilador","eje_corto","eje_largo","ruleman608","palanca_afilador","resorte_palanca","resorte_empuje"]


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

query_afialador_terminado = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = 'afilador_terminado' "





def provedores(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Porvedores")

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Provedores").grid(row=0,columnspan=3, sticky="nsew")

    box1 = tk.Frame(index)
    box1.grid(row=1, column=0)
    tk.Label(box1, text="Tabla de piezas de provedores").grid(row=0,column=0)

    tabla_principal = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    tabla_principal.heading("Pieza", text="Pieza")
    tabla_principal.heading("Cantidad", text="Cantidad")
    tabla_principal.column("#0", width=0,stretch=tk.NO)
    tabla_principal.column("Pieza", width=200)
    tabla_principal.column("Cantidad", width=70)
    tabla_principal.config(height=20)
    tabla_principal.grid(row=2, column=0)

    tk.Label(box1, text="Limpiar").grid(row=3, column=0)
    ttk.Button(box1, text="Limpiar", command=lambda: limpiar_tabla(tabla_principal)).grid(row=4, column=0)
    tk.Label(box1, text="Historial").grid(row=5, column=0)

    historial = tk.Listbox(box1, width=50)
    historial.grid(row=6,column=0)

    




    box2 = tk.Frame(index)
    box2.grid(row=1, column=1)


    soldador = tk.Frame(box2)
    soldador.grid(row=0, column=0)
    
    tk.Label(soldador, text="Soldador").grid(row=0, columnspan=2)
    tk.Label(soldador, text="Piezas para el SOLDADOR").grid(row=1, columnspan=2)
    tk.Button(soldador, text="Stock en fabrica", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_soldador)).grid(row=2, columnspan=2)
    tk.Label(soldador, text="Piezas por tipo de base").grid(row=3, column=0)
    
    box_btn = ttk.Frame(soldador)
    box_btn.grid(row=4, columnspan=3)

    tk.Button(box_btn, text="inox 330", command=lambda: mostrar_por_modelo("inox_330", tabla_principal)).grid(row=1, column=0)
    tk.Button(box_btn, text="inox 300", command=lambda: mostrar_por_modelo("inox_300", tabla_principal)).grid(row=1, column=1)
    tk.Button(box_btn, text="inox 250", command=lambda: mostrar_por_modelo("inox_250", tabla_principal)).grid(row=1, column=2)
    tk.Button(box_btn, text="Pintada 330", command=lambda: mostrar_por_modelo("pintada_330", tabla_principal)).grid(row=2, column=0)
    tk.Button(box_btn, text="Pintada 300", command=lambda: mostrar_por_modelo("pintada_330", tabla_principal)).grid(row=2, column=1)
    tk.Button(box_btn, text="ECO", command=lambda: mostrar_por_modelo("ECO", tabla_principal)).grid(row=2, column=2)
    
    tk.Label(soldador, text="ENVIOS y ENTREGAS").grid(row=5, column=0)
    
    tk.Label(soldador, text="Seleccione una base").grid(row=5, column=0)
    base_seleccionada_entrega = ttk.Combobox(soldador, values=bases)
    base_seleccionada_entrega.grid(row=5, column=1)
    tk.Label(soldador, text="Cantidad").grid(row=6, column=0)
    cantidad_de_bases_entregada = tk.Entry(soldador)
    cantidad_de_bases_entregada.grid(row=6, column=1)
    tk.Button(soldador, text="Enviar", command=lambda: enviar_a_soldar(base_seleccionada_entrega,cantidad_de_bases_entregada, historial)).grid(row=7, columnspan=2)
    
    tk.Label(soldador, text="Seleccione una base").grid(row=8, column=0)
    base_seleccionada_resivida = ttk.Combobox(soldador, values=bases)
    base_seleccionada_resivida.grid(row=8, column=1)
    tk.Label(soldador, text="Cantidad").grid(row=9, column=0)
    cantidad_de_bases_resividas = tk.Entry(soldador)
    cantidad_de_bases_resividas.grid(row=9, column=1)
    tk.Button(soldador, text="Resivir", command=lambda:resibir_bases(base_seleccionada_resivida, cantidad_de_bases_resividas, historial)).grid(row=10, columnspan=2)
    tk.Label(soldador, text="Info del Soldador").grid(row=11, column=0)
    tk.Button(soldador, text="Stock en Soldador", command=lambda: mostrar_piezas_tablas(tabla_principal,query_mostras_bases_ensoldador)).grid(row=12, column=0)
    tk.Button(soldador, text="Stock en fabrica", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_base_enfabrica)).grid(row=12, column=1)
    
    







    cabezales_terminados = ttk.Frame(box2, style='Pestania.TFrame')
    cabezales_terminados.grid(row=1, column=0)

    ttk.Label(cabezales_terminados, text="Cabezales", font=("Arial", 17, "bold"), style='WhiteOnRed.TLabel').grid(row=0, column=1, padx=2, pady=2)

    stock_cabezal = ttk.Frame(cabezales_terminados)
    stock_cabezal.grid(row=1, columnspan=2)

    tk.Label(stock_cabezal, text="Stock de cabezales").grid(row=0, column=0)

    btn_agregar_cabezal_inox = ttk.Button(
        stock_cabezal,
        text="INOX",
        style="TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, query_cabezales_inox)
        
        )
    btn_agregar_cabezal_inox.grid(row=1, column=0, padx=3)
    btn_agregar_cabezal_pintada = ttk.Button(
        stock_cabezal,
        text="PINTADA",
        style="TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, query_cabezales_pintada))
    btn_agregar_cabezal_pintada.grid(row=1, column=1, padx=3)
    btn_agregar_cabezal_250 = ttk.Button(
        stock_cabezal,
        text="250",
        style="TButton", 
        command= lambda: mostrar_piezas_tablas(tabla_principal, query_cabezales_250))
    btn_agregar_cabezal_250.grid(row=1, column=2, padx=3)

    botones = tk.Frame(cabezales_terminados)
    botones.grid(row=2 ,columnspan=2)


    ttk.Label(botones, style='WhiteOnRed.TLabel', text="acero").grid(row=1, column=0)

    entrada_cantida_inox = ttk.Entry(botones, width=10, style='WhiteOnRed.TEntry')
    entrada_cantida_inox.grid(row=2, column=0)

    btn_agregar_cabezal_inox = ttk.Button(
        botones,
        text="Agregar",
        style="TButton",
        command= lambda: armar_cabezales("cabezal_inox", entrada_cantida_inox, historial))
    btn_agregar_cabezal_inox.grid(row=3, column=0, padx=3)

    ttk.Label(botones, style='WhiteOnRed.TLabel', text="pintada").grid(row=1, column=1)

    entrada_cantidad_pintada = ttk.Entry(botones, width=10, style='WhiteOnRed.TEntry')
    entrada_cantidad_pintada.grid(row=2, column=1)

    btn_agregar_cabezal_pintada = ttk.Button(
        botones,
        text="Agregar",
        style="TButton",
        command= lambda: armar_cabezales("cabezal_pintada", entrada_cantidad_pintada, historial))
    btn_agregar_cabezal_pintada.grid(row=3, column=1, padx=3)
    
    ttk.Label(botones, style='WhiteOnRed.TLabel', text="250").grid(row=1, column=2)

    entrada_cantidad_250 = ttk.Entry(botones, width=10, style='WhiteOnRed.TEntry')
    entrada_cantidad_250.grid(row=2, column=2)

    btn_agregar_cabezal_250 = ttk.Button(
        botones,
        text="Agregar",
        style="TButton",
        command= lambda: armar_cabezales("cabezal_250", entrada_cantidad_250, historial))
    btn_agregar_cabezal_250.grid(row=3, column=2, padx=3 )
    






    box3 = tk.Frame(index)
    box3.grid(row=1, column=2)

    carmelo = ttk.Frame(box3)
    carmelo.grid(row=0, column=0)
    
    tk.Label(carmelo, text="Carmelo").grid(row=0, columnspan=2)
    tk.Label(carmelo, text="ENVIOS").grid(row=1, columnspan=2)
    tk.Label(carmelo, text="seleccione la piezas").grid(row=2, column=0)
    piezas_seleccionada_c = ttk.Combobox(carmelo, values=lista_piezas_carmerlo)
    piezas_seleccionada_c.grid(row=3, column=0)
    tk.Label(carmelo, text="Cantidad").grid(row=2, column=1)
    cantida_de_piezas_c = tk.Entry(carmelo)
    cantida_de_piezas_c.grid(row=3, column=1)
    
    tk.Button(carmelo, text="Enviar", command=lambda: mandar_piezas_a("pulidor_carmelo", cantida_de_piezas_c, piezas_seleccionada_c, tabla_principal, historial)).grid(row=3, column=2)
    tk.Label(carmelo, text="--------------------------------------").grid(row=4, columnspan=2)
    
    tk.Label(carmelo, text="ENTREGA").grid(row=5, columnspan=2)
    tk.Label(carmelo, text="seleccione la piezas").grid(row=6, column=0)
    piezas_resibida_c = ttk.Combobox(carmelo, values=lista_piezas_carmerlo)
    piezas_resibida_c.grid(row=7, column=0)
    tk.Label(carmelo, text="Cantidad").grid(row=6, column=1)
    cantida_de_resibida_c = tk.Entry(carmelo)
    cantida_de_resibida_c.grid(row=7, column=1)
    
    tk.Button(carmelo, text="Resivir", command=lambda: resicbir_piezas_de("pulidor_carmelo", cantida_de_resibida_c, piezas_resibida_c, tabla_principal, historial)).grid(row=7, column=2)

    tk.Label(carmelo, text="Stock Carmelo").grid(row=8, column=0)
    tk.Button(carmelo, text="Consuta de Stock", command=lambda: mostrar_piezas_tablas(tabla_principal, query_carmelo)).grid(row=9, column=0)
    
    tk.Label(carmelo, text="Stock en Fabrica bruto").grid(row=8, column=1)
    tk.Button(carmelo, text="Consuta de Stock", command=lambda: mostrar_piezas_tablas(tabla_principal, query_stock_fabrica_pulido)).grid(row=9, column=1)
    
    tk.Label(carmelo, text="--------------------------------------").grid(row=10, columnspan=2)
    
    maxi = tk.Frame(box3)
    maxi.grid(row=1, column=0)
    
    tk.Label(maxi, text="Maxi").grid(row=0, columnspan=2)
    tk.Label(maxi, text="ENVIOS").grid(row=1, columnspan=2)
    tk.Label(maxi, text="seleccione la piezas").grid(row=2, column=0)
    piezas_seleccionada_m = ttk.Combobox(maxi, values=lista_piezas_maxi)
    piezas_seleccionada_m.grid(row=3, column=0)
    tk.Label(maxi, text="Cantidad").grid(row=2, column=1)
    cantida_de_piezas_m = tk.Entry(maxi)
    cantida_de_piezas_m.grid(row=3, column=1)
    
    tk.Button(maxi, text="Enviar", command=lambda: mandar_piezas_a("pulidor_maxi", cantida_de_piezas_m, piezas_seleccionada_m, tabla_principal, historial)).grid(row=3, column=2)
    tk.Label(maxi, text="--------------------------------------").grid(row=4, columnspan=2)
    
    tk.Label(maxi, text="ENTREGA").grid(row=5, columnspan=2)
    tk.Label(maxi, text="seleccione la piezas").grid(row=6, column=0)
    piezas_resibida_m = ttk.Combobox(maxi, values=lista_piezas_maxi)
    piezas_resibida_m.grid(row=7, column=0)
    tk.Label(maxi, text="Cantidad").grid(row=6, column=1)
    cantida_de_resibida_m = tk.Entry(maxi)
    cantida_de_resibida_m.grid(row=7, column=1)
    
    tk.Button(maxi, text="Resivir", command=lambda: resicbir_piezas_de("pulidor_maxi", cantida_de_resibida_m, piezas_resibida_m, tabla_principal, historial)).grid(row=7, column=2)

    tk.Label(maxi, text="Stock Maxi").grid(row=8, column=0)
    tk.Button(maxi, text="Consuta de Stock", command=lambda: mostrar_piezas_tablas(tabla_principal, query_maxi)).grid(row=9, column=0)
    
    tk.Label(maxi, text="Stock en Fabrica bruto").grid(row=8, column=1)
    tk.Button(maxi, text="Consuta de Stock", command=lambda: mostrar_piezas_tablas(tabla_principal, query_stock_fabrica_pulido)).grid(row=9, column=1)
    
    tk.Label(maxi, text="--------------------------------------").grid(row=10, columnspan=2)







    box4 = tk.Frame(index)
    box4.grid(row=1, column=3)



    box6 = ttk.Frame(box4, style='Color.TFrame')
    box6.grid(row=2, column=0, columnspan=2)
    
    ttk.Label(box6, text="Pintura", style="WhiteOnRed.TLabel",font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3 )

    btn_group = tk.Frame(box6)
    btn_group.grid(row=1, column=0, columnspan=3)

    ttk.Button(
        btn_group,
        text="Stock en fabrica",
        style="Estilo2.TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_pintura_bruto)
    ).grid(row=1, column=0)
    ttk.Button(
        btn_group,
        text="Stock Terminado",
        style="Estilo2.TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_pintura_terminada)
    ).grid(row=1, column=1)
    ttk.Button(
        btn_group,
        text="Stock en Pintura",
        style="Estilo2.TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_en_pintura)
    ).grid(row=1, column=2)

    ttk.Separator(box6, orient="horizontal", style="Separador2.TSeparator").grid(
        row=2, column=0, columnspan=3, padx=5, pady=5
    )
    
    cajapintura1 = ttk.Frame(box6, style='Color.TFrame')
    cajapintura1.grid(row=3, column=0)
    
    ttk.Label(cajapintura1 , text="Envios A Pintura",font=("Arial", 11, "bold"), style="WhiteOnRed.TLabel").grid(row=3, column=0, columnspan=2)

    ttk.Label(cajapintura1 , text="Tipo", style="WhiteOnRed.TLabel",).grid(row=4, column=0, sticky="ew")
    modelo = ttk.Combobox(cajapintura1 , values=modelo_piezas,state="readonly", width=17)
    modelo.grid(row=4, column=1, sticky="w")

    ttk.Label(cajapintura1 , text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=5, column=0, sticky="ew")
    enviar_a_pintura = ttk.Entry(cajapintura1 , width=10, style='WhiteOnRed.TEntry' )
    enviar_a_pintura.grid(row=5, column=1, pady=2)

    tk.Button(
        cajapintura1 ,
        text="Enviar Bases",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command= lambda: mandar_a_pintar(modelo, enviar_a_pintura, tabla_principal, historial)
    ).grid(row=6, column=1)
    

    cajapintura4 = ttk.Frame(box6, style='Color.TFrame')
    cajapintura4.grid(row=5, column=0)


    ttk.Label(cajapintura4, text="Bases Resibidas",font=("Arial", 12, "bold"), style="WhiteOnRed.TLabel",).grid(row=11, column=0, columnspan=2)

    ttk.Label(cajapintura4, text="Tipo", style="WhiteOnRed.TLabel",).grid(row=12, column=0)
    modelo_pintur = ttk.Combobox(cajapintura4, values=modelo_piezas, state="readonly")
    modelo_pintur.grid(row=12, column=1)

    ttk.Label(cajapintura4, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=13, column=0)
    resibe_cantidad_pintura = ttk.Entry(cajapintura4, width=10, style='WhiteOnRed.TEntry')
    resibe_cantidad_pintura.grid(row=13, column=1, pady=3)

    tk.Button(
        cajapintura4,
        text="Cantida Resibida",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command= lambda: resivir_de_pintura(modelo_pintur, resibe_cantidad_pintura, tabla_principal, historial)
    ).grid(row=14, column=1, pady=2)

    ttk.Separator(cajapintura4, orient="horizontal", style="Separador2.TSeparator").grid(
        row=17, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )








    box5 = ttk.Frame(box4, style='Color.TFrame')
    box5.grid(row=0, column=0 ,columnspan=2)
    
    ttk.Label(box5, text="Niquelado", style="WhiteOnRed.TLabel",font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3)
    grupbtn = tk.Frame(box5)
    grupbtn.grid(row=1, column=0, columnspan=3)
    ttk.Button(
        grupbtn,
        text="Stock en bruto",
        style="Estilo2.TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_niquelado_bruto)
    ).grid(row=1, column=0)
    
    ttk.Button(
        grupbtn,
        text="Stock en fabrica",
        style="Estilo2.TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_niquelado_en_niquelado)
    ).grid(row=1, column=1)
    
    ttk.Button(
        grupbtn,
        text="Stock en niquelado",
        style="Estilo2.TButton",
        command= lambda: mostrar_piezas_tablas(tabla_principal, quety_niquelado_en_fabrica)
    ).grid(row=1, column=2)
    
    ttk.Label(box5, text="Piezas A Niquelar", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2)
    ttk.Label(box5, text="Piezas", style="WhiteOnRed.TLabel").grid(row=3, column=0, sticky="w")
    
    lista_piezas = ttk.Combobox(box5, values=niquelado, state="readonly", width=17)
    lista_piezas.grid(row=3, column=1, sticky="w")
    
    ttk.Label(box5, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=4, column=0, sticky="w")
    
    cantidad_a_niquelar = ttk.Entry(box5,style='WhiteOnRed.TEntry', width=10)
    cantidad_a_niquelar.grid(row=4, column=1, sticky="w",pady=1)

    tk.Button(
        box5,
        text="Enviar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command= lambda: mandar_a_niquelar(lista_piezas, cantidad_a_niquelar, tabla_principal, historial)
    ).grid(row=5, column=1, columnspan=2, padx=2, pady=2,sticky="w")

    ttk.Separator(box5, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(box5, text="Piezas Terminadas", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=2)
    ttk.Label(box5, text="Piezas", style="WhiteOnRed.TLabel").grid(row=8, column=0, sticky="w")
    
    lista_piezas_nique = ttk.Combobox(box5, values=niquelado, state="readonly", width=17)
    lista_piezas_nique.grid(row=8, column=1, sticky="w")
    
    ttk.Label(box5, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=9, column=0, sticky="w")
    
    cantidad_a_niquelado = ttk.Entry(box5,style='WhiteOnRed.TEntry', width=10)
    cantidad_a_niquelado.grid(row=9, column=1, sticky="w" ,pady=1)

    tk.Button(
        box5,
        text="Resibido",
        background="blue",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command= lambda: resibir_niquelado(lista_piezas_nique, cantidad_a_niquelado, tabla_principal, historial)
        ).grid(row=10, column=1, columnspan=2, padx=2, pady=2, sticky="w")

    ttk.Separator(box5, orient="horizontal", style="Separador2.TSeparator").grid(
        row=11, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )    




    
    box10 = tk.Frame(index)
    box10.grid(row=1, column=4)


    box1 = ttk.Frame(box10, style='Color.TFrame')
    box1.grid(row=0, column=3, sticky="n",pady=3, padx=4, columnspan=2)
    

    ttk.Label(box1, text="Armado De Afilador", style="WhiteOnRed.TLabel", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2)

    ttk.Label(box1, text="Mostrar Piezas", style="WhiteOnRed.TLabel").grid(row=1, column=0, columnspan=2)
    tk.Button(
        box1, 
        text="en Fabrica", 
        font=('Arial', 8, "italic"),
        background= "gray", 
        foreground= "white",
        padx=4,
        pady=1,
        command=  lambda: mostrar_piezas_tablas(tabla_principal,query_piezas_afialador_fabrica )).grid(row=2, column=1)
    tk.Button(
        box1, 
        text="en Roman", 
        font=('Arial', 8, "italic"),
        background= "gray", 
        foreground= "white",
        padx=4,
        pady=1, 
        command=  lambda: mostrar_piezas_tablas(tabla_principal,query_piezas_afialador_en_roman)).grid(row=2, column=0)
    

    ttk.Separator(box1, orient="horizontal", style="Separador2.TSeparator").grid(
        row=3, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    ttk.Label(box1, text="Afiladores Terminadas", style="WhiteOnRed.TLabel").grid(row=4, column=0)
    tk.Button(
        box1, 
        text="Mostrar", 
        font=('Arial', 8, "italic"),
        background= "gray", 
        foreground= "white",
        padx=4,
        pady=1, 
        command= lambda: mostrar_piezas_tablas(tabla_principal, query_afialador_terminado )).grid(row=4, column=1)

    ttk.Separator(box1, orient="horizontal", style="Separador2.TSeparator").grid(
        row=5, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    envios_afilador = ttk.Frame(box1, style='Color.TFrame')
    envios_afilador.grid(row=6, column=0, columnspan=2)
    
    ttk.Label(envios_afilador, text="Enviar piezas a Roman", font=("Arial", 12, "bold"), style="WhiteOnRed.TLabel").grid(row=0, column=0, columnspan=2)
    
    ttk.Label(envios_afilador, text="Piezas", style="WhiteOnRed.TLabel").grid(row=1, column=0)
    ttk.Label(envios_afilador, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=1)
    
    comboxboxafiladores = ttk.Combobox(envios_afilador, values=piezas_afilador ,state="readonly", width=15)
    comboxboxafiladores.grid(row=2, column=0)
    
    entrycantidad1 = ttk.Entry(envios_afilador, width=7)
    entrycantidad1.grid(row=2, column=1)
    
    tk.Button(envios_afilador, 
            text="Envios a Roman",
            background="green",
            foreground="white",
            padx=4,
            pady=1,
            command= lambda: mandar_a_roman(comboxboxafiladores, entrycantidad1, tabla_principal, historial) ).grid(row=3, column=1)
    
    
    ttk.Separator(envios_afilador, orient="horizontal", style="Separador2.TSeparator").grid(
        row=4, column=0, sticky="ew", columnspan=2, pady=3, padx=3)
    
    
    ttk.Label(envios_afilador, text="ENTREGA DE AFILADORES TERMINADOS" ,font=("Arial", 10, "bold"), style="WhiteOnRed.TLabel").grid(row=5, column=0, columnspan=2)
    cantidad_terminada = ttk.Entry(envios_afilador, width=10)
    cantidad_terminada.grid(row=6, column=0,columnspan=2, pady=2)
    tk.Button(envios_afilador,
            text="Afiladores Terminados",
            background="blue",
            foreground="white",
            padx=4,
            pady=1,
            command= lambda: resibir_afiladores(cantidad_terminada, historial)
            ).grid(row=7, column=0, columnspan=2)

    ttk.Separator(envios_afilador, orient="horizontal", style="Separador2.TSeparator").grid(
        row=8, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

