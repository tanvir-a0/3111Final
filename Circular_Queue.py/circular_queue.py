class Circular_Queue:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.item = []
        for i in range(0, size):
            self.item.append(None)
        

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("The Queue is full.")
            print(self)
            return
        
        if self.front == -1 and self.rear == -1:
            #This is the first value
            self.front = 0
            self.rear = 0
            self.item[self.rear] = data
            print(self)
            return
        
        self.rear = self.rear + 1
        if self.rear == self.size:
            self.rear = 0
        self.item[self.rear] = data
        print(self)

    def dequeue(self):
        if(self.front == -1):
            print("There is no data to dequeue")
            print(self)
            return
        
        if self.front == self.rear:
            #There is only one data left
            tmp = self.item[self.front]
            self.item[self.front] = None
            self.front = -1
            self.rear = -1
            print(self)
            return tmp

        tmp = self.item[self.front]
        self.item[self.front] = None
        self.front = (self.front + 1)%self.size
        print(self)
        return tmp

        
    def __str__(self):
        return str(self.item)+ "  Front: "+ str(self.front)+ "  Rear: "+ str(self.rear)

cq = Circular_Queue(5)
cq.enqueue(5)
cq.enqueue(15)
cq.enqueue(20)
cq.enqueue(64)
cq.enqueue(78)
cq.enqueue(98)
cq.dequeue()
cq.enqueue(25)
cq.enqueue(25)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.enqueue(78)
cq.enqueue(61)
cq.enqueue(8615)
cq.enqueue(67)
cq.enqueue(64)