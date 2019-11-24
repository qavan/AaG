from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph
ez = read_graph('files/for_X/MS.ini').copy()
ez = ms_ss(ez)
visualize(ez)
reprint(ez)

def do_dfs(xw: dict, start_node: int):
    time = 0
    times = [[None, None] for noniter in range(len(xw))]

    def depth_first_search(w: dict, cur_node: int, visited: list):
        nonlocal time, times
        time += 1
        visited.append(cur_node)
        print('Текущая вершина обхода в глубину:', cur_node)
        for node in [node for node in w[cur_node] if node not in visited]:
            times[node-1][0] = time
            depth_first_search(w, node, visited)
            time += 1
        times[cur_node - 1][1] = time
    depth_first_search(xw, start_node, [])
    for counter, elem in enumerate(times):
        print('Вершина', counter+1, 'имеет времена входа и выхода соответственно', elem[0], 'и', elem[1])


do_dfs(ez, 1)
