# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Graphs

# Graph Abstract Data Type


# Represents each vertex in the graph
# Each vertex uses a dict to keep track of the vertices to which it is connected to
# and the weight of each edge
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {} 

    # add a connection from this vertex to another
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # Returns all of the vertices in the adjacency list, 
    # as represented by the connectTo instance variable
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    # returns the weight of the edge 
    # from this vertes to the vertex passed as a parameter
    def getWeight(self,nbr):
        return self.connectedTo[nbr]



# Contains a dict that maps vertex names to vertex objects. 
# Provides methods for adding vertices to a graph and connecting one vertex to another
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # returns the names of all of the vertices in the graph
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    print(g.vertList)

    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

