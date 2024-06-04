import time
from min_heap import Min_Heap

class UCS:
    def __init__(self, graph, path_cost , source, goal):
        self.graph = graph
        self.source = source
        self.goal = goal
        self.path_cost = path_cost
        self.visited = []
        self.fringe = Min_Heap()
    

    def find_path(self):
        self.fringe.enqueue((self.source, 0))
        #print(self.fringe)

        while True:
            parent_node, acc_cost = self.fringe.dequue()
            if parent_node == self.goal:
                print("Found the goal with cost: ", acc_cost)
                return acc_cost
            for child in self.graph[parent_node]:
                self.fringe.enqueue((child, acc_cost + self.path_cost[(parent_node, child)]))
                print("ucs main: ", self.fringe)
                input("Press Enter to continue: ")



def take_graph_and_cost():
    graph = {}
    cost = {}
    
    graph_edge = input("Enter the edge node: ")
    while graph_edge != "exit":
        graph_edge = graph_edge.split(" ")
        #print(graph_edge)
        graph[graph_edge[0]] = []
        for node in graph_edge[1:]:
            graph[graph_edge[0]].append(node)
        graph_edge = input("Enter the edge node: ")
    print(graph)

    edge_cost = input("Enter the edge cost: ")
    while edge_cost != "exit":
        edge_cost = edge_cost.split(" ")
        print(edge_cost)
        cost[(edge_cost[0], edge_cost[1])] = int(edge_cost[2])
        edge_cost = input("Enter the edge cost: ")

    print(cost)

    return graph, cost
def check_valid_graph_cost(graph, cost):
    for key in graph:
        for value in graph[key]:
            if (key,value) in cost:
                pass
            else:
                print("Problem with ", f"({key},{value})")
                return False
    print("Everythin Ok")
    return True

graph1 = {
    'S': ['1', '3'],
    '1': ['G'],
    '3': ['1', 'G', '4'],
    'G': ['4'],
    '4': ['5', '2'],
    '5': ['G', '2'],
    '2': ['1']
}
path_cost1 = {
    ('S', '1'): 2,
    ('S', '3'): 5,
    ('1', 'G'): 1,
    ('3', '1'): 5,
    ('3', 'G'): 6,
    ('3', '4'): 2,
    ('4', '2'): 4,
    ('4', '5'): 3,
    ('5', '2'): 6,
    ('5', 'G'): 3,
    ('2', '1'): 4,
    ('G', '4'): 7
}
check_valid_graph_cost(graph1, path_cost1)
ucs = UCS(graph=graph1, path_cost=path_cost1, source='S', goal='G')
ucs.find_path()