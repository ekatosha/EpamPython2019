class GraphIterator:
    """Iterator for your graph"""

    def __init__(self, graph, root):
        self.graph = graph
        self.root = list(graph.keys())[root]
        self.visited = set()
        self.visited.add(self.root)
        self.queue = collections.deque([self.root])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration
        v = self.queue.popleft()
        try:
            for i in self.graph[v]:
                if i not in self.visited:
                    self.queue.append(i)
                    self.visited.add(i)
        except KeyError:
            print('not all vertices are listed in the graph')
            raise StopIteration
        return v


class Graph:
    """Class for your graph"""

    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self.E, 0)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
