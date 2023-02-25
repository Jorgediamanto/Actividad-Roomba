import tkinter as tk

# Creamos la ventana principal
root = tk.Tk()

# Creamos el botón
button = tk.Button(root, text="Cerrar ventana", command=root.destroy)
button.pack()

# Mostramos la ventana
root.mainloop()
