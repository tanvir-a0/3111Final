graph = {
    '0': ['1', '2', '3', '4'],
    '1': ['0', '2'],
    '2': ['1', '0', '3', '5'],
    '3': ['0', '2', '4', '5'],
    '4': ['0', '3', '5'],
    '5': ['2', '3', '4']
}

def BFS_efficient_path(graph, start_node, goal_node):
    fringe = [[start_node]]
    visited = []

    if start_node == goal_node:
        return [start_node]

    while fringe:
        current_path = fringe.pop(0)
        current_node = current_path[-1]

        if current_node == goal_node:
            return current_path
        
        print("fringe: ", fringe, " current_node: ", current_node, " current_path: ", current_path, " visited: ", visited)
        if current_node not in visited:
            visited.append(current_node)
            
            for child in graph[current_node]:
                new_path = list(current_path)
                new_path.append(child)
                fringe.append(new_path)
    
    return False

def BFS_traverse_path(graph, start_node, goal_node):
    fringe = [[start_node]]
    visited = []
    traverse_path = []

    if start_node == goal_node:
        return start_node

    while fringe:
        current_path = fringe.pop(0)
        current_node = current_path[-1]

        if current_node == goal_node:
            traverse_path.append(current_node)
            return traverse_path
        
        #print("fringe: ", fringe, " current_node: ", current_node, " current_path: ", current_path, " visited: ", visited)
        if current_node not in visited:
            visited.append(current_node)
            traverse_path.append(current_node)
            for child in graph[current_node]:
                new_path = list(current_path)
                new_path.append(child)
                fringe.append(new_path)
    
    return traverse_path
#print(BFS_efficient_path(graph=graph, start_node='1', goal_node='5'))
#print(BFS_traverse_path(graph=graph, start_node='1', goal_node='5'))


T = int(input())
for test_no in range(T):
    n = int(input())
    graph = {}
    for line_no in range(n):
        line = input()
        separate = line.split(" ")
        graph[str(line_no)] = separate[1:]
    #print(graph)
    print(' '.join(BFS_traverse_path(graph=graph, start_node='0', goal_node=None)))
    
