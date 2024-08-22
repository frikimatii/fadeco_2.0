import sqlite3 
import tkinter as tk
from tkinter import messagebox

def limpiar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)

def mostrar_categoria(tabla, categoria, tabladb, detalles, pieza):
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    # Consulta para obtener datos basados en TIPO_DE_MATERIAL
    cursor.execute(f"SELECT PIEZAS, CANTIDAD FROM {tabladb} WHERE TIPO_DE_MATERIAL = ?", (categoria,))
    datos = cursor.fetchall()
    conn.close()

    # Limpiar la tabla antes de insertar nuevos datos
    limpiar_tabla(tabla)

    # Insertar datos en la tabla
    for dato in datos:
        tabla.insert("", tk.END, values=dato)

    # Asociar el evento de selección en la tabla
    def on_item_selected(event):
        selected_item = tabla.selection()
        if selected_item:
            # Obtener el nombre de la pieza seleccionada
            pieza_nombre = tabla.item(selected_item[0], "values")[0]
            # Conectar a la base de datos para obtener detalles
            conn = sqlite3.connect("dbfadeco.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT DETALLES, CANTIDAD FROM {tabladb} WHERE PIEZAS = ?", (pieza_nombre,))
            pieza_detalle = cursor.fetchone()
            conn.close()

            # Mostrar el nombre y detalle en los widgets correspondientes
            pieza.config(text=pieza_nombre)
            if pieza_detalle:
                detalles.config(text=f"Detalles: {pieza_detalle[0]}")
            else:
                detalles.config(text="No se encontraron detalles para la pieza seleccionada.")
    tabla.bind("<<TreeviewSelect>>", on_item_selected)

def on_item_selected(event, treeview, label, detalles):
    selected_item = treeview.selection()
    if selected_item:
        item_text = treeview.item(selected_item[0], "values")[0]
        label.config(text=item_text)    
        

    else:
        label.config(text="...")
        detalles.config(text="...")

def agregar_piezas(pieza , cant_entry, tabla, accion):
    
    pieza_nombre =  pieza.cget("text").strip()
    cantidad_str = cant_entry.get().strip()

    if cantidad_str.isdigit():
        cantidad = int(cantidad_str)

        if cantidad < 0:
            messagebox.showerror("Error", "La Cantidad no Puede Ser Negativa")
            return

        confirmacion = messagebox.askyesno("Confirmar", f"Desea Agregar {cantidad} unidades de {pieza_nombre}")

        if confirmacion: 
            try:
                conn = sqlite3.connect("dbfadeco.db")
                cursor = conn.cursor()
                cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ? " ,(pieza_nombre,))
                resultado = cursor.fetchone()

                if resultado:
                    cantidad_actual = resultado[0]
                    nueva_cantidad = cantidad_actual + cantidad
                    cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? WHERE PIEZAS =? ", (nueva_cantidad, pieza_nombre,))
                    messagebox.showinfo("Exito")
                    limpiar_tabla(tabla)

                    accion.insert(0, f"Carga exitosa: se Cagaron {cantidad} unidades a {pieza_nombre}.")
                else: 
                    messagebox.showerror("Error", f"La Pieza {pieza_nombre} no se pudo encontrar")
                
                conn.commit()
            except sqlite3.DataError as e:
                messagebox.showerror("Error", f"Erorr en la base de datos: {e}")
            finally:
                conn.close()
        else:
            print("Operacions Cancelada")
    else: 
        messagebox.showerror("Error", "La Cantidad ingresas no es un numero valido")

    cant_entry.delete(0, 'end')


#def mostrar_datos(tabla, tablasql, categoria):
#    conn = sqlite3.connect("fadeco25.db")
#    cursor = conn.cursor()
#    cursor.execute(f"SELECT PIEZAS, CANTIDAD FROM {tablasql} WHERE TIPO_DE_MATERIAL = ?", (categoria,)")
#    datos = cursor.fetchall()
#    conn.close()
#
#    limpiar_tabla(tabla)
#    for dato in datos:
#        tabla.insert("", tk.END, values=(dato))