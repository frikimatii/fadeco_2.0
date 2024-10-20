import sqlite3
import tkinter as tk 
from tkinter import ttk

def obtenerpiezas():
    conn = sqlite3.connect("dbfadeco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT PIEZAS FROM piezas_terminadas")
    lista_de_piezas = cursor.fetchall()
    conn.close()

    return lista_de_piezas 


def chat_proceso_pieza(pieza_combobox, resultado_label):
    pieza_seleccionada = pieza_combobox.get()  # Obtén la pieza seleccionada del combobox
    procesos_piezas = {
    "BaseInox_330": [
        "ChapaBase_330Inox", 
        "varilla_330", 
        "lateral_i330_contecla", 
        "lateral_i330_sintecla", 
        "planchuela_330", 
        "portaeje", 
        "---",
        "PIEZAxPIEZA:",
        "ChapaBase = AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "lateral = MECANIZADO/plasma MECANIZADO/plegadora PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "planchuela, varilla, portaeje = MECANIZADO/sierra,balancin PORVEDOR/soldador PROVEDOR/maxi,carmerlo"
    ],
    
    "BaseInox_300": [
        "ChapaBase_300Inox", 
        "lateral_i300_contecla", 
        "lateral_i300_sintecla", 
        "planchuela_300", 
        "varilla_300", 
        "portaeje", 
        "---",
        "PIEZAxPIEZA:",
        "ChapaBase = AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "lateral = MECANIZADO/plasma MECANIZADO/plegadora PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "planchuela, varilla, portaeje = MECANIZADO/sierra,balancin PORVEDOR/soldador PROVEDOR/maxi,carmerlo"
    ],
    
    "BaseInox_250": [
        "ChapaBase_250Inox", 
        "lateral_i250_contecla", 
        "lateral_i250_sintecla", 
        "planchuela_250", 
        "varilla_250", 
        "portaeje", 
        "---",
        "PIEZAxPIEZA:",
        "ChapaBase = AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "lateral = MECANIZADO/plasma MECANIZADO/plegadora PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "planchuela, varilla, portaeje = MECANIZADO/sierra,balancin PORVEDOR/soldador PROVEDOR/maxi,carmerlo"
    ],
        
        "BasePintada_330": [
        "Pieza q nesecita son:", 
        "ChapaBase_330Pintada", 
        "lateral_p330_contecla", 
        "lateral_p330_sintecla", 
        "planchuela_330", 
        "varilla_330", 
        "portaeje", 
        "---",
        "PIEZAxPIEZA:",
        "ChapaBase = AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PORVEDOR/soldador PROVEDOR/Pintura",
        "lateral = MECANIZADO/plasma MECANIZADO/plegadora PORVEDOR/soldador PROVEDOR/Pintada",
        "planchuela, varilla, portaeje = MECANIZADO/sierra,balancin PORVEDOR/soldador PROVEDOR/Pintada"
    ],

    "BasePintada_300": [
        "Pieza q nesecita son:", 
        "ChapaBase_300Pintada", 
        "lateral_p300_contecla", 
        "lateral_p300_sintecla", 
        "planchuela_300", 
        "varilla_300", 
        "portaeje", 
        "---",
        "PIEZAxPIEZA:",
        "ChapaBase = AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PORVEDOR/soldador PROVEDOR/Pintura",
        "lateral = MECANIZADO/plasma MECANIZADO/plegadora PORVEDOR/soldador PROVEDOR/Pintada",
        "planchuela, varilla, portaeje = MECANIZADO/sierra,balancin PORVEDOR/soldador PROVEDOR/Pintada"
    ],

    "BaseECO": [
        "ChapaBase_330Inox", 
        "lateral_i330_eco", 
        "lateral_i330_sintecla", 
        "planchuela_330", 
        "varilla_330", 
        "portaeje", 
        "---",
        "PIEZAxPIEZA:",
        "ChapaBase = AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "lateral = MECANIZADO/plasma MECANIZADO/plegadora PORVEDOR/soldador PROVEDOR/maxi,carmerlo",
        "planchuela, varilla, portaeje = MECANIZADO/sierra,balancin PORVEDOR/soldador PROVEDOR/maxi,carmerlo"
    ],
        
        "Base_Pre_armado_i330": ["Las Piezas q lleva son:",  "BaseInox_330", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_330", "carros", "rueditas", "resorte_carro", "caja_330_armada", "capacitores"],
        
        "Base_Pre_armado_i300": ["Las Piezas q lleva son:", "BaseInox_300", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_300", "carros", "rueditas", "resorte_carro", "caja_300_armada", "capacitores"],
        
        "Base_Pre_armado_i250": ["Las Piezas q lleva son:", "BaseInox_250", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_250", "carros", "rueditas", "caja_250_armada", "capacitores_250"],
        
        "Base_Pre_armado_p330": ["Las Piezas q lleva son:",  "BasePintada_330", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_330", "carros", "rueditas", "resorte_carro", "caja_330_armada", "capacitores", "bandeja_330"],
        
        "Base_Pre_armado_p300": ["Las Piezas q lleva son:",  "BasePintada_300", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "teclas", "cable_220w", "varilla_330", "carros", "rueditas", "resorte_carro", "caja_300_armada", "capacitores", "bandeja_300"],
        
        "Base_Pre_armado_ECO": ["Las Piezas q lleva son:",  "BaseECO", "aro_numerador", "espiral", "perilla_numerador", "tapita_perilla", "patas", "movimiento", "eje_rectificado", "resorte_movimiento", "tornillo_guia", "guia_u", "cable_eco_220w", "varilla_330", "carros", "resorte_carro", "caja_eco_armada", "rueditas"], 
        
        "ChapaBase_250Inox": ["Proceso para llegar a la pieza lograda: ", "Proceso: AGREGADO PIEZAS/Chapa MECANIZADO: plegado, plamas"],
        
        "ChapaBase_300Inox": ["Proceso para llegar a la pieza lograda: ", "Proceso: AGREGADO PIEZAS/Chapa MECANIZADO: plegado, plamas"],
        
        "ChapaBase_300Pintada": ["Proceso para llegar a la pieza lograda: ", "Proceso: AGREGADO PIEZAS/Chapa MECANIZADO: plegado, plamas"],

        
        "ChapaBase_330Inox": ["Proceso para llegar a la pieza lograda: ", "Proceso: AGREGADO PIEZAS/Chapa MECANIZADO: plegado, plamas"],
        
        "ChapaBase_330Pintada": ["Proceso para llegar a la pieza lograda: ", "Proceso: AGREGADO PIEZAS/Chapa MECANIZADO: plegado, plamas"],
        
        "F_circulo": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "F_cuadrado": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "afilador_final": ["nesesita las piezas", "Piezas:  capuchon_afilador", "carcaza_afilador", "eje_corto", "eje_largo", "ruleman608", "palanca_afilador", "resorte_palanca", "resorte_empuje" , "se encuentra en PROVEDORES/Afilador"],
        
        "aro_numerador": ["Se encuentra en","AGREGADO DE PIEZAS/Aluminio", "PROVEDOR/maxi,carmelo"],
        
        "bandeja_300": ["Se encuentra en: ", "AGREGADO DE PIEZAS/chapa"],
        
        "bandeja_330": ["Se encuentra en: ", "AGREGADO DE PIEZAS/chapa"],
        
        "bandeja_cabezal_inox": ["se encuentra en:", "AGREGADO DE CHAPA/Chapa", "MECANIZADO/plegado, plasma", "PROVEDORES/soldador/cabezales", "MECANIZADO/pulido"],
        
        "bandeja_cabezal_inox_250": ["se encuentra en:", "AGREGADO DE CHAPA/Chapa", "MECANIZADO/plegado, plasma", "PROVEDORES/soldador/cabezales", "MECANIZADO/pulido"],
        
        "bandeja_cabezal_pintada": ["se encuentra en:", "AGREGADO DE CHAPA/Chapa", "MECANIZADO/plegado, plasma", "PROVEDORES/soldador/cabezales", "PROVEDOR/pintura"],
        
        "base_afilador_330": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Alumino"],
        
        "base_afilador_300": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Alumino"],
        
        "base_afilador_250": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Alumino"],
        
        "brazo_250": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio","MECANIZADO/augeriado", "PROVEDOR: MAXI/CARMELO envio, entrega"],
        
        "brazo_300": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio","MECANIZADO/augeriado", "PROVEDOR: MAXI/CARMELO envio, entrega"],
                
        "brazo_330": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio","MECANIZADO/augeriado", "PROVEDOR: MAXI/CARMELO envio, entrega"],
        
        "buje_eje_eco": ["Se encuentra en:", "MECANIZADO/sierra", "MECANIZADO/torno"],
        
        "cabezal_250": ["Proceso para llegar a esa pieza lograda: ","AGREGADO DE PEIZAS/Chapa", "MECANIZADO/plegado, plasma", "PROVEDOR/soldador", "MECANIZADO/pulido" , "Piezas: 'chapa_U_inox_250' , 'chapa_cubre_cabezal_inox_250' , 'bandeja_cabezal_inox_250' "],
        
        "cabezal_inox": ["---Piezas: 'chapa_U_inox', 'chapa_cubre_cabezal_inox', 'bandeja_cabezal_inox'", "==Piezas por separadas==","--chapaU_inox: AGREGADO DE PIEZAS/chapa MECANIZADO/balancin,plegadora PROVEDOR/soldador MECANIZADO/pulido", "--chapa_cubre_cabezal_inox: AGREGADO DE PIEZAS/Chapa MECANIZADO/cortar PROVEDOR/soldador MECANIZADO/pulido", "--bandeja_cabezal_inox: AGREGADO DE PIEZAS/chapa MECANIZADO/plegadora MECANIZADO/plasma PROVEDOR/soldador MECANIZADO/pulido"],
        
        
        "cabezal_pintada": ["Proceso para llegar a esa pieza lograda: ","AGREGADO DE PEIZAS/Chapa", "MECANIZADO/plegado, plasma", "PROVEDOR/soldador", "PROVEDOR/pintura", "Piezas: 'chapa_U_pintada', 'chapa_cubre_cabezal_pintada', 'bandeja_cabezal_pintada'"],
        
        "cable_220w": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "cable_corto_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "cable_eco_220w": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "caja_250_armada": ["CAJA TORNEADA LISTO PARA EL PRE ARMADO"],
        
        "caja_300_armada": ["CAJA TORNEADA LISTO PARA EL PRE ARMADO"],
        
        "caja_330_armada": ["CAJA TORNEADA LISTO PARA EL PRE ARMADO"],
        
        "caja_eco_armada": ["CAJA TORNEADA LISTO PARA EL PRE ARMADO"],
        
        "caja_soldada_eco": [
            "Proceso para llegar a esa pieza lograda: ", 
            "Piezas: AGREGADO DE PIEZAS/pieza_caja_eco o MECANIZADO/plasma",
            "PIezas: MECANIZADO/plasma/media_luna",
            "Piezas: MECANIZADO/sierra/panchuela_inferior"
            "Piezas: MECANIZADO/sierra/panchuela_interior"
            "PIEZA_FINAL:  MECANIZADO/soldador/Caja_soldada_eco"],
        
        "cajas_torneadas_250": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno  PROVEDORES/maxi, carmelo. "],
        
        "cajas_torneadas_300": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno  PROVEDORES/maxi, carmelo. "],
        
        "cajas_torneadas_330": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno  PROVEDORES/maxi, carmelo. "],
        
        "calco_tensor_correa": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "calco_verde_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        
        "capacitores": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "capacitores_250": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "capuchon_250": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "capuchon_afilador": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "capuchon_motor_dodo": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "carcaza_afilador": ["Se obtiene en: ", "AGREGADO DE PIEZAS/aluminio, PROVEDOR/afilador mecanizar carcaza"],
        
        "carros": ["Se obtiene en: ", "AGREGADO DE PIEZAS/fundidor, MECANIZADO/torno, MECANIZADO/augeriado"],
        
        "carros_250":  ["Se obtiene en: ", "AGREGADO DE PIEZAS/fundidor, MECANIZADO/torno, MECANIZADO/augeriado"],
        
        "chapa_U_inox": ["Se Obtiene en:", "AGREGADO DE PIEZAS/Chapa, MECANIZADO/plegadora, MECANIZADO/plama, PROVEDOR/soldador,  MECANIZADO/pulido"],
        
        "chapa_U_inox_250": ["Se Obtiene en:", "AGREGADO DE PIEZAS/Chapa, MECANIZADO/plegadora, MECANIZADO/plama, PROVEDOR/soldador,  MECANIZADO/pulido"],
        
        "chapa_U_pintada": ["Se Obtiene en:", "AGREGADO DE PIEZAS/Chapa, MECANIZADO/plegadora, MECANIZADO/plama, PROVEDOR/soldador,  PROVEDOR/Pintura"],
        
        "chapa_cubre_cabezal_inox": ["Se Obtiene en:", "AGREGADO DE PIEZAS/Chapa, MECANIZADO/plegadora, MECANIZADO/plama, PROVEDOR/soldador,  MECANIZADO/pulido"],
        
        "chapa_cubre_cabezal_inox_250": ["Se Obtiene en:", "AGREGADO DE PIEZAS/Chapa, MECANIZADO/plegadora, MECANIZADO/plama, PROVEDOR/soldador,  MECANIZADO/pulido"],
        
        "chapa_cubre_cabezal_pintada": ["Se Obtiene en:", "AGREGADO DE PIEZAS/Chapa, MECANIZADO/plegadora, MECANIZADO/plama, PROVEDOR/soldador,  PROVEDOR/Pintura"],
        
        "circulo_argentina": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "conector_hembra": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "corona_330": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "corona_300": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "corona_250": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "correa_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "cuadrado_regulador": ["Se encuentra en: ", "MECANIZADO/sierra, MECANIZADO/augeriado, MECANIZADO/soldador"],
        
        "cubre_300": ["Se Obtiene en: ", "AGREGADO DE PIEZAS/Aluminio  MECANIZADO/torno PROVEDORES/maxi, carmelo"],
        
        "cubre_motor_cuadrado": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"], 
        
        "cubre_motor_rectangulo": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"], 
        
        "cubrecuchilla_250": ["Se obtiene en: ", "AGREGADO DE PIEZAS/Aluminio PROVEDORES/maxi,carmelo"],
    
        "cubrecuchilla_330": ["Se obtiene en: ", "AGREGADO DE PIEZAS/Aluminio PROVEDORES/maxi,carmelo"],
        
        "cuchilla_250" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "cuchilla_300" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "cuchilla_330" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "eje": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno"],
        
        "eje_250": ["Se encuentra en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno"],
        
        "eje_corto": ["Se Obtiene en", "MECANIZADO/sierra MECANIZADO/balancin PROVEDORES/Afiladores" ],
        
        "eje_largo": ["Se Obtiene en", "MECANIZADO/sierra MECANIZADO/balancin PROVEDORES/Afiladores" ],
        
        "eje_rectificado": ["Se obtiene en: ", "MECANIZADO/sierra PROVEDOR/niquelado"],
        
        "espiral": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "etiqueta_peligro": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
                
        "etiqueta_cable": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],

        "fadeco_250_2estrella": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "fadeco_300_3estrella" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
    
        "fadeco_300_4estrella" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
    
        "fadeco_330_3estrella" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "fadeco_330_4estrella" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "garantia": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"], 
        
        "guia_u": ["Se obtiene en: ", "MECANIZADO/sierra o AGREGADO DE PIEZAS/Chapa, MECANIZADO/Balancin"],
        
        "lateral_i250_contecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_i250_sintecla":  ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_i300_contecla":  ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_i300_sintecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_i330_contecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_i330_sintecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_i330_eco":  ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/maxi,carmelo"],
        
        "lateral_p300_contecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/pintura"],
        
        "lateral_p300_sintecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/pintura"],

        "lateral_p330_contecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/pintura"], 

        "lateral_p330_sintecla": ["Se obtiene en: ", "MECANIZADO/plasma MECANIZADO/plegadora PROVEDORES/soldador PROVEDOR/pintura"],
        
        "media_luna": ["Media_luna"],    
        
        "manchon": ["Se obtiene en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno"],
        
        "manchon_250": ["Se obtiene en: ", "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno"],
        
        "manual_instruciones":  ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "motor250_220v": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "motor_220v": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "motor_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "movimiento" : ["Se obiene en", "AGREGADO DE PIEZAS/Fundicion MECANIZADO/torno MECANIZADO/Augeriado"],
        
        "oring": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "palanca_afilador": ["Se Obiene en: ", "MECANIZADO/sierra PROVEDOR/niquelado PROVEDOR/Afilador"],
        
        "patas": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "perilla_afilador": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "perilla_brazo": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "perilla_cubrecuchilla": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "perilla_numerador": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "piedra_afilador": ["Se encuentra en", "AGREGADO DE PIEZAS/shop", "--pane--"],
        
        "pinche_frontal": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Chapa"],
        
        "pinche_frontal_250": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Chapa"],
        
        "pinche_lateral": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Chapa"],

        "pinche_lateral_250":["se encuentra en: ", "AGREGANDO DE PIEZAS/Chapa"],
        
        "pipas": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "pitito_teletubi_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "planchada_final_250": ["Se obtiene en:", "AGREGARDO DE PIEZAS/Chapa o MECANIZADO/plasma" , "MECANIZADO/Fresa MECANIZADO/soldado", "PROVEDORES/maxi,carmerlo"],
        
        "planchada_final_300": ["Se obtiene en:", "AGREGARDO DE PIEZAS/Chapa o MECANIZADO/plasma" , "MECANIZADO/Fresa MECANIZADO/soldado", "PROVEDORES/maxi,carmerlo"],
        
        "planchada_final_330": ["Se obtiene en:", "AGREGARDO DE PIEZAS/Chapa o MECANIZADO/plasma" , "MECANIZADO/Fresa MECANIZADO/soldado", "PROVEDORES/maxi,carmerlo"],
        
        "planchuela_300": ["Se obtiene en:" , "MECANIZADO/sierra MECANIZADO/balancin", "PROVEDOR/soldador PROVEDOR/maxi,carmelo o pintura"],
        
        "planchuela_330": ["Se obtiene en:" , "MECANIZADO/sierra MECANIZADO/balancin", "PROVEDOR/soldador PROVEDOR/maxi,carmelo o pintura"],
        
        "planchuela_250": ["Se obtiene en:" , "MECANIZADO/sierra MECANIZADO/balancin", "PROVEDOR/soldador PROVEDOR/maxi,carmelo o pintura"],
        
        "planchuela_inferior": ["Se obtiene en:"],
        
        "planchuela_interior": ["Se obtiene en:"],
        
        
        "polea_chica": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "polea_grande": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "portaeje": ["Se Consigue en:", "MECANIZADO/sierra MECANIZADO/balancin"],
        
        "rectangulo_plastico_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],

        "resorte_brazo": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "resorte_carro": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "resorte_empuje": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "resorte_movimiento": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "resorte_palanca": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "rueditas": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "ruleman6000" : ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "ruleman608": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "rulemanR6" :["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "ruleman_6004": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "ruleman_6005":["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "ruleman_6204":["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "ruleman_6205":["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "seguer":["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "sinfin":["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "tapa_afilador": ["Se consiguen en: " ,"AGREGADO DE PIEZAS/Alumino, PROVEDORES/maxi,carmelo"],
        
        "tapa_afilador_250": ["Se consiguen en: " ,"AGREGADO DE PIEZAS/Alumino, PROVEDORES/maxi,carmelo"],
        
        "tapa_afilador_eco": ["Se consiguen en: " ,"AGREGADO DE PIEZAS/Alumino, PROVEDORES/maxi,carmelo"],
        
        "tapa_correa_eco": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "tapita_perilla": ["se encuentra en: ", "AGREGANDO DE PIEZAS/Plastico"],
        
        "teclas": ["se encuentra en: ", "AGREGANDO DE PIEZAS/shop"],
        
        "teletu_300": ["Se obtiene en:" "AGREGADO DE PIEZAS/Aluminio MECANIZADO/torno", "PROVEDOR/maxi,carmelo"],
        
        "teletubi_250": ["Se obtiene en:" "AGREGADO DE PIEZAS/Aluminio", "PROVEDOR/maxi,carmelo"],
        
        "teletubi_330": ["Se obtiene en:" "AGREGADO DE PIEZAS/Aluminio", "PROVEDOR/maxi,carmelo"],
        
        "teletubi_doblado_eco": ["Se obtiene:" ,"MECANIZADO/sierra MECANIZADO/Balancin", "PROVEDORES/Pintura"],
        
        "tornillo_guia": ["Se obtiene en la pestania: ", "AGREGADO DE PIEZA/shop MECANIZADO/torno"], 
        
        "tornillo_teletubi_eco": ["Se obtiene en la pestania: ", "AGREGADO DE PIEZA/shop MECANIZADO/torno MECANIZADO/augeriado"],
        
        "tubo_manija": ["Se obtiene en la pestania: ", "MECANIZADO/sierra  PROVEDORES/niquelado"],
        
        "tubo_manija_250": ["Se obtiene en la pestania: ", "MECANIZADO/sierra  PROVEDORES/niquelado"],

        "varilla_330" : ["varilla Soldada, se obtiene en:", "MECANIZADO/cortar MECANIZADO/soldar"],
        
        "varilla_300" : ["varilla Soldada, se obtiene en:", "MECANIZADO/cortar MECANIZADO/soldar"],
        
        "varilla_250" : ["varilla Soldada, se obtiene en:", "MECANIZADO/cortar MECANIZADO/soldar"],
        
        "varilla_brazo_330": ["Se obtiene en la pestania: ", "MECANIZADO/sierra  PROVEDORES/niquelado"],
        
        "varilla_brazo_300": ["Se obtiene en la pestania: ", "MECANIZADO/sierra  PROVEDORES/niquelado"],
        
        "varilla_brazo_250": ["Se obtiene en la pestania: ", "MECANIZADO/sierra  PROVEDORES/niquelado"],
        
        "vela_final_300": ["Se obtiene en la pestania: ", "MECANIZADO/plasma o AGREGADO DE PIEZAS/chapa", "MECANIZADO/fresa MECANIZADO/solador", "PROVEDOR/maxi,carmelo"],
        
        "vela_final_330": ["Se obtiene en la pestania: ", "MECANIZADO/plasma o AGREGADO DE PIEZAS/chapa", "MECANIZADO/fresa MECANIZADO/solador", "PROVEDOR/maxi,carmelo"],
        
        "vela_final_250": ["Se obtiene en la pestania: ", "MECANIZADO/plasma o AGREGADO DE PIEZAS/chapa", "MECANIZADO/fresa MECANIZADO/solador", "PROVEDOR/maxi,carmelo"],
        
        "velero": ["Se Obtiene en la Pestanias:", "AGREGADO DE PIEZAS/Aluminio PROVEDORES/maxi,carmelo"]
    }

    if pieza_seleccionada in procesos_piezas:
        # Une los elementos de la lista con saltos de línea
        res = f"La pieza {pieza_seleccionada} que necesita:\n" + '\n'.join  (procesos_piezas[pieza_seleccionada])

        resultado_label.config(state='normal')  # Habilita el widget para poder     modificarlo
        resultado_label.delete(1.0, tk.END)  # Borra el contenido anterior
        resultado_label.insert(tk.END, res)  # Inserta el nuevo texto
        resultado_label.config(state='disabled')  # Deshabilita de nuevo el     widget para hacerlo de solo lectura
    else:
        res = f"Pieza '{pieza_seleccionada}' no encontrada."

        resultado_label.config(state='normal')
        resultado_label.delete(1.0, tk.END)
        resultado_label.insert(tk.END, res)
        resultado_label.config(state='disabled')
        
        
def consultar_proceso_armado(proceso_combobox, text_widget):
    proceso_seleccionado = proceso_combobox.get()
    
    # Aquí podrías tener lógica para cada proceso
    procesos = {
        "Armado de Motores": "Pasos para armar el motor:\n1. Verifique si están todas las piezas. En la pestaña ZONA DE ARMADO, en la sección Armado de caja, puede verificar los motores correspondientes, así como los botones de cada modelo de caja. \n2. Seleccione un modelo y la cantidad. \n3.Una vez terminado el motor, este se deberá tornear para finalizar. Abajo hay dos botones que indican: P/Tornear y P/Armar. \n4. Diríjase a la pestaña MECANIZADO/Torno, seleccione el motor y la cantidad. \n ¡Su motor estará listo para el Pre-Armado!",
        
        "Pre armado": "Pasos para el Pre-Armado de la base: \n1. Verifique en la pestaña ZONA DE ARMADO, los motores listos para armar, en la sección Motores P/Armar. \n2.En la misma pestaña, en la sección Zona de Pre-Armado, puede verificar cada modelo de máquina, con botones que muestran qué piezas necesita cada una y sus cantidades. \n3.Seleccione el modelo de máquina y la cantidad. \n4. Al final de todo, encontrará un botón para verificar las máquinas pre-armadas listas.",
        
        "Armado final": "Pasos para el armado final de las máquinas : \n1. Verifique en la pestaña ZONA DE ARMADO, en la sección Zona Pre-Armado, las máquinas pre-armadas terminadas. \n2. En la misma pestaña, en la sección Zona de Armado, puede verificar las piezas necesarias para cada máquina, según su modelo. \n3. Seleccione el modelo y la cantidad. \4 Abajo, encontrará un botón que muestra las máquinas terminadas del mes.",
        

        "Graficos": "Pasos para visualizar los gráficos:\n1. En la pestaña Zona de Armado, en la sección Zona de Armado, hay un botón llamado Gráficos de Máquinas, que muestra el conteo de las máquinas por mes (en el gráfico encontrarás los diferentes modelos de máquinas representados con barras que indican la cantidad).\n2. En la misma pestaña, al final, encontrarás un botón llamado Mostrar Gráficos del Año, que muestra un gráfico anual con la cantidad de máquinas armadas por mes.",
        
        "Cierre del Mes": "Instrucciones para el cierre del mes: \n1. En la pestaña Zona de Armado, en la sección Cierre del Mes. \n2. Para cerrar el mes, simplemente seleccione el mes actual y presione el botón Terminar el Mes. \n3. Los datos se guardarán automáticamente en el gráfico. \n4. En el ultimo boton 'Mostrar Grafica del AÑo' muestra el grafico de todo el año. ", 
        
        "Agregado de Piezas": "Instrucciones para el agregado de piezas: \n1. A la izquierda encontrará botones con el tipo de cada materia. Seleccione el tipo deseado y presione el botón azul para mostrar las piezas correspondientes. \n2. Al mostrar las piezas en la tabla, seleccione la pieza que desea agregar o eliminar. Al seleccionar la pieza, se mostrará la imagen de la pieza elegida con los detalles correspondientes. \n3. Lo mismo se aplica para cada sección.",
        
        "Mecanizado": "Instrucciones para el mecanizado: \n1. Aquí es donde se encuentra todo el mecanizado de las piezas. \n2. Puede encontrar acciones como: Plegadora, Plasma, Sierra, Agujereado, Torno, Fresa, Soldador, Pulido, y Balancín. \n3. El mecanizado es el mismo para todos; seleccione la pieza que desea mecanizar y la cantidad.  \n4. También contará con botones para verificar el stock de cada producto, tanto terminado como en bruto." ,
        
        "Proveedores": "Instrucciones para proveedores: \n1. A la izquierda, puede encontrar distintos proveedores como: Soldador, Carmelo, Maxi, Pintura, Niquelado, y Afilador. \n2. En diferentes secciones, tendrá acceso al stock de cada pieza, así como a la información sobre las piezas que ofrece cada proveedor. ",
        
        "Control-calidad":"Instrucciones para la pestaña Control-Consulta: \n1. CONTROL: \n-- Botón: Mostrar máquinas terminadas - muestra las máquinas que están terminadas en el proceso de armado. \n--EMBALAJE: Seleccione las máquinas que han pasado por el control de calidad. Aquí se descontarán las calcomanías; seleccione la máquina y la cantidad. Debajo, encontrará dos botones para consultar las máquinas embaladas y el stock de calcomanías. \n--VENTAS: Se descontarán las máquinas que ya están embaladas para la venta del producto final. Al final, encontrará un botón que muestra la cantidad total de ventas.",
        
        "CONSULTORIO": "Instrucciones para la consulta de piezas importantes: \nMOTORES: Seleccione el tipo de motor y la cantidad deseada para verificar si se puede armar. Si la cantidad es correcta, aparecerá en el historial; de lo contrario, se mostrarán las piezas que faltan en la tabla. \nPRE ARMADO: Seleccione el tipo de motor y la cantidad deseada. Si es posible armar la cantidad, se registrará en el historial. Si no, se listarán las piezas que faltan. \n ARMADO FINAL: Seleccione el tipo de motor y la cantidad. Si es factible, se reflejará en el historial; de lo contrario, se indicarán las piezas necesarias en la tabla.", 
        
        "Consulta Pedido": "Instrucciones para la pestaña Control-Consulta: \n Simulador de pedidos \n1. Seleccione la cantidad de cada máquina. \n2.Presione el botón 'Averiguar' para ver los resultados.\n3. Su pedido se reflejará en el historial. \n4. Al hacer clic en el botón 'Abrir Registro', se abrirá un archivo con todos los detalles de las piezas de cada máquina que ha solicitado (se puede imprimir para mayor comodidad).",
        
        "Cierre Anual": "Instrucciones para cerrar el año:  \n1. En la pestaña 'Zona de Armado' hay un botón llamado 'MOSTRAR GRÁFICOS DEL AÑO', que muestra un gráfico con todos los meses y la cantidad de máquinas que se armaron en cada uno. \n2.Debajo, hay otro botón para 'Cerrar el AÑO', que reinicia todos los gráficos del mes a 0, comenzando de nuevo el registro para el nuevo año."
    }
    
    resultado = procesos.get(proceso_seleccionado, "Proceso no encontrado.")
    
    text_widget.config(state='normal')
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, resultado)
    text_widget.config(state='disabled')