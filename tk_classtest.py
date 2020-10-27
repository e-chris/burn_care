#!/usr/bin/env python3

import tkinter as tk

class ButtonEntry():
    def __init__(self, window):
        self.entry_var=""

        startLabel = tk.Label(window, text="User input: ")
        self.startEntry = tk.Entry(window)

        startLabel.pack()
        self.startEntry.pack()
        self.startEntry.focus_set()

        plotButton= tk.Button(window, text="plot",
                           command=self.hi).pack()

    def hi(self):
        self.entry_var = self.startEntry.get()
        print("inside class", self.entry_var)

if __name__ == "__main__":
    window = tk.Tk()
    BE = ButtonEntry(window)
    window.mainloop()

    print("\nBack in __main__")
    print(BE.entry_var)
