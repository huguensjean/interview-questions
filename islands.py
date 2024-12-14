from collections import deque

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight


class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0

    def addVertex(self, key):
        if key not in self.vertDict:
            newVertex = Vertex(key)
            self.numVertices += 1
            self.vertDict[key] = newVertex
        return self.vertDict[key]

    def __contains__(self, key):
        return key in self.vertDict

    def __iter__(self):
        return iter(self.vertDict.values())

    def getVertex(self, k):
        return self.vertDict.get(k, None)

    def count(self):
        return self.numVertices

    def getVertices(self):
        return self.vertDict.keys()

    def addEdge(self, f, t, weight=0):
        if f not in self.vertDict:
            self.addVertex(f)
        if t not in self.vertDict:
            self.addVertex(t)
        self.vertDict[f].addNeighbor(self.vertDict[t], weight)

    def bfs(self, start):
        # Breadth-First Search
        visited = set()
        queue = deque([self.vertDict[start].getId()])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                neighbors = [v.getId() for v in self.vertDict[vertex].getConnections()]
                queue.extend(set(neighbors) - visited)
        return visited

    def dfs(self, start):
        # Depth-First Search (iterative)
        visited = set()
        stack = [self.vertDict[start].getId()]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                neighbors = [v.getId() for v in self.vertDict[vertex].getConnections()]
                stack.extend(set(neighbors) - visited)
        return visited

    def dfsr(self, start, visited=None):
        # Depth-First Search (recursive)
        if visited is None:
            visited = set()
        visited.add(self.vertDict[start].getId())
        neighbors = [v.getId() for v in self.vertDict[start].getConnections()]
        for nbr in set(neighbors) - visited:
            self.dfsr(nbr, visited)
        return visited

    def bfs_paths(self, start, goal):
        # Find all BFS paths from start to goal
        queue = deque([(self.vertDict[start].getId(), [self.vertDict[start].getId()])])
        while queue:
            vertex, path = queue.popleft()
            neighbors = [v.getId() for v in self.vertDict[vertex].getConnections()]
            for nbr in set(neighbors) - set(path):
                if nbr == self.vertDict[goal].getId():
                    yield path + [nbr]
                else:
                    queue.append((nbr, path + [nbr]))

    def dfs_paths(self, start, goal):
        # Find all DFS paths from start to goal
        stack = [(self.vertDict[start].getId(), [self.vertDict[start].getId()])]
        while stack:
            vertex, path = stack.pop()
            neighbors = [v.getId() for v in self.vertDict[vertex].getConnections()]
            for nbr in set(neighbors) - set(path):
                if nbr == self.vertDict[goal].getId():
                    yield path + [nbr]
                else:
                    stack.append((nbr, path + [nbr]))

    def dfsr_paths(self, start, goal, path=None):
        # Recursive DFS paths
        if path is None:
            path = [self.vertDict[start].getId()]
        if start == goal:
            yield path
        neighbors = [v.getId() for v in self.vertDict[start].getConnections()]
        for nbr in set(neighbors) - set(path):
            yield from self.dfsr_paths(nbr, goal, path + [nbr])

    def shortest_path(self, start, goal):
        # First BFS path found is the shortest
        try:
            return next(self.bfs_paths(start, goal))
        except StopIteration:
            return None


def addEdges(w, h, i, j, graph_2d, graph_map):
    # Adjusted indexing: i corresponds to rows (0..h-1), j corresponds to columns (0..w-1)
    i_min = max(0, i - 1)
    i_max = min(h - 1, i + 1)
    j_min = max(0, j - 1)
    j_max = min(w - 1, j + 1)
    # 8-connected neighbors
    nbrs = [(x, y) for x in range(i_min, i_max + 1) for y in range(j_min, j_max + 1)
            if not (x == i and y == j)]
    for n in nbrs:
        if graph_2d[n[0]][n[1]] == 1:
            graph_map.addEdge((i, j), (n[0], n[1]))
    return graph_map


print("\nCount number of islands in a binary image.")
graph_map = Graph()
print("\nInput map:")
graph_2d = [
	[1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
	[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
	[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
	[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
	[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
	[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
	[1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

for r in graph_2d:
    print(r)

w, h = len(graph_2d[0]), len(graph_2d)

for i, row in enumerate(graph_2d):
    for j, cell in enumerate(row):
        if cell == 1:
            graph_map.addVertex((i, j))
            graph_map = addEdges(w, h, i, j, graph_2d, graph_map)

print("\nGraph node connections:")
for v in graph_map.getVertices():
    print(graph_map.vertDict[v])

# Count distinct islands
islands = []
for v in graph_map.getVertices():
    comp = graph_map.dfsr(v)
    # If this component is not a subset of any existing island, add it
    if not any(i.issubset(comp) for i in islands):
        islands.append(comp)

print("\nNumber of islands:")
print(len(islands))
