import tkinter as tk

def mostrarMensaje():
    print('Hola Mundo')

root = tk.Tk()

bt = tk.Button(root,text='Pulsame',command=mostrarMensaje)
bt.pack()

root.mainloop()