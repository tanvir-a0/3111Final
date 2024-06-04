import time
class BFS:
    def __init__(self, graph, source, target):
        self.graph = graph
        self.source = source
        self.target = target
        self.fringe = [] #first in first out
        self.visited = []
    
    def find_traverse_path(self):
        self.fringe.append(self.source)
        while len(self.fringe) != 0:
            #print(self.fringe, self.visited)
            #time.sleep(2)
            parent = self.fringe.pop(0)
            if parent in self.visited:
                continue
            self.visited.append(parent)
            if parent == self.target:
                break
            for child in self.graph[parent]:
                if child in self.visited:
                    pass
                else:
                    self.fringe.append(child)
        return(self.visited)
    
    def find_original_path(self):
            self.fringe.append(self.source)
            while len(self.fringe) != 0:
                print(self.fringe, self.visited)
                time.sleep(2)
                parent = self.fringe.pop(0)
                if parent in self.visited:
                    continue
                self.visited.append(parent)
                if parent == self.target:
                    break
                for child in self.graph[parent]:
                    if child in self.visited:
                        pass
                    else:
                        self.fringe.append(child)
            return(self.visited)


graph1 = {
    "0": ["1", '2', '3'],
    '1': ['5', '6'],
    '2': ['6'],
    '3': ['7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
}
graph2 = {
    '0': ['1', '3'],
    '3': ['0', '1', '2', '4'],
    '1': ['0', '3', '2', '5', '6'],
    '2': ['1', '3', '4', '5'],
    '4': ['2', '3', '6'],
    '5': ['1', '2'],
    '6': ['1', '4']
}
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
bfs = BFS(graph3, '1','10')
print(bfs.find_traverse_path())
