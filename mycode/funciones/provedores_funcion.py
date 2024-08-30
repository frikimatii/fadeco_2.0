import sqlite3
import tkinter as tk
from tkinter import messagebox

bases_dicc = {
    "inox_330":{
        "chapa_principal": "ChapaBase_330Inox",
        "lateral_con_tecla":"lateral_i330_contecla",
        "lateral_sin_tecla":"lateral_i330_sintecla",
        "plachuela":"planchuela_330",
        "varilla":"varilla_330",
        "portaeje":"portaeje",
    },
    "inox_300":{
        "chapa_principal": "ChapaBase_300Inox",
        "lateral_con_tecla":"lateral_i300_contecla",
        "lateral_sin_tecla":"lateral_i300_sintecla",
        "plachuela":"planchuela_300",
        "varilla":"varilla_300",
        "portaeje":"portaeje",
    },
    "inox_250":{
        "chapa_principal": "ChapaBase_250Inox",
        "lateral_con_tecla":"lateral_i250_contecla",
        "lateral_sin_tecla":"lateral_i250_sintecla",
        "plachuela":"planchuela_250",
        "varilla":"varilla_250",
        "portaeje":"portaeje",
        
    },"pintada_330":{
        "chapa_principal": "ChapaBase_330Pintada",
        "lateral_con_tecla":"lateral_p330_contecla",
        "lateral_sin_tecla":"lateral_p330_sintecla",
        "plachuela":"planchuela_330",
        "varilla":"varilla_330",
        "portaeje":"portaeje",
    },
    "pintada_300":{
        "chapa_principal": "ChapaBase_300Pintada",
        "lateral_con_tecla":"lateral_p300_contecla",
        "lateral_sin_tecla":"lateral_p300_sintecla",
        "plachuela":"planchuela_300",
        "varilla":"varilla_300",
        "portaeje":"portaeje",
    },
    "ECO":{
        "chapa_principal": "ChapaBase_330Eco",
        "lateral_con_tecla":"lateral_i330_eco",
        "lateral_sin_tecla":"lateral_i330_sintecla",
        "plachuela":"planchuela_330",
        "varilla":"varilla_330",
        "portaeje":"portaeje",
    }
}

BaseInox_330 = [
    "ChapaBase_330Inox",
    "varilla_330",
    "lateral_i330_contecla",
    "lateral_i330_sintecla",
    "planchuela_330",
    "portaeje",
]
BaseInox_300 = [
    "ChapaBase_300Inox",
    "lateral_i300_contecla",
    "lateral_i300_sintecla",
    "planchuela_300",
    "varilla_300",
    "portaeje"
]
BaseInox_250 = [
    "ChapaBase_250Inox",
    "lateral_i250_contecla",
    "lateral_i250_sintecla",
    "planchuela_250",
    "varilla_250",
    "portaeje"
]
BasePintada_330 = [
    "ChapaBase_330Pintada",
    "lateral_p330_contecla",
    "lateral_p330_sintecla",
    "planchuela_330",
    "varilla_330",
    "portaeje"
]
BasePintada_300 = [
    "ChapaBase_300Pintada",
    "lateral_p300_contecla",
    "lateral_p300_sintecla",
    "planchuela_300",
    "varilla_300",
    "portaeje"
]
BaseECO = [
    "ChapaBase_330Eco",
    "lateral_i330_eco",
    "lateral_i330_sintecla",
    "planchuela_330",
    "varilla_330",
    "portaeje"
]

cabezales_dic = {
    "cabezal_250": {
        "chapa_U_inox_250": "chapa_U_inox_250",
        "chapa_cubre_cabezal_inox_250": "chapa_cubre_cabezal_inox_250",
        "bandeja_cabezal_inox_250": "bandeja_cabezal_inox_250"
    },
    "cabezal_inox": {
        "chapa_U_inox": "chapa_U_inox",
        "chapa_cubre_cabezal_inox": "chapa_cubre_cabezal_inox",
        "bandeja_cabezal_inox": "bandeja_cabezal_inox"
    },
    "cabezal_pintada": {
        "chapa_U_pintada": "chapa_U_pintada",
        "chapa_cubre_cabezal_pintada": "chapa_cubre_cabezal_pintada",
        "bandeja_cabezal_pintada": "bandeja_cabezal_pintada"
    }
}


#query_mostrar_piezas_soldador = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'soldador'"

base = ["BaseInox_330",
"BaseInox_300",
"BaseInox_250",
"BaseECO"]

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

def mostrar_por_modelo(base_seleccionada, treeview):
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    datos = []
    for piezas, nombre in bases_dicc[base_seleccionada].items():
        # Verificar si la pieza es una varilla
        if "varilla" in piezas:
            cursor.execute("SELECT PIEZAS, CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (nombre,))
        else:
            cursor.execute("SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (nombre,))
        resultado = cursor.fetchall()
        if resultado:
            datos.extend(resultado)
    
    conn.close()
    
    limpiar_tabla(treeview)
    
    for pieza, cantidad in datos:
        treeview.insert("", tk.END, values=(pieza, cantidad))

def enviar_a_soldar(base_seleccionada, cantidad_ingresada, historial):
    base = base_seleccionada.get()
    cantidad_og = int(cantidad_ingresada.get())
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    # Define las listas de piezas para cada base
    bases_dicc = {
        "BaseInox_300": BaseInox_300,
        "BaseInox_330": BaseInox_330,
        "BaseInox_250": BaseInox_250,
        "BasePintada_330": BasePintada_330,
        "BasePintada_300": BasePintada_300,
        "BaseECO": BaseECO,
    }
    
    piezas = bases_dicc.get(base, [])

    if not piezas:
        historial.insert(0, f"La base {base} no es válida.")
        return
    
    # Paso 1: Verificación previa de stock
    for x in piezas:
        if "varilla" in x:  # Maneja todas las varillas
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (x,))
        else:
            cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (x,))
        
        resultado = cursor.fetchone()
        
        if resultado is not None:
            cantidad_actual = resultado[0]
            if cantidad_actual < cantidad_og:
                historial.insert(0, f"No hay suficientes unidades de {x} en stock. Se necesitan {cantidad_og}, pero solo hay {cantidad_actual}.")
                conn.close()
                return  # Sale de la función si no hay suficiente stock
        else:
            historial.insert(0, f"La pieza {x} no se encontró en la base de datos.")
            conn.close()
            return  # Sale de la función si la pieza no se encuentra

    # Mostrar mensaje de confirmación
    confirmar = messagebox.askyesno("Confirmación", f"¿Estás seguro de que quieres descontar {cantidad_og} unidades de todas las piezas de la base {base}?")
    
    if confirmar:  # Si el usuario confirma, se realiza la acción
        # Paso 2: Si todas las piezas tienen suficiente stock, realizar el descuento
        for x in piezas:
            if "varilla" in x:
                cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, x))
            else:
                cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, x))
        
        cursor.execute("UPDATE provedores SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, base))
        
        conn.commit()
        historial.insert(0, f"Se descontaron {cantidad_og} unidades de todas las piezas de la base {base}.")
        cantidad_ingresada.delete(0, "end")
    else:  # Si el usuario cancela, se añade un mensaje al historial
        historial.insert(0, "Operación cancelada por el usuario.")
    
    cursor.close()
    conn.close()

def resibir_bases(base_selecionada, cantidad_ingresada, historial):
    cantidad_og = cantidad_ingresada.get()
    base_og = base_selecionada.get()
    
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida.")
            return
        cantidad_og = int(cantidad_og)
        
        confirmar = messagebox.askokcancel("Confirmar Acción", f"¿Estás seguro de que quieres recibir {cantidad_og} unidades de {base_og}?")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM provedores WHERE PIEZAS = ?", (base_og,))
            resultado = cursor.fetchone()
            
            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    cursor.execute("UPDATE provedores SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, base_og))
                    cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, base_og))
                    historial.insert(0, f"Recibió {cantidad_og} unidades de {base_og}.")
                else:
                    historial.insert(0, f"No hay suficientes unidades de {base_og} en stock.")
            else:
                historial.insert(0, f"La pieza {base_og} no está registrada.")
                
            conn.commit()
            cantidad_ingresada.delete(0, "end")
        else:
            historial.insert(0, "Acción cancelada.")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

def mandar_piezas_a(provedor, canitada_ingresada, pieza_seleccionada, treeview, historial):
    cantidad_og = canitada_ingresada.get()
    pieza_og = pieza_seleccionada.get()
    
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una Cantidad Valida.")
            return
        cantidad_og = int(cantidad_og)
        
        confirmar = messagebox.askyesno("Confirmar accion", f"Estas Seguro que quiere Mandas {cantidad_og}, unidades de {pieza_og}")
        
        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (pieza_og, ))
            resultado = cursor.fetchone()
            
            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?",(cantidad_og, pieza_og))
                    cursor.execute(f"UPDATE {provedor} SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?",(cantidad_og, pieza_og))
                    historial.insert(0, f"Envio {cantidad_og} unidades de {pieza_og} a {provedor}")
                    limpiar_tabla(treeview)
                else:
                    historial.insert(0, f"No hay Suficientes Unideades de {pieza_og} en Stock")
            else:
                historial.insert(0, f"La Piezas {pieza_og} no esta registrado")
            
            conn.commit()
            canitada_ingresada.delete(0, "end")
            
        else:
            historial.insert(0, "Accion Cancelada")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

def resicbir_piezas_de(proveedor, cantidad_ingresada, pieza_seleccionada, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    pieza_og = pieza_seleccionada.get()
    
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una Cantidad Válida.")
            return
        cantidad_og = int(cantidad_og)
        
        if not pieza_og:
            historial.insert(0, "Seleccione una pieza.")
            return
        
        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro que quiere recibir {cantidad_og} unidades de {pieza_og} de {proveedor}?")
        
        if confirmar:
            cursor.execute(f"SELECT CANTIDAD FROM {proveedor} WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()
            
            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    cursor.execute(f"UPDATE {proveedor} SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                    cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
                    
                    historial.insert(0, f"Recibió {cantidad_og} unidades de {pieza_og} de {proveedor}.")
                    limpiar_tabla(treeview)
                else:
                    historial.insert(0, f"No hay suficientes unidades de {pieza_og} en el proveedor.")
            else:
                historial.insert(0, f"La pieza {pieza_og} no está registrada en el proveedor.")
            
            conn.commit()
            cantidad_ingresada.delete(0, "end")
            
        else:
            historial.insert(0, "Acción cancelada.")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

def armar_cabezales(modelo, cantidad, historial):
    cantidad = cantidad.get()  # Obtiene el valor del Entry
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    try:
        if modelo not in cabezales_dic:
            historial.insert(0, f"El modelo {modelo} no existe.")
            return

        piezas_necesarias = cabezales_dic[modelo]

        if not cantidad.isdigit() or int(cantidad) <= 0:
            historial.insert(0, "Ingrese una cantidad válida.")
            return
        cantidad = int(cantidad)

        # Confirmar la acción con el usuario
        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere armar {cantidad} unidades de {modelo}?")
        
        if not confirmar:
            historial.insert(0, "Acción cancelada por el usuario.")
            return

        # Verificación de stock
        for pieza_db_name in piezas_necesarias.values():
            cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (pieza_db_name,))
            resultado = cursor.fetchone()

            if not resultado or resultado[0] < cantidad:
                historial.insert(0, f"No hay suficiente stock de {pieza_db_name} para armar {cantidad} cabezales.")
                return

        # Descontar las piezas necesarias
        for pieza_db_name in piezas_necesarias.values():
            cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad, pieza_db_name))

        # Sumar la cantidad de cabezales armados
        cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (modelo,))
        resultado = cursor.fetchone()

        if resultado:
            nueva_cantidad = resultado[0] + cantidad
            cursor.execute("UPDATE piezas_brutas SET CANTIDAD = ? WHERE PIEZAS = ?", (nueva_cantidad, modelo))
        else:
            historial.insert(0, f"El modelo {modelo} no se encontró.")
            return

        conn.commit()
        historial.insert(0, f"Se armaron {cantidad} unidades de {modelo}.")

    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()

    finally:
        conn.close()

def mandar_a_niquelar(piezas_seleccionada, cantidad_seleccionada, treeview, historial):
    piezas_og = piezas_seleccionada.get()
    cantidad_og = cantidad_seleccionada.get()

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)

        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere mandar a niquelar {cantidad_og} unidades de {piezas_og}?")

        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM piezas_brutas WHERE PIEZAS = ?", (piezas_og,))
            resultado = cursor.fetchone()

            if resultado and resultado[0] >= cantidad_og:
                cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))

                # Verifica si la pieza existe en PIEZAS_RETOCADA
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_RETOCADA WHERE PIEZAS = ?", (piezas_og,))
                resultado_retoque = cursor.fetchone()

                if resultado_retoque:
                    cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                else:
                    historial.insert(0, "No se encontro la pieza seleccionada ")

                limpiar_tabla(treeview)
                historial.insert(0, f"Se mandaron a niquelar {cantidad_og} unidades de {piezas_og}")
                conn.commit()
            else:
                historial.insert(0, f"No se encontró la pieza {piezas_og} o no hay suficiente cantidad en stock.")
            cantidad_seleccionada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally: 
        conn.close()

def resibir_niquelado(piezas_seleccionada, cantidad_seleccionada, treeview, historial):
    piezas_og = piezas_seleccionada.get()
    cantidad_og = cantidad_seleccionada.get()

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    try:
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)

        confirmar = messagebox.askyesno("Confirmar acción", f"¿Está seguro de que quiere mandar a niquelar {cantidad_og} unidades de {piezas_og}?")

        if confirmar:
            cursor.execute("SELECT CANTIDAD FROM PIEZAS_RETOCADA WHERE PIEZAS = ?", (piezas_og,))
            resultado = cursor.fetchone()

            if resultado and resultado[0] >= cantidad_og:
                cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))

                # Verifica si la pieza existe en PIEZAS_RETOCADA
                cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (piezas_og,))
                resultado_retoque = cursor.fetchone()

                if resultado_retoque:
                    cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, piezas_og))
                else:
                    historial.insert(0, "No se encontro la pieza seleccionada ")

                limpiar_tabla(treeview)
                historial.insert(0, f"Se mandaron a niquelar {cantidad_og} unidades de {piezas_og}")
                conn.commit()
            else:
                historial.insert(0, f"No se encontró la pieza {piezas_og} o no hay suficiente cantidad en stock.")
            cantidad_seleccionada.delete(0, "end")
    except sqlite3.Error as e:
        historial.insert(0, f"Error en la base de datos: {e}")
        conn.rollback()
    finally: 
        conn.close()

def mandar_a_pintar(pieza_seleccionada, cantidad_seleccionada, treeview, historial):
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
                cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
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

def resivir_de_pintura(pieza_seleccionada, cantidad_seleccionada, treeview, historial):
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
            cursor.execute("SELECT CANTIDAD FROM PIEZAS_RETOCADA WHERE PIEZAS = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado and resultado[0] >= cantidad_og:
                cursor.execute("UPDATE PIEZAS_RETOCADA SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, pieza_og))
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



