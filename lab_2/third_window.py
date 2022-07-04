from tkinter import *

from utils import show_set, create_matrix_s, create_matrix_r


def third_window(set_a, set_b, set_female, matrix_s, matrix_r):
    third_window = Tk()

    third_window.configure()
    third_window.title('Вікно 3')
    third_window.geometry('1000x400')

    set_a_label = Label(third_window, text="Множина А", font="20")
    set_a_label.grid(column=1, row=1, pady=5)

    textarea_a = Text(
        third_window,
        bg='#D3D3D3',
        font="15",
        width=10,
        height=10,
    )
    textarea_a.grid(column=1, row=2, sticky=W, pady=10, padx=10, rowspan=20)

    show_a = Button(
        third_window,
        text="Відобразити\nмножину А",
        command=lambda: show_set(
            textarea_a,
            set_a
        ),
        bg='#D3D3D3',
        font="10"
    )
    show_a.grid(column=1, row=23, pady=5)

    set_b_label = Label(third_window, text="Множина B", font="20")
    set_b_label.grid(column=2, row=1, pady=5)

    textarea_b = Text(
        third_window,
        bg='#D3D3D3',
        font="15",
        width=10,
        height=10,
    )
    textarea_b.grid(column=2, row=2, sticky=W, pady=10, padx=10, rowspan=20)

    show_b = Button(
        third_window,
        text="Відобразити\nмножину В",
        command=lambda: show_set(
            textarea_b,
            set_b
        ),
        bg='#D3D3D3',
        font="10"
    )
    show_b.grid(column=2, row=23, pady=5)

    show_s = Button(
        third_window,
        text="Відобразити\nтаблицю S",
        command=lambda: create_matrix_s(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            third_window,
            matrix_s,
            set_female,
            show_s)
        ,
        bg='#D3D3D3',
        font="10"
    )
    show_s.grid(column=3, row=23, pady=5)

    show_r = Button(
        third_window,
        text="Відобразити\nтаблицю R",
        command=lambda: create_matrix_r(
            len(set_a),
            set_a,
            len(set_b),
            set_b,
            third_window,
            matrix_s,
            matrix_r,
            set_female,
            show_r)
        ,
        bg='#D3D3D3',
        font="10"
    )
    show_r.grid(column=70, row=23, pady=5)

    third_window.mainloop()
