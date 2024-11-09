import tkinter as tk
from tkinter import ttk
from mycode.funciones.add_funcion import ordenar_por, limpiar_tabla
from mycode.funciones.provedores_funcion import  mostrar_piezas_tablas, mandar_a_pintar, resivir_de_pintura

modelo_piezas = ["BasePintada_330", "BasePintada_300", "cabezal_pintada","caja_eco_augeriada", "teletubi_doblado_eco"]

quety_pintura_bruto = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pintura'"
quety_pintura_terminada = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE ORIGEN = 'pintura'"
quety_en_pintura = "SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'pintura'"


def ventana_pintura(parent):

    frame = ttk.Frame(parent)

    box1 = ttk.Frame(frame)
    box1.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box1, text="Tabla con piezas de Pintura", font=("Arial", 15, "bold"), foreground='white').grid(row=0, column=0, sticky="w", pady=15)


    mostrar_piezas = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza", command= lambda: ordenar_por(mostrar_piezas, "Pieza", False))
    mostrar_piezas.heading("Cantidad", text="Cantidad", command= lambda: ordenar_por(mostrar_piezas, "Cantidad", False))
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=250)
    mostrar_piezas.column("Cantidad", width=110)
    mostrar_piezas.config(height=18)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")


    ttk.Button(box1, text="Limpiar Tabla", command= lambda: limpiar_tabla(mostrar_piezas),bootstyle="primary").grid(row=2, columnspan=2, pady=5 )


    tk.Label(box1, text="Historial" ,font=("Arial", 9, "bold")).grid(row=3, column=0, sticky="sw")
    historial = tk.Listbox(box1, width=60, height=5, font=("Arial", 10, "bold"))
    historial.grid(row=4,column=0)



    box4 = ttk.Frame(frame, bootstyle="light")
    box4.grid(row=0, column=3, padx=40, pady=20)

    # Labelframe para Pintura
    labelframe_pintura = ttk.Labelframe(box4, text="Pintura", padding=30, border=20)
    labelframe_pintura.grid(row=0, column=0, padx=20, pady=20)

    labelframe_stock = ttk.Labelframe(labelframe_pintura, text="Opciones de Stock", padding=10)
    labelframe_stock.grid(row=1, column=0, columnspan=3)

    btn_group = tk.Frame(labelframe_stock,)
    btn_group.grid(row=0, column=0, columnspan=3, padx=5,pady=5)

    ttk.Button(
        btn_group,
        text="Stock en fabrica",bootstyle="primary",
        command=lambda: mostrar_piezas_tablas(mostrar_piezas, quety_pintura_bruto)
    ).grid(row=0, column=0, padx=3, pady=3)

    ttk.Button(
        btn_group,
        text="Stock Terminado",bootstyle="primary",
        command=lambda: mostrar_piezas_tablas(mostrar_piezas, quety_pintura_terminada)
    ).grid(row=0, column=1, padx=3, pady=3)

    ttk.Button(
        btn_group,
        text="Stock en Pintura",bootstyle="primary",
        command=lambda: mostrar_piezas_tablas(mostrar_piezas, quety_en_pintura)
    ).grid(row=1, columnspan=2, padx=3, pady=3)

    ttk.Separator(labelframe_pintura, orient="horizontal").grid(
        row=2, column=0, columnspan=3, padx=5, pady=5
    )

    # Envíos a Pintura
    labelframe_envios = ttk.Labelframe(labelframe_pintura, text="Envíos a Pintura", padding=10 )
    labelframe_envios.grid(row=3, column=0, columnspan=3, pady=5)

    ttk.Label(labelframe_envios, text="Tipo").grid(row=0, column=0, sticky="w")
    modelo = ttk.Combobox(labelframe_envios, values=modelo_piezas, state="readonly", width=17, font= ("Arial", 12, "bold"))
    modelo.grid(row=0, column=1, sticky="w")

    ttk.Label(labelframe_envios, text="Cantidad").grid(row=1, column=0, sticky="w")
    enviar_a_pintura = ttk.Entry(labelframe_envios, width=10)
    enviar_a_pintura.grid(row=1, column=1, sticky="e", pady=1)

    ttk.Button(
        labelframe_envios,
        text="Enviar Bases",bootstyle="warning",
        command=lambda: mandar_a_pintar(modelo, enviar_a_pintura, mostrar_piezas, historial)
    ).grid(row=2, column=1,columnspan=2, padx=2, pady=2, sticky="e")

    # Bases Recibidas
    labelframe_recibidas = ttk.Labelframe(labelframe_pintura, text="Bases Recibidas", padding=10)
    labelframe_recibidas.grid(row=4, column=0, columnspan=3, pady=5)

    ttk.Label(labelframe_recibidas, text="Tipo").grid(row=0, column=0, sticky="w")
    modelo_pintur = ttk.Combobox(labelframe_recibidas, values=modelo_piezas, state="readonly", width=17, font= ("Arial", 12, "bold"))
    modelo_pintur.grid(row=0, column=1, sticky="e")

    ttk.Label(labelframe_recibidas, text="Cantidad").grid(row=1, column=0, sticky="w")
    resibe_cantidad_pintura = ttk.Entry(labelframe_recibidas, width=10)
    resibe_cantidad_pintura.grid(row=1, column=1, sticky="e", pady=1)

    ttk.Button(
        labelframe_recibidas,
        text="Cantidad Recibida",bootstyle="success",
        command=lambda: resivir_de_pintura(modelo_pintur, resibe_cantidad_pintura, mostrar_piezas, historial)
    ).grid(row=2, column=1, padx=2, pady=2, sticky="e")


    return frame