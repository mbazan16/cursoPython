import tkinter as tk
from tkinter import messagebox

def cambiarColor(color):
    root['bg']=color

root = tk.Tk()

btn_red= tk.Button(root,text='Red',command=lambda:cambiarColor('#FF0000'))
btn_red.pack()
btn_blue= tk.Button(root,text='Blue',command=lambda:cambiarColor('#0000FF'))
btn_blue.pack()
btn_green= tk.Button(root,text='Green',command=lambda:cambiarColor('#00FF00'))
btn_green.pack()

root.mainloop()

