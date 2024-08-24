import tkinter as tk 
from tkinter import ttk

from mycode.funciones.provedores_funcion import limpiar_tabla, mostrar_piezas_tablas, mostrar_por_modelo, enviar_a_soldar, resibir_bases, mandar_piezas_a, resicbir_piezas_de

bases = ["BaseInox_330","BaseInox_300","BaseInox_250","BaseECO","BasePintada_330","BasePintada_300"]

query_mostrar_piezas_soldador = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'soldador' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'soldador' "

query_mostras_bases_ensoldador = "SELECT PIEZAS, CANTIDAD FROM provedores WHERE PROVEDOR = 'soldador'"

query_mostrar_base_enfabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'soldador'"


query_carmelo ="SELECT PIEZAS ,CANTIDAD FROM pulidor_carmelo"
query_maxi = "SELECT PIEZAS ,CANTIDAD FROM pulidor_maxi"

query_stock_fabrica_pulido = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pulidor'"


lista_piezas_carmerlo = ["brazo_250","brazo_300","brazo_330","caja_torneado_250","caja_torneado_300","caja_torneado_330","cubrecuchilla_250","cubrecuchilla_300","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO"
]

lista_piezas_maxi = ["brazo_250","brazo_300","brazo_330","caja_torneado_250","caja_torneado_300","caja_torneado_330","cubrecuchilla_250","cubrecuchilla_300","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO"
]




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
    tk.Button(soldador, text="Resivir", command=lambda:resibir_bases(base_seleccionada_resivida, cantidad_de_bases_resividas, historial) ).grid(row=10, columnspan=2)
    tk.Label(soldador, text="Info del Soldador").grid(row=11, column=0)
    tk.Button(soldador, text="Stock en Soldador", command=lambda: mostrar_piezas_tablas(tabla_principal,
query_mostras_bases_ensoldador)).grid(row=12, column=0)
    tk.Button(soldador, text="Stock en fabrica", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_base_enfabrica)).grid(row=12, column=1)
    
    
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

