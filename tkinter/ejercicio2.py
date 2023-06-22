import tkinter as tk

def incrementar():
   label['text'] += 1
    
    
def decrementar():
    label['text'] -= 1

valor=0
root = tk.Tk()

label = tk.Label(root, text=valor)
label.pack()

bt_inc= tk.Button(root,text='+', command=incrementar)
bt_inc.pack()

bt_dec= tk.Button(root,text='-', command=decrementar)
bt_dec.pack()


root.mainloop()