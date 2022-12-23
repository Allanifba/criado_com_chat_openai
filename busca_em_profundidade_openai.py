import networkx as nx
import matplotlib.pyplot as plt

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
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)
G.add_edge(4, 2)
G.add_edge(5, 2)
G.add_edge(5, 3)
G.add_edge(5, 8)
G.add_edge(6, 1)
G.add_edge(6, 7)
G.add_edge(7, 2)
G.add_edge(7, 6)
G.add_edge(8, 1)
G.add_edge(8, 3)

# Realiza a busca em profundidade a partir do vértice 1
edges = list(nx.dfs_edges(G, 1))

# Obtém as posições dos vértices para plotar o grafo
pos = nx.spring_layout(G)

ordem = []
# Imprime a ordem em que as arestas são escolhidas
for u, v in edges:
    ordem.append(f'({u},{v})')
print(f'A ordem de escolha de vértices e arestas é dada a seguir: \n{ordem}')

# Desenha o grafo com rótulos nos vértices
nx.draw(G, pos, with_labels=True)

# Desenha as arestas da busca em profundidade em vermelho
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2, alpha=0.6)

# Mostra o grafo
plt.show()
