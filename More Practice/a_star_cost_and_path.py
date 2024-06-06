import min_heap_ucs

def A_star_find_path_and_cost(graph, cost, source, goal, heuristics):
    fringe = min_heap_ucs.Min_Heap(heuristics=heuristics)
    fringe.enqueue((([source], 0), heuristics[source]))  # enqueue with initial heuristic

    while True:
        # Dequeue the element with the smallest estimated cost (actual cost + heuristic)
        (parent_path, acc_cost), _ = fringe.dequeue()
        parent_node = parent_path[-1]

        if parent_node == goal:
            print("Found the goal")
            return acc_cost, parent_path

        for child in graph[parent_node]:
            new_path = list(parent_path)
            new_path.append(child)
            new_cost = acc_cost + cost[(parent_node, child)]
            estimated_cost = new_cost + heuristics[child]
            fringe.enqueue(((new_path, new_cost), estimated_cost))



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
print(A_star_find_path_and_cost(graph2, path_cost2, 's', 'g', heuristics2))