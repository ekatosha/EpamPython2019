class Graph:
    """Iterator for your graph"""

    def __init__(self, graph):
        self.index = 0
        self.graph = graph
        self.root = list(graph.keys())[0]
        self.visited = set()
        self.visited.add(self.root)
        self.queue = collections.deque([self.root])
        self.length = len(graph)-1

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue and not self.length:
            raise StopIteration
        elif not self.queue:
            while not self.queue:
                self.index += 1
                if list(graph.keys())[self.index] not in self.visited:
                    self.queue.append(list(graph.keys())[self.index])
                    self.visited.add(list(graph.keys())[self.index])
                    self.length -= 1
        v = self.queue.popleft()
        try:
            for i in self.graph[v]:
                if i not in self.visited:
                    self.queue.append(i)
                    self.visited.add(i)
                    self.length -= 1
        except KeyError:
            print('not all vertices are listed in the graph')
            raise StopIteration
        return v


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)

