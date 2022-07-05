from tkinter import *

from second_window import second_window
from utils import show_graph, color_graph

weightedges = {}
vertex = []
tupedges = []



def main_window():
    root = Tk()

    root.configure()
    root.title("Головне вікно")
    root.geometry('370x540')

    pib_label = Label(root, text="ПІБ: Гончаров Павло Олексійович", font="20")
    pib_label.grid(column=1, row=1, sticky=W, padx=10, columnspan=4)

    group_label = Label(root, text="Моя група: ІО-11", font="20")
    group_label.grid(column=1, row=2, sticky=W, padx=10, columnspan=4)

    group_number_label = Label(root, text="Мій номер заліковки: 1106", font="20")
    group_number_label.grid(column=1, row=3, sticky=W, padx=10, columnspan=4)

    variant_label = Label(root, text="Мій варіант: 3", font="20")
    variant_label.grid(column=1, row=4, sticky=W, padx=10, columnspan=4)

    menu_label = Label(root, text="Меню відкриття інших вікон", font="20")
    menu_label.grid(column=1, row=5, pady=20, padx=10, columnspan=4)

    window_2 = Button(
        root,
        text="Матриця суміжнсті",
        command=lambda: second_window(weightedges, vertex, tupedges),
        bg='#bbbdc4',
        font="20",
        width=27
    )
    window_2.grid(column=1, row=6, padx=40, pady=10, columnspan=4)

    window_3 = Button(
        root,
        text="Відобразити граф",
        command=lambda: show_graph(vertex, tupedges),
        bg='#bbbdc4',
        font="20",
        width=27

    )
    window_3.grid(column=1, row=7, padx=40, pady=10, columnspan=4)

    window_4 = Button(
        root,
        text="Розфарбувати граф",
        command=lambda: color_graph(weightedges, vertex, tupedges),
        bg='#bbbdc4',
        font="20",
        width=27
    )
    window_4.grid(column=1, row=8, padx=40, pady=10, columnspan=4)

    textarea = Text(
        root,
        bg='#bbbdc4',
        font="15",
        width=30,
        height=4,
    )

    textarea.grid(column=1, row=10, pady=20, sticky=W, padx=20, columnspan=4)
    textarea.insert(END, f"Формула: I = NZK % 6 + 1\nI = {1106 % 6 + 1}\n")

    root.mainloop()
