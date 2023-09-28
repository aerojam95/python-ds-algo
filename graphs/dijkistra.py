# An implementation of dijkistra's algorithm

# data   : 27-09-2023
# Written by: JAM

import heapq

class Edge(object):
    # contrustor
    def __init__(self: object, weight: int , startVertex: any, endVertex: any):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex = endVertex

class Node(object):
    # Constructor
    def __init__(self: object, name: any):
        self.name = name
        self.visited = False
        self.prevVertex = None
        self.neighbourVertices = []
        self.minDistance = float("inf")
    
    # less than method to compare other nodes distances
    def __lt__(self: object, otherVertex: object):
        return self.minDistance < otherVertex.minDistance
    
    def addEdge(self: object, weight: int, destinationVertex: object):
        edge = Edge(weight, self, destinationVertex)
        self.neighbourVertices.append(edge)

class Dijkistra(object):
    # Constructor
    def __init__(self: object):
        self.heap = []

    def calculate(self: object, startVertex: object):
        startVertex.minDistance = 0
        heapq.heappush(self.heap, startVertex)
        while self.heap:
            # pop element with the shortest distance
            actualVertex = heapq.heappop(self.heap)
            if actualVertex.visited:
                continue
            # consider the nieghbours of the vertex in question
            for edge in actualVertex.neighbourVertices:
                start = edge.startVertex
                endVertex = edge.endVertex
                newDistance = start.minDistance + edge.weight
                if newDistance < endVertex.minDistance:
                    endVertex.minDistance = newDistance
                    endVertex.prevVertex = start
                    # update the heap
                    heapq.heappush(self.heap, endVertex)
            actualVertex.visited = True

    def getShortestPath(self: object, vertex: object):
        print(f"Shortest to {vertex.name} is {vertex.minDistance}")
        actualVertex = vertex
        while actualVertex is not None:
            print(actualVertex.name,end=" ")
            actualVertex= actualVertex.prevVertex

# Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Creates edges
nodeA.addEdge(6, nodeB)
nodeA.addEdge(10, nodeC)
nodeA.addEdge(9, nodeD)

nodeB.addEdge(5, nodeD)
nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(21, nodeG)
nodeC.addEdge(5, nodeH)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(4, nodeE)
nodeF.addEdge(12, nodeG)

nodeH.addEdge(2, nodeF)
nodeH.addEdge(14, nodeG)

algorithm = Dijkistra()
algorithm.calculate(nodeA)
algorithm.getShortestPath(nodeE)