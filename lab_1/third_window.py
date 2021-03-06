from tkinter import *

from utils import calculate_expression_w_3, save_calculation


def third_window(set_a, set_b, set_c):
    third_window = Tk()

    third_window.configure()
    third_window.title('Вікно 3')
    third_window.geometry('500x515')

    menu_label = Label(third_window, text="Елементи множин A, B, C", font="30")
    menu_label.grid(column=1, row=1, pady=20, columnspan=3)

    set_a_label = Label(third_window, text="A", font="20")
    set_a_label.grid(column=1, row=2, sticky=W, pady=5, padx=5)

    set_b_label = Label(third_window, text="B", font="20")
    set_b_label.grid(column=1, row=3, sticky=W, pady=5, padx=5)

    set_c_label = Label(third_window, text="C", font="20")
    set_c_label.grid(column=1, row=4, sticky=W, pady=5, padx=5)

    set_a_input = Entry(third_window, font="20", width="40")
    set_a_input.delete(0, END)
    set_a_input.insert(0, set_a.get())
    set_a_input.config(state="disabled")
    set_a_input.grid(column=2, row=2, sticky=W, pady=5, padx=5, columnspan=2)

    set_b_input = Entry(third_window, font="20", width="40")
    set_b_input.delete(0, END)
    set_b_input.insert(0, set_b.get())
    set_b_input.config(state="disabled")
    set_b_input.grid(column=2, row=3, sticky=W, pady=5, padx=5, columnspan=2)

    set_c_input = Entry(third_window, font="20", width="40")
    set_c_input.delete(0, END)
    set_c_input.insert(0, set_c.get())
    set_c_input.config(state="disabled")
    set_c_input.grid(column=2, row=4, sticky=W, pady=5, padx=5, columnspan=2)

    textarea = Text(
        third_window,
        bg='#D3D3D3',
        font="15",
        width=43,
        height=10,
    )
    textarea.grid(column=1, row=5, sticky=W, pady=15, padx=10, columnspan=3)

    calculate = Button(
        third_window,
        text="Обчислити вираз",
        command=lambda: calculate_expression_w_3(
            textarea,
            (set_a, "Значення множини А", "set"),
            (set_b, "Значення множини B", "set"),
            (set_c, "Значення множини C", "set"),
        ),
        bg='#D3D3D3',
        font="15"
    )
    calculate.grid(column=2, row=6, sticky=W, pady=5)

    save = Button(
        third_window,
        text="Зберегти дані",
        command=lambda: save_calculation(textarea, "d_simple"),
        bg='#bbbdc4',
        font="15"
    )
    save.grid(column=3, row=6, sticky=W, pady=5)

    third_window.mainloop()
