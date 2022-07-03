from random import randint
from tkinter import messagebox, END


def check_data_from_inputs(*args):
    values = []
    for key in args:
        if key[0].get() == "":
            messagebox.showerror("Помилка введення", f"{key[1]} не визначено")
            return
        else:
            try:
                values.append(int(key[0].get()))
                if key[2] == "set":
                    if int(key[0].get()) > (values[1] - values[0] + 1):
                        messagebox.showerror("Помилка введення", f"{key[1]} неможливе для універсуму")
                        return
            except:
                messagebox.showerror("Помилка введення", f"{key[1]} не число")
                return

    return values


def check_sets_data(*args):
    values = []
    for key in args:
        if key[0].get() == "":
            messagebox.showerror("Помилка введення", f"{key[1]} не визначено")
            return
        else:
            try:
                if key[2] == "number":
                    values.append(int(key[0].get()))
                elif key[2] == "set":
                    values.append(set(map(int, key[0].get().split(" "))))
            except:
                messagebox.showerror("Помилка введення", f"{key[1]} не число")
                return

    return values


def check_sets_from_inputs(*args):
    values = []
    for key in args:
        if key[0].get() == "":
            messagebox.showerror("Помилка введення", f"{key[1]} не визначено")
            return
        else:
            try:
                values.append(set(map(int, key[0].get().split(""))))
            except:
                messagebox.showerror("Помилка введення", f"{key[1]} не число")
                return

    return values


def generate_random_set(v_from, v_to, length):
    set_values = []
    while True:
        value = randint(v_from, v_to)
        if value not in set_values:
            set_values.append(value)
        if len(set_values) == length:
            break

    return set_values


def generate_random_sets(*args, **kwargs):
    checked_values = check_data_from_inputs(*args)

    if checked_values is not None:
        v_from, v_to, len_a, len_b, len_c = checked_values
    else:
        return

    sets = [i for i in [generate_random_set(v_from, v_to, j) for j in [len_a, len_b, len_c]]]

    for field, value in zip(kwargs.values(), sets):
        field.delete(0, END)
        field.insert(0, " ".join(map(str, value)))


def set_union(set_x, set_y):
    res_set = [*set_x]

    for i in set_y:
        if i not in res_set:
            res_set.append(i)

    return res_set


def calculate_expression_w_2(textarea, *args):
    checked_values = check_sets_data(*args)

    if checked_values is not None:
        v_from, v_to, set_a, set_b, set_c = checked_values
    else:
        return

    universum = set(range(v_from, v_to + 1))

    textarea.delete("0.0", END)
    textarea.insert(END, "-Починаю обчислення виразу:\n\n")
    not_set_b = universum - set_b
    textarea.insert(END, f"Крок 1\nМножини операнди:\n{universum}\n{not_set_b}\nОперація: Різниця\nРезультат:{2}\n\n")
    not_set_a = universum - set_a
    textarea.insert(END,
                    f"Крок 2\nМножини операнди:\n{universum}\n{set_a}\nОперація: Різниця\nРезультат:{not_set_a}\n\n")
    union_not_set_a_set_b = not_set_a | set_b
    textarea.insert(END,
                    f"Крок 3\nМножини операнди:\n{not_set_a}\n{set_b}\nОперація: Об'єднання\nРезультат:{union_not_set_a_set_b}\n\n")
    intersection_not_set_a_set_b = not_set_a & set_b
    textarea.insert(END,
                    f"Крок 4\nМножини операнди:\n{not_set_a}\n{set_b}\nОперація: Перетин\nРезультат:{intersection_not_set_a_set_b}\n\n")
    intersection_not_set_a_not_set_b = not_set_a & not_set_b
    textarea.insert(END,
                    f"Крок 5\nМножини операнди:\n{not_set_a}\n{not_set_b}\nОперація: Перетин\nРезультат:{intersection_not_set_a_not_set_b}\n\n")
    notintersection_not_set_a_set_b = universum - intersection_not_set_a_set_b
    textarea.insert(END,
                    f"Крок 6\nМножини операнди:\n{universum}\n{intersection_not_set_a_set_b}\nОперація: Різниця\nРезультат:{notintersection_not_set_a_set_b}\n\n")
    notintersection_not_set_a_not_set_b = universum - intersection_not_set_a_not_set_b
    textarea.insert(END,
                    f"Крок 7\nМножини операнди:\n{universum}\n{intersection_not_set_a_not_set_b}\nОперація: Різниця\nРезультат:{notintersection_not_set_a_not_set_b}\n\n")
    intersection_notintersection_not_set_a_set_b__notintersection_not_set_a_not_set_b__union_not_set_a_set_b = notintersection_not_set_a_set_b & notintersection_not_set_a_not_set_b & union_not_set_a_set_b
    textarea.insert(END,
                    f"Крок 8\nМножини операнди:\n{notintersection_not_set_a_set_b}\n{notintersection_not_set_a_not_set_b}\n{union_not_set_a_set_b}\nОперація: Перетин\nРезультат:{intersection_notintersection_not_set_a_set_b__notintersection_not_set_a_not_set_b__union_not_set_a_set_b}\n\n")
    set_d = set_c | intersection_notintersection_not_set_a_set_b__notintersection_not_set_a_not_set_b__union_not_set_a_set_b
    textarea.insert(END,
                    f"Крок 9\nМножини операнди:\n{set_c}\n{intersection_notintersection_not_set_a_set_b__notintersection_not_set_a_not_set_b__union_not_set_a_set_b}\nОперація: Об'єднання\n"
                    "Результат:{2}\n\n")
    textarea.insert(END,
                    f"Кінцевий результат:\nD={set_d}\n\n-------------------------------------------------------------------")


def calculate_expression_w_3(textarea, *args):
    checked_values = check_sets_data(*args)

    if checked_values is not None:
        set_a, set_b, set_c = checked_values
    else:
        return

    textarea.delete("0.0", END)
    textarea.insert(END, "-Починаю обчислення виразу:\n\n")
    intersection_set_a_set_b = set_a & set_b
    textarea.insert(END, f"Крок 1\nМножини операнди:\n{set_a}\n{set_b}\nОперація: Перетин\nРезультат:{intersection_set_a_set_b}\n\n")
    set_d = set_c | intersection_set_a_set_b
    textarea.insert(END, f"Крок 2\nМножини операнди:\n{set_c}\n{intersection_set_a_set_b}\nОперація: Об'єднання\nРезультат:{set_d}\n\n")
    textarea.insert(END, f"Кінцевий результат:\nD={set_d}\n\n-------------------------------------------------------------------")


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


def save_calculation(text, filename):
    f = open(f"{filename}.txt", "w")
    text2save = str(text.get(1.0, END))
    try:
        f.write(" ".join(text2save.split("\n")[-4][3:-1].split(", ")))
    except:
        messagebox.showerror("Помилка збереження", f"Обчислення не були виконані")
        return
    f.close()


def load_file(textarea, filename, label, set_var):
    f = open(f"{filename}.txt", "r")
    data_from_file = set(map(int, f.read().split(" ")))
    set_var.clear()
    set_var.extend(data_from_file)
    textarea.insert(END, f"{label} = {data_from_file}\n\n")
    f.close()


def compare_sets_values(textarea, set_d, set_d_simple):
    if not set_d and not set_d_simple:
        messagebox.showerror("Помилка порівняння", f"Множини не імпортовані")
        return

    if set_d == set_d_simple:
        textarea.insert(END, f"D={set_d}, D'={set_d_simple}. Однакові\n\n")
    else:
        textarea.insert(END, f"D={set_d}, D'={set_d_simple}. Різні\n\n")
