import networkx as nx
from collections import defaultdict

# Cria o grafo
G = nx.Graph()

# Adiciona vértices ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

# Adiciona arestas ao grafo
G.add_edge(1, 2)
G.add_edge(1, 6)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 5)
G.add_edge(4, 5)




def encontrar_circuito_euler_minimo(G, inicio):
    # Armazena o circuito de Euler
    circuito = []

    # Armazena as arestas ainda não visitadas de cada vértice
    arestas_restantes = defaultdict(list)
    for u, v in G.edges():
        arestas_restantes[u].append(v)
        arestas_restantes[v].append(u)

    # Inicia a busca pelo circuito a partir do vértice de início
    atual = inicio
    while arestas_restantes[atual]:
        # Verifica se existe alguma aresta que ligue o vértice atual a outro vértice e que não passe por um vértice já visitado
        aresta_valida = False
        for proximo in arestas_restantes[atual]:
            if proximo not in circuito:
                aresta_valida = True
                break

        # Se não existir, seleciona qualquer aresta que ligue o vértice atual a outro vértice
        if not aresta_valida:
            proximo = arestas_restantes[atual].pop()

        # Remove a aresta selecionada da lista de arestas restantes
        arestas_restantes[atual].remove(proximo)
        arestas_restantes[proximo].remove(atual)

        # Adiciona ao circuito e atualiza o vértice atual
        circuito.append((atual, proximo))
        atual = proximo

    return circuito

def encontrar_caminho_euler_minimo(G, inicio, fim):
    # Armazena o caminho de Euler
    caminho = []

    # Armazena as arestas ainda não visitadas de cada vértice
    arestas_restantes = defaultdict(list)
    for u, v in G.edges():
        arestas_restantes[u].append(v)
        arestas_restantes[v].append(u)

    # Inicia a busca pelo caminho a partir do vértice de início
    atual = inicio
    while atual != fim:
        # Verifica se existe alguma aresta que ligue o vértice atual a outro vértice e que não passe por um vértice já visitado
        aresta_valida = False
        for proximo in arestas_restantes[atual]:
            if proximo not in caminho:
                aresta_valida = True
                break

        # Se não existir, seleciona qualquer aresta que ligue o vértice atual a outro vértice
        if not aresta_valida:
            proximo = arestas_restantes[atual].pop()

        # Remove a aresta selecionada da lista de arestas restantes
        arestas_restantes[atual].remove(proximo)
        arestas_restantes[proximo].remove(atual)

        # Adiciona ao caminho e atualiza o vértice atual
        caminho.append((atual, proximo))
        atual = proximo

    return caminho



if all(deg % 2 == 0 for _, deg in G.degree()):
    # Encontra o circuito de Euler mínimo no grafo a partir do vértice 1
    circuito = encontrar_circuito_euler_minimo(G, 1)
    print(circuito)
else:
    print('Não possui um circuito de Euler.')

