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

# Cria a árvore geradora
T = nx.Graph()

# Inicializa a busca em largura com o primeiro vértice do grafo
queue = [list(G.nodes())[0]]

# Cria a lista que irá armazenar as arestas (ou vértices)
ordem = []

# Enquanto a fila de vértices não estiver vazia
while len(queue) > 0:
  # Remove o primeiro vértice da fila
  current = queue.pop(0)

  # Adiciona o vértice atual à árvore geradora
  T.add_node(current)
  # Adiciona o vértice atual à lista de ordem
  ordem.append(current)

  # Adiciona os vizinhos do vértice atual à fila
  for neighbor in G.neighbors(current):
    if neighbor not in T:
      T.add_edge(current, neighbor)
      # Adiciona a aresta ao grafo
      ordem.append((current, neighbor))
      queue.append(neighbor)

# Exibe a lista de ordem
print(f'A ordem de escolha de vértices e arestas é dada a seguir: \n{ordem}')

# Enquanto a fila de vértices não estiver vazia
while len(queue) > 0:
  # Remove o primeiro vértice da fila
  current = queue.pop(0)


  # Adiciona o vértice atual à árvore geradora
  T.add_node(current)

  # Adiciona os vizinhos do vértice atual à fila
  for neighbor in G.neighbors(current):
    if neighbor not in T:
      T.add_edge(current, neighbor)
      queue.append(neighbor)

# Desenha o grafo e a árvore geradora
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='b', edge_color='k', width=1, alpha=0.8, with_labels=True)
nx.draw_networkx_edges(T, pos, edge_color='r', width=2, alpha=1)


# Exibe a figura
plt.show()



