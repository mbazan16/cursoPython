import tkinter as tk

# Sin establecer el parámetro master
button1 = tk.Button(text="Botón 1")
button1.pack()

# Estableciendo el parámetro master
frame = tk.Frame()
frame.pack()
button2 = tk.Button(frame, text="Botón 2")
button2.pack()

tk.mainloop()