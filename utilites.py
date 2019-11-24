import re
import configparser


def depth_first_search_printer(w, cur_node, visited):
    for node in w[cur_node]:
        if node not in visited:
            print(node)
            visited.append(node)
            depth_first_search_printer(w, node, visited)


def reprint(w):
    if type(w) == list:
        for elem in w:
            print(elem)
    elif type(w) == dict:
        for elem, value in w.items():
            print(str(elem) + ":" + str(value))


def ms_ss(w):
    m = {}
    for counter, elem in enumerate(w):
        L = []
        for xcounter, xelem in enumerate(elem):
            if xelem == 1:
                L.append(xcounter+1)
        m.update({counter+1: L})
    return m


def ss_ms(w):
    m = [[0 for x in range(len(w))] for y in range(len(w))]
    counter = 0
    for elem, value in w.items():
        if value !=[]:
            for xelem in value:
                m[counter][xelem-1]=1
        counter += 1
    return m


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


def weight_of_nodes(w):
    m = [0 for x in range(len(w))]
    for counter, elem in enumerate(w):
        for x in range(counter, len(elem)):
            if elem[x] == 1:
                m[counter] = m[counter] + 1
                m[x] = m[x] + 1
    return m


def give_adjacent_node(node, w):
    m = []
    try:
        for counter, elem in enumerate(w[node-1]):
            m.append(counter+1) if elem == 1 else ...
        return 'нет' if m == [] else m
    except IndexError:
        return "!ОШИБКА! неправильно данная вершина"


def read_graph_from_ini(path):
    config = configparser.ConfigParser()
    config.read(path)#'g-files/for_2/MS.ini'
    nodes_count = int(config['config']['nodes_count'])
    if config['config']['type'] == 'MS':
        matrix = [[0 for x in range(nodes_count)] for y in range(nodes_count)]
        for count, elem in enumerate(config):
            for value in config[str(elem)]:
                if elem != 'config':
                    ne = list(str(config[elem][value]).split(','))
                    fromTo = re.findall(r'[0-9]', str(elem))[0]
                    for xelem in ne:
                        matrix[int(fromTo) - 1][int(xelem)-1] = 1
        return matrix
    else:
        return  'ini file err'
