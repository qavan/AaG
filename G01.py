import configparser
import re


def ms_mi(w):
    print("***")
    ec, temp = 0, []
    for counter, elem in enumerate(w):
        for x in range(counter, len(elem)):
            if elem[x] == 1:
                ec += 1
                temp.append([counter, x])
    m = [[0 for x in range(ec)] for y in range(len(w))]
    for x in range(0, len(temp)):
        m[temp[x][0]][x], m[temp[x][1]][x] = 1, 1
    print('Матрица инцидентности:')
    for elem in m:
        print(elem)
    return m


def ms_ss(w):
    print("***")
    m = {}
    for counter, elem in enumerate(w):
        L = []
        for xcounter, xelem in enumerate(elem):
            if xelem == 1:
                L.append(xcounter+1)
        m.update({counter+1: L})
    print('Список смежности:')
    for elem, value in m.items():
        print(str(elem) + ":" + str(value))
    return m


def ms_sr(w):
    print("***")
    temp = []
    for counter, elem in enumerate(w):
        for x in range(counter, len(elem)):
            if elem[x] == 1:
                temp.append([counter+1, x+1])
    m = {}
    for counter, elem in enumerate(temp):
        m.update({counter+1: elem})
    print('Список рёбер:')
    for elem, value in m.items():
        print(str(elem) + ":" + str(value))
    return m


def mi_ms(w):
    print("***")
    temp = []
    m = [[0 for x in range(len(w))] for y in range(len(w))]
    for i in range(len(w[0])):
        perv, vtor = 0, 0
        for j in range(len(w)):
            if perv == 0 or vtor == 0:
                if w[j][i] == 1 and perv == 0:
                    perv = j
                elif w[j][i] == 1 and vtor == 0:
                    vtor = j
            else:
                break
        temp.append([perv, vtor])
    for x in range(len(temp)):
        m[temp[x][0]][temp[x][1]], m[temp[x][1]][temp[x][0]] = 1, 1
    print("Матрица смежности")
    for elem in m:
        print(elem)
    return m


def mi_ss(w):
    print("***")
    temp = []
    m = {x+1: [] for x in range(len(w))}
    for i in range(len(w[0])):
        perv, vtor = 0, 0
        for j in range(len(w)):
            if perv == 0 or vtor == 0:
                if w[j][i] == 1 and perv == 0:
                    perv = j
                elif w[j][i] == 1 and vtor == 0:
                    vtor = j
            else:
                break
        temp.append([perv+1, vtor+1])
    for elem in temp:
        m[elem[0]], m[elem[1]] = m[elem[0]]+[elem[1]], m[elem[1]]+[elem[0]]
    for elem, value in m.items():
        elem = value.sort()
    print("Список смежности:")
    for elem, value in m.items():
        print(str(elem) + ":" + str(value))
    return m


def mi_sr(w):
    print("***")
    m = {x+1: [] for x in range(len(w[0]))}
    for i in range(len(w[0])):
        perv, vtor = 0, 0
        for j in range(len(w)):
            if perv == 0 or vtor == 0:
                if w[j][i] == 1 and perv == 0:
                    perv = j
                elif w[j][i] == 1 and vtor == 0:
                    vtor = j
            else:
                break
        sortof = [perv+1, vtor+1]
        sortof.sort()
        m[i+1] = m[i+1] + sortof
    print('Список рёбер:')
    for elem, value in m.items():
        print(str(elem) + ":" + str(value))
    return m


def ss_ms(w):
    print("***")
    m = [[0 for x in range(len(w))] for y in range(len(w))]
    counter = 0
    for elem, value in w.items():
        if value !=[]:
            for xelem in value:
                m[counter][xelem-1]=1
        counter += 1
    print('Матрица смежности:')
    for elem in m:
        print(elem)
    return m


def ss_mi(w):
    print("***")
    control = []
    for elem, value in w.items():
        for values in value:
            if ([elem, values] not in control) and ([values, elem] not in control):
                control.append([elem, values])
    m = [[0 for x in range(len(control))] for y in range(len(w))]
    for x in range(len(control)):
        m[control[x][0]-1][x], m[control[x][1]-1][x] = 1, 1
    print('Матрица инцидентности:')
    for elem in m:
        print(elem)
    return m


def ss_sr(w):
    print("***")
    m = {}
    for elem, value in w.items():
        for xelem in value:
            if ([elem, xelem] not in m.values()) and ([xelem, elem] not in m.values()):
                m.update({len(m)+1: [elem, xelem]})
    print('Список рёбер:')
    for elem, value in m.items():
        print(str(elem) + ":" + str(value))
    return m


def sr_ms(w):
    print("***")
    nodes_count_calculate = 0
    for elem, value in w.items():
        for xvalue in value:
            if int(xvalue) > nodes_count_calculate:
                nodes_count_calculate = xvalue
    print(nodes_count_calculate)
    m = [[0 for x in range(nodes_count_calculate)] for y in range(nodes_count_calculate)]
    for elem, value in w.items():
        m[value[0]-1][value[1]-1] = 1
    for x in range(len(m)):
        for y in range(x, len(m)):
            m[y][x] = m[x][y]
    print('Матрица смежности:')
    for elem in m:
        print(elem)


def sr_mi(w):
    print("***")
    nodes_count_calculate = 0
    for elem, value in w.items():
        for xvalue in value:
            if int(xvalue) > nodes_count_calculate:
                nodes_count_calculate = xvalue
    m = [[0 for x in range(len(w))] for y in range(nodes_count_calculate)]
    count = 0
    for elem, value in w.items():
        m[value[0]-1][count], m[value[1]-1][count] = 1, 1
        count += 1
    print('Матрица инцидентности:')
    for elem in m:
        print(elem)
    return m

def sr_ss(w):
    print("***")
    m = {}
    for elem, value in w.items():
        for values in value:
            if values not in m.keys():
                m.update({values: []})
    for elem, value in w.items():
        if value[1] not in m[value[0]]:
            m[value[0]] = m[value[0]] + [value[1]]
        if value[0] not in m[value[0]]:
            m[value[1]] = m[value[1]] + [value[0]]
    print('Список смежности:')
    for elem, value in m.items():
        print(str(elem) + ":" + str(value))
    return m


config = configparser.ConfigParser()
config.read('files/for_1/MS.ini')
# config.read('files/for_1/MI.ini')
# config.read('files/for_1/SS.ini')
# config.read('files/for_1/SR.ini')
nodes_count = int(config['config']['nodes_count'])
print("Количество вершин = " + str(nodes_count))
if config['config']['type'] == 'MS':
    matrix = [[0 for x in range(nodes_count)] for y in range(nodes_count)]
    for count, elem in enumerate(config):
        for value in config[str(elem)]:
            if elem != 'config':
                ne = list(str(config[elem][value]).split(','))
                fromTo = re.findall(r'[0-9]', str(elem))[0]
                # print(fromTo + " связана с " + ','.join(ne))#print(re.findall(r'[0-9]',str(elem))[0]+">>"+re.findall(r'[0-9]',str(value))[0])
                for xelem in ne:
                    matrix[int(fromTo) - 1][int(xelem)-1] = 1
    print()
    print('Матрица смежности:')
    for elem in matrix:
        print(elem)
elif config['config']['type'] == 'MI':
    matrix = [[0 for x in range(int(config['config']['edges_count']))] for y in range(nodes_count)]
    for count, elem in enumerate(config):
        for value in config[str(elem)]:
            if elem != 'config':
                ne = list(str(config[elem][value]).split(','))
                fromTo = re.findall(r'[0-9]', str(elem))[0]
                # print(fromTo + " является ребром вершин " + ','.join(ne))#print(re.findall(r'[0-9]',str(elem))[0]+">>"+re.findall(r'[0-9]',str(value))[0])
                matrix[int(ne[0])-1][int(fromTo) - 1], matrix[int(ne[1])-1][int(fromTo) - 1] = 1, 1
    print()
    print('Матрица инцидентности:')
    for elem in matrix:
        print(elem)
elif config['config']['type'] == 'SS':
    pseudoMatrix = {}
    for count, elem in enumerate(config):
        for value in config[str(elem)]:
            if elem != 'config':
                ne = list(str(config[elem][value]).split(','))
                int_ne = [int(ne[x]) for x in range(len(ne))]
                fromTo = re.findall(r'[0-9]', str(elem))[0]
                try:
                    int_ne = [int(ne[x]) for x in range(len(ne))]
                    pseudoMatrix.update({int(fromTo): int_ne})
                except ValueError:
                    pseudoMatrix.update({int(fromTo): []})
                # print(fromTo + " смежна с " + ','.join(ne))#print(re.findall(r'[0-9]',str(elem))[0]+">>"+re.findall(r'[0-9]',str(value))[0])
    print()
    print('Список смежности:')
    for elem, value in pseudoMatrix.items():
        print(str(elem) + ":" + str(value))
elif config['config']['type'] == 'SR':
    pseudoMatrix = {}
    for count, elem in enumerate(config):
        for value in config[str(elem)]:
            if elem != 'config':
                ne = list(str(config[elem][value]).split(','))
                int_ne = [int(ne[x]) for x in range(len(ne))]
                fromTo = re.findall(r'[0-9]', str(elem))[0]
                pseudoMatrix.update({int(fromTo): int_ne})
                # print(fromTo + " есть ребро " + ','.join(ne))#print(re.findall(r'[0-9]',str(elem))[0]+">>"+re.findall(r'[0-9]',str(value))[0])
    print()
    print('Список рёбер:')
    for elem, value in pseudoMatrix.items():
        print(str(elem) + ":" + str(value))
else:
    print('ini file err')

# ms_mi(matrix)
# ms_ss(matrix)
# ms_sr(matrix)

# mi_ms(matrix)
# mi_ss(matrix)
# mi_sr(matrix)

# ss_ms(pseudoMatrix)
# ss_mi(pseudoMatrix)
# ss_sr(pseudoMatrix)

# sr_ms(pseudoMatrix)
# sr_mi(pseudoMatrix)
# sr_ss(pseudoMatrix)
