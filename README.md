# Documentação da Classe Grafo

A classe `Grafo` é uma implementação de um grafo não direcionado usando matriz de adjacência, matriz de incidência e lista de adjacência.

## Classe Grafo

### Métodos

- `__init__(self, vertices)`: Construtor que inicializa o grafo com o número de vértices informado.
- `add_edge(self, u, v, weight=1)`: Adiciona uma aresta entre os vértices `u` e `v` com um peso opcional (o padrão é 1).
- `adjacency_matrix(self)`: Retorna a matriz de adjacência do grafo.
- `adjacency_list(self)`: Retorna a lista de adjacência do grafo.
- `incidence_matrix(self)`: Retorna a matriz de incidência do grafo.
- `vertex_degree(self, vertex)`: Retorna o grau de um vértice específico.
- `average_degree(self)`: Retorna o grau médio dos vértices do grafo.
- `depth_first_search(self, start_vertex)`: Realiza uma busca em profundidade a partir do vértice inicial informado e retorna a ordem dos vértices visitados.
- `breadth_first_search(self, start_vertex)`: Realiza uma busca em largura a partir do vértice inicial informado e retorna a ordem dos vértices visitados.

## Exemplo de uso

```python
# Criando o grafo
grafo = Grafo(6)

# Adicionando arestas
grafo.add_edge(0, 1, 2)
grafo.add_edge(0, 3, 1)
grafo.add_edge(1, 2, 3)
grafo.add_edge(1, 4, 1)
grafo.add_edge(2, 5, 2)
grafo.add_edge(3, 4, 1)
grafo.add_edge(4, 5, 3)

# Exibindo a matriz de adjacência
print("Matriz de adjacência:")
for row in grafo.adjacency_matrix():
    print(row)

# Exibindo a matriz de incidência
print("\nMatriz de incidência:")
for row in grafo.incidence_matrix():
    print(row)

# Exibindo a lista de adjacência
print("\nLista de adjacência:")
for i, adj in enumerate(grafo.adjacency_list()):
    print(f"{i}: {adj}")

# Exibindo o grau de cada vértice
print("\nGrau de vértices:")
for i in range(6):
    print(f"Grau do vértice {i}: {grafo.vertex_degree(i)}")

# Exibindo o grau médio do grafo
print(f"\nGrau médio do grafo: {grafo.average_degree()}")

# Busca em profundidade a partir do vértice 0
print(f"\nBusca em profundidade a partir do vértice 0: {grafo.depth_first_search(0)}")

# Busca em largura a partir do vértice 0
print(f"\nBusca em largura a partir do vértice 0: {grafo.breadth_first_search(0)}")
```

## Saída do exemplo

```
Matriz de adjacência:
[0, 2, 0, 1, 0, 0]
[2, 0, 3, 0, 1, 0]
[0, 3, 0, 0, 0, 2]
[1, 0, 0, 0, 1, 0]
[0, 1, 0, 1, 0, 3]
[0, 0, 2, 0, 3, 0]

Matriz de incidência:
[2, 1, 0, 0, 0, 0]
[2, 0, 3, 1, 0, 0]
[0, 0, 3, 0, 2, 0]
[1, 0, 0, 0, 0, 1]
[0, 1, 1, 0, 0, 3]
[0, 0, 0, 0, 2, 3]

Lista de adjacência:
0: [(1, 2), (3, 1)]
1: [(0, 2), (2, 3), (4, 1)]
2: [(1, 3), (5, 2)]
3: [(0, 1), (4, 1)]
4: [(1, 1), (3, 1), (5, 3)]
5: [(2, 2), (4, 3)]

Grau de vértices:
Grau do vértice 0: 2
Grau do vértice 1: 3
Grau do vértice 2: 2
Grau do vértice 3: 2
Grau do vértice 4: 3
Grau do vértice 5: 2

Grau médio do grafo: 2.3333333333333335

Busca em profundidade a partir do vértice 0: [0, 1, 2, 5, 4, 3]

Busca em largura a partir do vértice 0: [0, 1, 3, 2, 4, 5]
```

Esta documentação descreve a classe `Grafo`, seus métodos e um exemplo de uso.
