from tkinter import *

from utils import *

selected_males = []
selected_females = []


def second_window(array_male, array_female, aSet, bSet):
    second_window = Tk()

    second_window.configure()
    second_window.title('Вікно 2')
    second_window.geometry('550x450')

    males_label = Label(second_window, text="Чоловічі імена", font="30")
    males_label.grid(column=1, row=1, pady=10, padx=10, columnspan=2)

    males_listbox = Listbox(second_window, selectmode=MULTIPLE, height=15)
    male_set = IntVar(second_window)

    for males in array_male:
        males_listbox.insert(END, males)

    males_listbox.grid(column=1, row=2, columnspan=2, rowspan=4)

    a_male_checkbutton = Radiobutton(second_window, text="A", value=1, variable=male_set, padx=15, pady=10)
    a_male_checkbutton.grid(row=6, column=1, sticky=W)

    b_male_checkbutton = Radiobutton(second_window, text="B", value=2, variable=male_set, padx=15, pady=10)
    b_male_checkbutton.grid(row=6, column=2, sticky=W)

    def selected_item_male():
        selected_males.clear()
        for i in males_listbox.curselection():
            selected_males.append(males_listbox.get(i))

    def select_save_male():
        selected_item_male()
        save_male_name(male_set.get(), aSet, bSet, selected_males)

    save_male = Button(
        second_window,
        text="Зберегти\nв множину\nчоловіче ім'я",
        command=lambda: select_save_male(),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    save_male.grid(column=1, row=7, columnspan=2, padx=40, pady=5)

    females_label = Label(second_window, text="Жіночі імена", font="30")
    females_label.grid(column=3, row=1, pady=10, padx=10, columnspan=2)

    females_listbox = Listbox(second_window, selectmode=MULTIPLE, height=15)
    female_set = IntVar(second_window)

    for females in array_female:
        females_listbox.insert(END, females)

    females_listbox.grid(column=3, row=2, columnspan=2, rowspan=4)

    a_female_checkbutton = Radiobutton(second_window, text="A", value=1, variable=female_set, padx=15, pady=10)
    a_female_checkbutton.grid(row=6, column=3, sticky=W)

    b_female_checkbutton = Radiobutton(second_window, text="B", value=2, variable=female_set, padx=15, pady=10)
    b_female_checkbutton.grid(row=6, column=4, sticky=W)

    def selected_item_female():
        selected_females.clear()
        for i in females_listbox.curselection():
            selected_females.append(females_listbox.get(i))

    def select_save_female():
        selected_item_female()
        save_female_name(female_set.get(), aSet, bSet, selected_females)

    save_female = Button(
        second_window,
        text="Зберегти\nв множину\nжіноче ім'я",
        command=lambda: select_save_female(),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    save_female.grid(column=3, row=7, columnspan=2, padx=40, pady=5)

    save_set_a = Button(
        second_window,
        text="Зберегти\nмножину A",
        command=lambda: save_calculation(aSet, "SetA"),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    save_set_a.grid(column=5, row=2, padx=40, pady=5)

    clear_set_a = Button(
        second_window,
        text="Очистити\nмножину A",
        command=lambda: clear_file("SetA"),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    clear_set_a.grid(column=5, row=3, padx=40, pady=5)

    read_set_a = Button(
        second_window,
        text="Зчитати\nмножину A",
        command=lambda: load_file("SetA", aSet),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    read_set_a.grid(column=5, row=4, padx=40, pady=5)

    save_set_b = Button(
        second_window,
        text="Зберегти\nмножину B",
        command=lambda: save_calculation(bSet, "SetB"),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    save_set_b.grid(column=5, row=5, padx=40, pady=5)

    clear_set_b = Button(
        second_window,
        text="Очистити\nмножину B",
        command=lambda: clear_file("SetB"),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    clear_set_b.grid(column=5, row=6, padx=40, pady=5)

    read_set_b = Button(
        second_window,
        text="Зчитати\nмножину B",
        command=lambda: load_file("SetB", bSet),
        bg='#bbbdc4',
        font="10",
        width=10
    )
    read_set_b.grid(column=5, row=7, padx=40, pady=5)

    second_window.mainloop()
