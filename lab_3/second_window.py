from tkinter import *

from utils import generate_matrix_ui, fill_matrix_ui, save_calculation

matrix = []


def second_window(weightedges, vertex):
    second_window = Tk()

    second_window.configure()
    second_window.title('Вікно 2')
    second_window.geometry('360x515')

    vertex_count_label = Label(second_window, text="Кількість вершин", font="20")
    vertex_count_label.grid(column=1, row=1, pady=5, padx=10, columnspan=5)

    edge_number_label = Label(second_window, text="Кількість ребер", font="20")
    edge_number_label.grid(column=6, row=1, pady=5, padx=10, columnspan=1000)

    vertex_count_input = Entry(second_window, font="20", width="12")
    vertex_count_input.grid(column=1, row=2, pady=5, padx=10, columnspan=5)

    edge_number_input = Entry(second_window, font="20", width="12")
    edge_number_input.grid(column=6, row=2, pady=5, padx=10, columnspan=1000)

    vertex_set_button = Button(
        second_window,
        text="Задати",
        command=lambda: generate_matrix_ui(
            vertex_count_input,
            second_window,
            matrix,
            vertex
        ),
        bg='#D3D3D3',
        font="15",
        width=12
    )
    vertex_set_button.grid(column=1, row=3, pady=5, padx=10, columnspan=5)

    edge_set_button = Button(
        second_window,
        text="Задати",
        command=lambda: fill_matrix_ui(matrix, edge_number_input, vertex_count_input, weightedges),
        bg='#bbbdc4',
        font="15",
        width=12
    )
    edge_set_button.grid(column=6, row=3, pady=5, padx=5, columnspan=1000)

    save_matrix = Button(
        second_window,
        text="Зберегти матрицю",
        command=lambda: save_calculation(weightedges),
        bg='#bbbdc4',
        font="15",
    )
    save_matrix.grid(column=1, row=1000, pady=5, padx=10, columnspan=1000)

    second_window.mainloop()
