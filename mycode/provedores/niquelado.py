import tkinter as tk
from tkinter import ttk
from mycode.funciones.add_funcion import ordenar_por, limpiar_tabla
from mycode.funciones.provedores_funcion import  mostrar_piezas_tablas, mandar_a_niquelar, resibir_niquelado


quety_niquelado_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'niquelar'"
quety_niquelado_en_niquelado = "SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'niqular'"
quety_niquelado_en_fabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'niquelar'"

niquelado = [
    "eje_rectificado",
    "varilla_brazo_330",
    "varilla_brazo_300",
    "varilla_brazo_250",
    "tubo_manija",
    "tubo_manija_250",
    "palanca_afilador"
]

def ventana_niquelado(parent):
    frame = ttk.Frame(parent, style='Pestania.TFrame')

    box1 = ttk.Frame(frame, style='Pestania.TFrame')
    box1.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box1, text="Tabla P/ De Niquelado", font=("Arial", 15, "bold"), background= '#192965', foreground='white').grid(row=0, column=0, sticky="w", pady=15)


    mostrar_piezas = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza", command= lambda: ordenar_por(mostrar_piezas, "Pieza", False))
    mostrar_piezas.heading("Cantidad", text="Cantidad", command= lambda: ordenar_por(mostrar_piezas, "Cantidad", False))
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=250)
    mostrar_piezas.column("Cantidad", width=110)
    mostrar_piezas.config(height=20)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")


    ttk.Button(box1, text="Limpiar Tabla", command= lambda: limpiar_tabla(mostrar_piezas)).grid(row=2, columnspan=2 )


    tk.Label(box1, text="Historial" ,font=("Arial", 9, "bold")).grid(row=3, column=0, sticky="sw")
    historial = tk.Listbox(box1, width=60, height=5, font=("Arial", 10, "bold"))
    historial.grid(row=4,column=0)



    box4 = tk.Frame(frame)
    box4.grid(row=0, column=3, padx=40)


    # Labelframe para Niquelado/ Rectificado
    labelframe_niquelado = ttk.Labelframe(box4, text="Niquelado/ Rectificado",style="Bold9.TLabelframe" , padding=20)
    labelframe_niquelado.grid(row=3, column=0, columnspan=2, pady=5)

    # Opciones de Stock
    labelframe_stock = ttk.Labelframe(labelframe_niquelado, text="Opciones de Stock", style="Bold9.TLabelframe", padding=10)
    labelframe_stock.grid(row=1, column=0, columnspan=3, pady=5)

    grupbtn = tk.Frame(labelframe_stock)
    grupbtn.grid(row=0, column=0, columnspan=3)

    ttk.Button(
        grupbtn,
        text="Stock en bruto",
        command=lambda: mostrar_piezas_tablas(mostrar_piezas, quety_niquelado_bruto)
    ).grid(row=0, column=0)

    ttk.Button(
        grupbtn,
        text="Stock en niquelado",
        command=lambda: mostrar_piezas_tablas(mostrar_piezas, quety_niquelado_en_niquelado)
    ).grid(row=0, column=1)

    ttk.Button(
        grupbtn,
        text="Stock en fabrica",
        command=lambda: mostrar_piezas_tablas(mostrar_piezas, quety_niquelado_en_fabrica)
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
        command=lambda: mandar_a_niquelar(lista_piezas, cantidad_a_niquelar, mostrar_piezas, historial)
    ).grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky="w")

    # Piezas Terminadas
    labelframe_piezas_terminadas = ttk.Labelframe(labelframe_niquelado, text="Piezas Terminadas", style="Bold9.TLabelframe", padding=10)
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
        command=lambda: resibir_niquelado(lista_piezas_nique, cantidad_a_niquelado, mostrar_piezas, historial)
    ).grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky="w")


    box_info = tk.Frame(box4)
    box_info.grid(row=4, column=1)

    tk.Label(box_info, text="Informacion de la pieza", font=("Arial", 14, "bold")).grid(row=0, column=0)

    detalles = ttk.Labelframe(box_info, text="Detalles...", padding=10, relief="ridge", style="Bold9.TLabelframe")
    detalles.grid(row=1, column=0)

    piezas = tk.Label(detalles, text="", font=("Arial", 8, "bold"))
    piezas.grid(row=0, column=0, sticky="w")

    info_pieza = tk.Label(detalles, text="...", font=("Arial", 10, "bold") ,wraplength=150)
    info_pieza.grid(row=1, column=0)

    img_pieza = tk.Frame(detalles)
    img_pieza.grid(row=2, column=0)

    imagen_piezas = tk.Label(img_pieza)
    imagen_piezas.grid(row=0, column=0)

    return frame