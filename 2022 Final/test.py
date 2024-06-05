def find_cycles(graph):
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    for node in graph:
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True

    return False

# Example graph
graph = {
    '0': ['1', '2', '3', '4'],
    '1': ['0', '2'],
    '2': ['1', '0', '3', '5'],
    '3': ['0', '2', '4', '5'],
    '4': ['0', '3', '5'],
    '5': ['2', '3', '4']
}

if find_cycles(graph):
    print("The graph has a cycle.")
else:
    print("The graph has no cycles.")
