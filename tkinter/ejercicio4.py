import tkinter as tk
from tkinter import messagebox

def mostrarDialogoWarning(texto=...):
    print('Texto:',texto,'/')
    messagebox.showwarning('Alerta',entry.get())

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(text='Mostrar Alerta',command=mostrarDialogoWarning)
btn.pack()


root.mainloop()

