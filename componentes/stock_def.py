import sqlite3 
import tkinter as tk
from tkinter import messagebox

def limpiar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)

def mostrar_datos(tabla, tablasql):
    conn = sqlite3.connect("fadeco25.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT PIEZAS, CANTIDAD FROM {tablasql}")
    datos = cursor.fetchall()
    conn.close()

    limpiar_tabla(tabla)
    for dato in datos:
        tabla.insert("", tk.END, values=(dato))




def mostrar_categoria(tabla, categoria):
    categoria = categoria.get()

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE TIPO_DE_MATERIAL = ?", (categoria,))
    datos = cursor.fetchall()
    conn.close()

    limpiar_tabla(tabla)

    for dato in datos:
        tabla.insert("", tk.END, values=(dato))


def on_item_selected(event, treeview, label, detalles):
    selected_item = treeview.selection()
    if selected_item:
        item_text = treeview.item(selected_item[0], "values")[0]
        label.config(text=item_text)


        conn = sqlite3.connect("dbfadeco.db")
        cursos = conn.cursor()
        cursos.execute(f"SELECT DETALLES FROM piezas_brutas WHERE PIEZAS = ?",(item_text,))
        datos_detalles = cursos.fetchone()
        conn.close()
        detalles.config(text=datos_detalles[0])

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
                    accion.config(text=f"Carga exitosa: se Cagaron {cantidad} unidades a {pieza_nombre}.")
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

