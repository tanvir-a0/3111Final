import time

class DFS:
    def __init__(self, graph, source, target):
        self.graph = graph
        self.source = source
        self.target = target
        self.fringe = [] #FIFO
        self.visited = []

    
    def find_traverse_path(self):
        self.fringe.append(self.source)

        while(len(self.fringe) != 0):
            parent = self.fringe.pop(len(self.fringe)-1)

            if parent in self.visited:
                continue

            self.visited.append(parent)

            if parent == self.target:
                print("Reached the goal")
                break

            for child in self.graph[parent]:
                if child in self.visited:
                    pass
                else:
                    self.fringe.append(child)
            print(self.visited, self.fringe)

        return self.visited
    
graph3 = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12'],
    '9': [],
    '10': [],
    '6': [],
    '3': [],
    '8': [],
    '11': [],
    '12': []
}
dfs = DFS(graph3, '1','10')
print(dfs.find_traverse_path())
