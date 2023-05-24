# 🌐 Classe Grafo 💻

Este arquivo README explica de forma clara, fácil de entender e organizada a implementação de uma classe Grafo em Python. O código apresentado abaixo é a implementação de um grafo não-direcionado ponderado.

```python
class Grafo:
    ...
```

## 📚 Sumário

1. [🏁 Inicializando a classe Grafo](#-inicializando-a-classe-grafo)
2. [🔗 Adicionando Arestas](#-adicionando-arestas)
3. [📊 Matriz de Adjacência](#-matriz-de-adjacência)
4. [📜 Lista de Adjacência](#-lista-de-adjacência)
5. [🔢 Matriz de Incidência](#-matriz-de-incidência)
6. [🎓 Grau do Vértice](#-grau-do-vértice)
7. [📈 Grau Médio do Grafo](#-grau-médio-do-grafo)
8. [🔎 Busca em Profundidade](#-busca-em-profundidade)
9. [🔍 Busca em Largura](#-busca-em-largura)

## 🏁 Inicializando a classe Grafo

Para criar um objeto do tipo Grafo, é necessário informar o número de vértices. A classe irá inicializar as estruturas de dados internas, como a matriz de adjacências e a lista de adjacências.

```python
grafo = Grafo(4)
```

## 🔗 Adicionando Arestas

Para adicionar uma aresta ao grafo, é necessário informar os vértices `u` e `v`, bem como o peso da aresta. A função `adicionar_aresta(u, v, weight)` irá verificar se os vértices e o peso são válidos antes de adicionar a aresta.

```python
grafo.adicionar_aresta(0, 1, 2)
```

## 📊 Matriz de Adjacência

A matriz de adjacência é uma representação do grafo em formato matricial. Para exibir a matriz de adjacência do grafo, basta chamar a função `matriz_adjacencia()`.

```python
print("Matriz de adjacência:")
for row in grafo.matriz_adjacencia():
    print(row)
```

## 📜 Lista de Adjacência

A lista de adjacência é outra representação do grafo. Para exibir a lista de adjacência do grafo, basta chamar a função `lista_adjacencia()`.

```python
print("\nLista de adjacência:")
for i, adj in enumerate(grafo.lista_adjacencia()):
    print(f"{i}: {adj}")
```

## 🔢 Matriz de Incidência

A matriz de incidência é uma representação do grafo que relaciona vértices e arestas. Para exibir a matriz de incidência do grafo, basta chamar a função `matriz_incidencia()`.

```python
print("\nMatriz de incidência:")
for row in grafo.matriz_incidencia():
    print(row)
```

## 🎓 Grau do Vértice

Para obter o grau de um vértice específico, basta chamar a função `grau_vertice(vertex)`, passando o vértice desejado como argumento.

```python
print("\nGrau de vértices:")
for i in range(4):
    print(f"Grau do vértice {i}: {grafo.grau_vertice(i)}")
```

## 📈 Grau Médio do Grafo

Para obter o grau médio do grafo, basta chamar a função `grau_medio()`.

```python
print(f"\nGrau médio do grafo: {grafo.grau_medio()}")
```

## 🔎 Busca em Profundidade

A busca em profundidade é um algoritmo de travessia de grafos. Para executar a busca em profundidade a partir de um vértice inicial, basta chamar a função `busca_profundidade(start_vertex)`.

```python
print(f"\nBusca em profundidade a partir do vértice 0: {grafo.busca_profundidade(0)}")
```

## 🔍 Busca em Largura

A busca em largura é outro algoritmo de travessia de grafos. Para executar a busca em largura a partir de um vértice inicial, basta chamar a função `busca_largura(start_vertex)`.

```python
print(f"\nBusca em largura a partir do vértice 0: {grafo.busca_largura(0)}")
```

# 🚀 Exemplos

Aqui está um exemplo completo de como utilizar a classe Grafo:

```python
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
```

Esperamos que este README tenha sido útil para entender melhor a classe Grafo e suas funcionalidades! 😃🌟
