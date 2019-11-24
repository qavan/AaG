from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph
from utilites import matrix_of_far as mof
from utilites import weight_of_nodes as won

ez = read_graph('g-files/for_4/MS.ini').copy()


def weiner_index(w):
    xw, xm = mof(w), 0
    for x in range(len(xw)):
        for y in range(x, len(xw)):
            xm += xw[x][y]
    return xm


def randic_index(w):
    weight_matrix, xm = won(w), 0
    for x in range(len(w)):
        for y in range(x, len(w)):
            if w[x][y] == 1:
                xm += 1/((weight_matrix[x]*weight_matrix[y])**(1/2))
    return xm



def mini_maxi(w):
    import itertools
    maxi, mini = float('-inf'), float('inf')
    xw = []
    for elem in list(itertools.permutations(w)):
        temp = ""
        for xelem in elem:
            temp = temp + str("".join(str(x) for x in xelem))
        xw.append(temp)
    # print(len(xw))
    for elem in xw:
        pseudoelem = int(elem, 2)
        if pseudoelem > maxi:
            maxi = pseudoelem
        if pseudoelem < mini:
            mini = pseudoelem
    return mini, maxi


# def mini_maxi2(w):
#     xw = []
#     for elem in w:
#         for xelem in elem:
#             xw.append(str(xelem))
#     forMini = xw
#     forMini.sort()
#     forMaxi = forMini.copy()
#     pseudoMini = "".join(forMini)
#     pseudoMaxi = "".join(forMaxi)
#     print(pseudoMaxi)
#     maxi = 0
#     for counter, elem in enumerate(pseudoMaxi):
#         if elem != '0':
#             maxi += 2**int(counter)
#     mini = int(pseudoMini, 2)
#     return mini, maxi

# visualize(ms_ss(ez))
# print("X1\nМатрица смежности: \n" + str(ez).replace(", [", ", \n["))
# print("X2\nМатрица расстояний: \n" + str(mof(ez)).replace(", [", ", \n["))
# wi = str(weiner_index(ez))
# print("1)\nИндекс Винера: " + wi)
# ri = str(randic_index(ez))
# print("2)\nИндекс Рандича: " + ri)

# p3 = mini_maxi(ez.copy())
# print("3)\nМини-код : " + str(p3[0]) + "\nМакси-код: " + str(p3[1]))

# p31 = mini_maxi2(ez.copy())
# print("3.1)\nМини-код : " + str(p31[0]) + "\nМакси-код: " + str(p31[1]))
