from sage.all_cmdline import *

A = ('Alg', 'Eng', 'ED1', 'ED2', 'Cal', 'Fis1', 'Fis2')
B = ( ('Alg', 'ED2'), ('ED1', 'ED2'), ('Cal', 'ED1'), ('Fis1', 'Fis2') )

def aluno_relaxado(A, B):
    G = DiGraph()

    for v in A:
        G.add_vertex(v)
        G.set_vertex(v, 0)

    for e in B:
        G.add_edge(e[0], e[1])

    G.show()
    T = G.topological_sort()
    #print(T)

    for v in T:
        for u in G.neighbors_out(v):
                    if G.get_vertex(v) + 1 > G.get_vertex(u):
                        G.set_vertex(u, G.get_vertex(v) + 1)
    
    maior_semestre = 0
    lista_ordenada = []
    for i in G.get_vertices():
        lista_ordenada[G.get_vertex(i)].append(1)



aluno_relaxado(A, B)
