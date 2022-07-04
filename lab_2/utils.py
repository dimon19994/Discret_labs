from random import *

from tkinter import messagebox, END, Label, Entry


def set_union(set_x, set_y):
    res_set = [*set_x]

    for i in set_y:
        if i not in res_set:
            res_set.append(i)

    return res_set


def calculate_expression_w_4(textarea, set_x, set_y):
    set_x = list(map(int, set_x.split(" ")))
    set_y = list(map(int, set_y.split(" ")))

    res_set = set_union(set_x, set_y)

    textarea.delete("0.0", END)
    textarea.insert(END, "-Починаю обчислення виразу:\n\n")
    textarea.insert(END, f"Крок 1\nМножини операнди:\n{set_x}\n{set_y}\nОперація: Об'єднання\nZ={res_set}\n\n")
    textarea.insert(END, f"-------------------------------------------------------------------")


def calculate_expression_w_5(textarea, set_x, set_y, set_var):
    set_x = set(map(int, set_x.split(" ")))
    set_y = set(map(int, set_y.split(" ")))

    res_set = (set_x | set_y)

    set_var.clear()
    set_var.extend(list(res_set))

    textarea.insert(END, "-Починаю обчислення виразу:\n\n")
    textarea.insert(END, f"Крок 1\nМножини операнди:\n{set_x}\n{set_y}\nОперація: Об'єднання\nZ={res_set}\n\n")
    textarea.insert(END, f"-------------------------------------------------------------------")


def save_male_name(setMale, aSet, bSet, selection):
    if setMale != 2:
        for male in selection:
            aSet.append(male)
    else:
        for male in selection:
            bSet.append(male)


def save_female_name(setFemale, aSet, bSet, selection):
    if setFemale != 2:
        for female in selection:
            aSet.append(female)
    else:
        for female in selection:
            bSet.append(female)


def save_calculation(text, filename):
    f = open(f"{filename}.txt", "w")
    try:
        for i in text:
            f.write(i)
            f.write("\n")
    except:
        messagebox.showerror("Помилка збереження", f"Обчислення не були виконані")
        return
    f.close()


def load_file(filename, set_var):
    f = open(f"{filename}.txt", "r")
    data_from_file = set(f.read()[:-1].split("\n"))
    set_var.clear()
    set_var.extend(data_from_file)
    f.close()


def clear_file(filename):
    open(f"{filename}.txt", "w").close()


def show_set(textarea, name_set):
    textarea.delete("0.0", END)
    textarea.insert(END, "\n".join(name_set))


def create_matrix_s(size_a, set_a, size_b, set_b, window, all_entries, set_female, show_s):
    generate_matrix_s(size_a, set_a, size_b, set_b, window, all_entries)
    form_relation_s(set_a, set_b, set_female, all_entries)
    show_s.grid(column=3 + len(all_entries) // 2 - 2, row=23, pady=5, columnspan=len(all_entries[0]))
    for i in range(len(all_entries)):
        for j in range(len(all_entries[i])):
            all_entries[i][j] = all_entries[i][j].get()


def generate_matrix_s(size_a, set_a, size_b, set_b, window, all_entries):
    all_entries.clear()

    for c in range(size_b):
        l = Label(window, text=set_b[c])
        l.grid(row=2, column=c + 4)

    for r in range(size_a):
        entries_row = []
        l = Label(window, text=set_a[r])
        l.grid(row=r + 3, column=3)
        for c in range(size_b):
            e = Entry(window, width=5)
            e.insert('end', 0)
            e.grid(row=r + 3, column=c + 4)
            entries_row.append(e)
        all_entries.append(entries_row)


def form_relation_s(setA, setB, setFemale, relationS):
    if setA != set() and setB != set():
        selection_mother = list(setA)
        selection_child = list(setB)
        while selection_mother != list():
            mother = choice(selection_mother)
            selection_mother.remove(mother)
            if mother in setFemale:
                chance = 90
                if mother in selection_child: selection_child.remove(mother)
                selection_local_child = list(selection_child)
                while randrange(0, 101) in range(chance + 1) and selection_local_child != list():
                    child = choice(selection_local_child)
                    if child != mother and (child, mother) not in relationS:
                        col = setB.index(child)
                        row = setA.index(mother)
                        relationS[row][col].delete(0, END)
                        relationS[row][col].insert(END, 1)
                        selection_child.remove(child)
                        selection_local_child.remove(child)
                        chance -= 30
                        if child in selection_mother:
                            selection_mother.remove(child)
                    else:
                        selection_local_child.remove(child)
    return relationS


def create_matrix_r(size_a, set_a, size_b, set_b, window, matrix_s, all_entries, set_female, show_r):
    generate_matrix_r(size_a, set_a, size_b, set_b, window, all_entries)
    form_relation_r(set_a, set_b, set_female, all_entries, matrix_s)
    show_r.grid(column=70 + len(all_entries) // 2 - 2, row=23, pady=5, columnspan=len(all_entries[0]))
    for i in range(len(all_entries)):
        for j in range(len(all_entries[i])):
            all_entries[i][j] = all_entries[i][j].get()


def generate_matrix_r(size_a, set_a, size_b, set_b, window, all_entries):
    all_entries.clear()

    for c in range(size_b):
        l = Label(window, text=set_b[c])
        l.grid(row=2, column=c + 70)

    for r in range(size_a):
        entries_row = []
        l = Label(window, text=set_a[r])
        l.grid(row=r + 3, column=69)
        for c in range(size_b):
            e = Entry(window, width=5)
            e.insert('end', 0)
            e.grid(row=r + 3, column=c + 70)
            entries_row.append(e)
        all_entries.append(entries_row)


def form_relation_r(setA, setB, setFemale, relationR, relationS):
    if setA != set() and setB != set() and relationS != set():
        selection_svekruha = list(setA)
        selection_nevestka = list(setB)
        while selection_svekruha != list():
            svekruha = choice(selection_svekruha)
            selection_svekruha.remove(svekruha)
            if svekruha in setFemale:
                chance = 90
                selection_local_nevestka = list(selection_nevestka)
                while selection_local_nevestka != list() and randrange(0, 101) in range(chance + 1):
                    nevestka = choice(selection_local_nevestka)
                    if nevestka != svekruha and (
                            nevestka, svekruha) not in relationR and nevestka in setFemale \
                            and (nevestka, svekruha) not in relationS and (
                            svekruha, nevestka) not in relationS:
                        col = setB.index(nevestka)
                        row = setA.index(svekruha)
                        relationR[row][col].delete(0, END)
                        relationR[row][col].insert(END, 1)
                        selection_nevestka.remove(nevestka)
                        selection_local_nevestka.remove(nevestka)
                        chance -= 20
                    else:
                        selection_local_nevestka.remove(nevestka)
    return relationS


def generate_matrix(size_a, set_a, size_b, set_b, window, all_entries):
    for i in list(window.children):
        if i != "!label" and ("label" in i or "entry" in i):
            window.children[i].destroy()
    for c in range(size_b):
        l = Label(window, text=set_b[c])
        l.grid(row=2, column=c + 4)

    for r in range(size_a):
        l = Label(window, text=set_a[r])
        l.grid(row=r + 3, column=3)
        for c in range(size_b):
            e = Entry(window, width=5)
            e.insert('end', all_entries[r][c])
            e.grid(row=r + 3, column=c + 4)


def generate_reversed_matrix(size_a, set_a, size_b, set_b, window, all_entries):
    for i in list(window.children):
        if i != "!label" and ("label" in i or "entry" in i):
            window.children[i].destroy()
    for c in range(size_a):
        l = Label(window, text=set_a[c])
        l.grid(row=2, column=c + 4)

    for r in range(size_b):
        l = Label(window, text=set_b[r])
        l.grid(row=r + 3, column=3)
        for c in range(size_a):
            e = Entry(window, width=5)
            e.insert('end', all_entries[r][c])
            e.grid(row=r + 3, column=c + 4)


def get_intersection_r_s(size_a, set_a, size_b, set_b, window, relationS, relationR, show_r):
    intersection_r_s = []
    for i in range(len(relationS)):
        intersection_r_s.append([])
        for j in range(len(relationS[0])):
            intersection_r_s[i].append(0)

    for i in range(len(relationS)):
        for j in range(len(relationS[0])):
            if relationS[i][j] == "0" or relationR[i][j] == "0":
                intersection_r_s[i][j] = "0"
            else:
                intersection_r_s[i][j] = "1"

    generate_matrix(size_a, set_a, size_b, set_b, window, intersection_r_s)
    show_r.config(text="Матриця результата операції перетину R та S")


def get_union_r_s(size_a, set_a, size_b, set_b, window, relationS, relationR, show_r):
    union_r_s = []
    for i in range(len(relationS)):
        union_r_s.append([])
        for j in range(len(relationS[0])):
            union_r_s[i].append(0)

    for i in range(len(relationS)):
        for j in range(len(relationS[0])):
            if relationS[i][j] == "0" and relationR[i][j] == "0":
                union_r_s[i][j] = "0"
            else:
                union_r_s[i][j] = "1"

    generate_matrix(size_a, set_a, size_b, set_b, window, union_r_s)
    show_r.config(text="Матриця результата операції об'єднання R та S")


def get_difference_r_s(size_a, set_a, size_b, set_b, window, relationS, relationR, show_r):
    difference_r_s = []
    for i in range(len(relationR)):
        difference_r_s.append([])
        for j in range(len(relationR[0])):
            difference_r_s[i].append(relationR[i][j])

    for i in range(len(relationS)):
        for j in range(len(relationS[0])):
            if relationS[i][j] == "1":
                difference_r_s[i][j] = "0"

    generate_matrix(size_a, set_a, size_b, set_b, window, difference_r_s)
    show_r.config(text="Матриця результата операції різниці R та S")


def get_difference_u_r(size_a, set_a, size_b, set_b, window, relationR, show_r):
    difference_u_r = []
    for i in range(len(relationR)):
        difference_u_r.append([])
        for j in range(len(relationR[0])):
            difference_u_r[i].append(1)

    for i in range(len(relationR)):
        for j in range(len(relationR[0])):
            if relationR[i][j] == "1":
                difference_u_r[i][j] = "0"

    generate_matrix(size_a, set_a, size_b, set_b, window, difference_u_r)
    show_r.config(text="Матриця результата операції різниці U та R")


def get_reversed_s(size_a, set_a, size_b, set_b, window, relationS, show_r):
    reversed_s = []
    for i in range(len(relationS[0])):
        reversed_s.append([])
        for j in range(len(relationS)):
            reversed_s[i].append(0)

    for i in range(len(relationS)):
        for j in range(len(relationS[0])):
            if relationS[i][j] == "1":
                reversed_s[j][i] = "1"

    generate_reversed_matrix(size_a, set_a, size_b, set_b, window, reversed_s)
    show_r.config(text="Матриця результата операції обернення S")
