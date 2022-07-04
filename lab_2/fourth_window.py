from tkinter import *

from utils import *


def test():
    pass


def fourth_window(set_a, set_b, relationS, relationR):
    fourth_window = Tk()

    fourth_window.configure()
    fourth_window.title('Вікно 4')
    fourth_window.geometry('800x800')

    menu_label = Label(fourth_window, text="", font="10")
    menu_label.grid(column=1, row=1, pady=20, sticky=E)

    intersection = Button(
        fourth_window,
        text="Перетин R та S",
        command=lambda: get_intersection_r_s(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            fourth_window,
            relationS,
            relationR,
            menu_label
        ),
        bg='#D3D3D3',
        font="15"
    )
    intersection.grid(column=1, row=70, pady=5)

    union = Button(
        fourth_window,
        text="Об'єднання R та S",
        command=lambda: get_union_r_s(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            fourth_window,
            relationS,
            relationR,
            menu_label
        ),
        bg='#D3D3D3',
        font="15"
    )
    union.grid(column=1, row=71, pady=5)

    difference = Button(
        fourth_window,
        text="Різниця R та S",
        command=lambda: get_difference_r_s(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            fourth_window,
            relationS,
            relationR,
            menu_label
        ),
        bg='#D3D3D3',
        font="15"
    )
    difference.grid(column=1, row=72, pady=5)

    difference_u = Button(
        fourth_window,
        text="Різниця U та R",
        command=lambda: get_difference_u_r(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            fourth_window,
            relationR,
            menu_label
        ),
        bg='#D3D3D3',
        font="15"
    )
    difference_u.grid(column=1, row=73, pady=5)

    reversed_s = Button(
        fourth_window,
        text="Обернення S",
        command=lambda: get_reversed_s(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            fourth_window,
            relationS,
            menu_label
        ),
        bg='#D3D3D3',
        font="15"
    )
    reversed_s.grid(column=1, row=74, pady=5)

    fourth_window.mainloop()
