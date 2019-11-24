import itertools

from vizualizer import vizualize_ver0 as visualize

from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph

ez = read_graph('files/for_2/MS.ini').copy()


def weight_of_nodes(w):
    m = [0 for x in range(len(w))]
    for counter, elem in enumerate(w):
        for x in range(counter, len(elem)):
            if elem[x] == 1:
                m[counter] = m[counter] + 1
                m[x] = m[x] + 1
    return m


def isolated_nodes(w):
    m = []
    for counter, elem in enumerate(w):
        m.append(counter+1) if 1 not in elem else ...
    return len(m), m


def hanged_nodes(w):
    m = []
    for counter, elem in enumerate(w):
        if elem.count(1) == 1:
            m.append(counter+1)
    return len(m), m


def edges_count(w):
    m = 0
    for counter, elem in enumerate(w):
        for x in range(counter, len(elem)):
             m = m + 1 if elem[x] == 1 else m
    return m


def reverse_graphs_node_count(w):
    for counter, elem in enumerate(w):
        for xcounter, xelem in enumerate(elem):
            w[counter][xcounter] = 0 if w[counter][xcounter] == 1 else 1
    return edges_count(w)


def give_adjacent_node(node, w):
    m = []
    try:
        for counter, elem in enumerate(w[node-1]):
            m.append(counter+1) if elem == 1 else ...
        return 'нет' if m == [] else m
    except IndexError:
        return "!ОШИБКА! неправильно данная вершина"


def get_kirchhoff_matrix(w):
    weight_of_nodes_list = weight_of_nodes(w)
    m = [[weight_of_nodes_list[x] if x == y else None for y in range(len(w))] for x in range(len(w))]
    for counter, elem in enumerate(w):
        adjacent_node_list = give_adjacent_node(counter+1, w)
        if type(adjacent_node_list) == list:
            for xelem in adjacent_node_list:
                m[counter][int(xelem-1)], m[int(xelem-1)][counter] = -1, -1
    for counter, elem in enumerate(m):
        for xcounter, xelem in enumerate(elem):
            m[counter][xcounter] = 0 if xelem == None and counter != xcounter else m[counter][xcounter]
    return m


def delete_node_and_calculate_edges_count(node, w):
    try:
        for counter, elem in enumerate(w[node-1]):
            w[node-1][counter],w[counter][node-1] = 0, 0
        count_of_edges = edges_count(w)
        return w, count_of_edges
    except IndexError:
        return "!ОШИБКА!", "!ОШИБКА! неправильно данная вершина для удаления"


# visualize(ms_ss(ez))
# print("2 Степени вершин: " + str(weight_of_nodes(ez)))
# print("3 Изолированные вершины (номера и количество): " + str(isolated_nodes(ez)[1]) + " " + str(isolated_nodes(ez)[0]))
# print("4 Висячие вершины (номера и количество): " + str(hanged_nodes(ez)[1]) + " " + str(hanged_nodes(ez)[0]))
# print("5 Количество ребер в графе: " + str(edges_count(ez)))
# print("6 Количество ребер в дополнении графа: " + str(reverse_graphs_node_count(ez)))
# node_for_6 = 3
# print("7 Вершины смежные с " + str(node_for_6) + " : " + str(give_adjacent_node(node_for_6, ez)))
# print("8 Матрица Кирхгофа: \n" + str(get_kirchhoff_matrix(ez)).replace(", [", ", \n["))
# node_for_9 = 3
# print("9 Матрица смежности при удалении вершины " + str(node_for_9) + " с кол-вом рёбер " +
#       str(delete_node_and_calculate_edges_count(node_for_9, ez)[1]) + "\n" +
#       str(delete_node_and_calculate_edges_count(node_for_9, ez)[0]).replace(", [", ", \n["))
#

def in_da_numeric(count, offset, w):
    start = [x+offset for x in range(len(list(w.keys())))]
    if count >= 2 and count <= len(list(itertools.permutations(list(start)))):
        pretemp = []  # наборы из 4 номеров вершин
        for elem in list(itertools.permutations(list(start))):
            pretemp.append(list(elem))
        megatemp = []  # список словарей для комбинаций
        for g in range(count):
            megatemp.append({pretemp[g][count]: elem[0][0] for count, elem in enumerate(w.items())})
        # print(megatemp)
        xwx = []
        for elemx in megatemp:
            xw = {}
            for elem, value in w.items():
                counter = 0
                for xvalue in value:
                    for zelem, zvalue in elemx.items():
                            value[counter] = zelem if zvalue == value[counter] else value[counter]
                    counter += 1
            xw = {}
            for elem, value in w.items():
                for zelem, zvalue in elemx.items():
                    xw.update({zelem: value}) if elem == zvalue else ...
            xwx.append(xw)
        return xwx
    else:
        temp = {count+offset: elem[0][0] for count, elem in enumerate(w.items())}
        for elem, value in w.items():
            counter = 0
            for xvalue in value:
                for zelem, zvalue in temp.items():
                        value[counter] = zelem if zvalue == value[counter] else value[counter]
                counter += 1
        xw = {}
        for elem, value in w.items():
            for zelem, zvalue in temp.items():
                xw.update({zelem: value}) if elem == zvalue else ...
        return xw


def sum_of_graphs(w1, w2):
    xw = {}
    if len(w1) > len(w2):
        for elem, value in w1.items():
            try:
                xw.update({elem: list(set(value + w2[elem]))})
            except:
                xw.update({elem: value})
    elif len(w1) < len(w2):
        for elem, value in w2.items():
            try:
                xw.update({elem: list(set(value + w1[elem]))})
            except:
                xw.update({elem: value})
    return xw


def cross_of_graphs(w1, w2):  # adjacent list
    def crossingover(a, b):
        c = []
        for i in a:
            if i in c:
                continue
            for j in b:
                if i == j:
                    c.append(i)
                    break
        c.sort()
        return c
    xw = {}
    if len(w1) > len(w2):
        for elem, value in w1.items():
            try:
                if elem in list(w2.keys()):
                    xw.update({elem: crossingover(value, w2[elem])})
            except:
                print('some err?')
    elif len(w1) < len(w2):
        for elem, value in w2.items():
            try:
                if elem in w1.keys():
                    xw.update({elem: crossingover(value, w1[elem])})
            except:
                print('some err?')
    return xw


# reprint(ez)
# ez_test_visual ={1: [2, 6], 2: [1, 3], 3: [2, 4, 5], 4: [3], 5: [3, 6], 6: [1, 5], 7: [8, 9]}
# visualize(ez_test_visual)
# reprint(ms_ss(ez))

# ez_test = {
#     "X": ["W", "Y", "Z"],
#     "Y": ["X", "W", "Z"],
#     "Z": ["X", "Y", "W"],
#     "W": ["X", "Y", "Z"]
#     , "R": []
# }
# count_of_combination = 1
# ez_test = in_da_numeric(count_of_combination, 2, ez_test)
# # print(ez_test)
# if type(ez_test) == dict:
#     print("\n10.1 Объединение графов:")
#     result = sum_of_graphs(ms_ss(ez), ez_test)
#     visualize(result)
#     reprint(result)
#     #
#     # print("\n10.2 Пересечение графов:")
#     # result = cross_of_graphs(ms_ss(ez), ez_test)
#     # visualize(result)
#     # reprint(result)
# elif type(ez_test) == list:
#     for elem in ez_test:
#         print("\n10.1 Объединение графов:")
#         result = sum_of_graphs(ms_ss(ez), elem)
#         visualize(result)
#         reprint(result)
#         #
#         # print("\n10.2 Пересечение графов:")
#         # result = cross_of_graphs(ms_ss(ez), elem)
#         # visualize(result)
#         # reprint(result)
