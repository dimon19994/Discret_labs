from tkinter import *

from utils import (
    calculate_expression_w_5,
    check_sets_data,
    load_file,
    compare_sets_values,
)

set_d = []
set_d_simple = []
set_z = []
set_z_simple = []


def fifth_window(v_from, v_to, set_a, set_c):
    checked_values = check_sets_data(v_from, v_to, set_a, set_c)

    if checked_values is not None:
        v_from, v_to, set_a, set_c = checked_values
        universum = set(range(v_from, v_to + 1))
        set_x = " ".join(map(str, set_c))
        set_y = " ".join(map(str, universum - set_a))
    else:
        set_x = ""
        set_y = ""

    second_window = Tk()

    second_window.configure()
    second_window.title('Вікно 5')
    second_window.geometry('500x580')

    menu_label = Label(second_window, text="Елементи множин A, B, C", font="30")
    menu_label.grid(column=1, row=1, pady=20, columnspan=3)

    set_a_label = Label(second_window, text="X", font="20")
    set_a_label.grid(column=1, row=2, sticky=W, pady=5, padx=5)

    set_b_label = Label(second_window, text="Y", font="20")
    set_b_label.grid(column=1, row=3, sticky=W, pady=5, padx=5)

    set_a_input = Entry(second_window, font="20", width="40")
    set_a_input.delete(0, END)
    set_a_input.insert(0, set_x)
    set_a_input.config(state="disabled")
    set_a_input.grid(column=2, row=2, sticky=W, pady=5, padx=5, columnspan=2)

    set_b_input = Entry(second_window, font="20", width="40")
    set_b_input.delete(0, END)
    set_b_input.insert(0, set_y)
    set_b_input.config(state="disabled")
    set_b_input.grid(column=2, row=3, sticky=W, pady=5, padx=5, columnspan=2)

    textarea = Text(
        second_window,
        bg='#D3D3D3',
        font="15",
        width=43,
        height=10,
    )
    textarea.grid(column=1, row=4, sticky=W, pady=15, padx=10, columnspan=3)

    load_d = Button(
        second_window,
        text="Імпортувати D",
        command=lambda: load_file(textarea, "d", "D", set_d),
        bg='#D3D3D3',
        font="15"
    )
    load_d.grid(column=2, row=5, sticky=W, pady=5)

    load_d_simple = Button(
        second_window,
        text="Імпортувати D'",
        command=lambda: load_file(textarea, "d_simple", "D'", set_d_simple),
        bg='#bbbdc4',
        font="15"
    )
    load_d_simple.grid(column=3, row=5, sticky=W, pady=5)

    load_z = Button(
        second_window,
        text="Імпортувати Z",
        command=lambda: load_file(textarea, "z", "Z", set_z),
        bg='#D3D3D3',
        font="15"
    )
    load_z.grid(column=2, row=6, sticky=W, pady=5)

    calculate = Button(
        second_window,
        text="Обчислити Z'",
        command=lambda: calculate_expression_w_5(
            textarea,
            set_x,
            set_y,
            set_z_simple
        ),
        bg='#bbbdc4',
        font="15"
    )
    calculate.grid(column=3, row=6, sticky=W, pady=5)

    compare_d_d_simple = Button(
        second_window,
        text="Порівнять D та D'",
        command=lambda: compare_sets_values(textarea, set_d, set_d_simple),
        bg='#D3D3D3',
        font="15"
    )
    compare_d_d_simple.grid(column=2, row=7, sticky=W, pady=5)

    compare_z_z_simple = Button(
        second_window,
        text="Порівнять Z та Z'",
        command=lambda: compare_sets_values(textarea, set_z, set_z_simple),
        bg='#bbbdc4',
        font="15"
    )
    compare_z_z_simple.grid(column=3, row=7, sticky=W, pady=5)

    second_window.mainloop()
