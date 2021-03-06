import random


def is_graph_connected(xw: dict):
    def dfs(w: dict, cur_node: int, visited: list, cmpnts: list):
        nonlocal components
        cmpnts[cur_node-1] = components
        visited.append(cur_node)
        for node in w[cur_node]:
            if node not in visited:
                dfs(w, node, visited, cmpnts)
    visit, components, node_list = [], 0, list(xw.keys())
    cc = [0 for ni in range(len(node_list))]
    for xnode in node_list:
        if xnode not in visit:
            components += 1
            dfs(xw, xnode, visit, cc)
    if len(cc)-1 == cc.count(1):
        return True
    return False


def graph_component(xw: dict):
    def dfs(w: dict, cur_node: int):
        nonlocal visited, lil_component
        visited.append(cur_node)
        lil_component.append(cur_node)
        for node in w[cur_node]:
            if node not in visited:
                dfs(w, node)
        return
    node_list = list(xw.keys())
    visited = []
    components = []
    while visited != node_list:
        lil_component = []
        notvisited = [node for node in node_list if node not in visited]
        if notvisited == []:
            break
        dfs(xw, notvisited[0])
        components.append(lil_component)
    component_max = 0
    for counter, elem in enumerate(components):
        component_max = counter if len(elem) > component_max else component_max
    print('Число компонент связности графа: ', len(components))
    print('Компонента связности графа: ', components[component_max])
    print('Компоненты графа: ')
    for elem in components:
        print(elem)

def is_graph_bipartite_dfs(w: dict, cur_node: int, cur_node_color: int, color: list):
    color[cur_node-1] = cur_node_color
    for adj_node in w[cur_node]:
        if color[adj_node-1] == 0:
            return is_graph_bipartite_dfs(w, adj_node, cur_node_color * (-1), color)
        elif color[adj_node-1] == cur_node_color:
            return False
    return True
def is_graph_have_cycle(xw):
    def is_cycle_util(w: dict, cur_node: int, visited: list, recursive: list):
        visited[cur_node-1] = True
        recursive[cur_node-1] = True
        for node in w[cur_node]:
            if visited[node-1] is False:
                if is_cycle_util(w, node, visited, recursive) is True:
                    return True
            elif recursive[node-1] is True:
                print(visited, recursive)
                return True
        recursive[cur_node-1] = False
        return False

    def is_have_cycle(w: dict, cur_node: int):
        v = [False for x in range(len(xw))]
        r = [False for x in range(len(xw))]
        for node in w[cur_node]:
            if v[node-1] is False:
                if is_cycle_util(w, node, v, r) is True:
                    return True
        return False
    print('Граф цикличен') if is_have_cycle(xw, random.randint(1, len(list(xw.keys())))) else print('Граф ацикличен')


def find_cycles(xw: dict):
    def dfs(w: dict, cur_node: int, visited: list):
        nonlocal start_node, loop, cycles
        loop.append(cur_node)
        if cur_node in visited:
            if cur_node == start_node:
                cycles.append(loop)
            return
        visited.append(cur_node)
        for node in w[cur_node]:
            dfs(w, node, visited)
    cycles = []
    sorted = []
    result = []
    for start_node in xw.keys():
        visit = []
        loop = []
        dfs(xw, start_node, visit)
    if cycles != []:
        print('Все циклы:')
        for loop in cycles:
            copyloop = loop.copy()
            startnode = loop[0]
            indexes = []
            iter = 0
            while startnode in loop:
                point = loop.index(startnode)
                loop.pop(point)
                indexes.append(point+iter)
                iter += 1
            for x in range(1, len(indexes)):
                print(indexes[x], copyloop[indexes[x-1]:indexes[x]], copyloop, indexes)
                tmplist = copyloop[indexes[x-1]:indexes[x]]
                trpl = tmplist.copy()
                tmplist.sort()
                if tmplist not in sorted:
                    result.append(trpl+[startnode])
                    sorted.append(tmplist)
        for elem in result:
            print(elem)
    else:
        print('Нет циклов')


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
# ez3 = {
#     1: [2, 4],
#     2: [1, 3, 4],
#     3: [1, 2],
#     4: [1]
# }
# ez4 = {
#     1: [2, 3],
#     2: [1],
#     3: [1],
#     4: [5],
#     5: [4]
# }
#
# # 1 проверить граф на связность
# print('Граф связный') if is_graph_connected(ez1) else print('Граф не связный')
# print('Граф связный') if is_graph_connected(ez2) else print('Граф не связный')
# # 2 компонента связности
# graph_component(ez3)
# graph_component(ez4)
# # 3 проверить граф на двудольность
# v1 = [0 for ni in range(len(ez1))]
# v2 = [0 for ni in range(len(ez2))]
# print('Граф двудольный') if is_graph_bipartite_dfs(ez1, 1, 1, v1) else print('Граф не двудольный')
# print('Граф двудольный') if is_graph_bipartite_dfs(ez2, 1, 1, v2) else print('Граф не двудольный')
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
# ez3 = {
#     1: [2],
#     2: [3],
#     3: [1, 5],
#     4: [3],
#     5: [4]
# }
# # 4 проверить граф на ацикличность
# is_graph_have_cycle(ez1)
# is_graph_have_cycle(ez2)
# is_graph_have_cycle(ez3)
# # 5 найти циклы в неориентированном графе
# find_cycles(ez1)
# find_cycles(ez2)
# find_cycles(ez3)
