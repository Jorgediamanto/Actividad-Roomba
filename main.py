import tkinter as tk
from tkinter import messagebox

def callback():
    global numbers
    numbers = [
        [float(entries[0].get()), float(entries[1].get())],
        [float(entries[2].get()), float(entries[3].get())],
        [float(entries[4].get()), float(entries[5].get())],
        [float(entries[6].get()), float(entries[7].get())]
    ]
    print("Los números introducidos son:", numbers)
    print("Area 1 :"+str(numbers[0][0]*numbers[0][1])+"Area 2 :"+str(numbers[1][0]*numbers[1][1])+"Area 3 :"+str(numbers[2][0]*numbers[2][1])+"Area 4 :"+str(numbers[3][0]*numbers[3][1]))
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
