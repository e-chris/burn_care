#!/usr/bin/env python3

import tkinter as tk

def button_press():
	print(entry.get())

window = tk.Tk()
button = tk.Button(window, text="Test Button", command=button_press)

entry = tk.Entry(window, width=50)

button.grid()
entry.grid()

window.mainloop()
