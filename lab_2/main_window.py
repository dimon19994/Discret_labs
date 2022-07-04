from tkinter import *

from second_window import second_window
from third_window import third_window
from fourth_window import fourth_window

listSetMale = ["Іван", "Петро", "Остап", "Максим", "Олександр", "Богдан", "Свят", "Стас", "Дмитро", "Влад",
               "Олег", "Олексій", "Матвій", "Євген", "Єгор"]
listSetFemale = ["Ірина", "Марія", "Діана", "Настася", "Іванна", "Богдана", "Влада", "Вікторія", "Анна",
                 "Христина", "Софія", "Оксана", "Наталя", "Олена", "Зоя"]
aSet = []
bSet = []
matrix_s = []
matrix_r = []


def main_window():
    root = Tk()

    root.configure()
    root.title("Головне вікно")
    root.geometry('300x370')

    pib_label = Label(root, text="ПІБ: Гончаров Павло Олексійович", font="20")
    pib_label.grid(row=1, sticky=W, columnspan=2)

    group_label = Label(root, text="Моя група: ІО-11", font="20")
    group_label.grid(row=2, sticky=W, columnspan=2)

    group_number_label = Label(root, text="Мій номер у групі: 5", font="20")
    group_number_label.grid(row=3, sticky=W, columnspan=2)

    variant_label = Label(root, text="Мій варіант: 18", font="20")
    variant_label.grid(row=4, sticky=W, columnspan=2)

    menu_label = Label(root, text="Меню відкриття інших вікон", font="20")
    menu_label.grid(row=5, pady=5, columnspan=2)

    window_2 = Button(
        root,
        text="Вікно 2",
        command=lambda: second_window(listSetMale, listSetFemale, aSet, bSet),
        bg='#bbbdc4',
        font="20",
        width=20
    )
    window_2.grid(row=6, padx=40, pady=5)

    window_3 = Button(
        root,
        text="Вікно 3",
        command=lambda: third_window(
            aSet,
            bSet,
            listSetFemale,
            matrix_s,
            matrix_r),
        bg='#bbbdc4',
        font="20",
        width=20
    )
    window_3.grid(row=7, padx=40, pady=5)

    window_4 = Button(
        root,
        text="Вікно 4",
        command=lambda: fourth_window(
            aSet,
            bSet,
            matrix_s,
            matrix_r),
        bg='#bbbdc4',
        font="20",
        width=20
    )
    window_4.grid(row=8, padx=40, pady=5)

    textarea = Text(
        root,
        bg='#bbbdc4',
        font="15",
        width=30,
        height=4,
    )

    textarea.grid(row=9, sticky=W, pady=20, columnspan=2)
    textarea.insert(END, f"Формула: Z=((i+1)+G%60)%30+1\nZ={((5 + 1) + 11 % 60) % 30 + 1}\n")

    root.mainloop()
