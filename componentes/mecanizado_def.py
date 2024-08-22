import sqlite3 
import tkinter as tk
from tkinter import messagebox


def limpiar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)

def mostrar_datos(tabla, tipo):  
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    # Consulta combinada usando UNION
    query = f"""
    SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE MECANIZADO = ?
    UNION
    SELECT PIEZAS, CANTIDAD FROM {tipo} WHERE MECANIZADO = ?
    """
    cursor.execute(query, (tipo, tipo))
    datos_combinados = cursor.fetchall()
    conn.close()
    # Limpiar la tabla antes de insertar nuevos datos
    limpiar_tabla(tabla)
    # Insertar los datos combinados en el Treeview
    for dato in datos_combinados:
        tabla.insert("", tk.END, values=dato)

def on_item_selected(event , tabla, label):
    selectec_item = tabla.selection()
    if selectec_item: 
        item_tex  = tabla.item(selectec_item[0], "values")[0]
        label.config(text=item_tex)
    else:
        label.config(text="---")


def agregar_proceso(cantidad, pieza, proceso,table):
    pieza_og = pieza.cget("text")
    cantidad_og = cantidad.get()

    if cantidad_og.strip().isdigit():
        cantidad_og = int(cantidad_og)

        if cantidad_og < 0:
            print("La cantidad no puede ser negativa")
            return

        confirmacion = messagebox.askyesno("Confirmación", f"¿Desea agregar {cantidad_og} unidades de {pieza_og}?")

        if confirmacion:
            conn = sqlite3.connect("dbfadeco.db")
            cursor = conn.cursor()
            
            # Corregir error de sintaxis en la consulta SQL
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE MECANIZADO = ? AND PIEZAS = ?", (proceso, pieza_og))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]

                if cantidad_actual >= cantidad_og:
                    confir = messagebox.askyesno("Confirmar", "¿Estás seguro de continuar?")
                    if confir:
                        nueva_cantidad = cantidad_actual - cantidad_og
                        
                        # Corregir error de espacio antes de "WHERE" en la consulta SQL
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? WHERE MECANIZADO = ? AND PIEZAS = ?", (nueva_cantidad, proceso, pieza_og))
                        conn.commit()

                        # Corregir falta de parámetro en la consulta SQL
                        cursor.execute(f"UPDATE {table} SET CANTIDAD = CANTIDAD + ? WHERE MECANIZADO = ? AND PIEZAS = ?", (cantidad_og, proceso, pieza_og))
                        conn.commit()
                        conn.close()
                    else:
                        print("Operación cancelada por el usuario.")
                else:
                    print("No hay suficientes piezas disponibles.")
            else:
                print("La pieza o el proceso especificado no existe en la base de datos.")
        else:
            print("Operación cancelada por el usuario.")
    else:
        print("La cantidad ingresada no es válida.")

