import matplotlib.pyplot as plt
import networkx as nx
def vizualize_ver0(w):
    G = nx.Graph()
    for elem, value in w.items():
        for xvalue in value:
            G.add_edge(str(elem), str(xvalue))
            # G.add_edge(str(elem), str(xvalue), weight=(random.randint(10,100)/100))
    # simple = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw_networkx_nodes(G, pos, node_size=440, node_color='orange')
    nx.draw_networkx_edges(G, pos, width=len(list(w.keys())), edge_color='b')
    nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif', font_weight='bold')
    plt.axis('on')
    plt.show()
    return

