import tkinter as tk
from tkinter import ttk
import sqlite3
import ttkbootstrap as ttk


def limpiar_tabla(tabla):
    """Limpia todos los datos del Treeview."""
    for item in tabla.get_children():
        tabla.delete(item)


def mostrar_datos(tabla, material):
    """
    Muestra los datos en el Treeview, indicando el origen (brutas o terminadas).
    """
    consulta = """
    SELECT PIEZAS, CANTIDAD, DETALLES, 'piezas_brutas' AS ORIGEN 
    FROM piezas_brutas WHERE TIPO_DE_MATERIAL = ? 
    UNION 
    SELECT PIEZAS, CANTIDAD, DETALLES, 'piezas_terminadas' AS ORIGEN 
    FROM piezas_terminadas WHERE TIPO_DE_MATERIAL = ?
    """
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    try:
        cursor.execute(consulta, (material, material))
        datos = cursor.fetchall()
        limpiar_tabla(tabla)
        for dato in datos:
            tabla.insert("", tk.END, values=dato)
    except sqlite3.Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        conn.close()


def on_select(event):

    item = tabla.selection()
    if item:
        values = tabla.item(item, "values")
        pieza, cantidad, detalles, origen = values
        
        # Actualizar los valores en los widgets
        nombre_pieza.config(text=pieza)
        box_detalles.config(text=detalles)
        entry_cantidad.delete(0, tk.END)
        entry_cantidad.insert(0, cantidad)


def modificar_cantidad():

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    try:
        pieza = nombre_pieza.cget("text")
        nueva_cantidad = entry_cantidad.get()
        origen = tabla.item(tabla.selection()[0], "values")[3]  # Columna oculta del origen
        
        if origen == "piezas_brutas":
            cursor.execute(
                "UPDATE piezas_brutas SET CANTIDAD = ? WHERE PIEZAS = ?", 
                (nueva_cantidad, pieza)
            )
        elif origen == "piezas_terminadas":
            cursor.execute(
                "UPDATE piezas_terminadas SET CANTIDAD = ? WHERE PIEZAS = ?", 
                (nueva_cantidad, pieza)
            )
        
        conn.commit()
        print(f"Cantidad de {pieza} actualizada a {nueva_cantidad} en {origen}")
        # Refrescar la tabla
        mostrar_datos(tabla, origen.split("_")[1])  # Muestra los datos del material actual
    except sqlite3.Error as e:
        print(f"Error al modificar: {e}")
    except IndexError:
        print("Por favor, selecciona una pieza antes de modificar.")
    finally:
        conn.close()


def modificar_datosbrutos(parent):

    frame = ttk.Frame(parent)

    # Contenedor principal para la sección de "Modificar Piezas Brutas"
    caja = ttk.Frame(frame)
    caja.grid(row=0, column=0, padx=10, pady=10)
    
    # Título de la sección
    ttk.Label(caja, text="Modificar Piezas Brutas", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="n", pady=3)

    # Treeview para las piezas y cantidades
    caja_treeview = ttk.Frame(caja)
    caja_treeview.grid(row=1, column=0, padx=5, pady=5)
    
    global tabla
    tabla = ttk.Treeview(caja_treeview, columns=("Pieza", "Cantidad", "Detalles", "Origen"))
    tabla.heading("Pieza", text="Pieza")
    tabla.heading("Cantidad", text="Cant.")
    tabla.heading("Detalles", text="Detalles")
    tabla.column("#0", width=0, stretch=tk.NO)
    tabla.column("Pieza", width=150)
    tabla.column("Cantidad", width=70)
    tabla.column("Detalles", width=200)
    tabla.column("Origen", width=0, stretch=tk.NO)  # Columna oculta
    tabla.config(height=18)
    tabla.grid(row=0, column=0, sticky="nsew")
    
    # Caja para los botones
    caja_2 = ttk.Frame(caja_treeview)
    caja_2.grid(row=0, column=1, padx=10, pady=10)
    
    # Etiqueta de tipo de botones
    ttk.Label(caja_2, text="Tipos De Botones").grid(row=0, column=0, padx=10, pady=5)
    
    # Frame para los botones
    frame_botones = ttk.LabelFrame(caja_2, text="Botoneras", padding=10)
    frame_botones.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    # Creación de los botones
    ttk.Button(frame_botones, text="Aluminio", command=lambda: mostrar_datos(tabla, "Aluminio")).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(frame_botones, text="Chapa", command=lambda: mostrar_datos(tabla, "Chapa")).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(frame_botones, text="Shop", command=lambda: mostrar_datos(tabla, "shop")).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(frame_botones, text="Plastico", command=lambda: mostrar_datos(tabla, "Plastico")).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(frame_botones, text="Fundición Hierro", command=lambda: mostrar_datos(tabla, "Hierro")).grid(row=1, column=1, padx=5, pady=5)
    
    frame_detalles = ttk.LabelFrame(caja_2, text="Detalles de la pieza", padding=10)
    frame_detalles.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    
    ttk.Label(frame_detalles, text="Piezas:", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w", padx=3, pady=3)
    
    global nombre_pieza, entry_cantidad, box_detalles
    nombre_pieza = ttk.Label(frame_detalles, text=".", font=("Arial", 12, "bold"))
    nombre_pieza.grid(row=0, column=1, sticky="w", padx=3, pady=3)
    
    ttk.Label(frame_detalles, text="Cantidad:", font=("Arial", 14, "bold")).grid(row=1, column=0, sticky="w", padx=3, pady=3)
    entry_cantidad = ttk.Entry(frame_detalles)
    entry_cantidad.grid(row=1, column=1, sticky="w", padx=3, pady=3)
    
    ttk.Button(frame_detalles, text="Modificar", command=modificar_cantidad).grid(row=2, column=0, sticky="nsew", columnspan=2, padx=3, pady=3)
    
    ttk.Label(frame_detalles, text="Detalles:", font=("Arial", 14, "bold")).grid(row=3, column=0, sticky="w", padx=3, pady=3)
    box_detalles = ttk.Label(frame_detalles, text=".", wraplength=150, font=("Arial", 12, "bold"))
    box_detalles.grid(row=3, column=1, sticky="w", padx=3, pady=3)
    
    tabla.bind("<ButtonRelease-1>", on_select)
    
    return frame
