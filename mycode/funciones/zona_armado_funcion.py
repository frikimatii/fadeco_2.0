import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import sqlite3


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


def mostrar_piezas_motor(treeview, piezas):
    # Conectar a la base de datos
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    # Limpiar el Treeview antes de insertar nuevos datos
    for row in treeview.get_children():
        treeview.delete(row)
    # Preparar una consulta SQL
    query = "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?"
    # Iterar sobre las piezas y ejecutar la consulta para cada una
    for pieza in piezas:
        cursor.execute(query, (pieza,))
        resultados = cursor.fetchall()
        
        # Insertar los resultados en el Treeview
        for row in resultados:
            treeview.insert("", "end", values=(row[0], row[1]))
    
    # Cerrar la conexión
    conn.close()

def manejar_inventario(modelo, cantidad, historial):
    motores_terminado = {
        1: {
            "cajas_torneadas_330": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_6005": 1,
            "ruleman_6205": 2,
            "corona_330": 1,
            "seguer": 1,
            "sinfin": 1,
            "motor_220w": 1,
            "oring": 1,
            "ruleman6000": 1
        },
        2: {
            "caja_torneado_300": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_6005": 1,
            "ruleman_6205": 2,
            "corona_300": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores_220w": 1,
            "oring": 1,
            "ruleman6000": 1
        },
        3: {
            "caja_torneado_250": 1,
            "eje_250": 1,
            "manchon_250": 1,
            "ruleman_6004": 1,
            "ruleman_6204": 2,
            "corona_250": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores250_220w": 1,
            "oring": 1,
            "rulemanR6": 1
        },
        4: {
            "polea_grande": 1, 
            "polea_chica": 1,
            "tornillo_teletubi_eco_fin": 2,
            "teclas": 1,
            "capacitores_eco": 1,
            "conector_hembra": 1,
            "cable_corto_eco": 1,
            "motores_eco": 1,
            "caja_soldada_eco": 1, 
            "tapa_correa_eco": 1,
            "correa_eco": 1,
            "capuchon_motor_dodo": 1,
            "buje_eje_eco": 1,
            "rectangulo_plastico_eco": 1
        }
    }
    
    piezas_necesarias = motores_terminado.get(modelo, {})
    piezas_faltantes = []
    
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    
    for pieza, cantidad_necesaria in piezas_necesarias.items():
        cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ? AND SECTOR = 'armado_caja'", (pieza,))
        resultado = cursor.fetchone()
        
        if resultado is None or resultado[0] < cantidad_necesaria * cantidad:
            piezas_faltantes.append(pieza)
    
    if piezas_faltantes:
        piezas_faltan_str = ", ".join(piezas_faltantes)
        messagebox.showwarning("Piezas Faltantes", f"No hay suficiente cantidad de las siguientes piezas: {piezas_faltan_str}. No se puede armar la caja.")
        historial.insert(0, f"Faltan piezas: {piezas_faltan_str}")
        conn.close()
        return
    
    if not messagebox.askyesno("Confirmar", "¿Deseas armar la caja con las piezas disponibles?"):
        conn.close()
        historial.insert(0, "Armado de caja cancelado por el usuario.")
        return
    
    for pieza, cantidad_necesaria in piezas_necesarias.items():
        cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ? AND SECTOR = 'armado_caja'", (pieza,))
        resultado = cursor.fetchone()
        
        nueva_cantidad = resultado[0] - (cantidad_necesaria * cantidad)
        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = ? WHERE PIEZAS = ? AND SECTOR = 'armado_caja'", (nueva_cantidad, pieza))

    
    piezas_brutas_mapping = {
        1: 'caja_330_armada',
        2: 'caja_300_armada',
        3: 'caja_250_armada',
        4: 'caja_eco_armada'
    }
    
    pieza_bruta = piezas_brutas_mapping.get(modelo)
    if pieza_bruta:
        cursor.execute("UPDATE piezas_brutas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad, pieza_bruta))
        historial.insert(0, f"{pieza_bruta} actualizado en piezas_brutas.")
    
    conn.commit()
    conn.close()
