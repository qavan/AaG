import matplotlib.pyplot as plt
import networkx as nx
import random
def vizualize_ver0(w):
    G = nx.Graph()
    for elem, value in w.items():
        if value == []:
            G.add_edge(str(elem), str(random.randint(1, len(w))), weight=0)
            continue
        for xvalue in value:
            G.add_edge(str(elem), str(xvalue), weight=1)
    connected = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]
    isolated = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 0]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=440, node_color='orange')
    nx.draw_networkx_edges(G, pos, width=len(list(w.keys())), edge_color='b', edgelist=connected, alpha=1)
    nx.draw_networkx_edges(G, pos, width=len(list(w.keys())), edge_color='b', edgelist=isolated, alpha=0)
    nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif', font_weight='bold')
    plt.axis('on')
    plt.show()
    return True

