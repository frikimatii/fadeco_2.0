import tkinter as tk 
from tkinter import ttk
from mycode.funciones.mecanizasdo_funcion import accion_plegadora, accion_plasmas, mostrar_piezas_tablas, limpiar_tabla, accion_corte, accion_balancin, accion_torno, accion_augeriado, accion_fresa, accion_soldar, accion_pulir
from mycode.funciones.add_funcion import ordenar_por
from PIL import Image, ImageTk


lista_piezas_plegadora = ["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco", "bandeja_cabezal_inox_250", "bandeja_cabezal_pintada" , "bandeja_cabezal_inox", "chapa_U_inox_250", "chapa_U_pintada","chapa_U_inox"]

lista_piezas_plegadora.sort()


lista_piezas_plasma = ["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco", "planchada_330", "planchada_300", "planchada_250", "vela_330", "vela_300", "vela_250","bandeja_cabezal_inox_250", "bandeja_cabezal_pintada" , "bandeja_cabezal_inox", "pieza_caja_eco", "media_luna"]

lista_piezas_plasma.sort()

piezas_corte = [ "planchuela_250", "planchuela_300", "planchuela_330", "varilla_300", "varilla_330", "varilla_250", "portaeje", "eje_rectificado", "varilla_brazo_330" ,"varilla_brazo_300" ,"varilla_brazo_250" ,"tubo_manija" ,"tubo_manija_250" ,"cuadrado_regulador" ,"palanca_afilador" ,"eje_corto" ,"eje_largo" ,"buje_eje_eco" ,"teletubi_eco", "guia_u", "chapa_cubre_cabezal_inox", "chapa_cubre_cabezal_pintada", "chapa_cubre_cabezal_inox_250", "planchuela_inferior", "planchuela_interna"]

piezas_corte.sort()

piezas_balancin = ["planchuela_250","planchuela_300","planchuela_330","portaeje", "guia_u", "teletubi_eco", "chapaU_inox", "chapaU_pintada", "chapaU_inox_250", "eje_corto", "eje_largo"]

piezas_balancin.sort()

piezas_para_augeriar = ["cuadrado_regulador","brazo_330","brazo_300","brazo_250", "carros", "carros_250", "movimiento", "tornillo_teletubi_eco" ]

piezas_para_augeriar.sort()

piezas_torno = ["buje_eje_eco", "eje", "eje_250", "manchon", "manchon_250", "rueditas", "tornillo_guia", "carros", "carros_250","movimiento", "caja_300", "caja_330", "caja_250", "cubrecuchilla_300", "teletubi_300", "tornillo_teletubi_eco", "caja_330_armada", "caja_300_armada", "caja_250_armada", "caja_eco_armada", "tapa_afilador_eco_torno"]

piezas_torno.sort()

piezas_para_lijar = ["aro_numerador", "carcaza_afilador"]

piezas_para_lijar.sort()

piezas_para_fresar = ["vela_250", "vela_300", "vela_330","planchada_330","planchada_300","planchada_250"]

piezas_para_fresar.sort()

piezas_para_soldar =[ "vela_fresada_330","vela_fresada_300", "vela_fresada_250", "planchada_fresada_250", "planchada_fresada_330", "planchada_fresada_300", "varilla_330","varilla_300","varilla_250", "caja_soldada_eco", "cuadrado_regulador", "cabezal_inox", "cabezal_pintada", "cabezal_eco"] 

piezas_para_soldar.sort()

piezas_pulir = [ "cabezal_250" ,"cabezal_inox"]

piezas_pulir.sort()


query_mostrar_piezas_parar_doblar = "SELECT PIEZAS,CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'plegadora'"

query_mostrar_piezas_dobladas = "SELECT PIEZAS, CANTIDAD FROM plasma WHERE ORIGEN = 'plegado' UNION SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'plegado'"

query_mostar_piezas_para_plasma = "SELECT PIEZAS, CANTIDAD FROM plasma WHERE MECANIZADO = 'plasma' UNION SELECT PIEZAS,CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'plasma'"

query_piezas_plasma_teminadad = "SELECT PIEZAS,CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'soldar'"

query_piezas_para_cortar = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE  MECANIZADO = 'corte' UNION SELECT PIEZAS , CANTIDAD FROM piezas_brutas WHERE PIEZAS = 'buje_eje_eco' "

querty_piezas_cortadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'corte' "

query_mostrar_piezas_balancin_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'balancin'"

query_mostrar_piezas_balancin_terminado = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'balancin' UNION SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PIEZAS = 'teletubi_doblado_eco' "

query_mostar_piezas_para_tornear = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO ='torno_caja' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'torno' "

querty_mostrar_piezas_torneada = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MECANIZADO ='torno_caja' UNION SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'torno' UNION SELECT PIEZAS ,CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'torno' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE ORIGEN = 'torno'" 

querty_mostra_pieza_agujeriar = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'agueriado' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'augeriado'"

querty_pieza_agujeriar_terminadad = "SELECT PIEZAS,CANTIDAD FROM piezas_terminadas WHERE MECANIZADO = 'augeriado' UNION  SELECT PIEZAS,CANTIDAD FROM PIEZAS_RETOCADA WHERE ORIGEN = 'fundidor'"

querty_mostrar_velas_planchada_cortada = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = 'fresado'"

querty_mostrar_velas_planchada_fresada = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'fresado'"

querty_mostrar_para_pulir = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pulidor_'"

querty_mostrar_pulido = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'pulido_'"


querty_mostrar_para_soldador_ = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'soldado' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE PIEZAS = 'cuadrado_regulador' "

querty_mostrar_soldador_ = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'soldador_' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE ORIGEN = 'soldado_' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PIEZAS = 'caja_soldada_eco' "


query_piezas_plasma_terminadas = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'plama' UNION SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE TIPO_DE_MATERIAL = 'Chapa_' AND MECANIZADO = 'plegadora'"

def mecanizado(ventana):


    stylo_ventana = ttk.Style()
    stylo_ventana.configure('Pestania.TNotebook', background= '#192965')

    pestania = ttk.Frame(ventana)
    ventana.add(pestania, text="Mecanizado")

    index = ttk.Frame(pestania,)
    index.grid(row=0, column=0)

    ttk.Label(index, text="Mecanizado", font=("Arial", 25, "bold", 'underline'),).grid(row=0,columnspan=6 )

    box1 = ttk.Frame(index,)
    box1.grid(row=1, column=0, padx=5, sticky="nw")
    
    ttk.Label(box1, text="Tabla de piezas Mecanizado", font=("Arial", 16, "bold", "underline"),).grid(row=0,column=0 , sticky="w")

    tabla_principal = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    tabla_principal.heading("Pieza", text="Pieza", command= lambda: ordenar_por(tabla_principal, "Pieza", False))
    tabla_principal.heading("Cantidad", text="Cant.",command= lambda: ordenar_por(tabla_principal, "Cantidad", False))
    tabla_principal.column("#0", width=0,stretch=tk.NO)
    tabla_principal.column("Pieza", width=220)
    tabla_principal.column("Cantidad", width=40)
    tabla_principal.config(height=18)
    tabla_principal.grid(row=2, column=0, sticky="nsew")
    ttk.Button(box1, text="Limpiar", command=lambda: limpiar_tabla(tabla_principal),bootstyle="warning").grid(row=4, column=0, pady=5)

    ttk.Label(box1, text="Historial", font=("Arial", 9, "bold"),).grid(row=5, column=0, sticky="w")

    historial = tk.Listbox(box1, width=50, font=("Arial", 10, "bold"), height=7)
    historial.grid(row=6,column=0)

    
    
    
    
    box2 = ttk.Frame(index ,)
    box2.grid(row=1, column=1, padx=3, pady=3)

    img_plegadora = Image.open(r"C:\Fadeco_stock\img\dobladora.png")
    img_redimencionada = img_plegadora.resize((50, 50))
    img_plgadora_ = ImageTk.PhotoImage(img_redimencionada)

    # Configuración del marco mecánizmo
    mecanizsmo = ttk.Frame(box2,)
    mecanizsmo.grid(row=0, column=0, sticky="nw")

    # Configuración del marco plegadora
    style = ttk.Style()
    style.configure("Bold9.TLabelframe.Label", font=("Helvetica", 12, "bold"))
    style.configure("WhiteOnRed.TLabel", font=("Arial", 9, "bold"))
    # Configuración del marco plegadora

    plegadora = ttk.Frame(mecanizsmo, bootstyle="light", padding=4)
    plegadora.grid(row=0, column=0, columnspan=2)

    # Paned Window
    panel = ttk.PanedWindow(plegadora, orient=tk.VERTICAL)
    panel.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Frame Plegadora
    frame_plegar = ttk.Labelframe(panel, text="Plegadora",)
    panel.add(frame_plegar)

    ttk.Label(frame_plegar, text="Piezas a plegar", style='WhiteOnRed.TLabel').grid(row=0, column=0)

    piezas_a_plegar = ttk.Combobox(frame_plegar, values=(lista_piezas_plegadora), state="readonly", width=17, font= ("Arial", 12, "bold"))
    piezas_a_plegar.grid(row=1, column=0)

    ttk.Label(frame_plegar, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=0, column=1)

    cantidad_ingresada = ttk.Entry(frame_plegar, width=10, font=("Arial", 12, "bold"))
    cantidad_ingresada.grid(row=1, column=1)

    ttk.Button(
        frame_plegar,
        text="DOBLAR",
        bootstyle="success",
        command=lambda: accion_plegadora(cantidad_ingresada, piezas_a_plegar, tabla_principal, historial)
    ).grid(row=2, column=1, padx=5, pady=5)

    # Frame Stock del Plegado
    frame_stock = ttk.Labelframe(panel, text="Stock del Plegado",)
    panel.add(frame_stock)

    ttk.Button(
        frame_stock,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_parar_doblar)
    ).grid(row=0, column=0, pady=3, padx=3)

    ttk.Button(
        frame_stock,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_dobladas)
    ).grid(row=0, column=1, pady=3, padx=3)

    tk.Label(frame_stock, image=img_plgadora_).grid(row=0, column=2, pady=3, padx=3)



    # Retain reference to the image to prevent it from being garbage collected
    mecanizsmo.img_plgadora_ = img_plgadora_
    

    # Carga y redimensionamiento de la imagen del Plasma
    img_plasma = Image.open(r"C:\Fadeco_stock\img\plasma.png")
    img_redimensionada_plasma = img_plasma.resize((50, 50))
    img_plasma_ = ImageTk.PhotoImage(img_redimensionada_plasma)




    # Frame para Plasma
    plasma = ttk.Frame(mecanizsmo, bootstyle="light", padding=4)
    plasma.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    # Panel2 dentro de Plasma
    panel2 = ttk.PanedWindow(plasma, orient=tk.VERTICAL)
    panel2.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Frame Plasma con su etiqueta
    frame_plasma = ttk.Labelframe(panel2, text="Plasma",)
    panel2.add(frame_plasma)

    ttk.Label(frame_plasma, text="Piezas para Cortar", style="WhiteOnRed.TLabel").grid(row=0, column=0)

    # Combobox para seleccionar piezas a cortar
    piezas_a_cortar_plasma = ttk.Combobox(frame_plasma, values=lista_piezas_plasma, state="readonly", width=17, font= ("Arial", 12, "bold"))
    piezas_a_cortar_plasma.grid(row=1, column=0)

    # Label y Entry para ingresar la cantidad
    ttk.Label(frame_plasma, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=0, column=1)

    cantidad_ingresada_plasma = ttk.Entry(frame_plasma, width=10, font=("Arial", 12, "bold"))
    cantidad_ingresada_plasma.grid(row=1, column=1)

    # Botón para ejecutar la acción de cortar con Plasma
    ttk.Button(
        frame_plasma,
        text="PLASMA",
        bootstyle="success",
        command=lambda: accion_plasmas(cantidad_ingresada_plasma, piezas_a_cortar_plasma, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=5)

    # Frame para el stock del Plasma
    frame_stock2 = ttk.Labelframe(panel2, text="Stock para el Plasma",)
    panel2.add(frame_stock2)

    # Botones para mostrar el stock bruto y el stock terminado
    ttk.Button(
        frame_stock2,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostar_piezas_para_plasma)
    ).grid(row=1, column=0, pady=3, padx=3)

    ttk.Button(
        frame_stock2,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_piezas_plasma_terminadas)
    ).grid(row=1, column=1, pady=3, padx=3)

    tk.Label(frame_stock2, image=img_plasma_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    mecanizsmo.img_plasma_ = img_plasma_




    imagen_sierra = Image.open(r"C:\Fadeco_stock\img\sierra.png")
    img_redimensionada_sierra = imagen_sierra.resize((50, 50))
    img_sierra_ = ImageTk.PhotoImage(img_redimensionada_sierra)

    # Frame para Sierra
    cut = ttk.Frame(mecanizsmo, bootstyle="light", padding=4)
    cut.grid(row=2, column=0,columnspan=2)

    # Labelframe para la sección de corte
    frame_sierra = ttk.Labelframe(cut, text="PIEZAS CORTADAS",)
    frame_sierra.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Etiqueta y Combobox para seleccionar piezas a cortar
    ttk.Label(frame_sierra, text="Piezas De Corte", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_corte = ttk.Combobox(frame_sierra, values=piezas_corte, state="readonly", width=17, font= ("Arial", 12, "bold"))
    piezas_a_corte.grid(row=2, column=0)

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_sierra, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_corte = ttk.Entry(frame_sierra, width=10, font=("Arial", 12, "bold"))
    cantidad_ingresada_corte.grid(row=2, column=1)

    # Botón para ejecutar la acción de cortar
    ttk.Button(
        frame_sierra,
        text="Cortar",
        bootstyle="success",
        command=lambda: accion_corte(cantidad_ingresada_corte, piezas_a_corte, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=5)


    # Labelframe para el stock de piezas a cortar
    frame_stock_sierra = ttk.Labelframe(cut, text="Stock de Piezas Cortadas",)
    frame_stock_sierra.grid(row=1, column=0, columnspan=2, sticky="nsew")

    ttk.Button(
        frame_stock_sierra,
        text="Stock Bruto",
        bootstyle="info-outline", 
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_piezas_para_cortar)
    ).grid(row=1, column=0, pady=3, padx=3)

    # Añadir la imagen de la Sierra al frame de stock
    tk.Label(frame_stock_sierra, image=img_sierra_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    mecanizsmo.img_sierra_ = img_sierra_
    

    
    
    
    box3 = ttk.Frame(index,bootstyle="dark") 
    box3.grid(row=1, column=2, padx=3, pady=3)
    
    mecanizsmo2 = ttk.Frame(box3,)
    mecanizsmo2.grid(row=0, column=1, sticky="nw")



    imagen_augeriado = Image.open(r"C:\Fadeco_stock\img\augeriado.png")
    img_redimensionada_augeriado = imagen_augeriado.resize((50, 50))
    img_augeriado_ = ImageTk.PhotoImage(img_redimensionada_augeriado)


    # Frame principal para Augeriado
    augeriado = ttk.Frame(mecanizsmo2, bootstyle="light", padding=4)
    augeriado.grid(row=0, column=0, padx=5, pady=5,columnspan=2)

    # Labelframe para la sección de Augeriado
    frame_augeriado = ttk.Labelframe(augeriado, text="Augeriado",)
    frame_augeriado.grid(row=0, column=0, columnspan=2, sticky="nsew")


    # Etiqueta y Combobox para seleccionar piezas a augeriar
    ttk.Label(frame_augeriado, text="Piezas para Augeriar", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    
    piezas_a_augeriado = ttk.Combobox(frame_augeriado, values=piezas_para_augeriar, state="readonly", width=17, font= ("Arial", 12, "bold"))
    piezas_a_augeriado.grid(row=2, column=0)

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_augeriado, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_ingresada_agujeriado = ttk.Entry(frame_augeriado, width=10, font=("Arial", 12, "bold"))
    cantidad_ingresada_agujeriado.grid(row=2, column=1)

    # Botón para ejecutar la acción de augeriar
    ttk.Button(
        frame_augeriado,
        text="AUGERIADO",
        bootstyle="success",
        command=lambda: accion_augeriado(cantidad_ingresada_agujeriado, piezas_a_augeriado, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=5)

    # Labelframe para el stock de piezas a augeriar
    frame_stock_augeriado = ttk.Labelframe(augeriado, text="Stock de Augeriado",)
    frame_stock_augeriado.grid(row=1, column=0, columnspan=2, sticky="nsew")

    ttk.Button(
        frame_stock_augeriado,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostra_pieza_agujeriar)
    ).grid(row=1, column=0, pady=3, padx=3)

    ttk.Button(
        frame_stock_augeriado,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_pieza_agujeriar_terminadad)
    ).grid(row=1, column=1, pady=3, padx=3)

    tk.Label(frame_stock_augeriado, image=img_augeriado_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    mecanizsmo.img_augeriado_ = img_augeriado_
    


    # Carga y redimensionamiento de la imagen del Torno
    imagen_torno = Image.open(r"C:\Fadeco_stock\img\torno.png")
    img_redimensionada_torno = imagen_torno.resize((50, 50))
    img_torno_ = ImageTk.PhotoImage(img_redimensionada_torno)

    # Frame principal para Torno
    torno = ttk.Frame(mecanizsmo2, bootstyle="light", padding=5)
    torno.grid(row=1, column=0, padx=5, pady=5,columnspan=2)

    # Labelframe para la sección de Torno
    frame_torno = ttk.Labelframe(torno, text="Torno",)
    frame_torno.grid(row=0, column=0, columnspan=2, sticky="nsew")


    # Etiqueta y Combobox para seleccionar piezas a tornear
    ttk.Label(frame_torno, text="Piezas A Tornear", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_torner = ttk.Combobox(frame_torno, values=piezas_torno, state="readonly", width=17, font= ("Arial", 12, "bold"))
    piezas_a_torner.grid(row=2, column=0)

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_torno, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_torneada = ttk.Entry(frame_torno, width=10, font=("Arial", 12, "bold"))
    cantidad_torneada.grid(row=2, column=1)

    # Botón para ejecutar la acción de tornear
    ttk.Button(
        frame_torno,
        text="TORNEAR",
        bootstyle="success",
        command=lambda: accion_torno(cantidad_torneada, piezas_a_torner, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=5)

    # Labelframe para el stock de piezas tornear
    frame_stock_torno = ttk.Labelframe(torno, text="Stock de Torno",)
    frame_stock_torno.grid(row=1, column=0, columnspan=2, sticky="nsew")

    ttk.Button(
        frame_stock_torno,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostar_piezas_para_tornear)
    ).grid(row=1, column=0, pady=3, padx=3)

    ttk.Button(
        frame_stock_torno,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_piezas_torneada)
    ).grid(row=1, column=1, pady=3, padx=3)

    # Añadir la imagen del Torno al frame de stock
    tk.Label(frame_stock_torno, image=img_torno_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    mecanizsmo2.img_torno_ = img_torno_




    # Carga y redimensionamiento de la imagen de la Fresa
    imagen_fresa = Image.open(r"C:\Fadeco_stock\img\fresado.png")
    img_redimensionada_fresa = imagen_fresa.resize((50, 50))
    img_fresa_ = ImageTk.PhotoImage(img_redimensionada_fresa)

    # Frame principal para Fresa
    fresa = ttk.Frame(mecanizsmo2, bootstyle="light", padding=5)
    fresa.grid(row=2, column=0, padx=5, pady=5,columnspan=2)

    # Labelframe para la sección de Fresa
    frame_fresa = ttk.Labelframe(fresa, text="Fresa",)
    frame_fresa.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Etiqueta y Combobox para seleccionar piezas a fresar
    ttk.Label(frame_fresa, text="Piezas A Fresar", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_fresa = ttk.Combobox(frame_fresa, values=piezas_para_fresar,state="readonly", width=17, font= ("Arial", 12, "bold"))
    piezas_a_fresa.grid(row=2, column=0)

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_fresa, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_fresa = ttk.Entry(frame_fresa, width=10, font=("Arial", 12, "bold"))
    cantidad_fresa.grid(row=2, column=1)

    # Botón para ejecutar la acción de fresar
    ttk.Button(
        frame_fresa,
        text="FRESAR",
        bootstyle="success",
        command=lambda: accion_fresa(cantidad_fresa, piezas_a_fresa, tabla_principal, historial)
    ).grid(row=3, column=1, padx=2, pady=2)

    # Labelframe para el stock de piezas fresar
    frame_stock_fresa = ttk.Labelframe(fresa, text="Stock de Fresa",)
    frame_stock_fresa.grid(row=1, column=0, columnspan=2, sticky="nsew")


    ttk.Button(
        frame_stock_fresa,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_velas_planchada_cortada)
    ).grid(row=1, column=0, pady=3, padx=3)

    ttk.Button(
        frame_stock_fresa,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_velas_planchada_fresada)
    ).grid(row=1, column=1, pady=3, padx=3)

    # Añadir la imagen de la Fresa al frame de stock
    tk.Label(frame_stock_fresa, image=img_fresa_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    mecanizsmo2.img_fresa_ = img_fresa_






    box4 = ttk.Frame(index ,bootstyle="dark")
    box4.grid(row=1, column=3,padx=3, pady=3)
    

    # Carga y redimensionamiento de imágenes
    imagen_soldador = Image.open(r"C:\Fadeco_stock\img\soldador.png")
    img_redimensionada_soldador = imagen_soldador.resize((50, 50))
    img_soldador_ = ImageTk.PhotoImage(img_redimensionada_soldador)

    imagen_pulido = Image.open(r"C:\Fadeco_stock\img\pulido.png")
    img_redimensionada_pulido = imagen_pulido.resize((50, 50))
    img_pulido_ = ImageTk.PhotoImage(img_redimensionada_pulido)

    imagen_balancin = Image.open(r"C:\Fadeco_stock\img\balancin.png")
    img_redimensionada_balancin = imagen_balancin.resize((50, 50))
    img_balancin_ = ImageTk.PhotoImage(img_redimensionada_balancin)

    mecanizado5 = ttk.Frame(box4,)
    mecanizado5.grid(row=0, column=0, sticky="nw")
    
        # Frame principal para Soldador
    soldador = ttk.Frame(mecanizado5, bootstyle="light", padding=4)
    soldador.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    # Labelframe para la sección de Soldador
    frame_soldador = ttk.Labelframe(soldador, text="Soldador",)
    frame_soldador.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Etiqueta y Combobox para seleccionar piezas a soldar
    ttk.Label(frame_soldador, text="Piezas A Soldar", style='WhiteOnRed.TLabel').grid(row=1, column=0, sticky="ew")
    piezas_a_soldar = ttk.Combobox(frame_soldador, values=piezas_para_soldar, state="readonly", width=17, font=("Arial", 12, "bold"))
    piezas_a_soldar.grid(row=2, column=0, sticky="ew")

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_soldador, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1, sticky="ew")
    cantidad_sold = ttk.Entry(frame_soldador, width=10, font=("Arial", 12, "bold"))
    cantidad_sold.grid(row=2, column=1, sticky="ew")

    # Botón para ejecutar la acción de soldar
    ttk.Button(
        frame_soldador,
        text="SOLDAR",
        bootstyle="success",
        command=lambda: accion_soldar(cantidad_sold, piezas_a_soldar, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=5)

    # Labelframe para el stock de piezas soldar
    frame_stock_soldador = ttk.Labelframe(soldador, text="Stock de Soldador",)
    frame_stock_soldador.grid(row=1, column=0, columnspan=2, sticky="nsew")

    # Botones para stock
    ttk.Button(
        frame_stock_soldador,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_para_soldador_)
    ).grid(row=1, column=0, pady=3, padx=3, sticky="ew")

    ttk.Button(
        frame_stock_soldador,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_soldador_)
    ).grid(row=1, column=1, pady=3, padx=3, sticky="ew")

    # Añadir la imagen del Soldador al frame de stock
    tk.Label(frame_stock_soldador, image=img_soldador_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    box4.img_soldador_ = img_soldador_


    # Repetir la misma estructura para Pulido y Balancín
    # Frame principal para Pulido
    pulido = ttk.Frame(mecanizado5, bootstyle="light", padding=4)
    pulido.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    # Labelframe para la sección de Pulido
    frame_pulido = ttk.Labelframe(pulido, text="Pulido",)
    frame_pulido.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Etiqueta y Combobox para seleccionar piezas a pulir
    ttk.Label(frame_pulido, text="Piezas A Pulir", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    
    
    piezas_a_pulido = ttk.Combobox(frame_pulido, values=piezas_pulir, state="readonly", width=17, font=("Arial", 12, "bold"))
    piezas_a_pulido.grid(row=2, column=0, sticky="ew")

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_pulido, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1, sticky="ew")
    cantidad_pulido = ttk.Entry(frame_pulido, width=10, font=("Arial", 12, "bold"))
    cantidad_pulido.grid(row=2, column=1, sticky="ew")

    # Botón para ejecutar la acción de pulir
    ttk.Button(
        frame_pulido,
        text="PULIR",
        bootstyle="success",
        command=lambda: accion_pulir(piezas_a_pulido, cantidad_pulido, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=2,)

    # Labelframe para el stock de piezas pulir
    frame_stock_pulido = ttk.Labelframe(pulido, text="Stock de Pulido",)
    frame_stock_pulido.grid(row=1, column=0, columnspan=2, sticky="nsew")

    # Botones para stock
    ttk.Button(
        frame_stock_pulido,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_para_pulir)
    ).grid(row=1, column=0, pady=3, padx=3, sticky="ew")

    ttk.Button(
        frame_stock_pulido,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, querty_mostrar_pulido)
    ).grid(row=1, column=1, pady=3, padx=3, sticky="ew")

    # Añadir la imagen del Pulido al frame de stock
    tk.Label(frame_stock_pulido, image=img_pulido_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    box4.img_pulido_ = img_pulido_

    # Frame principal para Balancín
    balancin = ttk.Frame(mecanizado5, bootstyle="light", padding=5)
    balancin.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")

    # Labelframe para la sección de Balancín
    frame_balancin = ttk.Labelframe(balancin, text="Balancín",)
    frame_balancin.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Etiqueta y Combobox para seleccionar piezas a balancinear
    ttk.Label(frame_balancin, text="Piezas para Balancín", style='WhiteOnRed.TLabel').grid(row=1, column=0, sticky="ew")
    piezas_a_balancin = ttk.Combobox(frame_balancin, values=piezas_balancin, state="readonly", width=17, font=("Arial", 12, "bold"))
    piezas_a_balancin.grid(row=2, column=0, sticky="ew")

    # Etiqueta y Entry para ingresar la cantidad
    ttk.Label(frame_balancin, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=1, column=1, sticky="ew")
    cantidad_balancin = ttk.Entry(frame_balancin, width=10, font=("Arial", 12, "bold"))
    cantidad_balancin.grid(row=2, column=1, sticky="ew")

    # Botón para ejecutar la acción de balancinar
    ttk.Button(
        frame_balancin,
        text="Balancinar",
        bootstyle="success",
        command=lambda: accion_balancin(cantidad_balancin, piezas_a_balancin, tabla_principal, historial)
    ).grid(row=3, column=1, padx=5, pady=2, sticky="ew")

    # Labelframe para el stock de piezas balancinar
    frame_stock_balancin = ttk.Labelframe(balancin, text="Stock de Balancín",)
    frame_stock_balancin.grid(row=1, column=0, columnspan=2, sticky="nsew")

    # Botones para stock
    ttk.Button(
        frame_stock_balancin,
        text="Stock Bruto",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_balancin_bruto)
    ).grid(row=1, column=0, pady=3, padx=3, sticky="ew")

    ttk.Button(
        frame_stock_balancin,
        text="Stock Terminado",
        bootstyle="info-outline",
        command=lambda: mostrar_piezas_tablas(tabla_principal, query_mostrar_piezas_balancin_terminado)
    ).grid(row=1, column=1, pady=3, padx=3, sticky="ew")

    # Añadir la imagen del Balancín al frame de stock
    tk.Label(frame_stock_balancin, image=img_balancin_).grid(row=1, column=2, pady=3, padx=3)

    # Retener referencia de la imagen para evitar su eliminación por el recolector de basura
    box4.img_balancin_ = img_balancin_
