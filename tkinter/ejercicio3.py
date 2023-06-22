import tkinter as tk

def mostrarMensaje():
    label['text']=entry.get()

root = tk.Tk()

entry = tk.Entry(root,)
entry.pack()

bt = tk.Button(root,text='Mostrar',command=mostrarMensaje)
bt.pack()

label = tk.Label(root)
label.pack()


root.mainloop()