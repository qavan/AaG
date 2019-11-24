from vizualizer import vizualize_ver0 as visualize

from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph
ez = read_graph('g-files/for_3/MS.ini').copy()
reprint(ez)


def matrix_of_far(w):
    xw = w.copy()
    for counter, value in enumerate(xw):
        for xcounter, xvalue in enumerate(value):
            if counter != xcounter and xvalue == 0:
                xw[counter][xcounter] = float('inf')
    for k in range(len(xw)):
        for i in range(len(xw)):
            for j in range(len(xw)):
                xw[i][j] = min(xw[i][j], xw[i][k] + w[k][j])
    return xw


def dict_of_eccentricity(w):#ms
    xw = matrix_of_far(w)
    def max_finder(scope):
        max = scope[0]
        for elem in scope:
            max = elem if elem > max else max
        return max
    m = {x+1: max_finder(xw[x]) for x in range(len(xw))}
    return m


def median_by_mof(w):#ms
    xw = matrix_of_far(w)
    m = {x+1: 0 for x in range(len(xw))}
    for x in range(len(xw)):
        for y in range(len(xw[x])):
            if x != y:
                m[x+1] = m[x+1] + xw[x][y]
    return sorted(m.items(), key=lambda x: x[1])[0][0]


def radius(w):
    xw = matrix_of_far(w)
    return sorted(dict_of_eccentricity(xw).items(), key=lambda x: x[1])[0][1]


def diameter(w):
    xw = matrix_of_far(w)
    max = w[0][0]
    for x in range(len(xw)):
        for y in range(x, len(xw[x])):
            max = xw[x][y] if xw[x][y] > max else max
    return max


def central_nodes(w):
    global dict_of_eccentricity
    mof = matrix_of_far(w)
    rad = radius(mof)
    doe = dict_of_eccentricity(mof)
    m = [x for x in [list(doe.keys())[x] if rad == list(doe.values())[x] else None for x in range(len(doe))] if x != None]
    return m


def peripheral_nodes(w):
    global dict_of_eccentricity
    mof = matrix_of_far(w)
    d = diameter(mof)
    doe = dict_of_eccentricity(mof)
    m = [x for x in [list(doe.keys())[x] if d == list(doe.values())[x] else None for x in range(len(doe))] if x != None]
    return m


# print(mof_recursive_search(ms_ss(ez), 2, 6, [2], 0))
# print("1)\nМатрица расстояний: \n" + str(matrix_of_far(ez)).replace(", [", ", \n["))
# print("***")
# print("2)\nЭксцентриситет по вершинам: \n" + str(dict_of_eccentricity(ez)).replace(", ", "\n "))
# print("***")
# print("3)\nМедиана по матрице расстояний: \n" + str(median_by_mof(ez)).replace(", ", "\n "))
# print("***")
# print("4)\nРадиус:  " + str(radius(ez)) + "\nДиаметр:  " + str(diameter(ez)))
# print("***")
# print("5)\nЦентральные вершины:  " + str(central_nodes(ez)) + "\nПериферийные вершины:  " + str(peripheral_nodes(ez)))
# visualize(ms_ss(ez))


