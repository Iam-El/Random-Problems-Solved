import math


class graph:

    def __init__(self):
        self.nodes = []
        self.graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.nodes:
            self.nodes.append(node)
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.nodes:
            print(node, "->", self.graph_dict[node])

    def show_edge_in_linkedlist(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print(node, "->", neighbour)

    def adjacency_matrix(self):
        n = len(self.graph_dict)
        matrix = [[0 for i in range(n)] for j in range(n)]
        for node in self.graph_dict:
            node1 = self.nodes.index(node)
            print(node1)
            for neighbour in self.graph_dict[node]:
                neighbour1 = self.nodes.index(neighbour)
                matrix[node1][neighbour1] = 1
        for i in matrix:
            print(i)

    def bfs(self, s):
        queue = [s]
        visited = []
        while len(queue) >= 1:
            current = queue.pop()
            if current not in visited:
                visited.append(current)
                if current in self.graph_dict:
                    for neighbour in self.graph_dict[current]:
                        queue.append(neighbour)
        print(visited)

    def dfs(self, s):
        stack = [s]
        visited = []
        while len(stack) >= 1:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                if current in self.graph_dict:
                    for neighbour in self.graph_dict[current]:
                        stack.insert(0, neighbour)
        print(visited)


g = graph()
g.addEdge('a', 'b')
g.addEdge('a', 'c')
g.addEdge('b', 'c')
g.addEdge('b', 'a')
g.addEdge('c', 'a')
g.addEdge('c', 'b')
g.addEdge('c', 'd')
g.addEdge('d', 'c')

print("show edges:->")

g.show_edges()

print("show edges:->")

g.show_edge_in_linkedlist()

print("show adjacecy matrix:->")

g.adjacency_matrix()

g.bfs('a')

g.dfs('a')

print((5) // 2)
print(5 ** 2)

print(math.sqrt(10))
