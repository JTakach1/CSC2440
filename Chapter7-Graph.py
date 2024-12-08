class BuildGraph:
    def __init__(self, x):
        self.__n = x
        self.__g = [[0] * x for i in range(x)]

    def inputGraph(self):
        leedges = int(input("Enter Number of Edges: "))
        print("Enter the Edges Between The Nodes (example: 0 1), Press Enter Between Edges: ")
        print()

        for i in range(leedges):
            node1, node2 = map(int, input().split())
            self.__g[node1][node2] = 1
            self.__g[node2][node1] = 1

    def graphDisplay(self):
        for i in range(self.__n):
            print(' '.join(map(str, self.__g[i])))

    def deleteNode(self, node_to_delete):
        del self.__g[node_to_delete]

        for i in range(len(self.__g)):
            del self.__g[i][node_to_delete]
        self.__n -= 1

n = int(input("Enter Number Of Nodes: "))
finalGraph = BuildGraph(n)
finalGraph.inputGraph()
print()
print("Graph before Deletion:")
finalGraph.graphDisplay()
finalGraph.deleteNode(2)
print()
print("Graph With No Node 2:")
finalGraph.graphDisplay()



