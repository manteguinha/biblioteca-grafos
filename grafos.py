class Grafo:
    def __init__(self, vertices):
        # Verifica se o número de vértices é válido
        if vertices <= 0:
            raise ValueError("O número de vértices deve ser maior que 0.")
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        self.adj_list = [[] for _ in range(vertices)]

    def adicionar_aresta(self, u, v, weight=1):
        # Verifica se os vértices estão dentro dos limites do grafo
        if u < 0 or u >= self.vertices or v < 0 or v >= self.vertices:
            raise ValueError("Os vértices u e v devem estar dentro dos limites do grafo.")
        # Verifica se o peso da aresta é válido
        if weight <= 0:
            raise ValueError("O peso da aresta deve ser maior que 0.")
        # Adiciona a aresta no grafo
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def matriz_adjacencia(self):
        return self.adj_matrix

    def lista_adjacencia(self):
        return self.adj_list

    def matriz_incidencia(self):
        arestas = []
        for u in range(self.vertices):
            for v, weight in self.adj_list[u]:
                if u < v:
                    arestas.append((u, v, weight))

        matriz_incidencia = [[0] * len(arestas) for _ in range(self.vertices)]
        for col, (u, v, weight) in enumerate(arestas):
            matriz_incidencia[u][col] = weight
            matriz_incidencia[v][col] = weight

        return matriz_incidencia

    def grau_vertice(self, vertex):
        if vertex < 0 or vertex >= self.vertices:
            raise ValueError("O vértice deve estar dentro dos limites do grafo.")
        return len(self.adj_list[vertex])

    def grau_medio(self):
        grau_total = sum(self.grau_vertice(v) for v in range(self.vertices))
        return grau_total / self.vertices

    def busca_profundidade(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            raise ValueError("O vértice inicial deve estar dentro dos limites do grafo.")
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

    def busca_largura(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            raise ValueError("O vértice inicial deve estar dentro dos limites do grafo.")
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
grafo = Grafo(4)

# Adicionando arestas
grafo.adicionar_aresta(0, 1, 2)
grafo.adicionar_aresta(0, 3, 1)
grafo.adicionar_aresta(1, 2, 1)
grafo.adicionar_aresta(2, 3, 2)

# Exibindo a matriz de adjacência
print("Matriz de adjacência:")
for row in grafo.matriz_adjacencia():
    print(row)

# Exibindo a matriz de incidência
print("\nMatriz de incidência:")
for row in grafo.matriz_incidencia():
    print(row)

# Exibindo a lista de adjacência
print("\nLista de adjacência:")
for i, adj in enumerate(grafo.lista_adjacencia()):
    print(f"{i}: {adj}")

# Exibindo o grau de cada vértice
print("\nGrau de vértices:")
for i in range(4):
    print(f"Grau do vértice {i}: {grafo.grau_vertice(i)}")

# Exibindo o grau médio do grafo
print(f"\nGrau médio do grafo: {grafo.grau_medio()}")

# Busca em profundidade a partir do vértice 0
print(f"\nBusca em profundidade a partir do vértice 0: {grafo.busca_profundidade(0)}")

# Busca em largura a partir do vértice 0
print(f"\nBusca em largura a partir do vértice 0: {grafo.busca_largura(0)}")
