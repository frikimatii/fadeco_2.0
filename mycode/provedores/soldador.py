import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk


from mycode.funciones.add_funcion import ordenar_por, limpiar_tabla
from mycode.funciones.provedores_funcion import limpiar_tabla,  enviar_a_soldar, resibir_bases, mostrar_por_modelo, armar_cabezales, mostrar_piezas_tablas


bases = ["BaseInox_330","BaseInox_300","BaseInox_250","BaseECO","BasePintada_330","BasePintada_300"]


query_mostrar_piezas_soldador = """
SELECT PIEZAS, CANTIDAD 
FROM piezas_brutas 
WHERE ORIGEN = 'corte' AND PROSESO = 'soldado'
AND LOWER(TRIM(PIEZAS)) NOT IN ('planchuela_inferior', 'planchuela_interna')

UNION ALL

SELECT PIEZAS, CANTIDAD 
FROM piezas_terminadas 
WHERE PROVEDOR = 'soldador' ;
"""
query_mostras_bases_ensoldador = "SELECT PIEZAS, CANTIDAD FROM provedores WHERE PROVEDOR = 'soldador' AND PIEZAS NOT IN ('cabezal_Inox', 'cabezal_pintado', 'cabezal_250');"

query_cabezales_inox = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MODELO = 'inox' AND SECTOR = 'cabezal'"
query_cabezales_pintada = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MODELO = 'pintada' AND SECTOR = 'cabezal'"
query_cabezales_250 = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE MODELO = '250' AND SECTOR = 'cabezal' "

varilla = ["varilla_330", "varilla_300", "varilla_250"]

def on_item_selected(event, treeview, label, detalles):
    selected_item = treeview.selection()
    if selected_item:
        item_text = treeview.item(selected_item[0], "values")[0]
        label.config(text=item_text)    
    else:
        label.config(text="...")
        detalles.config(text="...")

def mostrar_categoria(tabla, detalles, pieza, imagen_label, query):
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    cursor.execute(query)
    datos = cursor.fetchall()
    conn.close()

    # Limpiar la tabla antes de insertar nuevos datos
    for row in tabla.get_children():
        tabla.delete(row)

    # Insertar datos en la tabla
    for dato in datos:
        tabla.insert("", tk.END, values=dato[:2])  # Solo insertar PIEZAS y CANTIDAD

    def on_item_selected(event):
        selected_item = tabla.selection()
        if selected_item:
            pieza_nombre = tabla.item(selected_item[0], "values")[0]

            with sqlite3.connect("dbfadeco.db") as conn:
                cursor = conn.cursor()

                if pieza_nombre in varilla:
                    cursor.execute("SELECT DETALLES, IMAGEN, CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_nombre,))
                    pieza_detalle = cursor.fetchone()
                else:
                    # Buscar primero en piezas_brutas
                    cursor.execute("SELECT DETALLES, IMAGEN, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (pieza_nombre,))
                    pieza_detalle = cursor.fetchone()

                # Si no se encuentran detalles en piezas_brutas, buscar en piezas_terminada

            # Mostrar el nombre, detalle e imagen en los widgets correspondientes
            pieza.config(text=pieza_nombre)
            if pieza_detalle:
                detalles.config(text=f"{pieza_detalle[0]}")

                # Mostrar imagen si está disponible
                imagen_ruta = pieza_detalle[1]
                if imagen_ruta:
                    imagen = tk.PhotoImage(file=imagen_ruta)
                    imagen_label.config(image=imagen)
                    imagen_label.image = imagen  # Necesario para mantener la referencia de la imagen
                else:
                    imagen_label.config(image="")
                    imagen_label.image = None
            else:
                detalles.config(text="No se encontraron detalles para la pieza seleccionada.")
                imagen_label.config(image="")
                imagen_label.image = None

    tabla.bind("<<TreeviewSelect>>", on_item_selected)


def ventana_soldador(parent):
    frame = ttk.Frame(parent)
    
    stylo_ventana = ttk.Style()
    stylo_ventana.configure('Pestania.TNotebook', background= '#192965')

    box1 = ttk.Frame(frame)
    box1.grid(row=0, column=0, sticky="nsew")


    ttk.Label(box1, text="Tabla con piezas para el Soldador", font=("Arial", 15, "bold")).grid(row=0, column=0, sticky="w", pady=15)


    mostrar_piezas = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza", command= lambda: ordenar_por(mostrar_piezas, "Pieza", False))
    mostrar_piezas.heading("Cantidad", text="Cant.", command= lambda: ordenar_por(mostrar_piezas, "Cantidad", False))
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=270)
    mostrar_piezas.column("Cantidad", width=60)
    mostrar_piezas.config(height=20)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")

    ttk.Button(box1, text="Limpiar Tabla", command= lambda: limpiar_tabla(mostrar_piezas)).grid(row=2, columnspan=2, pady=5)


    tk.Label(box1, text="Historial" ,font=("Arial", 9, "bold")).grid(row=3, column=0, sticky="sw")
    historial = tk.Listbox(box1, width=60, height=5, font=("Arial", 10, "bold"))
    historial.grid(row=4,column=0)




    box2 = tk.Frame(frame)
    box2.grid(row=0, column=1)
    
    soldador = tk.Frame(box2)
    soldador.grid(row=0, column=0, padx=10 , pady=10)
    
    # Sección de Stock
    stock_frame = ttk.LabelFrame(soldador, text="Stock Soldador", padding=7, relief="groove", style="Bold9.TLabelframe")
    stock_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    
    ttk.Button(stock_frame, text="Stock en fábrica", command=lambda: mostrar_categoria(mostrar_piezas, info_pieza, piezas , imagen_piezas, query_mostrar_piezas_soldador), bootstyle="primary-outline", padding=10).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(stock_frame, text="Stock en Soldador", command=lambda: mostrar_categoria(mostrar_piezas, info_pieza, piezas, imagen_piezas, query_mostras_bases_ensoldador), bootstyle="primary-outline", padding=10).grid(row=1, column=1, padx=5, pady=5)
    
    # Sección de Envíos y Recepciones
    envios_frame = ttk.LabelFrame(soldador, text="Envíos y Recepciones", padding=10, relief="groove", style="Bold9.TLabelframe")
    envios_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    
    tk.Label(envios_frame, text="Enviar a Soldar:").grid(row=1, column=0, pady=5, sticky="e")
    base_seleccionada_entrega = ttk.Combobox(envios_frame, values=bases, state="readonly", width=15, font= ("Arial", 12, "bold"))
    base_seleccionada_entrega.grid(row=1, column=1, pady=5, sticky="w")
    tk.Label(envios_frame, text="Cantidad:").grid(row=2, column=0, pady=5, sticky="e")
    cantidad_de_bases_entregada = tk.Entry(envios_frame)
    cantidad_de_bases_entregada.grid(row=2, column=1, pady=5, sticky="w")
    ttk.Button(envios_frame, text="Enviar",bootstyle="warning", padding=7,command=lambda: enviar_a_soldar(base_seleccionada_entrega,   cantidad_de_bases_entregada, historial)).grid(row=3, column=0, columnspan=2, pady=10)
    
    tk.Label(envios_frame, text="Recibir de Soldador:").grid(row=4, column=0, pady=5, sticky="e")
    base_seleccionada_resivida = ttk.Combobox(envios_frame, values=bases, state="readonly", width=15, font= ("Arial", 12, "bold"))
    base_seleccionada_resivida.grid(row=4, column=1, pady=5, sticky="w")
    tk.Label(envios_frame, text="Cantidad:").grid(row=5, column=0, pady=5, sticky="e")
    cantidad_de_bases_resividas = tk.Entry(envios_frame)
    cantidad_de_bases_resividas.grid(row=5, column=1, pady=5, sticky="w")
    ttk.Button(envios_frame, text="Recibir",bootstyle="success",padding=7, command=lambda: resibir_bases(base_seleccionada_resivida,cantidad_de_bases_resividas,historial)).grid(row=6, column=0, columnspan=2, pady=10)
    
    # Sección de Acciones del Soldador
    acciones_frame = ttk.LabelFrame(soldador, text="Piezas para el Soldador", padding=10, relief="groove", style="Bold9.TLabelframe")
    acciones_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    ttk.Button(acciones_frame, bootstyle="warning-outline",padding=10,text="inox 330", command=lambda: mostrar_por_modelo("inox_330", mostrar_piezas)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Button(acciones_frame, bootstyle="warning-outline",padding=10,text="inox 300", command=lambda: mostrar_por_modelo("inox_300", mostrar_piezas)).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    ttk.Button(acciones_frame, bootstyle="warning-outline",padding=10,text="inox 250", command=lambda: mostrar_por_modelo("inox_250", mostrar_piezas)).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    ttk.Button(acciones_frame, bootstyle="warning-outline",padding=10,text="Pintada 330", command=lambda: mostrar_por_modelo("pintada_330", mostrar_piezas)).grid  (row=2, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Button(acciones_frame, bootstyle="warning-outline",padding=10,text="Pintada 300", command=lambda: mostrar_por_modelo("pintada_300", mostrar_piezas)).grid  (row=2, column=1, padx=5, pady=5, sticky="nsew")
    ttk.Button(acciones_frame, bootstyle="warning-outline",padding=10,text="ECO", command=lambda: mostrar_por_modelo("ECO", mostrar_piezas)).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
    

    box3 = tk.Frame(frame)
    box3.grid(row=0, column=2)


    cabezales_terminados = ttk.Frame(box3, padding=5)
    cabezales_terminados.grid(row=1, column=0, pady=5)
    
    # Título con estilo

    ttk.Label(cabezales_terminados, text="Cabezales", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
    
    # Sección de stock de cabezales con bordes
    stock_cabezal = ttk.LabelFrame(cabezales_terminados, text="Piezas De Cabezales", padding=5, relief="solid",  style="Bold9.TLabelframe")
    stock_cabezal.grid(row=1, column=0, columnspan=3, pady=5)
    
    btn_agregar_cabezal_inox = ttk.Button(stock_cabezal, text="INOX", bootstyle="info-outline", padding=10,command=lambda: mostrar_piezas_tablas(mostrar_piezas, query_cabezales_inox))
    btn_agregar_cabezal_inox.grid(row=1, column=0, padx=5, pady=5)
    
    btn_agregar_cabezal_pintada = ttk.Button(stock_cabezal, text="Chapa Negra", bootstyle="info-outline", padding=10,command=lambda: mostrar_piezas_tablas(mostrar_piezas, query_cabezales_pintada))
    btn_agregar_cabezal_pintada.grid(row=1, column=1, padx=5, pady=5)
    
    btn_agregar_cabezal_250 = ttk.Button(stock_cabezal, text="250", bootstyle="info-outline", padding=10,command=lambda: mostrar_piezas_tablas(mostrar_piezas, query_cabezales_250))
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
    
        agregar_btn = ttk.Button(botones, text="Agregar", bootstyle="success", command=comando)
        agregar_btn.grid(row=2, column=i, padx=10, pady=5)
    
        # Asignando las entradas a variables
        if i == 0:
            entrada_cantida_inox = entrada
        elif i == 1:
            entrada_cantidad_pintada = entrada
        elif i == 2:
            entrada_cantidad_250 = entrada
    
    
    box_info = tk.Frame(box3)
    box_info.grid(row=2, column=0)

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