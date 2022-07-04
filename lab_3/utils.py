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


def fill_matrix_ui(all_entries, edge, vertex, weightedges):
    dekart = []
    edges = []
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

    edges.extend(sample(dekart, edge_count))

    for edge in edges:
        weight = randrange(1, 10)
        weightedges.update({(edge[0], edge[1]): weight, (edge[1], edge[0]): weight})

    for keey in weightedges.keys():
        all_entries[keey[0]][keey[1]].delete(0, END)
        all_entries[keey[0]][keey[1]].insert(END, weightedges[keey])


def save_calculation(weightedges):
    f = open("matrix.txt", "w")
    f.write("\n".join([f"{i[0][0]} {i[0][1]} {i[1]}" for i in weightedges.items()]))
    f.close()


def show_graph(weightedges, vertex):
    if not weightedges:
        messagebox.showerror("Помилка", "Матрицю не задано")
        return
    G = nx.Graph()
    G.add_nodes_from(vertex)
    G.add_edges_from(weightedges.keys())
    nx.draw_shell(G, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels=weightedges, label_pos=0.1)
    plt.show()


def topological_sort(pint_from_input, pint_to_input, weightedges, vertex):
    try:
        src = int(pint_from_input.get())
        if src not in vertex:
            messagebox.showerror("Помилка введення", "Не існуе!")
            return
    except ValueError:
        messagebox.showerror("Помилка введення", "Початкове значення вершини не число")
        return
    try:
        dest = int(pint_to_input.get())
        if dest not in vertex:
            messagebox.showerror("Помилка введення", "Не існуе!")
            return
    except ValueError:
        messagebox.showerror("Помилка введення", "Кінцеве значення вершини не число")
        return

    dist = [float("Inf")] * len(vertex)
    prev = [None] * len(vertex)
    dist[src] = 0
    for i in range(len(vertex) - 1):
        for key in weightedges.keys():
            if dist[key[0]] + weightedges[key] < dist[key[1]]:
                dist[key[1]] = dist[key[0]] + weightedges[key]
                prev[key[1]] = key[0]
            if dist[key[1]] + weightedges[key] < dist[key[0]]:
                dist[key[0]] = dist[key[1]] + weightedges[key]
                prev[key[0]] = key[1]

    curr = dest
    path = []
    while curr is not None:
        path.append(curr)
        curr = prev[curr]

    pathedges = []
    for i in range(len(path) - 1):
        pathedges.append((path[i], path[i + 1]))
    print(pathedges)
    colored_nodes = [src, dest]

    G = nx.Graph()
    G.add_nodes_from(vertex)
    G.add_edges_from(weightedges.keys())
    nx.draw_shell(G, with_labels=True)
    nx.draw_networkx_nodes(G, pos=nx.shell_layout(G), nodelist=colored_nodes, node_color="Yellow")
    nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels=weightedges, label_pos=0.1)
    nx.draw_networkx_edges(G, pos=nx.shell_layout(G), edgelist=pathedges, edge_color="yellow")
    plt.show()
