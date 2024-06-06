import min_heap_ucs

def UCS_find_cost(graph, cost, source, goal):
    fringe = min_heap_ucs.Min_Heap()
    fringe.enqueue((source, 0))

    while True:
        parent_node, acc_cost = fringe.dequeue()
        if parent_node == goal:
            print("Found the goal")
            return acc_cost
        for child in graph[parent_node]:
            fringe.enqueue((child, acc_cost + cost[(parent_node, child)]))







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
print(UCS_find_cost(graph=graph1, cost=path_cost1, source='S', goal='G'))