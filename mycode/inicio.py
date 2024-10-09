import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from mycode.funciones.chatbot_funcion import chat_proceso_pieza, obtener_piezas, consultar_proceso_armado

# Obtener y ordenar la lista de piezas
lista_pieza = obtener_piezas()
lista_pieza.sort()

# Crear la ventana principal
def inicio(ventana):
    
    stylo_ventana = ttk.Style()
    stylo_ventana.configure('Pestania.TNotebook', background= '#192965')
    
    ventana.columnconfigure(0, weight=1)
    # Crear pestaña de inicio
    pestania = ttk.Frame(ventana, style='Pestania.TFrame')
    ventana.add(pestania, text="Inicio")
    fondo = ttk.Style()
    fondo.configure('Pestania.TFrame', background='#192965')
    
    pestania.grid_columnconfigure(0, weight=1)

    # Título
    titulo_frame = ttk.Frame(pestania, style='Pestania.TFrame')
    titulo_frame.grid(row=0, column=0, columnspan=3, pady=20)
    titulo_frame.grid_columnconfigure(0, weight=1)
    titulo = tk.Label(titulo_frame, text="Control de Stock - Cortadoras de Fiambre", font=("Helvetica", 26, "bold"), bg='#192965' ,fg='white')
    titulo.grid(row=0, column=0, pady=10)

    # Imagen de la máquina
    imagen_frame = ttk.Frame(pestania, style='Pestania.TFrame')
    imagen_frame.grid(row=1, column=0, padx=20, sticky="nsew")
    imagen = Image.open('..\Fadeco_stock\img\Cortadora.png')
    imagen = imagen.resize((460, 460))
    imagen_tk = ImageTk.PhotoImage(imagen)

    imagen_label = tk.Label(imagen_frame, image=imagen_tk, bg='#192965')
    imagen_label.image = imagen_tk
    imagen_label.grid(row=0, column=0, columnspan=2)

    # Sección de ayuda estilo chat
    ayuda_frame = ttk.Frame(pestania, style='Pestania.TFrame')
    ayuda_frame.grid(row=1, column=2, padx=20, sticky="nsew")

    fadeco_img = Image.open('..\Fadeco_stock\img\logofadeco.png')
    fadeco_img = fadeco_img.resize((200, 75))
    fadeco_tk = ImageTk.PhotoImage(fadeco_img)

    imagen_fadeco = tk.Label(ayuda_frame, image=fadeco_tk, bg="#192965")
    imagen_fadeco.image = fadeco_tk
    imagen_fadeco.grid(row=0, column=0, columnspan=2, padx=10)

    # Combobox para consultar piezas
    tk.Label(ayuda_frame, text="¿Qué pieza necesita saber?", font=("Helvetica", 16, "bold"), bg="#192965", fg='white').grid(row=1, column=0, pady=10)
    pieza = ttk.Combobox(ayuda_frame, values=lista_pieza)
    pieza.grid(row=2, column=0, padx=5, pady=5)

    btn_pieza = tk.Button(ayuda_frame, text="Consultar Pieza", command=lambda: chat_proceso_pieza(pieza, historia))
    btn_pieza.grid(row=3, column=0, padx=5, pady=5)

    # Nuevo Combobox para consultar proceso de armado
    tk.Label(ayuda_frame, text="Instrucciones", font=("Helvetica", 16, "bold"), bg="#192965", fg='white').grid(row=1, column=1, pady=10)
    procesos_armado = ["Armado de Motores", "Pre armado", "Armado final", "Graficos", "Cierre del Mes", 
                        "Agregado de Piezas", "Mecanizado", "Proveedores", "Control-calidad", 
                        "CONSULTORIO", "Consulta Pedido", "Cierre Anual"]
    proceso = ttk.Combobox(ayuda_frame, values=procesos_armado)
    proceso.grid(row=2, column=1, padx=5, pady=5)

    btn_proceso = tk.Button(ayuda_frame, text="Consultar Proceso", command=lambda: consultar_proceso_armado(proceso, historia))
    btn_proceso.grid(row=3, column=1, padx=5, pady=5)

    # Texto para mostrar respuestas de ambas consultas
    global historia  # Definimos historia como global
    historia = tk.Text(ayuda_frame, width=50, height=17, state='disabled', wrap='word', font=("Helvetica", 12, "bold"))
    historia.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # Crear un botón para limpiar el Text
    boton_limpiar = tk.Button(ayuda_frame, text="Limpiar Texto", command=lambda: limpiar_historia(), font=("Helvetica", 12), bg="gray", fg="white")
    boton_limpiar.grid(row=5, column=0, columnspan=2, pady=10)

    # Modelos de la máquina
    modelos_frame = ttk.Frame(pestania, style='Pestania.TFrame')
    modelos_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    modelos_label = tk.Label(modelos_frame, text="Modelos de Máquinas:", font=("Helvetica",16, "bold", 'underline'), fg='white', bg="#192965")
    modelos_label.grid(row=0, column=0, pady=10)

    modelos = ["Inox 330", "Inox 300", "Inox 250", "Pintada 330", "Pintada 300", "Inox Eco"]
    for i, modelo in enumerate(modelos):
        tk.Label(modelos_frame, text=modelo, font=("Helvetica", 16), bg='#192965', fg='white').grid(row=i + 1, column=0, padx=7, pady=5)

def limpiar_historia():
    historia.config(state='normal')
    historia.delete(1.0, tk.END)  
    historia.config(state='disabled')

