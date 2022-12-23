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

# Aplica o algoritmo de Prim para obter a árvore geradora mínima do grafo
T = nx.minimum_spanning_tree(G)

# Cria a lista para armazenar a ordem em que os vértices são escolhidos
ordem = []

# Percorre as arestas da árvore geradora
for u, v in T.edges():
  # Adiciona os vértices da aresta à lista "ordem"
  ordem.append(f'[{u},{v}]')

# Imprime a lista com a ordem em que os vértices foram escolhidos
print(f'As arestas são: {ordem}')
print('Note que a escolha da primeira aresta começará do vértice "1" que certamente\n'
      'participará da árvore geradora mínima e não ncessariamente da aresta de menor\n'
      'peso. Isto não invalida a resposta uma vez que foi escolhida a aresta de\n'
      'menor peso adjacente a "1".')

# Desenha o grafo e a árvore geradora
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='b', edge_color='k', width=1, alpha=0.8, with_labels=True)
nx.draw_networkx_edges(T, pos, edge_color='r', width=2, alpha=1)

# Desenha os rótulos das arestas do grafo
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='#0000BB')

# Exibe a figura
plt.show()
