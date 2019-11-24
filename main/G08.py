from vizualizer import vizualize_ver0 as visualize


def topological_sort(xw: dict):
    def step(w: dict, cur_node: int, color: list, result: list):
        if color[cur_node - 1] is 'g':
            print('Найден цикл, сортировка невозможна')
            return Exception
        if color[cur_node - 1] is 'w':
            color[cur_node - 1] = 'g'
            for node in w[cur_node]:
                step(w, node, color, result)
            color[cur_node - 1] = 'b'
            result.insert(0, cur_node)
    color = ['w' for x in range(len(xw))]
    r = []
    for xnode in xw.keys():
        step(xw, xnode, color, r)
    print('Результат топологической сортировки:', r)

# ez = {
#     1: [2, 3, 4, 5],
#     2: [4],
#     3: [4, 5],
#     4: [5],
#     5: []
# }
# visualize(ez)
# topological_sort(ez)
