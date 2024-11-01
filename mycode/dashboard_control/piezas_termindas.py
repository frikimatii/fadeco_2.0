import tkinter as tk
from tkinter import ttk
import sqlite3
from mycode.funciones.add_funcion import ordenar_por

# Diccionario de consultas a la base de datos
consultas = {
    "todas": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas",
    "armado_final": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas WHERE SECTOR = 'armado_final'",
    "prearmado": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas WHERE SECTOR = 'Pre_armado'",
    "caja_armada": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas WHERE SECTOR = 'armado_caja'",
    "base": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas WHERE MODELO = 'base'",
    "pieza_afilador": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas WHERE SECTOR = 'pieza_afilador'",
    "embalar": "SELECT PIEZAS, CANTIDAD, STOCK_DESEADO, DETALLES FROM piezas_terminadas WHERE SECTOR = 'embalar'"
}

# Conexión a la base de datos
def conectar_db():
    try:
        return sqlite3.connect("dbfadeco.db")
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Funciones auxiliares
def limpiar_tabla(treeview):
    """Limpia todos los datos del Treeview."""
    for item in treeview.get_children():
        treeview.delete(item)

def mostrar_datos(tabla, query):
    """Muestra los datos en el Treeview según la consulta proporcionada."""
    conn = conectar_db()
    if conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute(query)
            datos = cursor.fetchall()
        
        limpiar_tabla(tabla)
        for dato in datos:
            pieza, cantidad, stock_deseado, detalles = dato
            item = tabla.insert("", tk.END, values=(pieza, cantidad, stock_deseado))
            
            # Aplicar color de fondo según el estado de stock
            if cantidad > stock_deseado:
                tabla.item(item, tags=("verde",))
            elif cantidad < stock_deseado:
                tabla.item(item, tags=("rojo",))
            else:  # cantidad == stock_deseado
                tabla.item(item, tags=("amarillo",))

# Funciones de evento
def seleccionar_pieza(event):
    """Actualiza los detalles de la pieza seleccionada en el Treeview."""
    seleccion = treeview.selection()
    if seleccion:
        item = seleccion[0]
        values = treeview.item(item, 'values')
        if values:
            pieza_nombre.set(values[0])
            cantidad_actual.set(values[1])
            stock_actual.set(values[2])
            
            # Obtener detalles desde la base de datos
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT DETALLES FROM piezas_terminadas WHERE PIEZAS = ?", (values[0],))
                detalles = cursor.fetchone()
                conn.close()

                # Actualizar detalles en la interfaz
                detalles_text.set(detalles[0] if detalles else "Sin detalles disponibles.")

def actualizar_stock():
    """Actualiza el STOCK_DESEADO de la pieza seleccionada y muestra solo esa pieza."""
    seleccion = treeview.selection()
    if seleccion:
        item = seleccion[0]
        pieza = treeview.item(item, 'values')[0]
        nuevo_stock = stock_entry.get()
        
        # Validación de entrada
        if not nuevo_stock.isdigit():
            print("Por favor, introduce un número válido para el stock.")
            return
        
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE piezas_terminadas SET STOCK_DESEADO = ? WHERE PIEZAS = ?", (nuevo_stock, pieza))
            conn.commit()
            
            # Mostrar solo la pieza actualizada
            cursor.execute("SELECT PIEZAS, CANTIDAD, STOCK_DESEADO FROM piezas_terminadas WHERE PIEZAS = ?", (pieza,))
            pieza_actualizada = cursor.fetchall()
            conn.close()

            # Limpiar Treeview y mostrar pieza actualizada
            limpiar_tabla(treeview)
            for dato in pieza_actualizada:
                pieza, cantidad, stock_deseado = dato
                item = treeview.insert("", tk.END, values=dato)
                
                # Aplicar color según la comparación
                if cantidad > stock_deseado:
                    treeview.item(item, tags=("verde",))
                elif cantidad < stock_deseado:
                    treeview.item(item, tags=("rojo",))
                else:  # cantidad == stock_deseado
                    treeview.item(item, tags=("amarillo",))

            # Actualizar detalles de la pieza seleccionada
            seleccionar_pieza(None)
            
        except sqlite3.Error as e:
            print(f"Error al actualizar el stock: {e}")


# Función para ordenar el Treeview por columnas
def ordenar_por(columna):
    """Ordena el Treeview por la columna seleccionada."""
    # Obtener los datos existentes en el Treeview
    datos = [(treeview.set(item, columna), item) for item in treeview.get_children('')]
    
    # Identificar si la columna es numérica
    if columna in ["Cantidad", "Stock Deseado"]:
        datos.sort(key=lambda x: int(x[0]), reverse=True)  # Convertir a int para comparar
    else:
        datos.sort(key=lambda x: x[0])  # Ordenar como texto
    
    # Reorganizar los elementos en el Treeview según el orden
    for index, (valor, item) in enumerate(datos):
        treeview.move(item, '', index)  # Mover el item a la nueva posición




# Ventana principal
def ventana_piezas_terminadas(parent):
    """Crea la ventana para mostrar las piezas terminadas."""
    frame = ttk.Frame(parent)
    
    # Encabezado
    header_frame = ttk.Frame(frame)
    header_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=(10, 20), columnspan=2)
    ttk.Label(header_frame, text="DashBoard - Piezas Terminadas", font=("Arial", 18, "bold")).grid(row=0, column=0, sticky="w")

    # Treeview para mostrar piezas
    global treeview
    columns = ("Nombre", "Cantidad", "Stock Deseado")
    treeview = ttk.Treeview(frame, columns=columns, show="headings", height=19)

    # Configuración de cada columna
    col_configs = {
        "Nombre": {"width": 280},
        "Cantidad": {"width": 70, "anchor": "center"},
        "Stock Deseado": {"width": 80, "anchor": "center"},
    }
    # Configuración del Treeview
    for col in columns:
        treeview.heading(col, text=col, anchor="center", command=lambda c=col: ordenar_por(c))
        treeview.column(col, **col_configs[col])

    treeview.grid(row=1, column=0, sticky="n", padx=20, pady=(0, 10), columnspan=2)

    # Configuración de colores en las filas
    treeview.tag_configure("verde", background="lightgreen")
    treeview.tag_configure("rojo", background="lightcoral")
    treeview.tag_configure("amarillo", background="#fffce1")

    # Cargar datos iniciales
    mostrar_datos(treeview, consultas["todas"])
    treeview.bind('<<TreeviewSelect>>', seleccionar_pieza)

    # Sección de botones para filtrar en LabelFrame
    filtro_frame = ttk.LabelFrame(frame, text="Filtrar Piezas", padding=(10, 10))
    filtro_frame.grid(row=2, column=0, pady=(10, 50), sticky="ew", padx=20, columnspan=2)
    filtro_frame.columnconfigure((0, 1, 2), weight=1)

    # Botones para acciones de filtro
    ttk.Button(filtro_frame, text="Armado Final", command=lambda: mostrar_datos(treeview, consultas["armado_final"]), bootstyle="light").grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(filtro_frame, text="Pre-armado", command=lambda: mostrar_datos(treeview, consultas["prearmado"])).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(filtro_frame, text="Motor", command=lambda: mostrar_datos(treeview, consultas["caja_armada"])).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(filtro_frame, text="Calcomanía", command=lambda: mostrar_datos(treeview, consultas["embalar"])).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(filtro_frame, text="Bases", command=lambda: mostrar_datos(treeview, consultas["base"])).grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(filtro_frame, text="Afilador", command=lambda: mostrar_datos(treeview, consultas["pieza_afilador"])).grid(row=1, column=2, padx=5, pady=5)

    # Sección de detalles de la pieza seleccionada
    detalles_frame = ttk.LabelFrame(frame, text="Detalles de la Pieza", padding=(10, 10))
    detalles_frame.grid(row=1, column=2, padx=20, pady=(30, 50))

    global pieza_nombre, cantidad_actual, stock_actual, detalles_text
    pieza_nombre = tk.StringVar()
    cantidad_actual = tk.StringVar()
    stock_actual = tk.StringVar()
    detalles_text = tk.StringVar()  # Para mostrar detalles de la pieza

    ttk.Label(detalles_frame, text="Nombre de Pieza:", font=("Arial", 18, "bold")).grid(row=0, column=0, sticky="w")
    ttk.Label(detalles_frame, textvariable=pieza_nombre, font=("Arial", 16)).grid(row=0, column=1, sticky="w")
    ttk.Label(detalles_frame, text="Cantidad Actual:", font=("Arial", 18, "bold")).grid(row=1, column=0, sticky="w")
    ttk.Label(detalles_frame, textvariable=cantidad_actual, font=("Arial", 16)).grid(row=1, column=1, sticky="w")
    ttk.Label(detalles_frame, text="Stock Deseado:", font=("Arial", 18, "bold")).grid(row=2, column=0, sticky="w")
    ttk.Label(detalles_frame, textvariable=stock_actual, font=("Arial", 16)).grid(row=2, column=1, sticky="w")
    ttk.Label(detalles_frame, text="Detalles:", font=("Arial", 18, "bold")).grid(row=3, column=0, sticky="w")
    ttk.Label(detalles_frame, textvariable=detalles_text, font=("Arial", 12),wraplength=200).grid(row=3, column=1, sticky="w")

    ttk.Label(detalles_frame, text="Modificar Stock", font=("Arial", 18, "bold")).grid(row=4, column=0, columnspan=2, pady=15)
    # Entrada para nuevo stock y botón de actualización
    global stock_entry
    stock_entry = ttk.Entry(detalles_frame, font=("Arial", 18, "bold"),justify='center')
    stock_entry.grid(row=5, column=0, columnspan=2, pady=(10, 0))
    ttk.Button(detalles_frame, text="Actualizar Stock", command=actualizar_stock, bootstyle='info').grid(row=6, column=0, columnspan=2, pady=(5, 0))

    frame.pack(fill=tk.BOTH, expand=True)
    
    return frame  # Retornar el frame

