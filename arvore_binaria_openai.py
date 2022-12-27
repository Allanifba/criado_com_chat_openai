import networkx as nx
import matplotlib.pyplot as plt


# Função para adicionar um nó à árvore de busca binária
def add_node(node, value):
    # Se o nó é nulo, retorna um novo nó com o valor passado como parâmetro
    if node is None:
        return {'value': value, 'left': None, 'right': None}

    # Se o valor passado como parâmetro é menor que o valor do nó atual, adiciona o novo nó à esquerda
    if value < node['value']:
        node['left'] = add_node(node['left'], value)
    # Se o valor passado como parâmetro é maior que o valor do nó atual, adiciona o novo nó à direita
    elif value > node['value']:
        node['right'] = add_node(node['right'], value)

    return node


# Função para percorrer a árvore de busca binária e adicionar as arestas ao grafo
def add_edges(node, G):
    # Se o nó atual não é nulo
    if node is not None:
        # Verifica se o nó tem filhos
        if node['left'] is not None:
            # Adiciona uma aresta entre o nó atual e o filho à esquerda
            G.add_edge(node['value'], node['left']['value'])
            # Percorre a subárvore esquerda e adiciona as arestas
            add_edges(node['left'], G)

        if node['right'] is not None:
            # Adiciona uma aresta entre o nó atual e o filho à direita
            G.add_edge(node['value'], node['right']['value'])
            # Percorre a subárvore direita e adiciona as arestas
            add_edges(node['right'], G)


# Cria o grafo
G = nx.Graph()

# Cria a árvore de busca binária
root = None
for value in [26, 23, 18, 25, 30, 27, 28, 32, 31, 34]:
    root = add_node(root, value)

# Adiciona as arestas ao grafo
add_edges(root, G)

# Obtém as posições dos vértices para plotar o grafo
pos = nx.spring_layout(G)

# Desenha o grafo com rótulos nos vértices
nx.draw(G, pos, with_labels=True, node_shape='o', node_size=700)

# Mostra o grafo
plt.show()
