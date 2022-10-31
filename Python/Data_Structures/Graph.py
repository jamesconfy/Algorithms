class Graph(object):
    def __init__(self, graph={}) -> None:
        self.graph = graph

    def getVertices(self):
        return list(self.graph.keys())

    def addVertice(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def getEdges(self):
        edge = []
        for key, values in self.graph.items():
            for val in values:
                edges = f"{key}{val}"
                if edges not in edge and edges[::-1] not in edge:
                    edg = f"{key}{val}"
                    edge.append(edg)
        return edge

    def addEdges(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def getGraph(self):
        return self.graph

graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = Graph()
g.addVertice("z")
g.addVertice("f")
g.addVertice("d")
g.addEdges({"p", "c"})
g.addEdges({"p", "f"})
g.addEdges({"z", "f"})
print(g.getVertices())
print(g.getEdges())
print(g.getGraph())