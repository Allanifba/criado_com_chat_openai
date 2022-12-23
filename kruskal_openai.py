import networkx as nx
from networkx.utils import UnionFind
import matplotlib.pyplot as plt
import random

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
G.add_edge(1, 2, weight = 5)
G.add_edge(2, 3, weight = 4)
G.add_edge(3, 4, weight = 7)
G.add_edge(4, 1, weight = 4)
G.add_edge(4, 2, weight = 7)
G.add_edge(5, 2, weight = 6)
G.add_edge(5, 3, weight = 5)
G.add_edge(5, 8, weight = 8)
G.add_edge(6, 1, weight = 9)
G.add_edge(6, 7, weight = 7)
G.add_edge(7, 2, weight = 8)
G.add_edge(7, 6, weight = 10)
G.add_edge(8, 1, weight = 9)
G.add_edge(8, 3, weight = 5)


# Obtém os pesos das arestas do grafo
edge_weights = nx.get_edge_attributes(G, 'weight')

# Cria uma lista de tuplas representando as arestas do grafo, com os seus respectivos pesos
edges = [(u, v, edge_weights[u, v]) for u, v in G.edges]

# Ordena as arestas da lista pelo peso, de forma crescente
edges = sorted(edges, key=lambda x: x[2])

# Cria uma estrutura de dados Union-Find para armazenar os conjuntos de vértices
uf = UnionFind()

# Cria uma lista para armazenar as arestas da árvore geradora mínima
min_spanning_tree_edges = []

# Percorre a lista de arestas, verificando se os vértices das arestas pertencem a conjuntos diferentes
for u, v, w in edges:
    if uf[u] != uf[v]:
        uf.union(u, v)
        G.add_edge(u, v, weight=w)
        min_spanning_tree_edges.append((u, v))

# Obtém as posições dos vértices para plotar o grafo
pos = nx.spring_layout(G)

# Desenha o grafo com rótulos nos vértices
nx.draw(G, pos, with_labels=True)

# Destaca as arestas ponderadas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

print(f'A ordem de escolha das arestas é dada a seguir: \n'
      f'{min_spanning_tree_edges}.')

# Desenha as arestas da árvore geradora mínima em vermelho
nx.draw_networkx_edges(G, pos, edgelist=min_spanning_tree_edges, edge_color='r', width=2, alpha=0.6)

# Mostra o grafo
plt.show()