from sage.all_cmdline import *

def aluno_relaxado(A, B):
    G = DiGraph()

    # Inicia todos os vertices (disciplinas) do grafo e atribui o valor de semestre de cada para zero
    for v in A:
        G.add_vertex(v)
        G.set_vertex(v, 0)

    # Adiciona todas as dependências de disciplinas no grafo
    for e in B:
        G.add_edge(e[0], e[1])

    #G.show()

    # Obtem o vetor de ordenacao topologica T
    T = G.topological_sort()

    # Imprime a resposta na saida padrao
    print("Aluno relaxado: ")
    for idx, x in enumerate(T):
        print(f"Semestre {idx + 1}: ", x)


def aluno_dedicado(A, B):
    G = DiGraph()

    # Inicia todos os vertices (disciplinas) do grafo e atribui o valor de semestre de cada para zero
    for v in A:
        G.add_vertex(v)
        G.set_vertex(v, 0)

    # Adiciona todas as dependências de disciplinas no grafo
    for e in B:
        G.add_edge(e[0], e[1])

    #G.show()

    # Obtem o vetor de ordenacao topologica T
    T = G.topological_sort()
    #print(T)

    # Para cada elemento de T, percorre sua lista de adjacencia
    # Se v aponta para um vertice u, e semestre(v) + 1 > semestre(u), atualiza-se o semestre de u para semestre(v) + 1 
    for v in T:
        for u in G.neighbors_out(v):
                    if G.get_vertex(v) + 1 > G.get_vertex(u):
                        G.set_vertex(u, G.get_vertex(v) + 1)
    
    # Gera uma lista ordenada contendo uma lista com todas as disciplinas do primeiro semestre na primeiro posicao, todas do segundo da segunda posicao e assim por diante
    lista_ordenada = []
    for i in G.vertices(sort=False):
        semestre = G.get_vertex(i)
        if semestre + 1 > len(lista_ordenada):
            lista_ordenada.append([i])
        else:
            lista_ordenada[semestre].append(i)

    # Imprime a lista para a saida padrao
    print("Aluno dedicado: ")
    for idx, x in enumerate(lista_ordenada):
        print(f"Semestre {idx + 1}: ", x)

A = ('Alg', 'Eng', 'ED1', 'ED2', 'Cal', 'Fis1', 'Fis2')
B = ( ('Alg', 'ED2'), ('ED1', 'ED2'), ('Cal', 'ED1'), ('Fis1', 'Fis2') )

aluno_relaxado(A, B)
print()
aluno_dedicado(A, B)