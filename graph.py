class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# UnDirected graph 
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node
    
    def print_edges(self):
        for i in range(self.v):
            print(f"Adjency list of vertex {i} head", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    V = 9 # 5 vertices
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(1, 7)
    graph.add_edge(2, 1)
    graph.add_edge(7, 3)
    graph.add_edge(0, 3)
    graph.add_edge(8, 1)

    graph.print_edges()
