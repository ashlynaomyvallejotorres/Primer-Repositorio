# Vallejo Torres Ashly Naomy 
# 3°B Programacion T.M

import tkinter as tk
from tkinter import ttk

# Crear pantalla principal
ventana = tk.Tk()
ventana.title("Lista descplagable ComboBox")
ventana.geometry("300x200")

# Etiqueta de instruccion
etiqueta = tk.Label(ventana,text = " Elige una opcion:")
etiqueta.pack(pady=10)

# Crear lista desplegable (Combobox)
opciones = ["Construccion","Programacion","ARH","Contabilidad","Mecatronica","Comercio electronico","Comercio internacional y aduanas"]
ComboCarreras = ttk.Combobox(ventana,values = opciones, state = "readonly")
ComboCarreras.pack(pady=5)

# Funcion que se ejecuta al seleccionar un elemento
def mostar_seleccion(event):
    seleccion = ComboCarreras.get()
    etiqueta_rsultado.config(text=f"Seleccionaste: {seleccion}")

ComboCarreras.bird("<<ComboSelected>>", mostar_seleccion)

etiqueta_rsultado = tk.Label(ventana,text="Aun no has seleccionado nada")
etiqueta_rsultado.pack(pady=20)

ventana.mailoop()
