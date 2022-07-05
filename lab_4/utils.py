from random import *

from tkinter import messagebox, Label, Entry, END
import networkx as nx
import matplotlib.pyplot as plt


def generate_matrix_ui(size, window, all_entries, vertex):
    try:
        int(size.get())
    except:
        messagebox.showerror("Помилка введення", "Кількість вершин не число")
        return

    vertex.extend(list(range(int(size.get()))))

    for i in all_entries:
        for j in i:
            j.destroy()

    for i in list(window.children):
        if i != "!label" and i != "!label2" and "label" in i:
            window.children[i].destroy()

    all_entries.clear()

    rows = int(size.get())
    cols = int(size.get())

    for c in range(cols):
        l = Label(window, text=str(c+1))
        l.grid(row=4, column=c+1)

    for r in range(rows):
        entries_row = []
        l = Label(window, text=str(r+1))
        l.grid(row=r+5, column=0)
        for c in range(cols):
            e = Entry(window, width=5)
            e.insert('end', 0)
            e.grid(row=r+5, column=c+1)
            entries_row.append(e)
        all_entries.append(entries_row)


def fill_matrix_ui(all_entries, edge, vertex, weightedges, tupedges):
    dekart = []
    vertex_count = int(vertex.get())
    if all_entries == []:
        messagebox.showerror("Помилка введення", "Вершин нема")
        return

    try:
        edge_count = int(edge.get())
    except TypeError:
        messagebox.showerror("Помилка введення", "Кількість ребер не число")
        return

    fac = 1
    fac_two = 1
    fac_three = 1

    for i in range(1, vertex_count+1):
        fac *= i

    for i in range(1, 3):
        fac_two *= i

    for i in range(1, vertex_count-1):
        fac_three *= i

    if edge_count > fac/(fac_two*fac_three):
        messagebox.showerror("Помилка введення", "Забагато")
        return

    for elem1 in range(vertex_count):
        for elem2 in range(vertex_count):
            if not elem1 == elem2 and (elem2, elem1) not in dekart:
                dekart.append((elem1, elem2))

    tupedges.extend(sample(dekart, edge_count))

    for elem in range(vertex_count):
        elemlist = list()
        for edge in tupedges:
            if elem == edge[0]:
                elemlist.append(edge[1])
            if elem == edge[1]:
                elemlist.append(edge[0])
        weightedges.update({elem: elemlist})

    for i in all_entries:
        for j in i:
            j.delete(0, END)
            j.insert(END, 0)

    for keey in tupedges:
        all_entries[keey[0]][keey[1]].delete(0, END)
        all_entries[keey[0]][keey[1]].insert(END, 1)
        all_entries[keey[1]][keey[0]].delete(0, END)
        all_entries[keey[1]][keey[0]].insert(END, 1)


def save_calculation(weightedges, matrix, tupedges, vertex):
    vertex.extend(list(range(len(matrix))))
    for i in range(len(matrix)):
        elemlist = list()
        for j in range(len(matrix[i])):
            if matrix[i][j].get() == "1":
                tupedges.extend([(i, j), (j, i)])
                elemlist.append(j)
        weightedges.update({i: elemlist})



    f = open("matrix.txt", "w")
    f.write("\n".join([f"{i[0]} {' '.join(map(str, i[1]))}" for i in weightedges.items()]))
    f.close()


def show_graph(vertex, tupedges):
    if not tupedges:
        messagebox.showerror("Помилка", "Матрицю не задано")
        return
    G = nx.Graph()
    G.add_nodes_from(vertex)
    G.add_edges_from(tupedges)
    nx.draw_shell(G, with_labels=True)
    plt.show()


def color_graph(weightedges, vertex, tupedges):
    if vertex == [] or tupedges == [] or weightedges == dict():
        messagebox.showerror("Помилка", "Матрицю не задано")
        return
    final = {}
    colors = ["orange", "cyan", "lime", "indigo", "yellow", "red", "blue", "green", "pink", "beige"]

    dictpower1 = dict()
    dictpower2 = dict()
    for edge in weightedges.keys():
        dictpower1[edge] = len(weightedges[edge])
    for edge in dictpower1.keys():
        power = 0
        for elem in weightedges[edge]:
            power += dictpower1[elem]
        dictpower2[edge] = [dictpower1[edge], power]
    print(dictpower2)
    sorted_power = sorted(dictpower2.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    print(sorted_power)
    sorted_list = [(elem[0], elem[1][0]) for elem in sorted_power]
    print(sorted_list)
    i = 0

    def delete_color():
        for color in colors:
            if color not in stackcolor:
                return color
        color = colors[i+1]
        colors.append(color)
        return color

    for elem in sorted_list:
        stackcolor = []
        for elem2 in weightedges[elem[0]]:
            if elem2 in final:
                stackcolor.append(final[elem2])
        color = delete_color()
        final[elem[0]] = color
    print(final)
    node_colormap = list(final.items())
    print(node_colormap)

    G = nx.Graph()
    G.add_nodes_from(vertex)
    G.add_edges_from(tupedges)
    nx.draw_shell(G, with_labels=True)
    for elem in node_colormap:
        nx.draw_networkx_nodes(G,  pos=nx.shell_layout(G), nodelist=[elem[0]], node_color=elem[1])
    plt.show()
