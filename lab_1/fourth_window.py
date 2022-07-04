from tkinter import *

from utils import calculate_expression_w_4, save_calculation, check_sets_data


def fourth_window(v_from, v_to, set_a, set_c):
    checked_values = check_sets_data(v_from, v_to, set_a, set_c)

    if checked_values is not None:
        v_from, v_to, set_a, set_c = checked_values
        universum = set(range(v_from, v_to + 1))
        set_x = " ".join(map(str, set_c))
        set_y = " ".join(map(str, universum - set_a))
    else:
        set_x = ""
        set_y = ""

    fourth_window = Tk()

    fourth_window.configure()
    fourth_window.title('Вікно 4')
    fourth_window.geometry('500x475')

    menu_label = Label(fourth_window, text="Елементи множин A, B, C", font="30")
    menu_label.grid(column=1, row=1, pady=20, columnspan=3)

    set_a_label = Label(fourth_window, text="X", font="20")
    set_a_label.grid(column=1, row=2, sticky=W, pady=5, padx=5)

    set_b_label = Label(fourth_window, text="Y", font="20")
    set_b_label.grid(column=1, row=3, sticky=W, pady=5, padx=5)

    set_a_input = Entry(fourth_window, font="20", width="40")
    set_a_input.delete(0, END)
    set_a_input.insert(0, set_x)
    set_a_input.config(state="disabled")
    set_a_input.grid(column=2, row=2, sticky=W, pady=5, padx=5, columnspan=2)

    set_b_input = Entry(fourth_window, font="20", width="40")
    set_b_input.delete(0, END)
    set_b_input.insert(0, set_y)
    set_b_input.config(state="disabled")
    set_b_input.grid(column=2, row=3, sticky=W, pady=5, padx=5, columnspan=2)

    textarea = Text(
        fourth_window,
        bg='#D3D3D3',
        font="15",
        width=43,
        height=10,
    )
    textarea.grid(column=1, row=4, sticky=W, pady=15, padx=10, columnspan=3)

    calculate = Button(
        fourth_window,
        text="Обчислити вираз",
        command=lambda: calculate_expression_w_4(
            textarea,
            set_x,
            set_y,
        ),
        bg='#D3D3D3',
        font="15"
    )
    calculate.grid(column=2, row=5, sticky=W, pady=5)

    save = Button(
        fourth_window,
        text="Зберегти дані",
        command=lambda: save_calculation(textarea, "z"),
        bg='#bbbdc4',
        font="15"
    )
    save.grid(column=3, row=5, sticky=W, pady=5)

    fourth_window.mainloop()
