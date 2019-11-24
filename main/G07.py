import random
from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph
# ez = read_graph('g-files/for_X/MSX.ini').copy()
# ez = read_graph('g-files/for_X/MS.ini').copy()
ez = read_graph('g-files/for_7/MS.ini').copy()
ez = ms_ss(ez)
visualize(ez)
reprint(ez)


def is_graph_connected(xw: dict):
    def dfs(w: dict, cur_node: int, visited: list):
        nodes = 1
        visited.append(cur_node)
        for node in [node for node in w[cur_node] if node not in visited]:
            nodes += dfs(w, node, visited)
        return nodes
    node_list = list(xw.keys())
    if dfs(xw, node_list[random.randint(0, len(node_list)-1)], []) == len(xw):
        return True
    return False


def graph_component(xw: dict):
    def dfs(w: dict, cur_node: int):
        nonlocal visited, pseudo_visited
        visited.append(cur_node)
        pseudo_visited.append(cur_node)
        for node in [node for node in w[cur_node] if node not in visited]:
            dfs(w, node)
        return visited
    nodes = list(xw.keys())
    visited = []
    visiteds = []
    # print('Список вершин графа:', nodes)
    # print('Количество вершин:', len(nodes))
    while visited != nodes:
        pseudo_visited = []
        notvisited = [node for node in nodes if node not in visited]
        if len(notvisited) > 1:
            next_node = random.randrange(1, len(notvisited))
        else:
            break
        dfs(xw, notvisited[next_node])
        visiteds.append(pseudo_visited)
    component_max = 0
    for counter, elem in enumerate(visiteds):
        component_max = counter if len(elem) > component_max else component_max
        # print(elem)
    print('Число компонент связности графа -', len(visiteds))
    print('Компонента связности графа -', visiteds[component_max])
    print('Ниже перечислены все компоненты графа')
    for elem in visiteds:
        print(elem)

def is_graph_bipartite_dfs(w: dict, cur_node: int, cur_node_color: int, color: list):
    color[cur_node-1] = cur_node_color
    for adj_node in w[cur_node]:
        if color[adj_node-1] == 0:
            is_graph_bipartite_dfs(w, adj_node, cur_node_color * (-1), color)
        elif color[adj_node-1] == cur_node_color:
            return False
    # print([counter+1 for counter, elem in enumerate(color) if elem == 1])
    # print([counter+1 for counter, elem in enumerate(color) if elem == -1])
    return True


# 1 проверить граф на связность
# print('Граф связный') if is_graph_connected(ez) else print('Граф не связный')
# 2 компонента связности
# graph_component(ez)
# 3 проверить граф на двудольность
# print('Граф двудольный') if is_graph_bipartite_dfs(ez, 1, 1, [0 for noniter in range(len(ez))]) else print('Граф не двудольный')
