#!/usr/bin/env python3

import tkinter as tk

#fields = ['Direction', 'Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol', 'Action']

def button_press():
	print(a1)

window = tk.Tk()
button = tk.Button(window, text="Test Button", command=button_press).grid()

entry1 = tk.Entry(window, width=50)
entry1.grid()

window.mainloop()
