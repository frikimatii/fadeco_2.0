import tkinter as tk 
from tkinter import ttk
from mycode.funciones.mecanizasdo_funcion import accion_plegadora, accion_plasmas, mostrar_piezas_tablas, limpiar_tabla, accion_corte, accion_balancin, accion_torno, accion_augeriado, accion_fresa


lista_piezas_plegadora = ["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","ChapaBase_330Eco","lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco", "bandeja_cabezal_inox_250", "bandeja_cabezal_pintada" , "bandeja_cabezal_inox", "chapa_U_inox_250", "chapa_U_pintada","chapa_U_inox"]

lista_piezas_plasma = ["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","ChapaBase_330Eco","lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco", "planchada_330", "planchada_300", "planchada_250", "vela_330", "vela_300", "vela_250","bandeja_cabezal_inox_250", "bandeja_cabezal_pintada" , "bandeja_cabezal_inox"]

piezas_corte = [ "planchuela_250", "planchuela_300", "planchuela_330", "varilla_300", "varilla_330", "varilla_250", "portaeje", "eje_rectificado", "varilla_brazo_330" ,"varilla_brazo_300" ,"varilla_brazo_250" ,"tubo_manija" ,"tubo_manija_250" ,"cuadrado_regulador" ,"palanca_afilador" ,"eje_corto" ,"eje_largo" ,"buje_eje_eco" ,"teletubi_eco", "guia_u", "chapa_cubre_cabezal_inox", "chapa_cubre_cabezal_pintada", "chapa_cubre_cabezal_inox_250"]


piezas_balancin = ["planchuela_250","planchuela_300","planchuela_330","portaeje", "guia_u", "teletubi_eco", "chapaU_inox", "chapaU_pintada", "chapaU_inox_250"]

piezas_para_augeriar = ["cuadrado_regulador","brazo_330","brazo_300","brazo_250", "carros", "carros_250", "movimiento", "tornillo_teletubi_eco" ]

piezas_torno = ["buje_eje_eco", "eje", "eje_250", "manchon", "manchon_250", "rueditas", "tornillo_guia", "carros", "carros_250","movimiento", "caja_300", "caja_330", "caja_250", "cubrecuchilla_300", "teletubi_300", "tornillo_teletubi_eco"]

piezas_para_fresar = ["vela_250", "vela_300", "vela_330","planchada_330","planchada_300","planchada_250"]


query_mostrar_piezas_parar_doblar = "SELECT PIEZAS,CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'plegadora'"

query_mostrar_piezas_dobladas = "SELECT PIEZAS, CANTIDAD FROM plasma WHERE ORIGEN = 'plegado' UNION SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'plegado'"

query_mostar_piezas_para_plasma = "SELECT PIEZAS, CANTIDAD FROM plasma WHERE MECANIZADO = 'plasma' UNION SELECT PIEZAS,CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'plasma'"

query_piezas_plasma_teminadad = "SELECT PIEZAS,CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'soldar'"

query_piezas_para_cortar = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'corte'"

querty_piezas_cortadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'corte' "

query_mostrar_piezas_balancin_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'balancin'"

query_mostrar_piezas_balancin_terminado = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'balancin'"

query_mostar_piezas_para_tornear = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'torno'"
querty_mostrar_piezas_torneada = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'torno' UNION SELECT PIEZAS ,CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'torno' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE ORIGEN = 'torno'" 


querty_mostra_pieza_agujeriar = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'agueriado' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'augeriado'"


querty_pieza_agujeriar_terminadad = "SELECT PIEZAS,CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'augeriado' UNION  SELECT PIEZAS,CANTIDAD FROM PIEZAS_RETOCADA WHERE ORIGEN = 'fundidor'"


querty_mostrar_velas_planchada_cortada = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'fresado'"

querty_mostrar_velas_planchada_fresada = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'fresado'"





def mecanizado(ventana):
    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Mecanizado")

    index = ttk.Frame(pestania)
    index.grid(row=0, column=0)

    tk.Label(index, text="Mecanizado").grid(row=0,columnspan=3, sticky="nsew")

    box1 = tk.Frame(index)
    box1.grid(row=1, column=0)
    tk.Label(box1, text="Tabla de piezas Mecanizado").grid(row=0,column=0)

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
    
    mecanizsmo = ttk.Frame(box2)
    mecanizsmo.grid(row=0, column=1)


    plegadora = ttk.Frame(mecanizsmo, style='Color.TFrame')
    plegadora.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    ttk.Label(plegadora, text="Plegadora", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Label(plegadora, text="Piezas a plegar",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_plegar_plegada = ttk.Combobox(plegadora, values=(lista_piezas_plegadora), state="readonly", width=20)
    piezas_a_plegar_plegada.grid(row=2, column=0)
    ttk.Label(plegadora, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_plegado = ttk.Entry(plegadora, width=10, style='WhiteOnRed.TEntry')
    cantidad_ingresada_plegado.grid(row=2, column=1)
    tk.Button(
        plegadora,
        text="Plegar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_plegadora(cantidad_ingresada_plegado, piezas_a_plegar_plegada, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)
    ttk.Separator(plegadora, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    stock_plegadora = ttk.Frame(plegadora, style='Color.TFrame')
    stock_plegadora.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_plegadora, text="Stock del piezas para PLEGAR", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_plegadora,
        text="Stock Bruto",
        style="Estilo4.TButton" ,command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_parar_doblar) ).grid(row=1, column=0, pady=3, padx=3) 
    ttk.Button(
        stock_plegadora,
        text="Stock Terminado",command=lambda: mostrar_piezas_tablas(tabla_principal,query_mostrar_piezas_dobladas ),
        style="Estilo4.TButton").grid(row=1, column=1, pady=3, padx=3)
    ttk.Separator(plegadora, orient="horizontal").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    
    
    
    
    
    
    plasma = ttk.Frame(mecanizsmo, style='Color.TFrame')
    plasma.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    ttk.Label(plasma, text="Plasma", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Label(plasma, text="Piezas para Cortar",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_plegar_plama = ttk.Combobox(plasma, values=(lista_piezas_plasma), state="readonly", width=16)
    piezas_a_plegar_plama.grid(row=2, column=0)
    ttk.Label(plasma, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_plasmas = ttk.Entry(plasma, width=10, style='WhiteOnRed.TEntry')
    cantidad_ingresada_plasmas.grid(row=2, column=1)
    tk.Button(
        plasma,
        text="Plasma/Cortar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_plasmas(cantidad_ingresada_plasmas, piezas_a_plegar_plama, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)
    ttk.Separator(plasma, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    stock_plasma = ttk.Frame(plasma, style='Color.TFrame')
    stock_plasma.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_plasma, text="Stock del piezas para plasma", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_plasma,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostar_piezas_para_plasma)
        ).grid(row=1, column=0, pady=3, padx=3) 
    ttk.Button(
        stock_plasma,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_piezas_plasma_teminadad)).grid(row=1, column=1, pady=3, padx=3)
    ttk.Separator(plasma, orient="horizontal").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    
    
    
    
    
    
    cut = ttk.Frame(mecanizsmo, style='Color.TFrame')
    cut.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
    ttk.Label(cut, text="Piezas Cortadas", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Label(cut, text="Piezas para Cortar",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_corte = ttk.Combobox(cut, values=(piezas_corte), state="readonly", width=16)
    piezas_a_corte.grid(row=2, column=0)
    ttk.Label(cut, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_corte = ttk.Entry(cut, width=10, style='WhiteOnRed.TEntry')
    cantidad_ingresada_corte.grid(row=2, column=1)
    tk.Button(
        cut,
        text="Cortar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_corte(cantidad_ingresada_corte, piezas_a_corte, tabla_principal, historial)
        
    ).grid(row=3, column=1, padx=2, pady=2)
    ttk.Separator(cut, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    stock_torno = ttk.Frame(cut, style='Color.TFrame')
    stock_torno.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_torno, text="Stock del piezas cortar", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_torno,
        text="Stock Bruto",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, query_piezas_para_cortar)).grid(row=1, columnspan=2, pady=3, padx=3) 
    
    
    
    
    
    
    
    balancin = ttk.Frame(mecanizsmo, style='Color.TFrame')
    balancin.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
    ttk.Label(balancin, text="Balancin", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Label(balancin, text="Piezas para balancin",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_balancin = ttk.Combobox(balancin, values=(piezas_balancin), state="readonly", width=16)
    piezas_a_balancin.grid(row=2, column=0)
    ttk.Label(balancin, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_balancin = ttk.Entry(balancin, width=10, style='WhiteOnRed.TEntry')
    cantidad_ingresada_balancin.grid(row=2, column=1)
    tk.Button(
        balancin,
        text="Balancin",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_balancin(cantidad_ingresada_balancin, piezas_a_balancin, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)
    ttk.Separator(balancin, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    stock_balancin = ttk.Frame(balancin, style='Color.TFrame')
    stock_balancin.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_balancin, text="Stock del piezas balancin", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_balancin,
        text="Stock Bruto",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_balancin_bruto)).grid(row=1, column=0, pady=3, padx=3) 
    ttk.Button(
        stock_balancin,
        text="Stock Terminado",
        style="Estilo4.TButton", 
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_balancin_terminado)).grid(row=1, column=1, pady=3, padx=3)
    ttk.Separator(balancin, orient="horizontal").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    
    
    
    
    
    box3 = tk.Frame(index)
    box3.grid(row=1, column=2)
    
    mecanizsmo2 = ttk.Frame(box3)
    mecanizsmo2.grid(row=0, column=1)



    augeriado = ttk.Frame(mecanizsmo2, style='Color.TFrame')
    augeriado.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    ttk.Label(augeriado, text="Augeriado", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Label(augeriado, text="Piezas para augeriadar",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_augeriado = ttk.Combobox(augeriado, values=(piezas_para_augeriar), state="readonly", width=16)
    piezas_a_augeriado.grid(row=2, column=0)
    ttk.Label(augeriado, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_agujeriado = ttk.Entry(augeriado, width=10, style='WhiteOnRed.TEntry')
    cantidad_ingresada_agujeriado.grid(row=2, column=1)
    tk.Button(
        augeriado,
        text="Balancin",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_augeriado(cantidad_ingresada_agujeriado, piezas_a_augeriado, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)
    ttk.Separator(augeriado, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    stock_agujeriado = ttk.Frame(augeriado, style='Color.TFrame')
    stock_agujeriado.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_agujeriado, text="Stock del piezas augeriar", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_agujeriado,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostra_pieza_agujeriar )).grid(row=1, column=0, pady=3, padx=3) 
    ttk.Button(
        stock_agujeriado,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_pieza_agujeriar_terminadad)).grid(row=1, column=1, pady=3, padx=3)
    ttk.Separator(augeriado, orient="horizontal").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    
    
    
    
    
    
    
    torno = ttk.Frame(mecanizsmo2, style='Color.TFrame')
    torno.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    ttk.Label(torno, text="Torno", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)

    ttk.Label(torno, text="Piezas A Tornear",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_torner = ttk.Combobox(torno, values=piezas_torno, state="readonly", width=16)
    piezas_a_torner.grid(row=2, column=0)

    ttk.Label(torno, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_torneada = ttk.Entry(torno, width=10, style='WhiteOnRed.TEntry')
    cantidad_torneada.grid(row=2, column=1)

    tk.Button(
        torno,
        text="Tornear",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_torno(cantidad_torneada, piezas_a_torner, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)

    ttk.Separator(torno, orient="horizontal", style="Separador2.TSeparator").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )

    stock_torno = ttk.Frame(torno, style='Color.TFrame')
    stock_torno.grid(row=5, column=0, columnspan=2)
    
    ttk.Label(stock_torno, text="Stock del Torno", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_torno,
        text="Stock Bruto",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostar_piezas_para_tornear)).grid(row=1, column=0, pady=3, padx=3)
    ttk.Button(
        stock_torno,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_piezas_torneada)).grid(row=1, column=1, pady=3, padx=3)

    ttk.Separator(torno, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )







    fresa = ttk.Frame(mecanizsmo2, style='Color.TFrame')
    fresa.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    ttk.Label(fresa, text="Fresa", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)

    ttk.Label(fresa, text="Piezas A Tornear",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_fresa = ttk.Combobox(fresa, values=piezas_para_fresar, state="readonly", width=16)
    piezas_a_fresa.grid(row=2, column=0)

    ttk.Label(fresa, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_fresa = ttk.Entry(fresa, width=10, style='WhiteOnRed.TEntry')
    cantidad_fresa.grid(row=2, column=1)

    tk.Button(
        fresa,
        text="Tornear",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_fresa(cantidad_fresa, piezas_a_fresa, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)

    ttk.Separator(fresa, orient="horizontal", style="Separador2.TSeparator").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )

    stock_fresa = ttk.Frame(fresa, style='Color.TFrame')
    stock_fresa.grid(row=5, column=0, columnspan=2)
    
    ttk.Label(stock_fresa, text="Stock del Torno", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_fresa,
        text="Stock Bruto",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_velas_planchada_cortada)).grid(row=1, column=0, pady=3, padx=3)
    ttk.Button(
        stock_fresa,
        text="Stock Terminado",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_velas_planchada_fresada)).grid(row=1, column=1, pady=3, padx=3)

    ttk.Separator(fresa, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    






    box4 = tk.Frame(index)
    box4.grid(row=1, column=3)
    


    soldador = ttk.Frame(box4, style='Color.TFrame')
    soldador.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    ttk.Label(soldador, text="SOLDADO", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)

    ttk.Label(soldador, text="Piezas A Tornear",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_fresa = ttk.Combobox(soldador, values=piezas_para_fresar, state="readonly", width=16)
    piezas_a_fresa.grid(row=2, column=0)

    ttk.Label(soldador, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_fresa = ttk.Entry(soldador, width=10, style='WhiteOnRed.TEntry')
    cantidad_fresa.grid(row=2, column=1)

    tk.Button(
        soldador,
        text="Tornear",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_fresa(cantidad_fresa, piezas_a_fresa, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)

    ttk.Separator(soldador, orient="horizontal", style="Separador2.TSeparator").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )

    stock_soldador = ttk.Frame(soldador, style='Color.TFrame')
    stock_soldador.grid(row=5, column=0, columnspan=2)
    
    ttk.Label(stock_soldador, text="Stock del Torno", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_soldador,
        text="Stock Bruto",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_velas_planchada_cortada)).grid(row=1, column=0, pady=3, padx=3)
    ttk.Button(
        stock_soldador,
        text="Stock Terminado",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_velas_planchada_fresada)).grid(row=1, column=1, pady=3, padx=3)

    ttk.Separator(soldador, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    

