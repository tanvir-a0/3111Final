import time

class Max_Heap:
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
            if self.heap[child_index] < self.heap[parent_index]:
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
        max_child_index = parent_index

        while True:
            #print("pi: ", parent_index, " lci: ", left_child_index, " rci: ", right_child_index, " size: ", self.get_size())
            #print(self.heap)
            #time.sleep(1)
            if self.heap[left_child_index] < self.heap[right_child_index] and self.heap[parent_index] < self.heap[right_child_index]:
                #swap parent with right child
                max_child_index = right_child_index

            if self.heap[left_child_index] > self.heap[right_child_index] and self.heap[left_child_index] > self.heap[parent_index]:
                #swap with right child
                max_child_index = left_child_index
            
            self.heap[max_child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[max_child_index]
            
            if max_child_index == parent_index:
                break

            parent_index = max_child_index
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


queue = Max_Heap()
queue.enqueue(4)
queue.enqueue(12)
queue.enqueue(88)
queue.enqueue(9)
queue.enqueue(43)
queue.enqueue(25)
queue.enqueue(77)
queue.enqueue(61)
queue.enqueue(70)
queue.enqueue(31)
queue.enqueue(33)


print(queue.dequue())
print(queue.dequue())
print(queue.dequue())
print(queue.dequue())
print(queue.dequue())










