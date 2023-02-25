import tkinter as tk
from tkinter import messagebox

def callback():
    global numbers
    numbers = []
    for entry in entries:
        try:
            numbers.append(float(entry.get()))
        except ValueError:
            messagebox.showerror("Error", "Debe introducir un número válido.")
            return

    print("Los números introducidos son:", numbers)
    window2.destroy()

def open_window():
    global entries
    global window2
    entries = []
    window2 = tk.Toplevel(root)
    window2.title("Introducir números")
    
    areas = ["Área 1", "Área 2", "Área 3", "Área 4"]
    for area in areas:
        tk.Label(window2, text=area).grid(column=0, row=areas.index(area))
        entry1 = tk.Entry(window2)
        entry2 = tk.Entry(window2)
        entry1.grid(column=1, row=areas.index(area))
        entry2.grid(column=2, row=areas.index(area))
        entries.append(entry1)
        entries.append(entry2)
    
    tk.Button(window2, text="Aceptar", command=callback).grid(column=1, row=len(areas)*2)

root = tk.Tk()
root.title("Ventana principal")

tk.Button(root, text="Comenzar", command=open_window).grid(column=0, row=0)
tk.Button(root, text="Terminar", command=root.quit).grid(column=1, row=0)

root.mainloop()
