import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from mycode.funciones.add_funcion import on_item_selected, limpiar_tabla, mostrar_categoria, agregar_piezas, mostrar_datos, ordenar_por, eliminar_piezas

def chapa(parent):

    frame = ttk.Frame(parent,)
    
    # Crear un Frame para la tabla de piezas
    box1 = ttk.Frame(frame,)
    box1.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box1, text="Tabla con piezas de Chapa", font=("Arial", 15, "bold"), 
    ).grid(row=0, column=0, sticky="w", pady=15)

    # Configurar la tabla de piezas
    mostrar_piezas = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza", command=lambda: ordenar_por(mostrar_piezas, "Pieza", False))
    mostrar_piezas.heading("Cantidad", text="Cant.", command=lambda: ordenar_por(mostrar_piezas, "Cantidad", False))
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=230)
    mostrar_piezas.column("Cantidad", width=110)
    mostrar_piezas.config(height=23)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")


    style_treeview = ttk.Style()
    style_treeview.configure("Treeview", font=("Arial", 10), rowheight=22, background= 'white',foreground="black",)
    style_treeview.configure("Treeview.Heading", font=("Arial", 18, "bold"))

    # Botón para limpiar la tabla
    ttk.Button(box1, text="Limpiar Tabla", command=lambda: limpiar_tabla(mostrar_piezas),bootstyle="secondary-outline").grid(row=2, columnspan=2, pady=10)

    # Crear un segundo Frame para la sección de acciones
    box2 = ttk.Frame(frame, width=300,)
    box2.grid(row=0, column=1, padx=30)

    ttk.Label(box2, text="Chapa", font=("Arial", 30, "bold", "underline"),).grid(row=0, column=0)
    ttk.Label(box2, text="Mostrar todas las piezas de Chapa y seleccionar una pieza de la tabla", font=("Arial", 12, "bold"), wraplength=300, ).grid(row=1, column=0)

    # Botón para mostrar las piezas
    ttk.Button(box2, padding=12, text="Mostrar Piezas", bootstyle="info", command=lambda: mostrar_categoria(mostrar_piezas, "Chapa", "piezas_brutas", detalles_piezas, pieza_seleccionada, imagen_piezas)).grid(row=2, column=0,padx=20, pady=5)

    ttk.Separator(box2, orient=tk.HORIZONTAL, bootstyle="info").grid(row=3, column=0, columnspan=3, sticky="EW", padx=2, pady=10)

    # Crear un Frame para las acciones relacionadas a las piezas seleccionadas
    box_acciones = ttk.Frame(box2,)
    box_acciones.grid(row=4, column=0, padx=7)

    ttk.Label(box_acciones, text="Seleccione una pieza de la tabla para ver sus características", font=("Arial", 12, "bold"),).grid(row=0, columnspan=2, sticky="nsew")

    ttk.Label(box_acciones, text="Pieza Seleccionada:", font=("Arial", 16, "bold"), ).grid(row=1, column=0)

    pieza_seleccionada = ttk.Label(box_acciones, text="...", font=("Arial", 20, "bold"), anchor=tk.CENTER, )
    pieza_seleccionada.grid(row=1, column=1, sticky="w")

    ttk.Label(box_acciones, text="Ingrese una Cantidad:", font=("Arial", 16, "bold"), ).grid(row=2, column=0)

    entry_cantidad_piezas = tk.Entry(box_acciones, font=("Arial", 20, "bold"), width=17)
    entry_cantidad_piezas.grid(row=2, column=1, sticky="w")

    box_btn = ttk.Frame(box_acciones,bootstyle="dark")
    box_btn.grid(row=3, columnspan=2)

    # Botón para agregar piezas
    btn_agregar = ttk.Button(box_btn, width=10, text="AGREGAR", bootstyle="success", command=lambda: agregar_piezas(pieza_seleccionada, entry_cantidad_piezas, mostrar_piezas, historial, "Chapa", "piezas_brutas"),padding=10)
    btn_agregar.grid(row=0, column=1, pady=10, padx=5)

    # Botón para eliminar piezas (sin funcionalidad implementada aún)
    btn_eliminar = ttk.Button(box_btn, width=10, text="ELIMINAR",bootstyle="danger", command=lambda: eliminar_piezas(pieza_seleccionada, entry_cantidad_piezas, mostrar_piezas, historial, "Chapa", "piezas_brutas"),padding=10)
    btn_eliminar.grid(row=0, column=0, pady=10, padx=5)

    ttk.Separator(box_acciones, orient=tk.HORIZONTAL,bootstyle="info").grid(row=4, column=0, columnspan=3, sticky="EW", padx=2, pady=7)

    # Frame para mostrar detalles de las piezas
    detalles = tk.Frame(box_acciones, highlightthickness=1, highlightbackground="#535c68", height=40)
    detalles.grid(row=5, columnspan=2, pady=10, sticky="nw")

    tk.Label(detalles, text="Detalles de las Piezas:", font=("Arial", 9, "bold", 'underline')).grid(row=0, column=0, sticky="nw")

    box_info = tk.Frame(detalles)
    box_info.grid(row=1, column=0)

    detalles_piezas = tk.Label(box_info, text="", width=25, wraplength=200, font=("Arial", 12, "bold"), height=7, justify="left", background="#192965" , foreground='white')
    detalles_piezas.grid(row=1, column=0, sticky="nw")

    # Frame para mostrar la imagen de la pieza
    img_pieza = tk.Frame(box_acciones, background="#192965")
    img_pieza.grid(row=5, column=1)

    imagen_piezas = tk.Label(img_pieza)
    imagen_piezas.grid(row=0, column=0)

    # Frame para el historial
    box_historial = tk.Frame(box_acciones, background="#192965" )
    box_historial.grid(row=6, columnspan=2)

    tk.Label(box_historial, text="Historial", background="#192965" , foreground='white').grid(row=0, column=0)

    historial = tk.Listbox(box_historial, width=80, height=6, font=("Arial", 10, "bold"))
    historial.grid(row=1, column=0)

    return frame
