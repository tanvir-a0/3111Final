import time
from min_heap import Min_Heap

class A_Star:
    def __init__(self, graph, path_cost , source, goal, heuristics):
        self.graph = graph
        self.source = source
        self.goal = goal
        self.path_cost = path_cost
        self.visited = []
        self.fringe = Min_Heap(heuristics)
    

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
    'a': ['f', 'b'],
    'b': ['a', 'c', 'd'],
    'c': ['b', 'e', 'd'],
    'd': ['b', 'c', 'e'],
    'e': ['c', 'd', 'i', 'j'],
    'j': ['e', 'i'],
    'i': ['e', 'j', 'g', 'h'],
    'g': ['i', 'f'],
    'h': ['i', 'f'],
    'f': ['g', 'h', 'a']
}
path_cost1 = {
    ('a','b'):6,
    ('b','a'):6,

    ('b','c'):3,
    ('c','b'):3,

    ('c','d'):1,
    ('d','c'):1,

    ('b','d'):2,
    ('d','b'):2,

    ('c','e'):5,
    ('e','c'):5,

    ('d','e'):8,
    ('e','d'):8,

    ('e','i'):5,
    ('i','e'):5,

    ('e','j'):5,
    ('j','e'):5,

    ('j','i'):3,
    ('i','j'):3,

    ('g','i'):3,
    ('i','g'):3,

    ('h','i'):2,
    ('i','h'):2,

    ('g','f'):1,
    ('f','g'):1,

    ('f','h'):7,
    ('h','f'):7,

    ('a','f'):3,
    ('f','a'):3
}

heuristics1 = {
    'a': 10,
    'b': 8,
    'c': 5,
    'd': 7,
    'e': 3,
    'j': 0,
    'i': 1,
    'h': 3,
    'g': 5,
    'f': 6
}
graph2 = {
    's': ['a', 'b', 'c'],
    'a': ['b', 'd'],
    'b': ['d'],
    'd': ['h', 'i', 'f'],
    'c': ['d','f','e'],
    'e': ['g'],
    'f': ['g'],
    'g': [],
    'h': ['i', 'j'],
    'i': ['j','k','g'],
    'j': ['k'],
    'k': ['g']
}
path_cost2 = {
    ('s', 'a'): 4,
    ('s', 'b'): 10,
    ('s', 'c'): 11,
    ('a', 'd'): 5,
    ('a', 'b'): 8,
    ('b', 'd'): 15,
    ('c', 'd'): 8,
    ('c', 'f'): 2,
    ('c', 'e'): 20,
    ('d', 'i'): 20,
    ('d', 'f'): 1,
    ('d', 'h'): 16,
    ('e', 'g'): 19,
    ('f', 'g'): 13,
    ('h', 'i'): 1,
    ('h', 'j'): 2,
    ('i', 'j'): 5,
    ('i', 'k'): 13,
    ('i', 'g'): 5,
    ('j', 'k'): 7,
    ('k', 'g'): 16
}
heuristics2 = {
    's': 7,
    'a': 8,
    'b': 6,
    'c': 5,
    'd': 5,
    'e': 3,
    'f': 3,
    'g': 0,
    'h': 7,
    'i': 4,
    'j': 5,
    'k': 3
}
check_valid_graph_cost(graph1, path_cost1)
a_star = A_Star(graph=graph2, path_cost=path_cost2, source='s', goal='g', heuristics= heuristics2)
a_star.find_path()