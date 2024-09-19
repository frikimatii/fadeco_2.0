import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os



tipo_maquina = ["inox_330","inox_300" ,"inox_250", "pintada_330", "pintada_300", "eco"]

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


def accion_embalar(cantidad_ingresada, pieza_seleccionar, treeview, historial):
    cantidad_og = cantidad_ingresada.get()
    pieza_og = pieza_seleccionar.get()
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()

    # Mapeo de calcomanías por cada tipo de máquina
    calcomanias_por_maquina = {
        "inox_330": ["garantia","manual_instruciones","etiqueta_peligro","F_circulo","F_cuadrado","circulo_argentina","etiqueta_cable","fadeco_330_4estrella"],
        "inox_300": ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_300_4estrella"],  # Calcomanías de ejemplo para inox_300
        "inox_250": ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_250_2estrella"],  # Calcomanías de ejemplo para inox_250
        "pintada_330": ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_330_3estrella"],  # Calcomanías de ejemplo para pintada_330
        "pintada_300": ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_300_3estrella"],  # Calcomanías de ejemplo para pintada_300
        "eco": ["garantia", "manual_instruciones", "etiqueta_peligro", "F_circulo", "F_cuadrado", "circulo_argentina", "etiqueta_cable", "fadeco_330_4estrella", "calco_tensor_correa", "calco_verde_eco"]  # Calcomanías de ejemplo para eco
    }

    try:
        # Validar que la cantidad ingresada sea un número positivo
        if not cantidad_og.isdigit() or int(cantidad_og) <= 0:
            historial.insert(0, "Ingrese una cantidad válida")
            return
        cantidad_og = int(cantidad_og)

        # Confirmar la acción con el usuario
        confirmar = messagebox.askokcancel("Confirmar Acción", f"¿Está seguro de que quiere pasar por el balancín {cantidad_og} unidades de {pieza_og}?")
        
        if confirmar:
            # Consultar el stock de la pieza seleccionada
            cursor.execute("SELECT CANTIDAD FROM maquinas WHERE MAQUINA = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    # Verificar si la pieza seleccionada tiene calcomanías asignadas
                    if pieza_og in calcomanias_por_maquina:
                        calcomanias = calcomanias_por_maquina[pieza_og]
                        
                        # Verificar si hay suficientes calcomanías
                        for calcomania in calcomanias:
                            cursor.execute("SELECT CANTIDAD FROM piezas_terminadas WHERE PIEZAS = ?", (calcomania,))
                            resultado_calco = cursor.fetchone()

                            if resultado_calco is None or resultado_calco[0] < cantidad_og:
                                historial.insert(0, f"No hay suficientes calcomanías '{calcomania}' para embalar {cantidad_og} unidades de {pieza_og}.")
                                return  # Salir de la función si faltan calcomanías

                        # Si hay suficientes calcomanías, descontarlas
                        for calcomania in calcomanias:
                            cursor.execute("UPDATE piezas_terminadas SET CANTIDAD = CANTIDAD - ? WHERE PIEZAS = ?", (cantidad_og, calcomania))
                    
                    # Mapeo de piezas fresadas
                    piezas_mapeo = {
                        "inox_250": "inox_250_embalada0",
                        "inox_300": "inox_300_embalada",
                        "inox_330": "inox_330_embalada",
                        "pintada_330": "pintada_330_embalada",
                        "pintada_300": "pintada_300_embalada",
                        "eco": "eco_embalada",
                    }

                    if pieza_og in piezas_mapeo:
                        pieza_fresada = piezas_mapeo[pieza_og]
                        # Actualizar las cantidades en la base de datos
                        cursor.execute("UPDATE maquinas SET CANTIDAD = CANTIDAD - ? WHERE MAQUINA= ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE maquinas SET CANTIDAD = CANTIDAD + ? WHERE MAQUINA= ?", (cantidad_og, pieza_fresada))
                        
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




def accion_venta(cantidad_ingresada, pieza_seleccionar, treeview, historial):
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
            cursor.execute("SELECT CANTIDAD FROM maquinas WHERE MAQUINA = ?", (pieza_og,))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_actual = resultado[0]
                if cantidad_actual >= cantidad_og:
                    piezas_mapeo = {
                        "inox_250_embalada": "inox_250_venta",
                        "inox_300_embalada": "inox_300_venta",
                        "inox_330_embalada": "inox_330_venta",
                        "pintada_330_embalada": "pintada_330_venta",
                        "pintada_300_embalada": "pintada_300_venta",
                        "eco_embalada": "eco_venta",
                    }
                    if pieza_og in piezas_mapeo:
                        pieza_fresada = piezas_mapeo[pieza_og]
                        cursor.execute("UPDATE maquinas SET CANTIDAD = CANTIDAD - ? WHERE MAQUINA= ?", (cantidad_og, pieza_og))
                        cursor.execute("UPDATE maquinas SET CANTIDAD = CANTIDAD + ? WHERE MAQUINA= ?", (cantidad_og, pieza_fresada))
                        
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




motor_330 = {
    "cajas_torneadas_330": 1,#
    "eje": 1,#
    "manchon": 1,#
    "ruleman_6005": 1,#
    "ruleman_6205": 2,#
    "corona_330": 1,#
    "seguer": 1,#
    "sinfin": 1,#
    "motor_220w": 1,
    "oring":1,
    "ruleman6000": 1
}


motor_300 =  {
    "cajas_torneadas_300": 1,#
    "eje": 1,#
    "manchon": 1,#
    "ruleman_6005": 1,#
    "ruleman_6205": 2,#
    "corona_300": 1,#
    "seguer": 1,#
    "sinfin": 1,#
    "motor_220w": 1,#
    "oring":1,            #
    "ruleman6000": 1#
}
motor_250 = {
    "cajas_torneadas_250": 1,#
    "eje_250": 1,#
    "manchon_250": 1,#
    "ruleman_6004": 1,#
    "ruleman_6204": 2,#
    "corona_250": 1,#
    "seguer": 1,#
    "sinfin": 1,#
    "motor250_220w": 1,#
    "oring":1,#
    "rulemanR6": 1#

}
motor_eco = {
    "polea_grande": 1, #
    "polea_chica": 1,#
    "tornillo_teletubi_eco": 2,#
    "capacitor_eco": 1,#
    "conector_hembra": 1,#
    "cable_corto_eco": 1,#
    "motor_eco": 1,#
    "caja_soldada_eco": 1, #
    "tapa_correa_eco": 1,#
    "correa_eco": 1,#
    "capuchon_motor_dodo": 1,#
    "teclas": 1,#
    "buje_eje_eco": 1,#
    "rectangulo_plastico_eco": 1#
}

def contar_motores_disponibles(modelo_motor):
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'armado_caja' "
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        # Manejo de errores, puedes adaptarlo según tus necesidades
        print(f"Error al obtener datos de la base de datos: {e}")
        return -1  # Indicador de error
    finally:
        conn.close()


    if modelo_motor == "330":
        piezas_necesarias = motor_330
    elif modelo_motor == "300":
        piezas_necesarias = motor_300
    elif modelo_motor == "250":
        piezas_necesarias = motor_250
    elif modelo_motor == "eco":
        piezas_necesarias = motor_eco

    
    # Verificar la cantidad mínima de piezas necesarias para un afilador

    # Calcular la cantidad máxima de afiladores que se pueden armar
    cantidad_minima = float('inf')
    for pieza, cantidad_necesaria in piezas_necesarias.items():
        for dato in datos:
            if dato[0] == pieza:
                cantidad_disponible = dato[1]
                cantidad_posible = cantidad_disponible // cantidad_necesaria
                cantidad_minima = min(cantidad_minima, cantidad_posible)

    return cantidad_minima





def obtener_cantidad_piezas_motor():
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas WHERE SECTOR = 'armado_caja'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return {}
    finally:
        conn.close()

    cantidades_disponibles = {}
    for pieza, cantidad in datos:
        cantidades_disponibles[pieza] = cantidad

    return cantidades_disponibles



def verificar_posibilidad_construccion_motor(cantidad_deseada, modelo_seleccionado):
    # Obtener la base según el modelo
    bases_prearmadas = {
        "330": motor_330,
        "300": motor_300,
        "250": motor_250,
        "eco": motor_eco
    }

    tipo_de_modelo = bases_prearmadas.get(modelo_seleccionado)

    if tipo_de_modelo is None:
        print(f"Modelo '{modelo_seleccionado}' no reconocido.")
        return False, {}

    # Obtener las cantidades de piezas disponibles desde la base de datos
    cantidades_disponibles = obtener_cantidad_piezas_motor()

    # Verificar si es posible armar la cantidad deseada
    cantidad_minima = float('inf')
    piezas_faltantes = {}

    for pieza, cantidad_necesaria in tipo_de_modelo.items():
        cantidad_disponible = cantidades_disponibles.get(pieza, 0)

        # Calcular la cantidad máxima que se puede armar sin exceder las cantidades disponibles
        cantidad_maxima_posible = cantidad_disponible // cantidad_necesaria

        cantidad_minima = min(cantidad_minima, cantidad_maxima_posible)

        # Calcular la cantidad faltante y actualizar el diccionario piezas_faltantes
        cantidad_faltante = max(0, cantidad_deseada * cantidad_necesaria - cantidad_disponible)
        if cantidad_faltante > 0:
            piezas_faltantes[pieza] = cantidad_faltante

    # Verificar si la cantidad deseada es alcanzable
    if cantidad_minima >= cantidad_deseada:
        return True, piezas_faltantes
    else:
        return False, piezas_faltantes


def consultar_piezas_sector_motor(entry_cantidad, tabla_consultas, lista_acciones, tipo_pre_combox):
    # Esta función realiza la consulta y actualiza la interfaz gráfica
    for item in tabla_consultas.get_children():
        tabla_consultas.delete(item)

    cantidad_deseada = int(entry_cantidad.get())
    modelo_seleccionado = tipo_pre_combox.get()

    se_puede_armar, piezas_faltantes = verificar_posibilidad_construccion_motor(cantidad_deseada, modelo_seleccionado)

    if se_puede_armar:
        mensaje = f"Se pueden armar {cantidad_deseada} Motores {modelo_seleccionado}."
        lista_acciones.insert(0, mensaje)
    else:
        mensaje = f"No se pueden armar {cantidad_deseada} Motores {modelo_seleccionado}. Piezas faltantes en la tabla:"
        lista_acciones.insert(0, mensaje)
        for pieza, cantidad_faltante in piezas_faltantes.items():
            # Agregar las filas al treeview
            tabla_consultas.insert("", tk.END, values=(pieza, cantidad_faltante), tags=("blue",))



base_pre_inox_armada330 = {
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
        }
base_pre_inox_armada300 = {
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
        }
base_pre_inox_armada250 = {
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
   }
base_pre_pintada_armada330 ={
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
    }
base_pre_pintada_armada300 ={
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
    }
base_pre_inox_armadaeco = {
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
    

def stock_de_prearmado(modelo):
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas  "
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return -1
    finally:
        conn.close()

    # Obtener la base según el modelo
    if modelo == "inoxidable 330":
        tipo_de_modelo = base_pre_inox_armada330
    elif modelo == "inoxidable 300":
        tipo_de_modelo = base_pre_inox_armada300
    elif modelo == "inoxidable 250":
        tipo_de_modelo = base_pre_inox_armada250
    elif modelo == "pintada 330":
        tipo_de_modelo = base_pre_pintada_armada330
    elif modelo == "pintada 300":
        tipo_de_modelo = base_pre_pintada_armada300
    elif modelo == "inoxidable eco":
        tipo_de_modelo = base_pre_inox_armadaeco

    cantidad_minima = float('inf')
    for pieza, cantidad_necesaria in tipo_de_modelo.items():
        for dato in datos:
            if dato[0] == pieza:
                cantidad_disponible = dato[1]
                cantidad_posible = cantidad_disponible // cantidad_necesaria
                cantidad_minima = min(cantidad_minima, cantidad_posible)

    return cantidad_minima




def obtener_cantidad_piezas_prearmado():
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return {}
    finally:
        conn.close()

    cantidades_disponibles = {}
    for pieza, cantidad in datos:
        cantidades_disponibles[pieza] = cantidad

    return cantidades_disponibles


def verificar_posibilidad_construccion(cantidad_deseada, modelo_seleccionado):
    # Obtener la base según el modelo
    bases_prearmadas = {
        "inoxidable 330": base_pre_inox_armada330,
        "inoxidable 300": base_pre_inox_armada300,
        "inoxidable 250": base_pre_inox_armada250,
        "pintada 330": base_pre_pintada_armada330,
        "pintada 300": base_pre_pintada_armada300,
        "inoxidable eco" : base_pre_inox_armadaeco,
    }

    tipo_de_modelo = bases_prearmadas.get(modelo_seleccionado)

    if tipo_de_modelo is None:
        print(f"Modelo '{modelo_seleccionado}' no reconocido.")
        return False, {}

    # Obtener las cantidades de piezas disponibles desde la base de datos
    cantidades_disponibles = obtener_cantidad_piezas_prearmado()

    # Verificar si es posible armar la cantidad deseada
    cantidad_minima = float('inf')
    piezas_faltantes = {}

    for pieza, cantidad_necesaria in tipo_de_modelo.items():
        cantidad_disponible = cantidades_disponibles.get(pieza, 0)

        # Calcular la cantidad máxima que se puede armar sin exceder las cantidades disponibles
        cantidad_maxima_posible = cantidad_disponible // cantidad_necesaria

        cantidad_minima = min(cantidad_minima, cantidad_maxima_posible)

        # Calcular la cantidad faltante y actualizar el diccionario piezas_faltantes
        cantidad_faltante = max(0, cantidad_deseada * cantidad_necesaria - cantidad_disponible)
        if cantidad_faltante > 0:
            piezas_faltantes[pieza] = cantidad_faltante

    # Verificar si la cantidad deseada es alcanzable
    if cantidad_minima >= cantidad_deseada:
        return True, piezas_faltantes
    else:
        return False, piezas_faltantes

def consultar_piezas_sector(entry_cantidad, tabla_consultas, lista_acciones, tipo_pre_combox):
    # Esta función realiza la consulta y actualiza la interfaz gráfica
    for item in tabla_consultas.get_children():
        tabla_consultas.delete(item)

    cantidad_deseada = int(entry_cantidad.get())
    modelo_seleccionado = tipo_pre_combox.get()

    se_puede_armar, piezas_faltantes = verificar_posibilidad_construccion(cantidad_deseada, modelo_seleccionado)

    if se_puede_armar:
        mensaje = f"Se pueden armar {cantidad_deseada} {modelo_seleccionado}."
        lista_acciones.insert(0, mensaje)
    else:
        mensaje = f"No se pueden armar {cantidad_deseada} {modelo_seleccionado}. Piezas faltantes en la tabla:"
        lista_acciones.insert(0, mensaje)
        for pieza, cantidad_faltante in piezas_faltantes.items():
            # Agregar las filas al treeview
            tabla_consultas.insert("", tk.END, values=(pieza, cantidad_faltante), tags=("blue",))




inox_330__ = {
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
}
inox_300__ = {
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
}
inox_250__ = {
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
}
pintada_330__ = {
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
        }
pintada_300__= {
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
}
eco__ = {
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





def maquinas_dis(modelo_maquina):
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas" )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return -1
    finally:
        conn.close()

    if modelo_maquina == "inox 330":
        piezas_necesarias = inox_330__
    elif modelo_maquina == "inox 300":
        piezas_necesarias = inox_300__
    elif modelo_maquina == "inox 250":
        piezas_necesarias = inox_250__
    elif modelo_maquina == "pint 330":
        piezas_necesarias = pintada_330__
    elif modelo_maquina == "pint 300":
        piezas_necesarias = pintada_300__
    elif modelo_maquina == "inox eco":
        piezas_necesarias = eco__
    
    cantidad_minima = float('inf')
    for pieza, cantidad_necesaria in piezas_necesarias.items():
        for dato in datos:
            if dato[0] == pieza:
                cantidad_disponible = dato[1]
                cantidad_posible = cantidad_disponible // cantidad_necesaria
                cantidad_minima = min(cantidad_minima, cantidad_posible)

    return cantidad_minima





def obtener_maquina_final():
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT PIEZAS, CANTIDAD FROM piezas_terminadas"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return {}
    finally:
        conn.close()

    cantidades_disponibles = {}
    for pieza, cantidad in datos:
        cantidades_disponibles[pieza] = cantidad

    return cantidades_disponibles


def verificar_posibilidad_maquina_teminada(cantidad_deseada, modelo_seleccionado):
    # Obtener la base según el modelo
    maquina_final = {
        "inoxidable 330": inox_330__,
        "inoxidable 300": inox_300__,
        "inoxidable 250": inox_250__,
        "pintada 330": pintada_330__,
        "pintada 300": pintada_300__,
        "inoxidable eco":  eco__
    }

    tipo_de_modelo = maquina_final.get(modelo_seleccionado)

    if tipo_de_modelo is None:
        print(f"Modelo '{modelo_seleccionado}' no reconocido.")
        return False, {}

    # Obtener las cantidades de piezas disponibles desde la base de datos
    cantidades_disponibles = obtener_maquina_final()

    # Verificar si es posible armar la cantidad deseada
    cantidad_minima = float('inf')
    piezas_faltantes = {}

    for pieza, cantidad_necesaria in tipo_de_modelo.items():
        cantidad_disponible = cantidades_disponibles.get(pieza, 0)

        # Calcular la cantidad máxima que se puede armar sin exceder las cantidades disponibles
        cantidad_maxima_posible = cantidad_disponible // cantidad_necesaria

        cantidad_minima = min(cantidad_minima, cantidad_maxima_posible)

        # Calcular la cantidad faltante y actualizar el diccionario piezas_faltantes
        cantidad_faltante = max(0, cantidad_deseada * cantidad_necesaria - cantidad_disponible)
        if cantidad_faltante > 0:
            piezas_faltantes[pieza] = cantidad_faltante

    # Verificar si la cantidad deseada es alcanzable
    if cantidad_minima >= cantidad_deseada:
        return True, piezas_faltantes
    else:
        return False, piezas_faltantes


def consultar_maquinas_final(entry_cantidad, tabla_consultas, lista_acciones, tipo_pre_combox):
    # Esta función realiza la consulta y actualiza la interfaz gráfica
    for item in tabla_consultas.get_children():
        tabla_consultas.delete(item)

    cantidad_deseada = int(entry_cantidad.get())
    modelo_seleccionado = tipo_pre_combox.get()

    se_puede_armar, piezas_faltantes = verificar_posibilidad_maquina_teminada(cantidad_deseada, modelo_seleccionado)

    if se_puede_armar:
        mensaje = f"Se pueden armar {cantidad_deseada} Motores {modelo_seleccionado}."
        lista_acciones.insert(0, mensaje)
    else:
        mensaje = f"No se pueden armar {cantidad_deseada} Motores {modelo_seleccionado}. Piezas faltantes en la tabla:"
        lista_acciones.insert(0, mensaje)
        for pieza, cantidad_faltante in piezas_faltantes.items():
            # Agregar las filas al treeview
            tabla_consultas.insert("", tk.END, values=(pieza, cantidad_faltante), tags=("blue",))





#-------------------------------------------------------------------------------------------





def obtener_stock_piezas():
    try:
        conn = sqlite3.connect("dbfadeco.db")
        cursor = conn.cursor()
        cursor.execute("SELECT PIEZAS, CANTIDAD FROM piezas_terminadas")
        datos_piezas = dict(cursor.fetchall())
        return datos_piezas
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
        return {}
    finally:
        conn.close()

def obtener_base_piezas_modelo(modelo):
    # Asegúrate de que estas variables estén definidas en otro lugar de tu código
    bases_prearmadas = {
        "inoxidable 330": inox_330__,
        "inoxidable 300": inox_300__,
        "inoxidable 250": inox_250__,
        "pintada 330": pintada_330__,
        "pintada 300": pintada_300__,
        "inoxidable eco": eco__,
    }
    return bases_prearmadas.get(modelo, {})

def verificar_disponibilidad_pedido(pedido_maquinas, modelos_prioridad):
    stock_piezas = obtener_stock_piezas()
    piezas_faltantes_totales = {}
    piezas_faltantes_por_modelo = {}

    for modelo in modelos_prioridad:
        if modelo not in pedido_maquinas:
            continue

        cantidad_pedido = pedido_maquinas[modelo]
        try:
            cantidad_pedido = int(cantidad_pedido) if str(cantidad_pedido).isdigit() else 0
        except ValueError:
            cantidad_pedido = 0
        
        base_piezas_modelo = obtener_base_piezas_modelo(modelo)
        if not base_piezas_modelo:
            print(f"Modelo '{modelo}' no reconocido.")
            continue

        piezas_faltantes_por_modelo[modelo] = {}
        
        for pieza, cantidad_necesaria in base_piezas_modelo.items():
            try:
                cantidad_necesaria = int(cantidad_necesaria) if str(cantidad_necesaria).isdigit() else 0
            except ValueError:
                cantidad_necesaria = 0
                
            cantidad_disponible = int(stock_piezas.get(pieza, 0))
            cantidad_requerida = cantidad_necesaria * cantidad_pedido

            if cantidad_disponible < cantidad_requerida:
                cantidad_faltante = cantidad_requerida - cantidad_disponible
                piezas_faltantes_por_modelo[modelo][pieza] = cantidad_faltante
                piezas_faltantes_totales[pieza] = piezas_faltantes_totales.get(pieza, 0) + cantidad_faltante

                stock_piezas[pieza] = 0

            else:
                stock_piezas[pieza] -= cantidad_requerida

    if not piezas_faltantes_totales:
        return True, {}
    else:
        return False, {
            "totales": piezas_faltantes_totales,
            "por_modelo": piezas_faltantes_por_modelo
        }

def on_averiguar_click(entry_i330, entry_i300, entry_i250, entry_p330, entry_p300, entry_ieco, priority_i330, priority_i300, priority_i250, priority_p330, priority_p300, priority_ieco, tree, listbox):
    for item in tree.get_children():
        tree.delete(item)
    
    listbox.delete(0, 'end')

    # Obtener las prioridades
    prioridades = {
        "inoxidable 330": int(priority_i330.get() or 0),
        "inoxidable 300": int(priority_i300.get() or 0),
        "inoxidable 250": int(priority_i250.get() or 0),
        "pintada 330": int(priority_p330.get() or 0),
        "pintada 300": int(priority_p300.get() or 0),
        "inoxidable eco": int(priority_ieco.get() or 0),
    }

    # Ordenar los modelos por prioridad (más alto primero)
    modelos_prioridad = sorted(prioridades.keys(), key=lambda x: prioridades[x])
    
    pedido_maquinas = {
        "inoxidable 330": entry_i330.get(),
        "inoxidable 300": entry_i300.get(),
        "inoxidable 250": entry_i250.get(),
        "pintada 330": entry_p330.get(),
        "pintada 300": entry_p300.get(),
        "inoxidable eco": entry_ieco.get(),
    }

    se_puede_armar, piezas_faltantes = verificar_disponibilidad_pedido(pedido_maquinas, modelos_prioridad)

    reporte_piezas_faltantes = ""
    if se_puede_armar:
        listbox.insert(0, "El pedido se puede armar.")
        reporte_piezas_faltantes += "El pedido se puede armar.\n"
    else:
        listbox.insert(0, "No hay suficientes piezas para armar el pedido.")
        reporte_piezas_faltantes += "No hay suficientes piezas para armar el pedido.\n"
        
        # Mostrar el total de piezas faltantes
        listbox.insert('end', "Piezas faltantes (total):")
        reporte_piezas_faltantes += "Piezas faltantes (total):\n"
        for pieza, cantidad_faltante in piezas_faltantes["totales"].items():
            listbox.insert('end', f"  - {pieza}: Faltan {cantidad_faltante}")
            reporte_piezas_faltantes += f"  - {pieza}: Faltan {cantidad_faltante}\n"

        # Mostrar desglose por modelo
        listbox.insert('end', "\nDesglose por modelo:")
        reporte_piezas_faltantes += "\nDesglose por modelo:\n"
        for modelo, piezas_modelo in piezas_faltantes["por_modelo"].items():
            listbox.insert('end', f"\nFaltan piezas para el modelo {modelo}:")
            reporte_piezas_faltantes += f"\nFaltan piezas para el modelo {modelo}:\n"
            for pieza, cantidad_faltante in piezas_modelo.items():
                listbox.insert('end', f"  - {pieza}: Faltan {cantidad_faltante}")
                reporte_piezas_faltantes += f"  - {pieza}: Faltan {cantidad_faltante}\n"

    guardar_reporte_en_txt(reporte_piezas_faltantes)
    return reporte_piezas_faltantes

def guardar_reporte_en_txt(reporte):
    with open("reporte_piezas_faltantes.txt", "w") as file:
        file.write(reporte)

def abrir_archivo_reporte():
    # Función para abrir el archivo creado
    archivo = "reporte_piezas_faltantes.txt"
    if os.path.exists(archivo):
        os.startfile(archivo)  # Solo en Windows
    else:
        print("El archivo no existe.")
