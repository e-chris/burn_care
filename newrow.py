#!/usr/bin/env python3

import tkinter as tk

class App:
    def new_row(self):
        new_entry = tk.Entry(root)

        self.num_rows += 1
        new_entry.grid(column=0, row=self.num_rows)

    def __init__(self):
        self.num_rows = 1
        createRow_button = tk.Button(root, text='New Row', command=self.new_row)
        createRow_button.grid()

root = tk.Tk()
app = App()

root.mainloop()
