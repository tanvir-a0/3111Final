def MiniMax(graph, root, terminal_values, state = True):

    if len(graph[root]) == 0:
        #This is the terminal value
        return terminal_values[root]

    if state == True:
        #calculate max
        v = -float('inf')
        for child in graph[root]:
            v = max(v, MiniMax(graph, child, terminal_values, False))
        return v
    
    if state == False:
        #calculate min
        v = +float('inf')
        for child in graph[root]:
            v = min(v, MiniMax(graph, child, terminal_values, True))
        return v
    

graph1 = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': ['h', 'i'],
    'e': ['j', 'k'],
    'f': ['l', 'm'],
    'g': ['n', 'o'],
    'h': [],
    'i': [],
    'j': [],
    'k': [],
    'l': [],
    'm': [],
    'n': [],
    'o': []
}

terminal_values1 = {
    'h': -1,
    'i': 4,
    'j': 2,
    'k': 6,
    'l': -3,
    'm': -5,
    'n': 0,
    'o': 7
}

print(MiniMax(graph1, 'a', terminal_values1))