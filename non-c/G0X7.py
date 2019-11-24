from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import read_graph_from_ini as read_graph
# ez = read_graph('files/for_X/MSX.ini').copy()
ez = read_graph('files/for_X/MS.ini').copy()
ez = ms_ss(ez)
visualize(ez)
reprint(ez)


def depth_first_search_bipartite_test(w: dict, cur_node: int, cur_node_color: int, color: list):
    color[cur_node-1] = cur_node_color
    for adj_node in w[cur_node]:
        if color[adj_node-1] == 0:
            depth_first_search_bipartite_test(w, adj_node, cur_node_color*(-1), color)
        elif color[adj_node-1] == cur_node_color:
            return False
    print([counter+1 for counter, elem in enumerate(color) if elem == 1])
    print([counter+1 for counter, elem in enumerate(color) if elem == -1])
    return True


print('Граф двудольный') if depth_first_search_bipartite_test(ez, 1, 1, [0 for noniter in range(len(ez))]) == True else print('Граф не двудольный')

