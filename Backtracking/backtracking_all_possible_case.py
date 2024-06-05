graph = {
    '0': ['1', '2', '3'],
    '1': ['0', '2'],
    '2': ['0', '1', '3'],
    '3': ['0', '2']
}

domain = ['r', 'g', 'b']
color_assignment = {}

def is_correct(vertex, color, graph, color_assignment):
    for neighbour in graph[vertex]:
        if neighbour in color_assignment and color_assignment[neighbour] == color:
            return False
    return True
    
def graphColoringBT(graph, color_assignment, vertex, all_solutions):
    if len(color_assignment) == len(graph):
        all_solutions.append(color_assignment.copy())
        return
    
    for c in domain:
        if is_correct(vertex=vertex, color=c, graph=graph, color_assignment=color_assignment):
            color_assignment[vertex] = c
            next_vertex_index = list(graph.keys()).index(vertex) + 1
            if next_vertex_index < len(graph):
                next_vertex = list(graph.keys())[next_vertex_index]
                graphColoringBT(graph=graph, color_assignment=color_assignment, vertex=next_vertex, all_solutions=all_solutions)
            else:
                graphColoringBT(graph=graph, color_assignment=color_assignment, vertex=None, all_solutions=all_solutions)
            del color_assignment[vertex]

all_solutions = []
graphColoringBT(graph=graph, color_assignment=color_assignment, vertex='0', all_solutions=all_solutions)

print(f"Total solutions: {len(all_solutions)}")
for solution in all_solutions:
    print(solution)
