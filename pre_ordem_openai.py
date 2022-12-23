# Importa a biblioteca de manipulação de grafos do NetworkX e a biblioteca de plotagem do Matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import *


# Cria o grafo
G = nx.Graph()

# Adiciona vértices ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)

# Adiciona arestas ao grafo
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(3, 5)
G.add_edge(3, 6)
G.add_edge(4, 7)
G.add_edge(4, 8)


# Define a função de travessia em pré-ordem
def preorder_traversal(G, node, visited=[]):
    # Adiciona o nó atual à lista de visitados
    visited.append(node)

    # Para cada vizinho do nó atual
    for neighbor in G.neighbors(node):
        # Se o vizinho ainda não foi adicionado à lista de visitados
        if neighbor not in visited:
            # Realiza a travessia em pré-ordem no vizinho
            preorder_traversal(G, neighbor, visited)

    return visited


# Executa a travessia em pré-ordem a partir do nó 1
visited = preorder_traversal(G, 1)

# Exibe a lista de nós visitados
print(visited)


# PARA DESENHAR O GRAFO
# Desenha o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# Adiciona os rótulos aos vértices
labels = {i: i for i in range(1, 6)}
nx.draw_networkx_labels(G, pos, labels, font_size=12)

# Exibe a figura
plt.show()

