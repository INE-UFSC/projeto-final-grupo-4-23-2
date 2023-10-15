"""
  > references: 
    - https://algs4.cs.princeton.edu/43mst/

"""

import random

class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.edges = []

  def add_edge(self, u, v):
    self.edges.append((u, v))

  def find_parent(self, parent, i):
    if parent[i] == i:
      return i
    return self.find_parent(parent, parent[i])

  def union(self, parent, rank, x, y):
    root_x = self.find_parent(parent, x)
    root_y = self.find_parent(parent, y)
    if rank[root_x] < rank[root_y]:
      parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
      parent[root_y] = root_x
    else:
      parent[root_y] = root_x
      rank[root_x] += 1

  def kruskal(self):
    minimum_spanning_tree = set()
    parent = {}
    rank = {}

    for v in self.vertices:
      parent[v] = v
      rank[v] = 0

    first = self.edges[0]
    last = self.edges[-1]
    minimum_spanning_tree.add(first)
    minimum_spanning_tree.add(last)
    self.union(parent, rank, first[0], first[1])
    self.union(parent, rank, last[0], last[1])
    
    random.shuffle(self.edges) # ordena por peso
    for edge in self.edges:
      u, v = edge
      root_u = self.find_parent(parent, u)
      root_v = self.find_parent(parent, v)
      if root_u != root_v: # não pertecem ao mesmo nó "pai", ou seja, não formam um loop
        minimum_spanning_tree.add(edge)
        self.union(parent, rank, root_u, root_v)
    return minimum_spanning_tree
  
  def binaryMatrix(size:int=20):
    width = size
    height = size

    # mapeia todos os 'vertices' como coordenadas de uma matriz
    vertices = [(x, y) for x in range(width) 
                      for y in range(height)]

    # for y in range(height):
    #   for x in range(width):
    #     print((x, y), end=" ") 
    #   print()

    g = Graph(vertices)

    for v in vertices:
      if v[0] < size-1:
        g.add_edge(v, (v[0]+1, v[1]))
      if v[1] < size-1:
        g.add_edge(v, (v[0], v[1]+1))

    mst = g.kruskal()

    mat = [[1 for _ in range((size*2)+1)] for _ in range((size*2)+1)]

    for edge in mst:
      u, v = edge

      xu = u[0]*2 + 1
      yu = u[1]*2 + 1

      xv = v[0]*2 + 1
      yv = v[1]*2 + 1

      if u[0] == v[0]:
        mat[xu][yu] = 0
        mat[xu][yu + 1] = 0
        mat[xv][yv] = 0
      else:
        mat[xu][yu] = 0
        mat[xu + 1][yu] = 0
        mat[xv][yv] = 0

    #mat[0][1] = 0
    mat[-1][-2] = 0
    
    return mat