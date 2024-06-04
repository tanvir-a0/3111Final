class Linear_Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop(0)
    
    def __str__(self):
        return str(self.items)

lq = Linear_Queue()
lq.push(5)
lq.push(6)
lq.push(15)
lq.push(58)
lq.push(95)
print(lq)

lq.pop()
lq.pop()
print(lq)
