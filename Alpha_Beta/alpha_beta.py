visited_node = []

def MiniMax(graph, root, terminal_values, state , alpha, beta):

    if root in terminal_values:
        #This is the terminal value
        visited_node.append(root)
        return terminal_values[root]

    if state == True:
        #calculate max
        v = -float('inf')
        for child in graph[root]:
            v = max(v, MiniMax(graph, child, terminal_values, False, alpha, beta))
            alpha = max(alpha, v)
            visited_node.append(child)
            if alpha >= beta:
                break
        return v
    
    if state == False:
        #calculate min
        v = +float('inf')
        for child in graph[root]:
            v = min(v, MiniMax(graph, child, terminal_values, True, alpha, beta))
            beta = min(v, beta)
            visited_node.append(child)
            if alpha >= beta:
                break
        return v
    
def find_pruned_node(graph, root):
    visited_node.append(root)
    all_node = []
    for key in graph:
        all_node.append(key)
        for node in graph[key]:
            all_node.append(node)
    all_node = set(all_node)
    visited_node_temp = set(visited_node)
    pruned_node = []
    for node in all_node:
        if node not in visited_node_temp:
            pruned_node.append(node)
    print(pruned_node)

graph1 = {
    'a': ['b', 'c', 'd'],
    'b': ['e', 'f'],
    'c': ['g', 'h'],
    'd': ['i', 'j'],
    'e': ['k', 'l'],
    'f': ['m'],
    'g': ['n', 'o'],
    'h': ['p'],
    'i': ['q'],
    'j': ['r', 's'],
    'k': ['t', 'u'],
    'l': ['v', 'w', 'x'],
    'm': ['y'],
    'n': ['z'],
    'o': ['aa', 'ab'],
    'p': ['ac'],
    'q': ['ad'],
    'r': ['ae', 'af'],
    's': ['ag']
}

terminal_values1 = {
    't': 5,
    'u': 6,
    'v': 7,
    'w': 4,
    'x': 5,
    'y': 3,
    'z': 6,
    'aa': 6,
    'ab': 9,
    'ac': 7,
    'ad': 5,
    'ae': 9,
    'af': 8,
    'ag': 6
}

print(MiniMax(graph=graph1, root='a', terminal_values=terminal_values1, state=True, alpha=-float('inf'), beta=float('inf')))
print(visited_node)
find_pruned_node(graph=graph1, root='a')