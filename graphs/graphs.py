# A class for defining grpahs

# data   : 27-09-2023
# Written by: JAM

# import libraries
from collections import deque

class Graph(object):
    # define graph
    def __init__(self: object, gdict: dict = {}):
        self.gdict = gdict
        self.noVertices = 0
    
    def printGraph(self: object):
        for vertex in self.gdict:
            print(f"{vertex} : {self.gdict[vertex]}")

    def addVertex(self: object, vertex: str):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            self.noVertices += 1
            return True
        return False
    
    def addEdge(self: object, vertex1: str, vertex2: str):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict.get(vertex1).append(vertex2)
            self.gdict.get(vertex2).append(vertex1)
            return True
        return False
    
    def removeVertex(self: object, vertex: str):
        if vertex in self.gdict.keys():
            for i in self.gdict.get(vertex):
                self.gdict.get(i).remove(vertex)
            self.gdict.pop(vertex)
            self.noVertices -= 1
            return True
        return False

    
    def removeEdge(self: object, vertex1: str, vertex2: str):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try: # Need to add as vertices may exist but no existing edge is
                 # present
                self.gdict.get(vertex1).remove(vertex2)
                self.gdict.get(vertex2).remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    # breadth first search, Ot(noVertices + noEdges), Om(noVertices)
    # Use: when target is close to starting point
    def bfs(self: object, vertex: str):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex]) # created double ended queue
        while queue:
            currentVertex = queue.popleft()
            for adjacentVertex in self.gdict.get(currentVertex):
                if adjacentVertex not in visited:
                    visited.add(adjacentVertex)
                    queue.append(adjacentVertex)
        return visited
    
    # Depth first search- goes to deepest node in edge arrays, Ot(noVertices + noEdges), Om(noVertices)
    # USe: if the target is buried in the graph
    def dfs(self: object, vertex:str):
        visited = set()
        stack = [vertex] # FILO
        while stack:
            currentVertex = stack.pop()
            if currentVertex not in visited:
                visited.add(currentVertex)
            for adjacentVertex in self.gdict.get(currentVertex):
                if adjacentVertex not in visited:
                    stack.append(adjacentVertex)
        return visited
    
    # Topological sort helper function
    def topologicalSortUtil(self: object, vertex: str, visited: set, stack: list):
        visited.add(vertex)
        for i in self.gdict.get(vertex):
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, vertex)
    
    # Topological sort, Ot(V + E), Om(V + E)
    def topologicalSort(self: object):
        visited = set()
        stack = []
        for i in list(self.gdict):
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        return stack
    
    # BFS for SSSP, Ot(E), Om(E)
    def sssp(self: object, start: str, end: str):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacentVertex in self.gdict.get(node):
                newPath = list(path)
                newPath.append(adjacentVertex)
                queue.append(newPath)


testDict = {
    "a" : ["c"],
    "b" : ["c", "d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : ["f", "h"],
    "f" : ["g"],
    "g" : [],
    "h" : []
}
testGraph = Graph(testDict)
print(testGraph.topologicalSort())
print(testGraph.sssp("a", "h"))