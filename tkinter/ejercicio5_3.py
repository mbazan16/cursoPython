import tkinter as tk
from tkinter import messagebox

def cambiarRojo():
    root['bg']='red' #Igual que root['bg']='#FF0000'
def cambiarAzul():
    root['bg']='blue'
def cambiarVerde():
    root['bg']='green'

root = tk.Tk()

btn_red= tk.Button(root,text='Red',command=cambiarRojo)
btn_red.pack()
btn_blue= tk.Button(root,text='Blue',command=cambiarAzul)
btn_blue.pack()
btn_green= tk.Button(root,text='Green',command=cambiarVerde)
btn_green.pack()

root.mainloop()

