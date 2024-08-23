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

#query_mostrar_piezas_soldador = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PROVEDOR = 'soldador'"


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
                    cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad_og, base_og))
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
