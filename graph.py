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
		return list(visited)

	def dfs(self, start):
		visited, stack = set(), [self.vertDict[start].getId()]
		while stack:
			vertex = stack.pop()
			if vertex not in visited:
				visited.add(vertex)
				stack.extend(list(set([v.getId() for v in self.vertDict[vertex].getConnections()])-visited))
		return list(visited)

	def dfsr(self, start, visited=None):
		if visited is None:
			visited = set()
		visited.add(self.vertDict[start].getId())
		for next in set([v.getId() for v in self.vertDict[start].getConnections()])-visited:
			self.dfsr(next, visited)
		return list(visited)

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

graph = Graph()
l = [i for i in range(100)]
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
l2 = list(group_adjacent(l, 10))
for g in l2:
	for i, e in enumerate(g[1:]):
		graph.addEdge(g[0]+i, e)
print(list(graph.dfs_paths(10, 19)))
