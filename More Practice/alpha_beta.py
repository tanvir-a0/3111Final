visited_node = []
def alpha_beta(graph, terminal_values, root, state, alpha, beta):

    if root in terminal_values:
        visited_node.append(root)
        return terminal_values[root]
    
    if state == True:
        v = -float('inf')
        for child in graph[root]:
            visited_node.append(child)
            v = max(v,alpha_beta(graph, terminal_values, child, False, alpha, beta))
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v


    if state == False:
        v = float('inf')
        for child in graph[root]:
            visited_node.append(child)
            v = min(v, alpha_beta(graph, terminal_values, child, True, alpha, beta))
            beta = min(v, beta)
            if alpha >= beta:
                break
        return v
    
with open('alpha_beta.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        lines[i] = lines[i].split(" ")
    line_no = int(lines[0][0])
    root = lines[0][1]
    graph = {}
    for i in range(0+1, line_no+1):
        graph[lines[i][0]] = lines[i][1:]
    #print(lines, line_no, root)
    #print(graph)

    terminal_node_count = int(lines[1+line_no][0])
    terminal_nodes = {}
    #print("tnc: ", terminal_node_count)
    for i in range(0+1+line_no+1, line_no+1+terminal_node_count+1):
        terminal_nodes[lines[i][0]] = int(lines[i][1])
        #print(lines[i])
    print(graph)
    print(terminal_nodes)
    print(alpha_beta(graph=graph,terminal_values=terminal_nodes,root= lines[0][1], state=True, alpha=-float('inf'), beta=float('inf')))

    all_node = []
    for key in graph:
        all_node.append(key)
        for child in graph[key]:
            all_node.append(child)
    all_node = set(all_node)
    all_node = sorted(all_node)
    print("all nodes: ", all_node)
    visited_node.append(root)
    visited_node = set(visited_node)
    visited_node = sorted(visited_node)
    print("visited nodes: ", visited_node)
    pruned_node = []
    for element in all_node:
        if element not in visited_node:
            pruned_node.append(element)
    print("pruned nodes: ", pruned_node)
    print(visited_node)

    