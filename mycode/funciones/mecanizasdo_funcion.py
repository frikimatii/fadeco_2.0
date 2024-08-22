import sqlite3 
import tkinter as tk
from tkinter import messagebox


chapasbase=["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","ChapaBase_330Eco"]

laterales=["lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco"]

piezas_corte = ["planchuela_250","planchuela_300","planchuela_330","varilla_300","varilla_330","varilla_250", "portaeje"]


def limpiar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)

def mostrar_piezas_tablas(treeview, quety):
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    cursor.execute(quety)
    datos = cursor.fetchall()
    conn.close()
    limpiar_tabla(treeview)
    for dato in datos:
        treeview.insert("", tk.END, values=(dato))

def accion_plegadora(cantidad_ingresada, pieza_seleccionada, treeview, historia):
    cantidad_og = cantidad_ingresada.get()
    piezas_og = pieza_seleccionada.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    print(piezas_og)
    
    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historia.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)
        print(piezas_og)
        # Confirmar la acción con el usuario
        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere doblar {cantidad_og} unidades de {piezas_og}?")
        if confirmar: 
            # Obtener la cantidad actual de la pieza en la tabla 'piezas_brutas'
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (piezas_og,) )
            resultado = cursor.fetchone()
            if resultado:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    print(piezas_og)
                    if piezas_og in chapasbase:
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE plasma SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                    
                    elif piezas_og in laterales:
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                    
                    historia.insert(0, f"Se doblaron {cantidad_og} unidades de {piezas_og}")
                    limpiar_tabla(treeview)  # Limpiar la tabla antes de actualizar los datos
                else:
                    historia.insert(0, f"No hay suficientes unidades de {piezas_og} en stock")
            else: 
                historia.insert(0, f"No hay piezas de {piezas_og} en stock")
            conn.commit()  # Confirmar los cambios en la base de datos
            cantidad_ingresada.delete(0, "end")  # Limpiar la entrada de cantidad
    except sqlite3.Error as e:
        historia.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()  # Revertir los cambios en caso de error
    finally:
        conn.close()  # Cerrar la conexión a la base de datosrrar la conexión a la base de datos'

def accion_plasmas(cantidad_ingresada, pieza_seleccionada, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    piezas_og = pieza_seleccionada.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return    
        cantidad_og = int(cantidad_og)
        
        # Confirmar la acción con el usuario
        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere cortar {cantidad_og} unidades de {piezas_og}?")
        
        if confirmar:
            # Verificar si la pieza está en las listas correspondientes
            if piezas_og in laterales:
                cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (piezas_og,))
                resultado = cursor.fetchone()
            elif piezas_og in chapasbase:
                cursor.execute("SELECT CANTIDAD FROM plasma WHERE PIEZAS = ?", (piezas_og,))
                resultado = cursor.fetchone()
            else:
                historial.insert(0, f"La pieza {piezas_og} no está registrada en ninguna categoría válida")
                return
            
            # Si la pieza existe en la base de datos, actualizarla
            if resultado is not None:
                cantidad_actual = resultado[0]
                if piezas_og in chapasbase:
                    if cantidad_actual >= cantidad_og:
                        cursor.execute("UPDATE plasma SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        historial.insert(0, f"Se cortaron {cantidad_og} unidades de {piezas_og}")
                    else:
                        historial.insert(0, f"No hay suficientes unidades de {piezas_og} en stock")
                elif piezas_og in laterales:
                    cantidad_actual += cantidad_og
                    cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? WHERE PIEZAS = ?", (cantidad_actual, piezas_og))
                    historial.insert(0, f"Se cortaron {cantidad_og} unidades de {piezas_og}")
                    limpiar_tabla(treeview)
            else:
                historial.insert(0, f"La pieza {piezas_og} está registrada pero no tiene stock inicial")
            
            conn.commit()
            cantidad_ingresada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

def accion_corte(cantidad_ingresada, pieza_seleccionada, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    piezas_og = pieza_seleccionada.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)
        
        # Confirmar la acción con el usuario
        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere cortar {cantidad_og} unidades de {piezas_og}?")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (piezas_og, ))
            resultado = cursor.fetchone()
            
            if resultado:
                cantidad_actual = resultado[0] + cantidad_og
                # Actualizar la cantidad existente
                cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? WHERE PIEZAS = ?", (cantidad_actual, piezas_og))
            else:
                historial.insert(0, f"No se encontro la pieza {piezas_og}")
                            
            limpiar_tabla(treeview)
            historial.insert(0, f"Se cortaron {cantidad_og} unidades de {piezas_og}")
            conn.commit()
            cantidad_ingresada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

