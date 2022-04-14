import tkinter as tk

window = tk.Tk()
btn = tk.Button(window, text="Click Me")

#Nombre de la ventana
window.title("Proyecto. NEDW")
window.geometry('500x500')

#Texto a mostrar en el interior
lbl = tk.Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn.grid(column=1, row=0)

#Permite que se muestre la ventana
window.mainloop()