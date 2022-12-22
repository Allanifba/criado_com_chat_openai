import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo
G = nx.Graph()

# Adiciona vértices ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)


# Adiciona arestas ao grafo
G.add_edge(1, 2, weight = 5)
G.add_edge(2, 3, weight = 4)
G.add_edge(3, 4, weight = 7)
G.add_edge(4, 1, weight = 10)


# Calcula as posições dos nós com o layout de mola
pos = nx.spring_layout(G)

# Desenha o grafo
nx.draw(G, pos=pos, with_labels=True)


# Desenha os rótulos nos nós
nx.draw_networkx_labels(G, pos=pos)

# Desenha o grafo
nx.draw(G, pos=pos, with_labels=True)

# Obtém os pesos das arestas como um dicionário
edge_labels = nx.get_edge_attributes(G, 'weight')

# Desenha os rótulos das arestas
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

# Exibe o gráfico
plt.show()