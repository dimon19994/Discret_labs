from tkinter import *

from utils import generate_random_sets
from second_window import second_window
from third_window import third_window
from fourth_window import fourth_window
from fifth_window import fifth_window


def main_window():
    root = Tk()

    root.configure()
    root.title("Головне вікно")
    root.geometry('640x480')


    pib_label = Label(root, text="ПІБ: Гончаров Павло Олексійович", font="20")
    pib_label.grid(column=1, row=1, sticky=W, columnspan=2)

    group_label = Label(root, text="Моя група: ІО-11", font="20")
    group_label.grid(column=1, row=2, sticky=W, columnspan=2)

    group_number_label = Label(root, text="Мій номер у групі: 5", font="20")
    group_number_label.grid(column=1, row=3, sticky=W, columnspan=2)

    variant_label = Label(root, text="Мій варіант: 19", font="20")
    variant_label.grid(column=1, row=4, sticky=W, columnspan=2)

    menu_label = Label(root, text="Меню відкриття інших вікон", font="20")
    menu_label.grid(column=1, row=5, pady=20, columnspan=2)

    window_2 = Button(
        root,
        text="Вікно 2",
        command=lambda: second_window(universum_from_input, universum_to_input, set_a_input, set_b_input, set_c_input),
        bg='#bbbdc4',
        font="20"
    )
    window_2.grid(column=1, row=6, sticky=W, padx=40)

    window_3 = Button(
        root,
        text="Вікно 3",
        command=lambda: third_window(set_a_input, set_b_input, set_c_input),
        bg='#bbbdc4',
        font="20"
    )
    window_3.grid(column=2, row=6, sticky=E, padx=40)

    window_4 = Button(
        root,
        text="Вікно 4",
        command=lambda: fourth_window(
            (universum_from_input, "Початкове значення універсуму", "number"),
            (universum_to_input, "Кінцеве значення універсуму", "number"),
            (set_a_input, "Значення множини А", "set"),
            (set_c_input, "Значення множини C", "set"),
        ),
        bg='#bbbdc4',
        font="20"
    )
    window_4.grid(column=1, row=7, sticky=W, padx=40, pady=20)

    window_5 = Button(
        root,
        text="Вікно 5",
        command=lambda: fifth_window(
            (universum_from_input, "Початкове значення універсуму", "number"),
            (universum_to_input, "Кінцеве значення універсуму", "number"),
            (set_a_input, "Значення множини А", "set"),
            (set_c_input, "Значення множини C", "set"),
        ),
        bg='#bbbdc4',
        font="20"
    )
    window_5.grid(column=2, row=7, sticky=E, padx=40, pady=20)

    textarea = Text(
        root,
        bg='#bbbdc4',
        font="15",
        width=30,
        height=4,
    )

    textarea.grid(column=1, row=9, sticky=W, pady=20, columnspan=2)
    textarea.insert(END, f"Формула: Z=((i+2)+G%60)%30+1\nZ={((5+2)+11%60)%30+1}\n")

    universum_label = Label(root, text="Задання універсальної множини", font="20")
    universum_label.grid(column=3, row=1, columnspan=6)

    universum_from_label = Label(root, text="Від", font="20", width=2)
    universum_from_label.grid(column=3, row=2, sticky=W, pady=5)

    universum_to_label = Label(root, text="До", font="20", width=2)
    universum_to_label.grid(column=6, row=2, sticky=W, pady=5)

    universum_from_input = Entry(root, font="20", width="5")
    universum_from_input.grid(column=4, row=2, sticky=W, columnspan=2, pady=5)

    universum_to_input = Entry(root, font="20", width="5")
    universum_to_input.grid(column=7, row=2, sticky=W, columnspan=2, pady=5)

    universum_label = Label(root, text="Задання потужності множини", font="20")
    universum_label.grid(column=3, row=3, columnspan=6)

    universum_a_label = Label(root, text="A", font="20")
    universum_a_label.grid(column=3, row=4, sticky=W, pady=5)

    universum_b_label = Label(root, text="B", font="20")
    universum_b_label.grid(column=5, row=4, sticky=W, pady=5)

    universum_c_label = Label(root, text="C", font="20")
    universum_c_label.grid(column=7, row=4, sticky=W, pady=5)

    universum_a_input = Entry(root, font="20", width="3")
    universum_a_input.grid(column=4, row=4, sticky=W, pady=5)

    universum_b_input = Entry(root, font="20", width="3")
    universum_b_input.grid(column=6, row=4, sticky=W, pady=5)

    universum_c_input = Entry(root, font="20", width="3")
    universum_c_input.grid(column=8, row=4, sticky=W, pady=5)

    set_label = Label(root, text="Задання множини", font="20")
    set_label.grid(column=3, row=5, columnspan=6)

    set_a_label = Label(root, text="A", font="20")
    set_a_label.grid(column=3, row=6, sticky=W)

    set_b_label = Label(root, text="B", font="20")
    set_b_label.grid(column=3, row=7, sticky=W)

    set_c_label = Label(root, text="C", font="10")
    set_c_label.grid(column=3, row=8, sticky=W)

    set_a_input = Entry(root, font="20", width="20")
    set_a_input.grid(column=4, row=6, sticky=W, columnspan=5)

    set_b_input = Entry(root, font="20", width="20")
    set_b_input.grid(column=4, row=7, sticky=W, columnspan=5)

    set_c_input = Entry(root, font="20", width="20")
    set_c_input.grid(column=4, row=8, sticky=W, columnspan=5)

    random_sets = Button(
        root,
        text="Задати множину випадково",
        command=lambda: generate_random_sets(
            (universum_from_input, "Початкове значення універсуму", "number"),
            (universum_to_input, "Кінцеве значення універсуму", "number"),
            (universum_a_input, "Значення потоужності А", "set"),
            (universum_b_input, "Значення потоужності B", "set"),
            (universum_c_input, "Значення потоужності C", "set"),
            set_a=set_a_input,
            set_b=set_b_input,
            set_c=set_c_input,
        ),
        bg='#bbbdc4',
        font="20"
    )
    random_sets.grid(column=3, row=9, sticky=E, columnspan=6)

    root.mainloop()
