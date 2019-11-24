from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph
from utilites import give_adjacent_node as adjacent_node_list  # adjacent nodes list
ez = read_graph('g-files/for_X/MS.ini').copy()


def breadth_first_search(f: int, xw: list):
    query = adjacent_node_list(f, xw)  ############# for f adjacent nodes
    used = [False for noniter in range(len(xw))]  ## checked node
    parent = [None for noniter in range(len(xw))]  # parent
    depth = [0 for noniter in range(len(xw))]  ##### depth
    path, used[f-1], parent[f-1] = {}, True, -1
    for elem in query:
        used[elem-1], depth[elem-1], parent[elem-1] = True, 1, f
    while query:
        v = query.pop(0)
        for adj_node in adjacent_node_list(v, xw):
            if used[adj_node - 1] is False:
                used[adj_node - 1] = True
                query.append(adj_node)
                depth[adj_node - 1] = depth[v-1] + 1
                parent[adj_node-1] = v
    for counter, elem in enumerate(used):
        if elem is False:
            print("no path to ", elem + 1, " node")
        elif parent[counter] != -1:
            node = counter + 1
            pseudopath = []
            while parent[node - 1] != -1:
                node = parent[node - 1]
                pseudopath.append(node)
            path.update({counter+1: pseudopath})
    return parent, depth, path


visualize(ms_ss(ez))
selected_node = 6
bfs = breadth_first_search(selected_node, ez)
print("Список предков: ", bfs[0])
print("Список глубины: ", bfs[1])
print("Вершина >> цепочка пути к начальной:")
reprint(bfs[2])
