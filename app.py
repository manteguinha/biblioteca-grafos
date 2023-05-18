class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def adjacency_matrix(self):
        return self.adj_matrix

    def adjacency_list(self):
        return self.adj_list

    def incidence_matrix(self):
        edges = []
        for u in range(self.vertices):
            for v, weight in self.adj_list[u]:
                if u < v:
                    edges.append((u, v, weight))

        incidence_matrix = [[0] * len(edges) for _ in range(self.vertices)]
        for col, (u, v, weight) in enumerate(edges):
            incidence_matrix[u][col] = weight
            incidence_matrix[v][col] = weight

        return incidence_matrix

    def vertex_degree(self, vertex):
        return len(self.adj_list[vertex])

    def average_degree(self):
        total_degree = sum(self.vertex_degree(v) for v in range(self.vertices))
        return total_degree / self.vertices

    def depth_first_search(self, start_vertex):
        visited = [False] * self.vertices
        traversal = []

        def dfs(vertex):
            visited[vertex] = True
            traversal.append(vertex)
            for neighbor, _ in self.adj_list[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(start_vertex)
        return traversal

    def breadth_first_search(self, start_vertex):
        visited = [False] * self.vertices
        visited[start_vertex] = True
        queue = [start_vertex]
        traversal = []

        while queue:
            current_vertex = queue.pop(0)
            traversal.append(current_vertex)
            for neighbor, _ in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal

      
# EXEMPLOS
      
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
