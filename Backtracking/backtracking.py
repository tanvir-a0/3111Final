graph = {
    '0': ['1','2','3'],
    '1': ['0','2'],
    '2': ['0','1','3'],
    '3': ['0','2']
}

domain = ['r', 'g', 'b']
color_assignment = {}

#finding the next vertex
# print(list(graph.keys())[list(graph.keys()).index('0') + 1])
# print(type(list(graph.keys())[list(graph.keys()).index('0') + 1]))

def is_corroect(vertex, color, graph, color_assignment):
    for neighbour in graph[vertex]:
        if neighbour not in color_assignment.keys():
            return True
        if color_assignment[neighbour] == color:
            return False
    return True
    
def graphColoringBT(graph, color_assignment, vertex):
    print(color_assignment)
    print(vertex)
    if (len(color_assignment) == len(graph)):
        return True
    
    for c in domain:
        if(is_corroect(graph=graph, color=c, vertex=vertex, color_assignment=color_assignment)):
            color_assignment[vertex] = c
            if (len(color_assignment) == len(graph)):
                print("returning from here")
                print(color_assignment)
                return True
            if graphColoringBT(graph=graph, color_assignment=color_assignment, vertex=  list(graph.keys())[list(graph.keys()).index(vertex) + 1] ) :
                return True
            else:
                del color_assignment[vertex]
    return False

print(graphColoringBT(graph=graph, color_assignment=color_assignment, vertex='0'))
