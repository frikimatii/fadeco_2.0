import sqlite3 
import tkinter as tk
from tkinter import messagebox

def limpiar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)
import tkinter as tk
import sqlite3

def mostrar_categoria(tabla, categoria, tabladb, detalles, pieza, imagen_label):
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    # Consulta para obtener datos basados en TIPO_DE_MATERIAL
    query = f"""
    SELECT PIEZAS, CANTIDAD, 'brutas' AS source 
    FROM {tabladb} 
    WHERE TIPO_DE_MATERIAL = ? 
    UNION ALL 
    SELECT PIEZAS, CANTIDAD, 'terminadas' AS source 
    FROM piezas_terminadas 
    WHERE TIPO_DE_MATERIAL = ?
    """
    cursor.execute(query, (categoria, categoria))
    datos = cursor.fetchall()
    conn.close()

    # Limpiar la tabla antes de insertar nuevos datos
    limpiar_tabla(tabla)

    # Insertar datos en la tabla
    for dato in datos:
        tabla.insert("", tk.END, values=dato[:2])  # Solo insertar PIEZAS y CANTIDAD, ignorando 'source'

    def on_item_selected(event):
        selected_item = tabla.selection()
        if selected_item:
            pieza_nombre = tabla.item(selected_item[0], "values")[0]

            with sqlite3.connect("dbfadeco.db") as conn:
                cursor = conn.cursor()

                # Primero buscar en piezas_brutas
                cursor.execute(f"SELECT DETALLES, IMAGEN, CANTIDAD FROM {tabladb} WHERE PIEZAS = ?", (pieza_nombre,))
                pieza_detalle = cursor.fetchone()

                # Si no se encuentran detalles en piezas_brutas, buscar en piezas_terminadas
                if not pieza_detalle:
                    cursor.execute("SELECT DETALLES, IMAGEN, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (pieza_nombre,))
                    pieza_detalle = cursor.fetchone()

            # Mostrar el nombre, detalle e imagen en los widgets correspondientes
            pieza.config(text=pieza_nombre)
            if pieza_detalle:
                detalles.config(text=f"{pieza_detalle[0]}")

                # Mostrar imagen si está disponible
                imagen_ruta = pieza_detalle[1]
                if imagen_ruta:
                    # Cargar la imagen
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


def on_item_selected(event, treeview, label, detalles):
    selected_item = treeview.selection()
    if selected_item:
        item_text = treeview.item(selected_item[0], "values")[0]
        label.config(text=item_text)    
        

    else:
        label.config(text="...")
        detalles.config(text="...")

def mostrar_datos(tabla, tipo_de_material, tabladb):
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    # Usar parámetros para evitar inyecciones SQL
    cursor.execute(f"SELECT PIEZAS, CANTIDAD FROM {tabladb} WHERE TIPO_DE_MATERIAL = '{tipo_de_material}' UNION SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE TIPO_DE_MATERIAL = '{tipo_de_material}'")
    datos = cursor.fetchall()
    conn.close()
    limpiar_tabla(tabla)
    for dato in datos:
        tabla.insert("", tk.END, values=dato)

def agregar_piezas(pieza, cant_entry, tabla, accion, categoria, tabladb):
    pieza_nombre = pieza.cget("text").strip()
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

                # Buscar primero en la tabla principal
                cursor.execute(f"SELECT CANTIDAD FROM {tabladb} WHERE PIEZAS = ?", (pieza_nombre,))
                resultado = cursor.fetchone()

                if resultado:
                    # Si se encuentra la pieza, actualizar la cantidad en la tabla principal
                    cantidad_actual = resultado[0]
                    nueva_cantidad = cantidad_actual + cantidad
                    cursor.execute(f"UPDATE {tabladb} SET CANTIDAD = ? WHERE PIEZAS = ?", (nueva_cantidad, pieza_nombre,))
                    messagebox.showinfo("Éxito", f"Se actualizaron {cantidad} unidades a {pieza_nombre} en {tabladb}.")
                    accion.insert(0, f"Carga exitosa: se cargaron {cantidad} unidades a {pieza_nombre} en {tabladb}.")
                else:
                    # Si no se encuentra en la tabla principal, buscar en 'piezas_terminadas'
                    cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (pieza_nombre,))
                    resultado = cursor.fetchone()

                    if resultado:
                        # Si se encuentra en 'piezas_terminadas', actualizar la cantidad
                        cantidad_actual = resultado[0]
                        nueva_cantidad = cantidad_actual + cantidad
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = ? WHERE PIEZAS = ?", (nueva_cantidad, pieza_nombre,))
                        messagebox.showinfo("Éxito", f"Se actualizaron {cantidad} unidades a {pieza_nombre} en piezas terminadas.")
                        accion.insert(0, f"Carga exitosa: se cargaron {cantidad} unidades a {pieza_nombre} en piezas terminadas.")
                    else:
                        # Si no se encuentra en ninguna tabla, mostrar un mensaje de error
                        messagebox.showerror("Error", f"La pieza {pieza_nombre} no se pudo encontrar en {tabladb} ni en piezas terminadas.")
                
                conn.commit()
            except sqlite3.DataError as e:
                messagebox.showerror("Error", f"Error en la base de datos: {e}")
            finally:
                conn.close()
        else:
            print("Operación Cancelada")
    else: 
        messagebox.showerror("Error", "La Cantidad ingresada no es un número válido")
    
    mostrar_datos(tabla, categoria, tabladb)
    cant_entry.delete(0, 'end')


def ordenar_por(treeview, col, reverse):
    # Obtener los datos actuales en la Treeview
    lista = [(treeview.set(k, col), k) for k in treeview.get_children('')]
    
    # Ordenar los datos alfabéticamente o numéricamente
    lista.sort(reverse=reverse)
    
    # Reorganizar los elementos en la Treeview según el ordenamiento
    for index, (val, k) in enumerate(lista):
        treeview.move(k, '', index)
    
    # Cambiar el estado de ordenamiento para la próxima vez que se haga clic
    treeview.heading(col, command=lambda: ordenar_por(treeview, col, not reverse))
