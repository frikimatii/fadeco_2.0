import tkinter as tk 
from tkinter import ttk
from mycode.funciones.mecanizasdo_funcion import accion_plegadora, accion_plasmas, mostrar_piezas_tablas, limpiar_tabla, accion_corte, accion_balancin

macanizado = ["plasma", "plegadora", "soldador", ""]

lista_piezas_plasma = ["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","ChapaBase_330Eco","lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco"]

piezas_corte = ["planchuela_250","planchuela_300","planchuela_330","varilla_300","varilla_330","varilla_250","portaeje"]

piezas_balancin = ["planchuela_250","planchuela_300","planchuela_330","portaeje"]

query_mostrar_piezas_parar_doblar = "SELECT PIEZAS,CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'plegadora'"

query_mostrar_piezas_dobladas = "SELECT PIEZAS, CANTIDAD FROM plasma WHERE ORIGEN = 'plegado' UNION SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'plegado'"

query_mostar_piezas_para_plasma = "SELECT PIEZAS, CANTIDAD FROM plasma WHERE MECANIZADO = 'plasma' UNION SELECT PIEZAS,CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'plasma'"

query_piezas_plasma_teminadad = "SELECT PIEZAS,CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'soldar' "

query_piezas_para_cortar = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'corte'"

querty_piezas_cortadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'corte' "

query_mostrar_piezas_balancin_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'balancin'"

query_mostrar_piezas_balancin_terminado = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'balancin'"



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
    piezas_a_plegar_plegada = ttk.Combobox(plegadora, values=(lista_piezas_plasma), state="readonly", width=20)
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
    
    
    
    
    
    
    
    
    torno = ttk.Frame(mecanizsmo, style='Color.TFrame')
    torno.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
    ttk.Label(torno, text="Piezas Cortadas", style="WhiteOnRed.TLabel", font=("Verdana", 15, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Label(torno, text="Piezas para Cortar",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_corte = ttk.Combobox(torno, values=(piezas_corte), state="readonly", width=16)
    piezas_a_corte.grid(row=2, column=0)
    ttk.Label(torno, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_corte = ttk.Entry(torno, width=10, style='WhiteOnRed.TEntry')
    cantidad_ingresada_corte.grid(row=2, column=1)
    tk.Button(
        torno,
        text="Cortar",
        background="green",
        foreground="white",
        padx=4,
        pady=1,
        font=('Helvetica', 8, "bold"),
        command=lambda: accion_corte(cantidad_ingresada_corte, piezas_a_corte, tabla_principal, historial)
        
    ).grid(row=3, column=1, padx=2, pady=2)
    ttk.Separator(torno, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    stock_torno = ttk.Frame(torno, style='Color.TFrame')
    stock_torno.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_torno, text="Stock del piezas cortar", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_torno,
        text="Stock Bruto",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, query_piezas_para_cortar)).grid(row=1, column=0, pady=3, padx=3) 
    ttk.Button(
        stock_torno,
        text="Stock Terminado",
        style="Estilo4.TButton", command=lambda: mostrar_piezas_tablas(tabla_principal, querty_piezas_cortadas)).grid(row=1, column=1, pady=3, padx=3)
    ttk.Separator(torno, orient="horizontal").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=2, pady=2
    )
    
    
    
    
    
    
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
    