import tkinter as tk
from tkinter import ttk
from mycode.funciones.add_funcion import ordenar_por, limpiar_tabla
from mycode.funciones.provedores_funcion import mandar_piezas_a, resicbir_piezas_de
import sqlite3

lista_piezas_maxi = ["brazo_augeriado_250", "brazo_augeriado_300", "brazo_augeriado_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO","tapa_afilador_eco"
]

lista_piezas_maxi_para_fabrica = ["brazo_250", "brazo_300", "brazo_330","cajas_torneadas_250","cajas_torneadas_300","cajas_torneadas_330","cubrecuchilla_250","cubre_300_torneado","cubrecuchilla_330","velero","vela_final_330","vela_final_250","vela_final_300","planchada_final_330","planchada_final_300","planchada_final_250","tapa_afilador","aro_numerador","tapa_afilador_250","teletubi_330","teletubi_300_torneado","teletubi_250","BaseInox_330","BaseInox_300","BaseInox_250","BaseECO", "tapa_afilador_eco"
]

query_maxi = "SELECT PIEZAS ,CANTIDAD FROM pulidor_maxi"

query_stock_fabrica_pulido = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pulidor' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'pulido' "

query_carmelo ="SELECT PIEZAS ,CANTIDAD FROM pulidor_maxi"

query_stock_fabrica_pulido = "SELECT PIEZAS ,CANTIDAD FROM piezas_brutas WHERE PROSESO = 'pulidor' UNION SELECT PIEZAS, CANTIDAD FROM PIEZAS_RETOCADA WHERE MECANIZADO = 'pulido' "

def mostrar_categoria(tabla, detalles, pieza, imagen_label, query, pulidor ):
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

    def obtener_detalle_pieza(pieza_nombre):
        with sqlite3.connect("dbfadeco.db") as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT DETALLES, IMAGEN, CANTIDAD FROM {pulidor} WHERE PIEZAS = ?", (pieza_nombre,))
            pieza_detalle = cursor.fetchone()
        return pieza_detalle

    def on_item_selected(event):
        selected_item = tabla.selection()
        if selected_item:
            pieza_nombre = tabla.item(selected_item[0], "values")[0]
            pieza_detalle = obtener_detalle_pieza(pieza_nombre)

            # Mostrar el nombre, detalle e imagen en los widgets correspondientes
            pieza.config(text=pieza_nombre)
            if pieza_detalle:
                detalles.config(text=f"{pieza_detalle[0]}")

                # Mostrar imagen si está disponible
                imagen_ruta = pieza_detalle[1]
                if imagen_ruta:
                    try:
                        imagen = tk.PhotoImage(file=imagen_ruta)
                        imagen_label.config(image=imagen)
                        imagen_label.image = imagen  # Necesario para mantener la referencia de la imagen
                    except Exception as e:
                        print(f"Error al cargar la imagen: {e}")
                        imagen_label.config(image="")
                        imagen_label.image = None
                else:
                    imagen_label.config(image="")
                    imagen_label.image = None
            else:
                detalles.config(text="No se encontraron detalles para la pieza seleccionada.")
                imagen_label.config(image="")
                imagen_label.image = None

    tabla.bind("<<TreeviewSelect>>", on_item_selected)


def ventana_maxi(parent):
    
    stylo_ventana = ttk.Style()
    stylo_ventana.configure('Pestania.TNotebook', background= '#192965')
    frame = ttk.Frame(parent, style='Pestania.TFrame')

    box1 = ttk.Frame(frame, style='Pestania.TFrame')
    box1.grid(row=0, column=0, sticky="nsew")

    ttk.Label(box1, text="Tabla P/ De Maxi", font=("Arial", 25, "bold"), background= '#192965', foreground='white').grid(row=0, column=0, sticky="w", pady=15)


    mostrar_piezas = ttk.Treeview(box1, columns=("Pieza", "Cantidad"))
    mostrar_piezas.heading("Pieza", text="Pieza", command= lambda: ordenar_por(mostrar_piezas, "Pieza", False))
    mostrar_piezas.heading("Cantidad", text="Cantidad", command= lambda: ordenar_por(mostrar_piezas, "Cantidad", False))
    mostrar_piezas.column("#0", width=0, stretch=tk.NO)
    mostrar_piezas.column("Pieza", width=150)
    mostrar_piezas.column("Cantidad", width=60)
    mostrar_piezas.config(height=20)
    mostrar_piezas.grid(row=1, column=0, sticky="nsew")

    ttk.Button(box1, text="Limpiar Tabla", command= lambda: limpiar_tabla(mostrar_piezas)).grid(row=2, columnspan=2 )

    tk.Label(box1, text="Historial" ,font=("Arial", 9, "bold")).grid(row=3, column=0, sticky="sw")
    historial = tk.Listbox(box1, width=60, height=5, font=("Arial", 10, "bold"))
    historial.grid(row=4,column=0)


    box2 = tk.Frame(frame, background= '#192965')
    box2.grid(row=0, column=1, padx=30)
    # Crear un Labelframe para Maxi
    maxi_frame = ttk.Labelframe(box2, text="Maxi", padding="7", style="Bold9.TLabelframe")
    maxi_frame.grid(row=0, column=0, padx=20, pady=20)

    # Envíos para Maxi
    tk.Label(maxi_frame, text="Envios", font=("Arial", 9,"bold" ,"underline")).grid(row=0, column=0, columnspan=2, sticky="w")
    tk.Label(maxi_frame, text="Seleccione la pieza").grid(row=1, column=0, sticky="w")
    piezas_seleccionada_m = ttk.Combobox(maxi_frame, values=lista_piezas_maxi, state="readonly", width=20, font= ("Arial", 12, "bold"))
    piezas_seleccionada_m.grid(row=1, column=1, padx=5)
    tk.Label(maxi_frame, text="Cantidad").grid(row=2, column=0, sticky="w")
    cantida_de_piezas_m = tk.Entry(maxi_frame)
    cantida_de_piezas_m.grid(row=2, column=1, padx=5)
    tk.Button(maxi_frame, text="Enviar",bg="blue",fg="white", command=lambda: mandar_piezas_a("pulidor_maxi", cantida_de_piezas_m, piezas_seleccionada_m, mostrar_piezas, historial)).grid(row=3, column=0, columnspan=2, pady=5)

    # Entrega para Maxi
    tk.Label(maxi_frame, text="ENTREGA", font=("Arial", 9,"bold" ,"underline")).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))
    tk.Label(maxi_frame, text="Seleccione la pieza").grid(row=5, column=0, sticky="w")
    piezas_resibida_m = ttk.Combobox(maxi_frame,  values=lista_piezas_maxi_para_fabrica, state="readonly", width=20, font= ("Arial", 12, "bold"))
    piezas_resibida_m.grid(row=5, column=1, padx=5)
    tk.Label(maxi_frame, text="Cantidad").grid(row=6, column=0, sticky="w")
    cantida_de_resibida_m = tk.Entry(maxi_frame)
    cantida_de_resibida_m.grid(row=6, column=1, padx=5)
    tk.Button(maxi_frame, text="Recibir",bg="green",fg="white", command=lambda: resicbir_piezas_de("pulidor_maxi", cantida_de_resibida_m, piezas_resibida_m, mostrar_piezas, historial)).grid(row=7, column=0, columnspan=2, pady=5)

    # Stock para Maxi
    tk.Label(maxi_frame, text="Stock Maxi", font=("Arial", 8,"bold" ,"underline")).grid(row=8, column=0, pady=(10, 0))
    tk.Button(maxi_frame, text="EN MAXI", command=lambda: mostrar_categoria(mostrar_piezas, info_pieza, piezas, imagen_piezas, query_maxi, "pulidor_maxi")).grid(row=9, column=0, pady=5)
    tk.Label(maxi_frame, text="Stock en Fabrica bruto", font=("Arial", 8,"bold" ,"underline")).grid(row=8, column=1, pady=(10, 0))
    tk.Button(maxi_frame, text="BRUTO FABRICA", command=lambda: mostrar_categoria(mostrar_piezas, info_pieza, piezas , imagen_piezas, query_stock_fabrica_pulido, "piezas_brutas")).grid(row=9, column=1)
    


    return frame