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
		newVertex = Vertex(key)
		self.numVertices = self.numVertices + 1
		self.vertDict[key] = newVertex
		return newVertex

	def __contains__(self, key):
		return key in self.vertDict

	def __iter__(self):
		return iter(self.vertDict.values())

	def getVertex(self, k):
		if k in self.vertDict:
			return self.vertDict[k]
		else:
			return None
	
	def count(self):
		return self.numVertices

	def getVertices(self):
		return self.vertDict.keys()

	def addEdge(self, f, t, weight=0):
		if f not in self.vertDict:
			nv = self.addVertex(f)
		if t not in self.vertDict:
			nv = self.addVertex(t)
		self.vertDict[f].addNeighbor(self.vertDict[t], weight)

	def bfs(self, start):
		visited, stack = set(), [self.vertDict[start].getId()]
		while stack:
			vertex = stack.pop(0)
			if vertex not in visited:
				visited.add(vertex)
				stack.extend(list(set([v.getId() for v in self.vertDict[vertex].getConnections()])-visited))
		return visited

	def dfs(self, start):
		visited, stack = set(), [self.vertDict[start].getId()]
		while stack:
			vertex = stack.pop()
			if vertex not in visited:
				visited.add(vertex)
				stack.extend(list(set([v.getId() for v in self.vertDict[vertex].getConnections()])-visited))
		return visited

	def dfsr(self, start, visited=None):
		if visited is None:
			visited = set()
		visited.add(self.vertDict[start].getId())
		for next in set([v.getId() for v in self.vertDict[start].getConnections()])-visited:
			self.dfsr(next, visited)
		return visited

	def bfs_paths(self, start, goal):
		stack = [(self.vertDict[start].getId(), [self.vertDict[start].getId()])]
		while stack:
			vertex, path = stack.pop(0)
			for next in set([v.getId() for v in self.vertDict[vertex].getConnections()])-set(path):
				if next == self.vertDict[goal].getId():
					yield path + [next]
				stack.append((next, path+[next]))

	def dfs_paths(self, start, goal):
		stack = [(self.vertDict[start].getId(), [self.vertDict[start].getId()])]
		while stack:
			vertex, path = stack.pop()
			for next in set([v.getId() for v in self.vertDict[vertex].getConnections()])-set(path):
				if next == self.vertDict[goal].getId():
					yield path + [next]
				stack.append((next, path+[next]))				

	def dfsr_paths(self, start, goal, path=None):
		if path is None:
			path = [self.vertDict[start].getId()]
		if start == goal:
			yield path
		for next in set([v.getId() for v in self.vertDict[start].getConnections()])-set(path):
			yield from self.dfsr_paths(next, goal, path+[next])

	def shortest_path(self, start, goal):
		try:
			return next(self.bfs_paths(start, goal))
		except StopIteration:
			return None

graph1 = Graph()
graph1.addEdge(0,1,5)
graph1.addEdge(0,5,2)
graph1.addEdge(1,2,4)
graph1.addEdge(2,3,9)
graph1.addEdge(3,4,7)
graph1.addEdge(3,5,3)
graph1.addEdge(4,0,1)
graph1.addEdge(5,4,8)
graph1.addEdge(5,2,1)
for v in graph1.getVertices():
	print(graph1.vertDict[v])
print(graph1.dfs(0))
print(graph1.bfs(0))
print(graph1.dfsr(0))
print(graph1.bfs(5))
print(graph1.dfsr(5))
print(list(graph1.dfs_paths(0, 5)))
print(list(graph1.bfs_paths(0, 5)))
print(list(graph1.dfsr_paths(0, 5)))
print(graph1.shortest_path(0, 5))


graph_map = Graph()
graph_2d =[[1, 1, 1, 1, 1, 1, 0, 0, 0, 1], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

index = 0
w, h = len(graph_2d[0]), len(graph_2d)


def addEdges(w, h, i, j, graph_2d, graph_map):
	i_min = max(0, i-1)
	i_max = min(w-1, i+1)
	j_min = max(0, j-1)
	j_max = min(w-1, j+1)
	nbrs = [(i_min, j_min), (i_min, j), (i_min, j_max),(i, j_min), (i,j_max), (i_max, j_max), (i_max, j), (i_max, j_min)]
	for n in nbrs:
		if graph_2d[n[0]][n[1]]:
			graph_map.addEdge((i, j), (n[0], n[1]))
	return graph_map


for i, r in enumerate(graph_2d):
	for j, c in enumerate(r):
		if graph_2d[i][j]==1:
			graph_map.addVertex((i,j))
			graph_map = addEdges(w, h, i, j, graph_2d, graph_map)

for v in graph_map.getVertices():
	print(graph_map.vertDict[v])

islands = []
isSub = False
for v in graph_map.getVertices():
	p = graph_map.dfs(v)
	if p not in islands:
		for i in islands:
			if i.issubset(p):
				isSub=True
		if not isSub:
			islands.append(p)
		isSub=False

print(len(islands))










	

