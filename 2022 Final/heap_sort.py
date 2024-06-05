import time
import copy


class Max_Heap:
    def __init__(self):
        self.heap = []

    def reheap_up(self):
        if(len(self.heap) == 1):
            return
        
        child_index = len(self.heap) - 1
        while True:
            parent_index = (child_index - 1)//2

            print("ci: ", child_index, " pi: ", parent_index)
            #time.sleep(2)

            if parent_index < 0:
                break

            if self.heap[child_index] <= self.heap[parent_index]:
                #everything is ok
                pass
            else:
                self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
            
            child_index = parent_index
    
    def __str__(self):
        return str(self.heap)


    def enqueue(self, data):
        self.heap.append(data)
        self.reheap_up()

    def reheap_down(self):
        pi = 0
        lci = 2*pi + 1
        rci = 2*pi + 2

        while True:
            max_child_index = pi
            lci = 2*pi + 1
            rci = 2*pi + 2

            if lci >= len(self.heap):
                lci = len(self.heap) - 1
            if rci >= len(self.heap):
                rci = len(self.heap) - 1
            if rci >= len(self.heap) and lci>= len(self.heap):
                break

            if self.heap[pi] < self.heap[lci] and self.heap[rci] < self.heap[lci]:
                #swap parent with left
                max_child_index = lci
            if self.heap[pi] < self.heap[rci] and self.heap[lci] < self.heap[rci]:
                #swap parent with right
                max_child_index = rci

            if max_child_index == pi:
                break
            else:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
                pi = max_child_index


    def dequeue(self):
        if len(self.heap) == 0:
            print("There is no data")
            return 
        if len(self.heap) == 1:
            tmp = self.heap.pop()
            return tmp
        tmp = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        self.reheap_down()
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
print(queue)


print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
