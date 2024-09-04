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
            "cajas_torneadas_300": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_6005": 1,
            "ruleman_6205": 2,
            "corona_300": 1,
            "seguer": 1,
            "sinfin": 1,
            "motor_220w": 1,
            "oring": 1,
            "ruleman6000": 1
        },
        3: {
            "cajas_torneadas_250": 1,
            "eje_250": 1,
            "manchon_250": 1,
            "ruleman_6004": 1,
            "ruleman_6204": 2,
            "corona_250": 1,
            "seguer": 1,
            "sinfin": 1,
            "motor250_200w": 1,
            "oring": 1,
            "rulemanR6": 1
        },
        4: {
            "polea_grande": 1, 
            "polea_chica": 1,
            "tornillo_teletubi_eco": 2,
            "teclas": 1,
            "capacitor_eco": 1,
            "conector_hembra": 1,
            "cable_corto_eco": 1,
            "motor_eco": 1,
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

def pre_armado_(modelo, cantidad, historial):
    bases_pre_armadas = {
        "inox_330": {
            "BaseInox_330": 1,
            "aro_numerador": 1,
            "espiral": 1,
            "perilla_numerador": 1,
            "tapita_perilla": 2,
            "patas": 4,
            "movimiento": 1,
            "eje_rectificado": 1,
            "resorte_movimiento": 1,
            "tornillo_guia": 1,
            "guia_u": 1,
            "teclas": 1,
            "cable_220w": 1,
            "varilla_330": 1,
            "carros": 1,
            "rueditas": 4,
            "resorte_carro": 2,
            "caja_330_armada": 1,
            "capacitores": 1
        },
        "inox_300": {
            "BaseInox_300": 1,
            "aro_numerador": 1,
            "espiral": 1,
            "perilla_numerador": 1,
            "tapita_perilla": 2,
            "patas": 4,
            "movimiento": 1,
            "eje_rectificado": 1,
            "resorte_movimiento": 1,
            "tornillo_guia": 1,
            "guia_u": 1,
            "teclas": 1,
            "cable_220w": 1,
            "varilla_300": 1,
            "carros": 1,
            "rueditas": 4,
            "resorte_carro": 2,
            "caja_300_armada": 1,
            "capacitores": 1
        },
        "inox_250": {
            "BaseInox_250": 1,
            "aro_numerador": 1,
            "espiral": 1,
            "perilla_numerador": 1,
            "tapita_perilla": 2,
            "patas": 4,
            "movimiento": 1,
            "eje_rectificado": 1,
            "resorte_movimiento": 1,
            "tornillo_guia": 1,
            "guia_u": 1,
            "teclas": 1,
            "cable_220w": 1,
            "varilla_250": 1,
            "carros": 1,
            "rueditas": 4,
            "caja_250_armada": 1,
            "capacitores_250": 1
        },
        "pintada_330": {
            "BasePintada_330": 1,
            "aro_numerador": 1,
            "espiral": 1,
            "perilla_numerador": 1,
            "tapita_perilla": 2,
            "patas": 4,
            "movimiento": 1,
            "eje_rectificado": 1,
            "resorte_movimiento": 1,
            "tornillo_guia": 1,
            "guia_u": 1,
            "teclas": 1,
            "cable_220w": 1,
            "varilla_330": 1,
            "carros": 1,
            "rueditas": 4,
            "resorte_carro": 2,
            "caja_330_armada": 1,
            "capacitores": 1,
            "bandeja_330": 1
        },
        "pintada_300": {
            "BasePintada_300": 1,
            "aro_numerador": 1,
            "espiral": 1,
            "perilla_numerador": 1,
            "tapita_perilla": 2,
            "patas": 4,
            "movimiento": 1,
            "eje_rectificado": 1,
            "resorte_movimiento": 1,
            "tornillo_guia": 1,
            "guia_u": 1,
            "teclas": 1,
            "cable_220w": 1,
            "varilla_330": 1,
            "carros": 1,
            "rueditas": 4,
            "resorte_carro": 2,
            "caja_300_armada": 1,
            "capacitores": 1,
            "bandeja_300": 1
        },
        "eco": {
            "BaseECO": 1,
            "aro_numerador": 1,
            "espiral": 1,
            "perilla_numerador": 1,
            "tapita_perilla": 2,
            "patas": 4,
            "movimiento": 1,
            "eje_rectificado": 1,
            "resorte_movimiento": 1,
            "tornillo_guia": 1,
            "guia_u": 1,
            "cable_eco_220w": 1,
            "varilla_330": 1,
            "carros": 1,
            "resorte_carro": 2,
            "caja_eco_armada": 1,
            "rueditas": 4
        }
    }
    piezas_necesarias = bases_pre_armadas.get(modelo, {})
    piezas_faltantes = []

    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    for pieza, cantidad_necesaria in piezas_necesarias.items():
        cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ? ", (pieza,))
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
        cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ? ", (pieza,))
        resultado = cursor.fetchone()

        nueva_cantidad = resultado[0] - (cantidad_necesaria * cantidad)
        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = ? WHERE PIEZAS = ? ", (nueva_cantidad, pieza))

    piezas_brutas_mapping = {
        "inox_330": 'Base_Pre_armado_i330',
        "inox_300": 'Base_Pre_armado_i300',
        "inox_250": 'Base_Pre_armado_i250',
        "pintada_330": 'Base_Pre_armado_p330',
        "pintada_300": 'Base_Pre_armado_p300',
        "eco": 'Base_Pre_armado_ECO'
    }

    pieza_bruta = piezas_brutas_mapping.get(modelo)
    if pieza_bruta:
        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD + ? WHERE PIEZAS = ?", (cantidad, pieza_bruta))
        historial.insert(0, f"{pieza_bruta} actualizado en piezas terminadas.")

    conn.commit()
    conn.close()

def armado_final_final(modelo, cantidad, historia):
    # Definimos los componentes necesarios para cada modelo
    maquinas = {
        "inox_330": {
            "brazo_330": 1,
            "cubrecuchilla_330": 1,
            "velero": 1,
            "perilla_brazo": 1,
            "cabezal_inox": 1,
            "teletubi_330": 1,
            "cuchilla_330": 1,
            "cuadrado_regulador": 1,
            "vela_final_330": 1,
            "cubre_motor_rectangulo": 1,
            "cubre_motor_cuadrado": 1,
            "planchada_final_330": 1,
            "varilla_brazo_330": 1,
            "resorte_brazo": 1,
            "tapa_afilador": 1,
            "pipas": 2,
            "tubo_manija": 1,
            "afilador_final": 1,
            "perilla_cubrecuchilla": 2,
            "perilla_afilador": 1,
            "base_afilador_330": 1,
            "Base_Pre_armado_i330": 1,
            "piedra_afilador": 1,
            "pinche_frontal": 1,
            "pinche_lateral": 1
        },
        "inox_300": {
            "brazo_300": 1,
            "cubre_300": 1,
            "velero": 1,
            "perilla_brazo": 1,
            "cabezal_inox": 1,
            "teletu_300": 1,
            "cuchilla_300": 1,
            "cuadrado_regulador": 1,
            "vela_final_300": 1,
            "cubre_motor_rectangulo": 1,
            "cubre_motor_cuadrado": 1,
            "planchada_final_300": 1,
            "varilla_brazo_300": 1,
            "resorte_brazo": 1,
            "tapa_afilador": 1,
            "pipas": 2,
            "tubo_manija": 1,
            "afilador_final": 1,
            "perilla_cubrecuchilla": 2,
            "perilla_afilador": 1,
            "base_afilador_300": 1,
            "Base_Pre_armado_i300": 1,
            "piedra_afilador": 1,
            "pinche_frontal": 1,
            "pinche_lateral": 1
        },
        "inox_250": {
            "brazo_250": 1,
            "cubrecuchilla_250": 1,
            "velero": 1,
            "perilla_brazo": 1,
            "cabezal_250": 1,
            "teletubi_250": 1,
            "cuchilla_250": 1,
            "cuadrado_regulador": 1,
            "vela_final_250": 1,
            "cubre_motor_rectangulo": 1,
            "planchada_final_250": 1,
            "varilla_brazo_250": 1,
            "resorte_brazo": 1,
            "tapa_afilador_250": 1,
            "pipas": 2,
            "tubo_manija_250": 1,
            "afilador_final": 1,
            "perilla_cubrecuchilla": 2,
            "perilla_afilador": 1,
            "base_afilador_250": 1,
            "Base_Pre_armado_i250": 1,
            "piedra_afilador": 1,
            "capuchon_250": 1,
            "pinche_frontal_250": 1,
            "pinche_lateral_250": 1
        },
        "pintada_330": {
            "brazo_330": 1,
            "cubrecuchilla_330": 1,
            "velero": 1,
            "perilla_brazo": 1,
            "cabezal_pintada": 1,
            "teletubi_330": 1,
            "cuchilla_330": 1,
            "cuadrado_regulador": 1,
            "vela_final_330": 1,
            "cubre_motor_rectangulo": 1,
            "cubre_motor_cuadrado": 1,
            "planchada_final_330": 1,
            "varilla_brazo_330": 1,
            "resorte_brazo": 1,
            "tapa_afilador": 1,
            "pipas": 2,
            "tubo_manija": 1,
            "afilador_final": 1,
            "perilla_cubrecuchilla": 2,
            "perilla_afilador": 1,
            "base_afilador_330": 1,
            "Base_Pre_armado_p330": 1,
            "piedra_afilador": 1,
            "pinche_frontal": 1,
            "pinche_lateral": 1
        },
        "pintada_300": {
            "brazo_300": 1,
            "cubre_300": 1,
            "velero": 1,
            "perilla_brazo": 1,
            "cabezal_pintada": 1,
            "teletu_300": 1,
            "cuchilla_300": 1,
            "cuadrado_regulador": 1,
            "vela_final_300": 1,
            "cubre_motor_rectangulo": 1,
            "cubre_motor_cuadrado": 1,
            "planchada_final_300": 1,
            "varilla_brazo_300": 1,
            "resorte_brazo": 1,
            "tapa_afilador": 1,
            "pipas": 2,
            "tubo_manija": 1,
            "afilador_final": 1,
            "perilla_cubrecuchilla": 2,
            "perilla_afilador": 1,
            "base_afilador_300": 1,
            "Base_Pre_armado_p300": 1,
            "piedra_afilador": 1,
            "pinche_frontal": 1,
            "pinche_lateral": 1
        },
        "eco": {
            "brazo_330": 1,
            "cubrecuchilla_330": 1,
            "velero": 1,
            "perilla_brazo": 1,
            "cabezal_inox": 1,
            "teletubi_doblado_eco": 1,
            "cuchilla_330": 1,
            "vela_final_330": 1,
            "cuadrado_regulador": 1,
            "planchada_final_330": 1,
            "varilla_brazo_330": 1,
            "resorte_brazo": 1,
            "tapa_afilador_eco": 1,
            "pitito_teletubi_eco": 1,
            "pipas": 2,
            "tubo_manija": 1,
            "afilador_final": 1,
            "perilla_cubrecuchilla": 2,
            "perilla_afilador": 1,
            "base_afilador_250": 1,
            "Base_Pre_armado_ECO": 1,
            "piedra_afilador": 1,
            "pinche_lateral": 1,
            "pinche_frontal": 1
        }
    }

    # Obtener las piezas necesarias para el modelo
    piezas_necesarias = maquinas.get(modelo, {})
    piezas_faltantes = []

    # Conexión a la base de datos
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    # Verificar disponibilidad de piezas
    for pieza, cantidad_necesaria in piezas_necesarias.items():
        cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (pieza,))
        resultado = cursor.fetchone()

        if resultado is None or resultado[0] < cantidad_necesaria * cantidad:
            piezas_faltantes.append(pieza)
    
    if piezas_faltantes:
        piezas_faltan_str = ", ".join(piezas_faltantes)
        messagebox.showwarning("Piezas Faltantes", f"No hay suficientes cantidad de las siguientes pieza:  {piezas_faltan_str}. No se puede armar la maquina")
        historia.insert(0, f"Faltan Piezas: {piezas_faltan_str}")
        conn.close()
        return

    # Confirmar antes de proceder
    if not messagebox.askyesno("Confirmar", "¿Desea proceder con el armado?"):
        historia.insert(0, "El armado fue cancelado por el usuario.")
        conn.close()
        return

    # Proceder al armado
    for pieza, cantidad_necesaria in piezas_necesarias.items():
        cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_necesaria * cantidad, pieza))
    
    # Actualizar la cantidad del modelo armado en la base de datos
    cursor.execute("UPDATE maquinas SET CANTIDAD = CANTIDAD + ? WHERE MAQUINA = ?", (cantidad, modelo))
    historia.insert(0, f"Se armó {cantidad} máquina(s) del modelo {modelo}.")
    
    conn.commit()
    conn.close()

    # Notificar al usuario del éxito
    messagebox.showinfo("Éxito", f"{cantidad} máquina(s) del modelo {modelo} se armaron con éxito.")
