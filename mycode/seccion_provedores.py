import tkinter as tk
from tkinter import ttk

from mycode.provedores.soldador import ventana_soldador
from mycode.provedores.carmelo import ventana_carmelo
from mycode.provedores.maxi import ventana_maxi
from mycode.provedores.pintura import ventana_pintura
from mycode.provedores.niquelado import ventana_niquelado
from mycode.provedores.afiladores import ventana_afilador

def def_provedor(notebook_principal):

    pestania_principal = ttk.Frame(notebook_principal)
    notebook_principal.add(pestania_principal, text="Provedores")

    contenido_frame = ttk.Frame(pestania_principal)
    contenido_frame.grid(row=0, column=2, sticky="nsew")

    vertical_frame = ttk.Frame(pestania_principal, width=200)
    vertical_frame.grid(row=0, column=1, sticky="ns", padx=50)

    soldador = ttk.Button(vertical_frame, text="Soldador", padding=20, width=10, command= lambda: mostrar_contenido(contenido_frame, "soldadura"))
    soldador.grid(row=1, column=0, pady=5)

    carmerlo = ttk.Button(vertical_frame, text="Carmelo",padding=20, width=10, command= lambda: mostrar_contenido(contenido_frame, "carmelo"))
    carmerlo.grid(row=2, column=0, pady=5)

    maxi = ttk.Button(vertical_frame, text="Maxi",padding=20, width=10, command= lambda: mostrar_contenido(contenido_frame, "maxi"))
    maxi.grid(row=3, column=0, pady=5)

    pintura = ttk.Button(vertical_frame, text="Pintura",padding=20, width=10, command= lambda: mostrar_contenido(contenido_frame, "pintura"))
    pintura.grid(row=4, column=0, pady=5)

    niquelado = ttk.Button(vertical_frame, text="Niqueado",padding=20,width=10, command= lambda: mostrar_contenido(contenido_frame , "niquelado"))
    niquelado.grid(row=5, column=0, pady=5)

    afiladores = ttk.Button(vertical_frame, text="Afilador",padding=20, width=10, command= lambda: mostrar_contenido(contenido_frame, "afiladores"))
    afiladores.grid(row=6, column=0, pady=5)





    def mostrar_contenido(contenido_frame, texto):
        for widget in contenido_frame.winfo_children():
            widget.destroy()
        if texto == "soldadura":
            frame = ventana_soldador(contenido_frame)
        elif texto == "carmelo":
            frame = ventana_carmelo(contenido_frame)
        elif texto == "maxi":
            frame = ventana_maxi(contenido_frame)
        elif texto == "pintura":
            frame = ventana_pintura(contenido_frame)
        elif texto == "niquelado":
            frame = ventana_niquelado(contenido_frame)
        elif texto == "afiladores":
            frame = ventana_afilador(contenido_frame)

        frame.grid(row=0, column=0 , sticky="nsew")

    
    mostrar_contenido(contenido_frame, "soldadura")

