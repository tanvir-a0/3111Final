def BFS_efficient_path_with_loop(graph, start_node, goal_node):
    visited = []
    fringe = [[start_node]]
    looped_node = []

    if start_node == goal_node:
        return [start_node]
    
    while fringe:
        current_path = fringe.pop(0)
        current_node = current_path[-1]

        if current_node == goal_node:
            return current_path, looped_node
        
        if current_node not in visited:
            visited.append(current_node)

            for child in graph[current_node]:
                new_path = list(current_path)
                new_path.append(child)
                fringe.append(new_path)
        else:
            #This is where the loop is detected
            print('Node ', current_node, " is already visited")
            looped_node.append(current_node)
            pass
    return False, looped_node

graph = {
    '0': ['1', '2', '3', '4'],
    '1': ['0', '2'],
    '2': ['1', '0', '3', '5'],
    '3': ['0', '2', '4', '5'],
    '4': ['0', '3', '5'],
    '5': ['2', '3', '4']
}
graph1 = {
    '0': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6', '7'],
    '3': ['8', '9'],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': []
}
print(BFS_efficient_path_with_loop(graph=graph1, start_node='1', goal_node=None))
    
