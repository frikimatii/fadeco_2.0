import sqlite3 
import tkinter as tk
from tkinter import messagebox


chapasbase=["ChapaBase_330Inox","ChapaBase_300Inox","ChapaBase_330Pintada","ChapaBase_300Pintada","ChapaBase_250Inox","ChapaBase_330Eco", "bandeja_cabezal_inox_250", "bandeja_cabezal_pintada" , "bandeja_cabezal_inox"]

laterales=["lateral_i330_contecla","lateral_i330_sintecla","lateral_i300_contecla","lateral_i300_sintecla","lateral_i250_contecla","lateral_i250_sintecla","lateral_p330_contecla","lateral_p330_sintecla","lateral_p300_contecla","lateral_p300_sintecla","lateral_i330_eco", "planchada_330", "planchada_300", "planchada_250", "vela_330", "vela_300", "vela_250" , "chapa_U_inox_250", "chapa_U_pintada","chapa_U_inox", "pieza_caja_eco"]

piezas_torno_1 = ["carros", "carros_250", "movimiento", "caja_300", "caja_330", "caja_250", "cubrecuchilla_300", "teletubi_300" ,"tornillo_teletubi_eco"]

piezas_torno_2 = ["buje_eje_eco", "eje", "eje_250", "manchon", "manchon_250", "rueditas", "tornillo_guia", "caja_330_armada", "caja_300_armada", "caja_250_armada", "caja_eco_armada"]

piezas_para_augeriar = ["cuadrado_regulador","brazo_330","brazo_300","brazo_250", "carros", "carros_250", "movimiento", "tornillo_teletubi_eco" ]

piezas_corte = ["planchuela_250","planchuela_300","planchuela_330","varilla_300","varilla_330","varilla_250", "portaeje"]

piezas_augeriado_extra = ["brazo_330","brazo_300","brazo_250"]

piezas_augeriado_extra_1 = ["carros", "carros_250", "movimiento", "tornillo_teletubi_eco"]

piezaas_chapa_u = ["chapaU_inox", "chapaU_pintada", "chapaU_inox_250"]

chapa_cubre_cabezal = ["chapa_cubre_cabezal_inox","chapa_cubre_cabezal_pintada","chapa_cubre_cabezal_inox_250" ]


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
            if piezas_og in chapa_cubre_cabezal:
                cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (piezas_og,))
            else:
                cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (piezas_og,))

            resultado = cursor.fetchone()
            
            if resultado:
                if piezas_og in chapa_cubre_cabezal:
                    cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                else:
                    nueva_cantidad = resultado[0] + cantidad_og
                    cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? WHERE PIEZAS = ?", (nueva_cantidad, piezas_og))
            else:
                historial.insert(0, f"No se encontró la pieza {piezas_og}")
                return  # Salir de la función si no se encuentra la pieza

            limpiar_tabla(treeview)
            historial.insert(0, f"Se cortaron {cantidad_og} unidades de {piezas_og}")
            conn.commit()

            # Limpia el campo de cantidad ingresada
            cantidad_ingresada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

def accion_balancin(cantidad_ingresada, pieza_seleccionar, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    piezas_og = pieza_seleccionar.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)
        
        # Confirmar la acción con el usuario
        confirmar = messagebox.askokcancel("Confirmar Acción", f"¿Está seguro de que quiere pasar por el balancín {cantidad_og} unidades de {piezas_og}?")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (piezas_og,))
            resultado = cursor.fetchone()
            
            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    piezas_mapeo = {
                        "chapaU_inox": "chapa_U_inox",
                        "chapaU_pintada": "chapa_U_pintada",
                        "chapaU_inox_250": "chapa_U_inox_250",
                    }
                    if piezas_og in piezas_mapeo:
                        pieza_fresada = piezas_mapeo[piezas_og]
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_fresada))
                    else:
                        # Actualizar las cantidades en la base de datos para piezas no mapeadas
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                    
                    historial.insert(0, f"Se pasaron {cantidad_og} unidades de {piezas_og} por el balancín.")
                    limpiar_tabla(treeview)
                else:
                    historial.insert(0, f"No hay suficientes unidades de {piezas_og} en stock.")
            else:
                historial.insert(0, f"La pieza {piezas_og} no está registrada.")
            
            conn.commit()
            cantidad_ingresada.delete(0, "end")
        else:
            historial.insert(0, "Acción cancelada.")
    
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    
    finally: 
        conn.close()

def accion_torno(cantidad_ingresada, pieza_seleccionada, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    pieza_og = pieza_seleccionada.get()
    
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        # Validación de la cantidad ingresada
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0: 
            historial.insert(0, "Ingrese una cantidad válida")
            return
        
        cantidad_og = int(cantidad_og)
        
        confirmar = messagebox.askyesno("Confirmar Acción", f"¿Está seguro que quiere tornear {cantidad_og} unidades de {pieza_og}?")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_actual = resultado[0]
                
                if cantidad_actual >= cantidad_og:
                    if pieza_og in piezas_torno_2:
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                        historial.insert(0, f"Se torneo {cantidad_og} unidades de {pieza_og}.")
                    elif pieza_og in piezas_torno_1:
                        # Diccionario para mapeo de piezas y sus piezas resultantes
                        piezas_mapeo = {
                            "caja_330": "cajas_torneadas_330",
                            "caja_300": "cajas_torneadas_300",
                            "caja_250": "cajas_torneadas_250",
                            "cubrecuchilla_300": "cubre_300_torneado",
                            "teletubi_300": "teletubi_300_torneado"
                        }
                        
                        if pieza_og in piezas_mapeo:
                            pieza_torneada = piezas_mapeo[pieza_og]
                            cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                            cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_torneada))
                        
                        if pieza_og in ["carros", "carros_250", "movimiento", "tornillo_teletubi_eco"]:
                            cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                            cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))

                        historial.insert(0, f"Se doblaron {cantidad_og} unidades de {pieza_og}.")
                    else:
                        historial.insert(0, f"No hay suficientes unidades de {pieza_og} en stock.")
                else:
                    historial.insert(0, f"No hay suficientes unidades de {pieza_og} en stock.")
            else:
                historial.insert(0, f"No hay piezas de {pieza_og} en stock.")

            conn.commit()  # Confirmar los cambios en la base de datos
            cantidad_ingresada.delete(0, "end")  # Limpiar la entrada de cantidad
            limpiar_tabla(treeview)  # Limpiar la tabla antes de actualizar los datos
            
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()  # Revertir los cambios en caso de error
    finally:
        conn.close()  # Cerrar la conexión a la base de datos

def accion_augeriado(cantidad_ingresada, pieza_seleccionada, treeview, historial):
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
        print(piezas_og)
        
        # Confirmar la acción con el usuario
        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere augeriar {cantidad_og} unidades de {piezas_og}?")
        if confirmar:
            # Determinar la categoría de la pieza seleccionada
            if piezas_og in piezas_augeriado_extra:
                cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS =?", (piezas_og,))
                resultado = cursor.fetchone()
            elif piezas_og in piezas_augeriado_extra_1:
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_RETOCADA WHERE PIEZAS =?", (piezas_og,))
                resultado = cursor.fetchone()
            elif piezas_og == "cuadrado_regulador":
                cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS =?", (piezas_og,))
                resultado = cursor.fetchone()
            else:
                historial.insert(0, f"La pieza {piezas_og} no está registrada en ninguna categoría válida.")
                return
            
            # Comprobar si hay stock de la pieza seleccionada
            if resultado is not None:
                cantidad_actual = resultado[0]
                
                if cantidad_actual >= cantidad_og:
                    if piezas_og in piezas_augeriado_extra:
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        historial.insert(0, f"Se augeriaron {cantidad_og} unidades de {piezas_og}.")
                    elif piezas_og in piezas_augeriado_extra_1:
                        cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        historial.insert(0, f"Se completaron {cantidad_og} unidades de {piezas_og}.")
                    elif piezas_og == "cuadrado_regulador":
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                        historial.insert(0, f"Se completaron {cantidad_og} unidades de {piezas_og}.")
                    
                    limpiar_tabla(treeview)
                else:
                    historial.insert(0, f"No hay suficientes unidades de {piezas_og} en stock.")
            else:
                historial.insert(0, f"La pieza {piezas_og} está registrada pero no tiene stock inicial.")
            
            conn.commit()
            cantidad_ingresada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

def accion_fresa(cantidad_ingresada, pieza_seleccionar, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    pieza_og = pieza_seleccionar.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)
        
        # Confirmar la acción con el usuario
        confirmar = messagebox.askokcancel("Confirmar Acción", f"¿Está seguro de que quiere pasar por el balancín {cantidad_og} unidades de {pieza_og}?")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    piezas_mapeo = {
                        "vela_250": "vela_fresada_250",
                        "vela_300": "vela_fresada_300",
                        "vela_330": "vela_fresada_330",
                        "planchada_330": "planchada_fresada_330",
                        "planchada_300": "planchada_fresada_300",
                        "planchada_250": "planchada_fresada_250",
                    }
                    if pieza_og in piezas_mapeo:
                        pieza_fresada = piezas_mapeo[pieza_og]
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS= ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS= ?", (cantidad_og, pieza_fresada))
                        
                        historial.insert(0, f"Se fresaron {cantidad_og} unidades de {pieza_og}.")
                    else:
                        historial.insert(0, f"No se pudo encontrar un mapeo para la pieza {pieza_og}.")
                else:
                    historial.insert(0, f"No hay suficientes unidades de {pieza_og} en stock.")
            else:
                historial.insert(0, f"No hay piezas de {pieza_og} en stock.")

            conn.commit()  # Confirmar los cambios en la base de datos
            cantidad_ingresada.delete(0, "end")  # Limpiar la entrada de cantidad
            limpiar_tabla(treeview)  # Limpiar la tabla antes de actualizar los datos
            
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()  # Revertir los cambios en caso de error
    finally:
        conn.close()  # Cerrar la conexión a la base de datos

def accion_lijar(pieza_seleccionada, cantidad_seleccionada, treeview, historial):
    pieza_og = pieza_seleccionada.get()
    cantidad_og = cantidad_seleccionada.get()

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0: 
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)

        confirmar = messagebox.askyesno("Confirmar Acción", f"¿Está seguro de que quiere mandar a pintar {cantidad_og} unidades de {pieza_og}?")

        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado and resultado[0] >= cantidad_og:
                cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                limpiar_tabla(treeview)
                historial.insert(0, f"Se mandaron a pintar {cantidad_og} unidades de {pieza_og}")
                conn.commit()
            else:
                historial.insert(0, f"No hay suficiente cantidad en stock.")
        
        cantidad_seleccionada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()   

def accion_soldar(cantidad_ingresada, pieza_seleccionar, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    pieza_og = pieza_seleccionar.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)
        
        # Confirmar la acción con el usuario
        confirmar = messagebox.askokcancel("Confirmar Acción", f"¿Está seguro de que quiere pasar por el balancín {cantidad_og} unidades de {pieza_og}?")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    piezas_mapeo = {
                        "vela_fresada_250": "vela_final_250",
                        "vela_fresada_300": "vela_final_300",
                        "vela_fresada_330": "vela_final_330",
                        "planchada_fresada_330": "planchada_final_330",
                        "planchada_fresada_300": "planchada_final_300",
                        "planchada_fresada_250": "planchada_final_250",
                    }
                    
                    # Mapeo y actualización según el tipo de pieza
                    if pieza_og in piezas_mapeo:
                        pieza_fresada = piezas_mapeo[pieza_og]
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS= ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS= ?", (cantidad_og, pieza_fresada))
                        
                        historial.insert(0, f"Se soldaron {cantidad_og} unidades de {pieza_og}.")
                    elif pieza_og == "pieza_caja_eco":
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS= ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS= 'caja_soldada_eco'", (cantidad_og,))
                        historial.insert(0, f"Se soldaron {cantidad_og} unidades de caja_soldada_eco.")
                    else:
                        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS= ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS= ?", (cantidad_og, pieza_og))
                        historial.insert(0, f"Se soldaron {cantidad_og} unidades de {pieza_og}.")
                else:
                    historial.insert(0, f"No hay suficientes unidades de {pieza_og} en stock.")
            else:
                historial.insert(0, f"No hay piezas de {pieza_og} en stock.")

            conn.commit()  # Confirmar los cambios en la base de datos
            cantidad_ingresada.delete(0, "end")  # Limpiar la entrada de cantidad
            limpiar_tabla(treeview)  # Limpiar la tabla antes de actualizar los datos
            
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()  # Revertir los cambios en caso de error
    finally:
        conn.close()  # Cerrar la conexión a la base de datos

def accion_pulir(pieza_seleccionada, cantidad_seleccionada, treeview, historial):
    pieza_og = pieza_seleccionada.get()
    cantidad_og = cantidad_seleccionada.get()

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0: 
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)

        confirmar = messagebox.askyesno("Confirmar Acción", f"¿Está seguro de que quiere mandar a pintar {cantidad_og} unidades de {pieza_og}?")

        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado and resultado[0] >= cantidad_og:
                cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                limpiar_tabla(treeview)
                historial.insert(0, f"Se mandaron a pintar {cantidad_og} unidades de {pieza_og}")
                conn.commit()
            else:
                historial.insert(0, f"No hay suficiente cantidad en stock.")
        
        cantidad_seleccionada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()