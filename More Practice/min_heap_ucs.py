class Min_Heap:
    def __init__(self, heuristics):
        self.heap = []
    
    def get_size(self):
        return len(self.heap)
    
    def reheapup(self):
        if self.get_size() <= 1:
            return 
        
        ci = self.get_size() - 1
        
        while True:
            pi = (ci - 1)//2
            if pi < 0:
                break

            if self.heap[pi][1] <= self.heap[ci][1]:
                #everythin is ok
                pass
            else: 
                self.heap[pi] , self.heap[ci] = self.heap[ci] , self.heap[pi]
            
            ci = pi


    
    def enqueue(self, data):
        self.heap.append(data)
        self.reheapup()

    def reheapdown(self):
        pi = 0
        while True:
            lci = 2*pi + 1
            rci = 2*pi + 2
            

            if lci >= self.get_size():
                lci = self.get_size() - 1
            if rci >= self.get_size():
                rci = self.get_size() - 1
            

            mci = pi
            if self.heap[lci][1] < self.heap[pi][1] and self.heap[lci][1] <= self.heap[rci][1]:
                mci = lci
            
            if self.heap[rci][1] < self.heap[lci][1] and self.heap[rci][1] <= self.heap[pi][1]:
                mci = rci
            #print("lv: ", self.heap[lci][1], " rv: ", self.heap[rci][1], " pv: ", self.heap[pi][1])
            #print("pi: ", pi, " lci: ", lci, " rci: ", rci," mci: ", mci,  " heap: ", self.heap)
            
            if pi == mci:
                break

            self.heap[pi] , self.heap[mci] = self.heap[mci], self.heap[pi]
            pi = mci
    
    def dequeue(self):
        #print("\n\n size: ", self.get_size())
        if self.get_size() == 0:
            print("There is no data in heap ", self.get_size())
            return None
        
        if self.get_size() == 1:
            tmp = self.heap.pop(0)
            return tmp
        
        tmp = self.heap[0]
        self.heap[0] = self.heap[self.get_size() - 1]
        self.heap.pop(self.get_size() - 1)
        self.reheapdown()
        return tmp

    def __str__(self):
        return str(self.heap)
    
# queue = Min_Heap()
# queue.enqueue(('s',4))
# queue.enqueue(('a',5))
# queue.enqueue(('d', 88))
# queue.enqueue(('f', 96))
# queue.enqueue(('g',2))
# queue.enqueue(('h',645))
# queue.enqueue(('j', 87))
# queue.enqueue(('k',61))
# queue.enqueue(('l',70))
# queue.enqueue(('z',31))
# queue.enqueue(('x', 33))
# print(queue)

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
