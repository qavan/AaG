from vizualizer import vizualize_ver0 as visualize
from utilites import reprint as reprint
from utilites import ms_ss as ms_ss
from utilites import ss_ms as ss_ms
from utilites import read_graph_from_ini as read_graph
from utilites import matrix_of_far as mof
from utilites import weight_of_nodes as won
from utilites import give_adjacent_node as anl
# ez = read_graph('files/for_4/MS.ini').copy()
ez = read_graph('files/for_X/MS.ini').copy()


def BFS(f, xw):
    query = anl(f, xw)  # for f adjacent nodes
    # print("start query: ", query)
    used = [False for noniter in range(len(xw))]  # checked node
    parent = [None for noniter in range(len(xw))]  # parent
    depth = [0 for noniter in range(len(xw))]  # depth
    used[f-1], parent[f-1] = True, -1
    for elem in query:
        used[elem-1] = True
        depth[elem-1] = 1
        parent[elem-1] = f
    path = {}
    while query:
        # cq = query.copy()
        v = query.pop(0)
        #ANL = adjacent_node_list(v, xw)
        #print("node:", v, " with adjacent's:", ANL, " query:", cq, " >>> ", query)
        # for w in ANL:
        for w in anl(v, xw):
            if used[w - 1] is False:
                used[w - 1] = True
                query.append(w)
                depth[w - 1] = depth[v-1] + 1
                parent[w-1] = v
    print("Список предков: ", parent)
    print("Список глубины: ", depth)
    for counter, elem in enumerate(used):
        # print("iter", counter)
        if elem is False:
            print("no path to ", elem + 1, " node")
        elif parent[counter] != -1:
            node = counter + 1
            pseudopath = []
            # print("for ", node, " path build starts...")
            while parent[node - 1] != -1:
                node = parent[node - 1]
                # print(node)
                pseudopath.append(node)
            # print(pseudopath)
            path.update({counter+1: pseudopath})
        # else:
        #     print("there is start node", counter, " WLLKNWN ", counter + 1)
    # print(path)
        # построение пути по предку
    reprint(path)


#reprint(ez)
visualize(ms_ss(ez))
BFS(1, ez)
