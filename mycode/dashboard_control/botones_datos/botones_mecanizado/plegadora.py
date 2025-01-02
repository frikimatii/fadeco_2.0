from tkinter import ttk
import ttkbootstrap as ttk
import sqlite3


def ejecutar_consulta(query):
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        return datos
    except sqlite3.Error as e:
        print(f"Error al ejecutar consulta: {e}")
        return []


def cargar_datos(tree, query):
    datos = ejecutar_consulta(query)
    for item in tree.get_children():
        tree.delete(item)
    for fila in datos:
        tree.insert("", "end", values=fila)

def piezas_por_doblar_frame(parent):
    frame = ttk.Frame(parent)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    ttk.Label(frame, text="PIEZAS PARA DOBLAR ").grid(row=0, column=0, sticky="w")

    tree = ttk.Treeview(frame, columns=("pieza", "cantidad", "detalles"), show="headings")
    tree.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    
    tree.heading("pieza", text="Pieza")
    tree.column("pieza", width=150, anchor="center")
    
    tree.heading("cantidad", text="Cantidad")
    tree.column("cantidad", width=70, anchor="center")
    
    tree.heading("detalles", text="Detalles")
    tree.column("detalles", width=200, anchor="w")
    
    tree.config(height=16)
    
    query = "SELECT PIEZAS, CANTIDAD, DETALLES FROM piezas_brutas WHERE MECANIZADO = 'plegadora'"
    cargar_datos(tree, query)

    detalles_frame = ttk.Frame(frame, padding=10 )
    detalles_frame.grid(row=1, column=1)
    
    
    box_frame = ttk.LabelFrame(detalles_frame, text="Detalles", padding=10)
    box_frame.grid(row=0, column=0)
    
    ttk.Label(box_frame, text="Piezas").grid(row=0, column=0, sticky="w")
    piezas_label = ttk.Label(box_frame, text="")
    piezas_label.grid(row=0, column=1)
    
    ttk.Label(box_frame, text="Cantidad").grid(row=1, column=0, sticky="w")
    cantidad_entry = ttk.Entry(box_frame)
    cantidad_entry.grid(row=1, column=1)
    
    ttk.Label(box_frame, text="Detalles").grid(row=2, column=0)
    detalles_label = ttk.Label(box_frame, text="", wraplength=200)
    detalles_label.grid(row=2, column=1)
    
    
    estado_label = ttk.Label(box_frame, text="")
    estado_label.grid(row=4, column=0, columnspan=2)
    
    def actualizar_dato(texto):
        estado_label.config(text=texto)
    
    def seleccionar_fila(event):
        selected_item = tree.selection()
        if selected_item:
            dato_fila = tree.item(selected_item[0], 'values')
            pieza = dato_fila[0]
            cantidad = dato_fila[1]
            detalles = dato_fila[2]
            
            piezas_label.config(text=pieza)
            cantidad_entry.delete(0, 'end')
            cantidad_entry.insert(0, cantidad)
            detalles_label.config(text=detalles)

    # Bind the Treeview select event to the function
    tree.bind("<<TreeviewSelect>>", seleccionar_fila)
    
    def modificar_pieza():
        pieza = piezas_label.cget("text")
        cantidad = cantidad_entry.get()
        detalles = detalles_label.cget("text")
        
        if pieza and cantidad and detalles:
            try:
                conn = sqlite3.connect("dbfadeco.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? , DETALLES = ? WHERE PIEZAS = ?", (cantidad, detalles, pieza))
                conn.commit()
                conn.close()
                actualizar_dato(f"Pieza '{pieza}' Modificada Correctamente ")
                cargar_datos(tree, query)
            except sqlite3.Error as e:
                print(f"Error al Modificar Pieza: {e}")
                actualizar_dato(f"Error al Modificar la Pieza '{pieza}'")
        else:
            actualizar_dato("Por Favor Complete Los Campos")

    ttk.Button(box_frame, text="Modificar", command=modificar_pieza).grid(row=3, columnspan=2, pady=5)
    
    
    return frame



def piezas_dobladas_frame(parent):
    frame = ttk.Frame(parent)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    ttk.Label(frame, text="PIEZAS DOBLADAS ").grid(row=0, column=0, sticky="w")
    
    tree = ttk.Treeview(frame, columns=("pieza", "cantidad", "detalles"), show="headings")
    tree.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    
    tree.heading("pieza", text="Pieza")
    tree.column("pieza", width=150, anchor="center")
    
    tree.heading("cantidad", text="Cantidad")
    tree.column("cantidad", width=70, anchor="center")
    
    tree.heading("detalles", text="Detalles")
    tree.column("detalles", width=200, anchor="w")

    tree.config(height=16)
    
    query = """SELECT PIEZAS, CANTIDAD, DETALLES, 'plegado' as origen FROM piezas_brutas WHERE MECANIZADO = 'plegadora'
           UNION
           SELECT PIEZAS, CANTIDAD, DETALLES, 'plasma' as origen FROM plasma WHERE ORIGEN = 'plegado'
           UNION
           SELECT PIEZAS, CANTIDAD, DETALLES, 'terminadas' as origen FROM piezas_terminadas WHERE ORIGEN = 'plegado'
           UNION
           SELECT PIEZAS, CANTIDAD, DETALLES, 'plegado' as origen FROM piezas_brutas WHERE TIPO_DE_MATERIAL = 'Chapa_' AND ORIGEN = 'plegado'"""

    cargar_datos(tree, query)

    detalles_frame = ttk.Frame(frame, padding=10)
    detalles_frame.grid(row=1, column=1)
    
    box_frame = ttk.LabelFrame(detalles_frame, text="Detalles", padding=10)
    box_frame.grid(row=0, column=0)
    
    ttk.Label(box_frame, text="Piezas").grid(row=0, column=0, sticky="w")
    piezas_label = ttk.Label(box_frame, text="")
    piezas_label.grid(row=0, column=1)
    
    ttk.Label(box_frame, text="Cantidad").grid(row=1, column=0 , sticky="w")
    cantidad_entry = ttk.Entry(box_frame)
    cantidad_entry.grid(row=1, column=1)
    
    ttk.Label(box_frame, text="Detalles").grid(row=2, column=0)
    detalles_label = ttk.Label(box_frame, text="", wraplength=200)
    detalles_label.grid(row=2, column=1)
    
    
    estado_label = ttk.Label(box_frame, text="")
    estado_label.grid(row=4, column=0, columnspan=2)

    def actualizar_dato(texto):
        estado_label.config(text=texto)
        
    def seleccionar_fila(event):
        selected_item = tree.selection()
        if selected_item:
            dato_fila = tree.item(selected_item[0], 'values')
            pieza = dato_fila[0]
            cantidad = dato_fila[1]
            detalles = dato_fila[2]
            
            piezas_label.config(text=pieza)
            cantidad_entry.delete(0, 'end')
            cantidad_entry.insert(0, cantidad)
            detalles_label.config(text=detalles)
            
    tree.bind("<<TreeviewSelect>>", seleccionar_fila)
    
    def modificar_pieza():
        pieza = piezas_label.cget("text")
        cantidad = cantidad_entry.get()
        detalles = detalles_label.cget("text")

        # Obtener la tabla de la pieza seleccionada
        selected_item = tree.selection()
        if selected_item:
            dato_fila = tree.item(selected_item[0], 'values')
            pieza = dato_fila[0]
            cantidad = dato_fila[1]
            detalles = dato_fila[2]

            # Determinar de qué tabla proviene la pieza
            origen = dato_fila[3]  # Si tienes una columna adicional 'origen' que indique de qué    tabla proviene la pieza.

            if pieza and cantidad and detalles:
                try:
                    conn = sqlite3.connect("dbfadeco.db")
                    cursor = conn.cursor()

                    # Modificar solo la tabla correspondiente
                    if origen == 'plegado':
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ?, DETALLES = ? WHERE   PIEZAS = ?", (cantidad, detalles, pieza))
                    elif origen == 'plasma':
                        cursor.execute("UPDATE plasma SET CANTIDAD = ?, DETALLES = ? WHERE PIEZAS   = ?", (cantidad, detalles, pieza))
                    elif origen == 'terminadas':
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = ?, DETALLES = ?     WHERE PIEZAS = ?", (cantidad, detalles, pieza))

                    conn.commit()
                    conn.close()
                    actualizar_dato(f"Pieza '{pieza}' Modificada Correctamente")
                    cargar_datos(tree, query)  # Volver a cargar los datos de la tabla actualizada
                except sqlite3.Error as e:
                    print(f"Error al Modificar Pieza: {e}")
                    actualizar_dato(f"Error al Modificar la Pieza '{pieza}'")
            else:
                actualizar_dato("Por Favor Complete Los Campos")

    ttk.Button(box_frame, text="Modificar", command=modificar_pieza).grid(row=3, columnspan=2, pady=5)


    return frame
    
def modificar_plegadora(parent):
    # Frame contenedor principal
    main_frame = ttk.Frame(parent)
    main_frame.grid(row=0, column=0, sticky="nsew")
    
    # Frame para botones de navegación
    botones_frame = ttk.Frame(main_frame)
    botones_frame.grid(row=0, column=0, padx=10, pady=10)

    # Variables globales para los frames de las tablas
    piezas_por_doblar_frame_obj = None
    piezas_dobladas_frame_obj = None

    # Función para mostrar "Piezas por Doblar"
    def mostrar_piezas_por_doblar():
        nonlocal piezas_por_doblar_frame_obj, piezas_dobladas_frame_obj
        # Si existe un frame de piezas dobladas, lo eliminamos
        if piezas_dobladas_frame_obj:
            piezas_dobladas_frame_obj.grid_forget()

        # Si no existe, lo creamos
        if not piezas_por_doblar_frame_obj:
            piezas_por_doblar_frame_obj = piezas_por_doblar_frame(main_frame)
        
        piezas_por_doblar_frame_obj.grid(row=1, column=0, sticky="nsew")

    # Función para mostrar "Piezas Dobladas"
    def mostrar_piezas_dobladas():
        nonlocal piezas_por_doblar_frame_obj, piezas_dobladas_frame_obj
        # Si existe un frame de piezas por doblar, lo eliminamos
        if piezas_por_doblar_frame_obj:
            piezas_por_doblar_frame_obj.grid_forget()

        # Si no existe, lo creamos
        if not piezas_dobladas_frame_obj:
            piezas_dobladas_frame_obj = piezas_dobladas_frame(main_frame)
        
        piezas_dobladas_frame_obj.grid(row=1, column=0, sticky="nsew")

    # Botones para navegar entre las secciones
    ttk.Button(botones_frame, text="Piezas por Doblar", command=mostrar_piezas_por_doblar).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(botones_frame, text="Piezas Dobladas", command=mostrar_piezas_dobladas).grid(row=0, column=1, padx=5, pady=5)

    return main_frame

    