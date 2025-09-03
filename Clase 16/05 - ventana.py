import tkinter as tk

# Craemos una ventana
ventana = tk.Tk()

# Redimensionar la ventana
ventana.geometry('800x500')

# Modificar el titulo
ventana.title('Nueva Ventana')

# Icono de la ventana 
ventana.iconbitmap('icono.ico')

# Evitar redimensionar la ventana
ventana.resizable(1,0)  # (ancho, alto) 0 = no, 1 = si

# Color de la ventana
ventana.configure(background='#1d2d44') # Color en hexadecimal

# Hacemos visible la ventana
ventana.mainloop()
