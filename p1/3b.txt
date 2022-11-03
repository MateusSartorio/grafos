from sage.all_cmdline import *

def dois_conjuntos(L):
    # Cria o grafo
    G = Graph()
    
    # Adiciona todas as arestas ao grafo, onde o peso eh a distancia Euclidiana entre os vertices
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            G.add_edge(L[i], L[j], sqrt((L[i][0] - L[j][0])**2 + (L[i][1] - L[j][1])**2))

    # Cria os conjuntos de vertices, onde cada vertice pertence a um conjunto diferente inicialmente 
    S = DisjointSet(G.vertices(sort=False))
    
    # Armazena o conjunto de arestas ja ordenadas em ordem crescente de distancia
    E = G.edges(sort=True, key=lambda e: e[2])

    #G.show(edge_labels=True)

    qtd_arestas = 0
    V = len(L)
    for e in E:
        if qtd_arestas >= V - 2:
            break
        
        # Une os conjuntos dos vertices conectados pela aresta analisada
        if S.find(e[0]) != S.find(e[1]):
            S.union(e[0], e[1])
            qtd_arestas += 1
    
    # 
    A = list(S)[0]
    B = list(S)[1]
    print("Conjunto A: ", A)
    print("Conjunto B: ", B)

    return A, B


L = ( (0,0), (3, 2), (1, 2.5), (2, 2), (5, 1), (1, 1) )
result = dois_conjuntos(L)