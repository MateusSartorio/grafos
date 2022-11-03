from sage.all import *

G = Graph({
    "a":{"b":4,"h":8},
    "b":{"c":8,"h":4},
    "c":{"d":7,"f":4,"i":2},
    "d":{"e":9,"f":14},
    "e":{"f":10},
    "f":{"g":2},
    "g":{"h":1, "i":6},
    "h":{"i":7}}
)

aresta = ("b", "h")

G.show()

print(G.has_edge(aresta))