import numpy as np
from tkinter import *


def generate_matrix_ui(size, window, all_entries):
    for i in all_entries:
        for j in i:
            j.destroy()

    for i in list(window.children):
        if i != "!label" and i != "!label2" and "label" in i:
            window.children[i].destroy()

    all_entries.clear()

    rows = int(size.get())
    cols = int(size.get())

    for c in range(cols):
        l = Label(window, text=str(c+1))
        l.grid(row=4, column=c+1)

    for r in range(rows):
        entries_row = []
        l = Label(window, text=str(r+1))
        l.grid(row=r+5, column=0)
        for c in range(cols):
            e = Entry(window, width=5)
            e.insert('end', 0)
            e.grid(row=r+5, column=c+1)
            entries_row.append(e)
        all_entries.append(entries_row)


def fill_matrix_ui(all_entries):
    pass
