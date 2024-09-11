
import tkinter as tk
from tkinter import ttk
from mycode.funciones.add_funcion import ordenar_por, limpiar_tabla
from mycode.funciones.provedores_funcion import  mostrar_piezas_tablas, mecanizar_carcaza, resibir_afiladores

piezas_afilador = ["capuchon_afilador","carcaza_afilador","eje_corto","eje_largo","ruleman608","palanca_afilador","resorte_palanca","resorte_empuje"]


query_piezas_afialador_fabrica = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'pieza_afilador'"

query_piezas_afialador_en_roman = "SELECT PIEZAS, CANTIDAD FROM AFILADOR "

query_afialador_terminado = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = 'afilador_final' "

query_piezas_carcaza = "SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PIEZAS = 'carcaza_afilador' "


def ventana_afilador(parent):
    frame = ttk.Frame(parent)

    box1 = ttk.Frame(frame)
    box1.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box1, text="Tabla con piezas de Carmelo", font=("Arial", 15, "bold")).grid(row=0, column=0, sticky="w", pady=15)


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



    box10 = tk.Frame(frame)
    box10.grid(row=0, column=4, padx=40)

    # Sección del Armado De Afilador en un Labelframe
    labelframe_afilador = ttk.Labelframe(box10, text="Armado De Afilador", style="Bold9.TLabelframe", padding=20)
    labelframe_afilador.grid(row=0, column=3, sticky="n", pady=3, padx=4, columnspan=2)

    # Mostrar Piezas
    ttk.Label(labelframe_afilador, text="Mostrar Piezas", style="WhiteOnRed.TLabel").grid(row=1, column=0, columnspan=2)
    tk.Button(labelframe_afilador, text="En Fabrica", font=('Arial', 8, "italic"), bg="gray", fg="white", command=lambda:   mostrar_piezas_tablas(mostrar_piezas, query_piezas_afialador_fabrica)).grid(row=2, column=1)
    tk.Button(labelframe_afilador, text="En Roman", font=('Arial', 8, "italic"), bg="gray", fg="white", command=lambda:     mostrar_piezas_tablas(mostrar_piezas, query_piezas_afialador_en_roman)).grid(row=2, column=0)

    # Separador
    ttk.Separator(labelframe_afilador, orient="horizontal").grid(row=3, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    # Afiladores Terminados
    ttk.Label(labelframe_afilador, text="Afiladores Terminadas", style="WhiteOnRed.TLabel").grid(row=4, column=0, columnspan=2)
    tk.Button(labelframe_afilador, text="Mostrar", font=('Arial', 8, "italic"), bg="gray", fg="white", command=lambda:  mostrar_piezas_tablas(mostrar_piezas, query_afialador_terminado)).grid(row=5, column=0, columnspan=2)

    # Separador
    ttk.Separator(labelframe_afilador, orient="horizontal").grid(row=6, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    # Sección de envíos de Afilador en un sub-Labelframe
    labelframe_envios = ttk.Labelframe(labelframe_afilador, text="Envíos de Afilador", padding=10, style="Bold9.TLabelframe")
    labelframe_envios.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=5, padx=5)

    # Carcaza mecanizadas
    ttk.Label(labelframe_envios, text="ingrese Cantidad De Carcaza mecanizadas", font=("Arial", 10, "bold")).grid(row=0, column=0)
    cantidad_ingresada_carcaza = ttk.Entry(labelframe_envios)
    cantidad_ingresada_carcaza.grid(row=2, column=0, pady=2)

    tk.Button(labelframe_envios, text="Mecanizar", command=lambda: mecanizar_carcaza(cantidad_ingresada_carcaza, mostrar_piezas,   historial)).grid(row=3, column=0, pady=10)
    tk.Button(labelframe_envios, text="Consulta Carcaza brutas", command=lambda: mostrar_piezas_tablas(mostrar_piezas,    query_piezas_carcaza)).grid(row=3, column=1, pady=10)

    # Separador
    ttk.Separator(labelframe_envios, orient="horizontal").grid(row=4, column=0, sticky="ew", columnspan=2, pady=3, padx=10)

    # Enviar piezas a Roman
    ttk.Label(labelframe_envios, text="Enviar piezas a Roman", font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2)
    ttk.Label(labelframe_envios, text="Piezas").grid(row=6, column=0)
    ttk.Label(labelframe_envios, text="Cantidad").grid(row=6, column=1)

    comboxboxafiladores = ttk.Combobox(labelframe_envios, values=piezas_afilador, state="readonly", width=17, font=("Arial", 12,    "bold"))
    comboxboxafiladores.grid(row=7, column=0)

    entrycantidad1 = ttk.Entry(labelframe_envios, width=7)
    entrycantidad1.grid(row=7, column=1)

    tk.Button(labelframe_envios, text="Envios a Roman", bg="green", fg="white", command=lambda: mandar_a_roman(comboxboxafiladores,     entrycantidad1, tabla_principal, historial)).grid(row=8, column=1)

    # Separador
    ttk.Separator(labelframe_envios, orient="horizontal").grid(row=9, column=0, sticky="ew", columnspan=2, pady=3, padx=3)

    # Entrega de Afiladores Terminados
    ttk.Label(labelframe_envios, text="Entrega de Afiladores Terminados", font=("Arial", 10, "bold")).grid(row=10, column=0,    columnspan=2)

    cantidad_terminada = ttk.Entry(labelframe_envios, width=10)
    cantidad_terminada.grid(row=11, column=0, columnspan=2, pady=2)

    tk.Button(labelframe_envios, text="Afiladores Terminados", bg="blue", fg="white", command=lambda: resibir_afiladores    (cantidad_terminada, historial)).grid(row=12, column=0, columnspan=2)
    
    return frame