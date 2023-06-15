# Criamos uma classe chamada "Grafo" para representar um grafo
class Grafo:
    # O construtor da classe recebe o número de vértices (pontos) do grafo
    def __init__(self, vertices):
        # Verifica se o número de vértices é válido (deve ser maior que 0)
        if vertices <= 0:
            raise ValueError("O número de vértices deve ser maior que 0.")
        # Guarda o número de vértices
        self.vertices = vertices
        # Cria a matriz de adjacência (tabela que mostra conexões entre os pontos)
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        # Cria a lista de adjacência (outra maneira de mostrar conexões entre os pontos)
        self.adj_list = [[] for _ in range(vertices)]

    # Função para adicionar uma aresta (linha que conecta dois pontos) ao grafo
    def adicionar_aresta(self, u, v, weight=1):
        # Verifica se os vértices estão dentro dos limites do grafo
        if u < 0 or u >= self.vertices or v < 0 or v >= self.vertices:
            raise ValueError("Os vértices u e v devem estar dentro dos limites do grafo.")
        # Verifica se o peso da aresta é válido (deve ser maior que 0)
        if weight <= 0:
            raise ValueError("O peso da aresta deve ser maior que 0.")
        # Adiciona a aresta no grafo (atualiza a matriz e a lista de adjacência)
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    # Função para retornar a matriz de adjacência
    def matriz_adjacencia(self):
        return self.adj_matrix

    # Função para retornar a lista de adjacência
    def lista_adjacencia(self):
        return self.adj_list

    # Função para criar e retornar a matriz de incidência (tabela que mostra arestas e pontos conectados)
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

    # Função para calcular o grau de um vértice (quantas arestas estão conectadas a ele)
    def grau_vertice(self, vertex):
        if vertex < 0 or vertex >= self.vertices:
            raise ValueError("O vértice deve estar dentro dos limites do grafo.")
        return len(self.adj_list[vertex])

    # Função para calcular o grau médio do grafo (média de conexões entre os pontos)
    def grau_medio(self):
        grau_total = sum(self.grau_vertice(v) for v in range(self.vertices))
        return grau_total / self.vertices

    # Função para fazer busca em profundidade no grafo (explora o grafo "mergulhando" nas conexões)
    def busca_profundidade(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            raise ValueError("O vértice inicial deve estar dentro dos limites do grafo.")
        visited = [False] * self.vertices
        traversal = []

        # Função auxiliar para fazer a busca em profundidade
        def dfs(vertex):
            visited[vertex] = True
            traversal.append(vertex)
            for neighbor, _ in self.adj_list[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(start_vertex)
        return traversal

    # Função para fazer busca em largura no grafo (explora o grafo "alargando" as conexões)
    def busca_largura(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            raise ValueError("O vértice inicial deve estar dentro dos limites do grafo.")
        visited = [False] * self.vertices
        visited[start_vertex] = True
        queue = [start_vertex]
        traversal = []

        # Enquanto a fila não estiver vazia, continuamos a busca
        while queue:
            # Remove o primeiro vértice da fila e o adiciona à lista de vértices visitados
            current_vertex = queue.pop(0)
            traversal.append(current_vertex)
            # Para cada vizinho do vértice atual, se ainda não foi visitado, marca como visitado e adiciona à fila
            for neighbor, _ in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal

    
####################### USANDO NA PRÁTICA! #######################

qtd_arestas = 4

# Criando o grafo
grafo = Grafo(qtd_arestas)

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
for i in range(qtd_arestas):
    print(f"Grau do vértice {i}: {grafo.grau_vertice(i)}")

# Exibindo o grau médio do grafo
print(f"\nGrau médio do grafo: {grafo.grau_medio()}")

# Busca em profundidade a partir do vértice 0
print(f"\nBusca em profundidade a partir do vértice 0: {grafo.busca_profundidade(0)}")

# Busca em largura a partir do vértice 0
print(f"\nBusca em largura a partir do vértice 0: {grafo.busca_largura(0)}")
