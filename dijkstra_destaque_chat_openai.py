# Algoritmo de Dijkstra com caminho mínimo destacado na cor vermelha (editável).
import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo
G = nx.Graph()

# Adiciona vértices ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)



# Adiciona arestas ao grafo
G.add_edge(1, 2, weight = 5)
G.add_edge(2, 3, weight = 4)
G.add_edge(3, 4, weight = 7)
G.add_edge(4, 1, weight = 10)
G.add_edge(4, 2, weight = 10)
G.add_edge(5, 2, weight = 10)
G.add_edge(5, 3, weight = 10)
G.add_edge(5, 8, weight = 10)
G.add_edge(6, 1, weight = 10)
G.add_edge(6, 7, weight = 10)
G.add_edge(7, 2, weight = 10)
G.add_edge(7, 6, weight = 10)
G.add_edge(8, 1, weight = 10)
G.add_edge(8, 3, weight = 10)


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


caminho = nx.dijkstra_path(G, 7, 8)


peso_total = 0
for i in range(len(caminho) - 1):
    peso_total += G[caminho[i]][caminho[i+1]]['weight']


print(peso_total)
print(caminho)

# Transforma a lista de nós em uma lista de arestas
arestas = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]

# Desenha o grafo com as arestas destacadas
nx.draw_networkx_edges(G, pos=pos, edgelist=arestas, width=2, edge_color='r')


# Exibe o gráfico
plt.show()





