graph = {
    '0': ['1', '2', '3', '4'],
    '1': ['0', '2'],
    '2': ['1', '0', '3', '5'],
    '3': ['0', '2', '4', '5'],
    '4': ['0', '3', '5'],
    '5': ['2', '3', '4']
}

def BFS(graph, goal_node, visited_node = [], fringe = []):
    print("'visited: ", visited_node)
    print("fring: ", fringe)

    next_node_to_explore = fringe.pop(0)
    while next_node_to_explore in visited_node:
        next_node_to_explore = fringe.pop(0)
    print("next_node_to_visit: ", next_node_to_explore)
    visited_node.append(next_node_to_explore)
    print("\n")
    if next_node_to_explore == goal_node:
        print("reached the goal")
        return visited_node
    else:
        for child in graph[next_node_to_explore]:
            if child in visited_node:
                continue
            fringe.append(child)
        return BFS(graph=graph, goal_node=goal_node, visited_node=visited_node, fringe=fringe)

print("traversed path: ", str(BFS(graph=graph, goal_node='5', fringe=['1'])))


def BFS_shortest_path(graph, start_node, goal_node):
    visited = []
    fringe = [[start_node]]

    if start_node == goal_node:
        return [start_node]
    
    while fringe:
        
        path = fringe.pop(0)
        node = path[-1]
        print("fringe: ", fringe, " visited: ", visited, " path: ", path, " node: ", node)
        if node not in visited:
            for child in graph[node]:
                new_path = list(path)
                new_path.append(child)
                print("child: ", child, " new path: ",new_path)
                fringe.append(new_path)

                if child == goal_node:
                    return new_path
            
            visited.append(node)
    
    return False

print(BFS_shortest_path(graph=graph, start_node='1', goal_node='5'))
