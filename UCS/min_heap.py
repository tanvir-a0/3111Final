import time

class Min_Heap:
    def __init__(self):
        self.heap = []

    def reheap_up(self):
        if (self.get_size() <= 1):
            #don't need to be reheap up
            return
        
        child_index = len(self.heap) - 1
        parent_index = (child_index - 1)//2

        while True:
            #print("ci: ", child_index, " pi: ", parent_index)
            #print(self.heap)
            if self.heap[child_index][1] > self.heap[parent_index][1] :
                #swap them
                self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
            
            parent_index = child_index
            child_index = (child_index - 1)//2

            if child_index < 0:
                break

    def get_size(self):
        return len(self.heap)
    
    def reheap_down(self):
        parent_index = 0
        left_child_index = 2*parent_index + 1
        right_child_index = 2*parent_index + 2
        min_child_index = parent_index

        if left_child_index >= self.get_size():
            left_child_index = self.get_size() - 1
        if right_child_index >= self.get_size():
            right_child_index = self.get_size() - 1

        while True:
            print("pi: ", parent_index, " lci: ", left_child_index, " rci: ", right_child_index, " size: ", self.get_size())
            print(self.heap)
            #time.sleep(1)
            if self.heap[left_child_index][1]  > self.heap[right_child_index][1] and self.heap[parent_index][1] > self.heap[right_child_index][1]:
                #swap parent with right child
                min_child_index = right_child_index

            if self.heap[left_child_index][1] < self.heap[right_child_index][1] and self.heap[left_child_index][1] < self.heap[parent_index][1]:
                #swap with right child
                min_child_index = left_child_index
            
            self.heap[min_child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[min_child_index]
            
            if min_child_index == parent_index:
                break

            parent_index = min_child_index
            left_child_index = 2*parent_index + 1
            right_child_index = 2*parent_index + 2

            if left_child_index >= self.get_size() and right_child_index >= self.get_size():
                break

            if left_child_index >= self.get_size():
                left_child_index = self.get_size() - 1
            if right_child_index >= self.get_size():
                right_child_index = self.get_size() - 1

            
    
    def enqueue(self, data):
        self.heap.append(data)
        self.reheap_up()
        #print(self.heap)

    def dequue(self):
        print("len: ", self.get_size())
        if self.get_size() == 0:
            print("There is no data")
        elif self.get_size() == 1:
            #print(self.heap)
            return self.heap.pop()
        else:
            tmp = self.heap[0]
            self.heap[0], self.heap[self.get_size()-1] = self.heap[self.get_size() - 1], self.heap[0]
            self.heap.pop()
            self.reheap_down()
            #print(self.heap)
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


# print(queue.dequue())
# print(queue.dequue())
# print(queue.dequue())
# print(queue.dequue())
# print(queue.dequue())










