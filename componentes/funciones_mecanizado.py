import sqlite3
import tkinter as tk
from tkinter import messagebox

def limpiar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)

def mostrar_piezas_en_bruto(tabla, categoria):
    categoria = categoria.get()

    conn = sqlite3.connect("fadeco25.db")
    cursor = conn.cursor()
    cursor.execute("SELECT PIEZAS, CANTIDAD FROM PIEZAS_BRUTO WHERE MECANIZADO = ?", (categoria,))
    datos = cursor.fetchall()
    cursor.close()

    limpiar_tabla(tabla)

    for dato in datos:
        tabla.insert("", tk.END, values=(dato))


def mostrar_piezas_en_proseso(tabla, categoria):
    categoria =categoria.get()
    conn = sqlite3.connect("fadeco25.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT PIEZAS, CANTIDAD FROM proseso_de_piezas WHERE MECANIZADO = ?", (categoria,))
    datos = cursor.fetchall()
    cursor.close()

    limpiar_tabla(tabla)

    for dato in datos:
        tabla.insert("", tk.END, values=(dato))

def on_item_selected(event, treeview, label, cantidad_bruto, cant_terminada, categoria):
    selected_item = treeview.selection()
    if selected_item:
        item_text = treeview.item(selected_item[0], "values")[0]
        label.config(text=item_text)

        conn = sqlite3.connect("fadeco25.db")
        cursor = conn.cursor()
        
        tipo_categoria = categoria.get()

        if tipo_categoria == "soldar":
            if item_text == "varilla_330":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("varilla_330_carros",))
                cantidad_Terminadas = cursor.fetchone()
                
            elif item_text == "varilla_300":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("varilla_300_carros",))
                cantidad_Terminadas = cursor.fetchone()

            elif item_text == "varilla_250":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("varilla_250_carros",))
                cantidad_Terminadas = cursor.fetchone()
                
        if tipo_categoria == "balancin":
            cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
            cantidad_brutosql = cursor.fetchone()
            cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", (item_text,))
            cantidad_Terminadas = cursor.fetchone()

        if tipo_categoria == "plegadora":
            if item_text == "chapa_base_i330":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_i330",))
                cantidad_Terminadas = cursor.fetchone()

            elif item_text == "chapa_base_i300":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_i300",))
                cantidad_Terminadas = cursor.fetchone()

            elif item_text == "chapa_base_i250":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_i250",))
                cantidad_Terminadas = cursor.fetchone()

            elif item_text == "chapa_base_p330":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_p330",))
                cantidad_Terminadas = cursor.fetchone()

            elif item_text == "chapa_base_p300":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_p300",))
                cantidad_Terminadas = cursor.fetchone()   
#---------------------------------------------------------------------------------------------------------------
            elif item_text == "lateral_i330_contecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i330_contecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_i330_sintecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i330_sintecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_i300_contecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i300_contecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_i300_sintecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i300_sintecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_i250_contecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i250_contecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_i250_sintecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i250_sintecla_final",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_p330_contecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_p330_contecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_p330_sintecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_p330_sintecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_p300_contecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_p300_contecla_final",))
                cantidad_Terminadas = cursor.fetchone()   
            
            elif item_text == "lateral_p300_sintecla_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_p300_sintecla_final",))
                cantidad_Terminadas = cursor.fetchone()   

            elif item_text == "lateral_i330_eco_doblado":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", ("lateral_i330_eco_final",))
                cantidad_Terminadas = cursor.fetchone()   
#--------------------------------------------------------------------------------------------------------------
        if tipo_categoria == "plasma":
            if item_text == "lateral_i330_contecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i330_contecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 

            elif item_text == "lateral_i330_sintecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i330_sintecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_i300_contecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i300_contecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_i300_sintecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i300_sintecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_i250_contecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i250_contecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_i250_sintecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i250_sintecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() \
            
            elif item_text == "lateral_p330_contecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_p330_contecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_p330_sintecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_p330_sintecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_p300_contecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_p300_contecla_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "lateral_p300_sintecla":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_p300_sintecla_doblado",))
                cantidad_Terminadas = cursor.fetchone()

            elif item_text == "lateral_i330_eco":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("lateral_i330_eco_doblado",))
                cantidad_Terminadas = cursor.fetchone() 
#-----------------------------------------------------------------------------------------
            elif item_text == "chapa_base_i330":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_i330",))
                cantidad_Terminadas = cursor.fetchone() 
            
            elif item_text == "chapa_basedoblada_i300":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_i300",))
                cantidad_Terminadas = cursor.fetchone() 

            elif item_text == "chapa_basedoblada_i250":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_i250",))
                cantidad_Terminadas = cursor.fetchone() 
                    
            elif item_text == "chapa_basedoblada_p330":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_p330",))
                cantidad_Terminadas = cursor.fetchone() 

            elif item_text == "chapa_basedoblada_p300":
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (item_text,))
                cantidad_brutosql = cursor.fetchone()
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", ("chapa_basedoblada_p300",))
                cantidad_Terminadas = cursor.fetchone() 

        
        cursor.close()
        conn.close()

        if cantidad_brutosql and cantidad_Terminadas:
            cantidad_bruto.config(text=cantidad_brutosql[0])
            cant_terminada.config(text=cantidad_Terminadas[0])
        else:
            cantidad_bruto.config(text="No encontrado")
            cant_terminada.config(text="No encontrado")
    else:
        label.config(text="...")
        cantidad_bruto.config(text="...")
        cant_terminada.config(text="...")



def accion_actualizar(cantidad, pieza, categoria):

    actualizar_pieza = pieza.cget("text")
    actualizar_cantidad = cantidad.get()
    tipo_mecanizado = categoria.get()

    if actualizar_cantidad.strip().isdigit():
        actualizar_cantidad = int(actualizar_cantidad)

        if actualizar_cantidad < 0:
            print("La cantidad no puede ser negativa")
        else:
            confirmacion = messagebox.askyesno("Confirmar", f"Desea agregar la cantidad de {actualizar_cantidad} a {actualizar_pieza}?")

            if confirmacion:
                conn = sqlite3.connect("fadeco25.db")
                cursor = conn.cursor()

                # Obtener las cantidades actuales en ambas tablas
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_BRUTO WHERE PIEZAS = ?", (actualizar_pieza,))
                cantidad_actual_bruto = cursor.fetchone()

                if tipo_mecanizado == "soldar":
                    if actualizar_pieza == "varilla_330":
                        nueva_pieza_final = "varilla_330_carros"
                    elif actualizar_pieza == "varilla_300":
                        nueva_pieza_final = "varilla_300_carros"
                    elif actualizar_pieza == "varilla_250":
                        nueva_pieza_final = "varilla_250_carros"
                    else:
                        nueva_pieza_final = actualizar_pieza
                
                cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", (nueva_pieza_final,))
                cantidad_actual_final = cursor.fetchone()
                
                if tipo_mecanizado == "plegadora":
                    if accion_actualizar == "capa_base_i330":
                        nueva_pieza_final == "chapa_basedoblada_i330"
                    
                        cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", (nueva_pieza_final,))
                        cantidad_actual_final = cursor.fetchone()
                
                if tipo_mecanizado == "plasma":
                    cursor.execute("SELECT CANTIDAD FROM PIEZAS_FINAL WHERE PIEZAS = ?", (nueva_pieza_final,))
                    cantidad_actual_final = cursor.fetchone()
                

                if cantidad_actual_bruto is not None and cantidad_actual_final is not None:
                    cantidad_actual_bruto = cantidad_actual_bruto[0]
                    cantidad_actual_final = cantidad_actual_final[0]

                    if cantidad_actual_bruto >= actualizar_cantidad:
                        # Actualizar la tabla PIEZAS_BRUTO
                        nueva_cantidad_bruto = cantidad_actual_bruto - actualizar_cantidad
                        cursor.execute("UPDATE PIEZAS_BRUTO SET CANTIDAD = ? WHERE PIEZAS = ?", (nueva_cantidad_bruto, actualizar_pieza))

                        # Actualizar la tabla PIEZAS_FINAL
                        nueva_cantidad_final = cantidad_actual_final + actualizar_cantidad
                        cursor.execute("UPDATE PIEZAS_FINAL SET CANTIDAD = ? WHERE PIEZAS = ?", (nueva_cantidad_final, nueva_pieza_final))

                        conn.commit()
                        print("Actualización exitosa")
                    else:
                        print(f"No hay suficiente stock en bruto para {actualizar_pieza}")
                else:
                    print(f"No se encontró la pieza {actualizar_pieza} en las tablas correspondientes")
                
                conn.close()

    else:
        print("La cantidad ingresada no es un número válido")
        
    cantidad.delete(0, 'end')

def actualiar(cantidad, piezas, categoria):
    actualiza_pieza = piezas.cget("text")
    actualizar_cantidad = cantidad.get()
    tipo_mecanizado = categoria.get()

    if actualizar_cantidad.strip().isdigit():
        actualizar_cantidad = int(actualizar_cantidad)

        if actualizar_cantidad < 0:
            messagebox.showerror("ERROR", "La cantidada no puede ser negativo")
            return
        
        confimacion = messagebox.askyesno("Confirmar")

        if confimacion:
            conn = sqlite3.connect("fadeco25.db")
            cursor = conn.cursor()
            



            