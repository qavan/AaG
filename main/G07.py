import random
from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph


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
        if notvisited == []:
            break
        dfs(xw, notvisited[0])
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
            return is_graph_bipartite_dfs(w, adj_node, cur_node_color * (-1), color)
        elif color[adj_node-1] == cur_node_color:
            return False
    print([counter+1 for counter, elem in enumerate(color) if elem == 1])
    print([counter+1 for counter, elem in enumerate(color) if elem == -1])
    return True


def is_graph_have_cycle(xw):
    def is_cycle_util(w: dict, cur_node: int, visited: list, recursive: list):
        visited[cur_node] = True
        recursive[cur_node] = True
        for node in w[cur_node]:
            if visited[node] is False:
                if is_cycle_util(w, node, visited, recursive) is True:
                    return True
            elif recursive[node] is True:
                return True
        recursive[cur_node] = False
        return False

    def is_have_cycle(w: dict, cur_node: int):
        v = [False for x in range(len(xw) + 1)]
        r = [False for x in range(len(xw) + 1)]
        for node in w[cur_node]:
            if v[node] is False:
                if is_cycle_util(w, node, v, r) is True:
                    return True
        return False
    print('Граф цикличен') if is_have_cycle(xw, random.randint(1, len(list(xw.keys())))) else print('Граф ацикличен')


# ez1 = {
#     1: [2],
#     2: [3],
#     3: [1],
#     4: [1]
# }
# ez2 = {
#     1: [2, 3],
#     2: [],
#     3: [],
#     4: [5],
#     5: []
# }
# 1 проверить граф на связность
# print('Граф связный') if is_graph_connected(ez1) else print('Граф не связный')
# print('Граф связный') if is_graph_connected(ez2) else print('Граф не связный')
# 2 компонента связности
# graph_component(ez1)
# graph_component(ez2)
# 3 проверить граф на двудольность
# v1 = [0 for noniter in range(len(ez1))]
# v2 = [0 for noniter in range(len(ez2))]
# print('Граф двудольный') if is_graph_bipartite_dfs(ez1, 1, 1, v1) else print('Граф не двудольный')
# print('Граф двудольный') if is_graph_bipartite_dfs(ez2, 1, 1, v2) else print('Граф не двудольный')
# 4 проверить граф на ацикличность
# is_graph_have_cycle(ez1)
# is_graph_have_cycle(ez2)
# 5 найти циклы в неориентированном графе
# ???
# visualize(ez1)
# visualize(ez2)
# reprint(ez1)
# reprint(ez2)