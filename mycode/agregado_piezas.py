import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Importar funciones para el contenido de cada pestaña
from mycode.piezas.aluminio import aluminio
from mycode.piezas.chapa import chapa
#from mycode.piezas.acero_dulce import acero_dulce
from mycode.piezas.compra import shop
from mycode.piezas.plastico import plastico
from mycode.piezas.hierro import hierro

def agregado_piezas(notebook_principal):
    
    stylo_ventana = ttk.Style()
    stylo_ventana.configure('Pestania.TNotebook', background= '#192965')
    # Cargar la imagen usando PIL y redimensionarla
    img_original = Image.open(r"C:\Fadeco_stock\img\img_aluminio.png")
    img_redimensionada = img_original.resize((90, 90))  # Ajustar el tamaño (ancho, alto)
    img_aluminio_ = ImageTk.PhotoImage(img_redimensionada)

    img_original1 = Image.open(r"C:\Fadeco_stock\img\img_chapa.png")
    img_redimensionada1 = img_original1.resize((90, 90))
    img_chapa_ = ImageTk.PhotoImage(img_redimensionada1)

    img_original2 = Image.open(r"C:\Fadeco_stock\img\img_plastico.png")
    img_redimensionada2 = img_original2.resize((90, 90))
    img_plastico_ = ImageTk.PhotoImage(img_redimensionada2)

    img_original3 = Image.open(r"C:\Fadeco_stock\img\img_shop.png")
    img_redimensionada3 = img_original3.resize((90, 90))
    img_shop_ = ImageTk.PhotoImage(img_redimensionada3)

    img_original4 = Image.open(r"C:\Fadeco_stock\img\img_hierro.png")
    img_redimensionada4 = img_original4.resize((90, 90))
    img_hierro_ = ImageTk.PhotoImage(img_redimensionada4)


    # Crear una nueva pestaña en el notebook principal
    pestania_principal = ttk.Frame(notebook_principal ,)
    notebook_principal.add(pestania_principal, text='Agregado de Piezas')

    # Crear un Frame para el contenido de las pestañas
    contenido_frame = ttk.Frame(pestania_principal,)
    contenido_frame.grid(row=0, column=2, sticky="nsew")


    # Crear un Frame para contener las pestañas verticales
    vertical_frame = ttk.Frame(pestania_principal, width=200, )
    vertical_frame.grid(row=0, column=1, sticky="ns", padx=50, pady=20)

    # Crear botones para las pestañas verticales, incluyendo la imagen redimensionada
    #boton1 = ttk.Button(vertical_frame, text="Acero", command=lambda: mostrar_contenido(contenido_frame, 'acero_dulce'))
    boton2 = ttk.Button(vertical_frame, text='Aluminio',image=img_aluminio_,compound='top', command=lambda: mostrar_contenido(contenido_frame, 'aluminio'), width=30, bootstyle="info")
    boton3 = ttk.Button(vertical_frame, text='Chapa',image=img_chapa_ ,compound='top', command=lambda: mostrar_contenido(contenido_frame, 'chapa'), width=30, bootstyle="info")
    boton4 = ttk.Button(vertical_frame, text='Shop',image=img_shop_,compound='top', command=lambda: mostrar_contenido(contenido_frame, 'shop'), width=30, bootstyle="info")
    boton5 = ttk.Button(vertical_frame, text='Plástico',image=img_plastico_,compound='top', command=lambda: mostrar_contenido(contenido_frame, 'plastico'), width=30, bootstyle="info")
    boton7 = ttk.Button(vertical_frame, text='Fundicion hierro', image=img_hierro_,compound='top', command=lambda: mostrar_contenido(contenido_frame, 'hierro'), width=30, bootstyle="info")

    # Empacar los botones verticalmente en el vertical_frame
    #boton1.grid(row=0, column=0)
    boton2.grid(row=1, column=0, pady=5)
    boton3.grid(row=2, column=0, pady=5)
    boton4.grid(row=3, column=0, pady=5)
    boton5.grid(row=4, column=0, pady=5)
    boton7.grid(row=6, column=0, pady=5)

    # Función para mostrar el contenido de la pestaña seleccionada
    def mostrar_contenido(contenido_frame, texto):
        for widget in contenido_frame.winfo_children():
            widget.destroy()  # Elimina el contenido actual
#        if texto == 'acero_dulce':
#            frame = acero_dulce(contenido_frame)
        if texto == 'aluminio':
            frame = aluminio(contenido_frame)
        elif texto == 'chapa':
            frame = chapa(contenido_frame)
        elif texto == 'shop':
            frame = shop(contenido_frame)
        elif texto == 'plastico':
            frame = plastico(contenido_frame)
        elif texto == 'hierro':
            frame = hierro(contenido_frame)
        frame.grid(row=0, column=0, sticky="nsew")

    # Mostrar el contenido de la primera pestaña por defecto
    mostrar_contenido(contenido_frame, 'chapa')

    # Configurar el peso de las filas y columnas para el contenido
    pestania_principal.grid_rowconfigure(0, weight=1)
    pestania_principal.grid_columnconfigure(1, weight=0)  # Columna de los botones
    pestania_principal.grid_columnconfigure(2, weight=1)  # Columna de contenido

    # Configurar el peso de las filas y columnas para los frames internos
    contenido_frame.grid_rowconfigure(0, weight=1)
    contenido_frame.grid_columnconfigure(0, weight=1)

    # Almacenar la imagen en el contexto de la función para evitar que sea recolectada
    pestania_principal.img_aluminio_ = img_aluminio_
    pestania_principal.img_chapa_ = img_chapa_
    pestania_principal.img_plastico_ = img_plastico_
    pestania_principal.img_shop_ = img_shop_
    pestania_principal.img_hierro_ = img_hierro_


