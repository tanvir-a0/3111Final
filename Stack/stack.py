class Stack:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        print(len(self.item))
        return len(self.item) == 0
    
    def push(self,data):
        self.item.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("There is no more data on the stack")
        
        return self.item.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("There is no more data")
        
        return self.item[0]

    def size(self):
        return len(self.item)
    
    def __str__(self):
        return str(self.item)
    


stack = Stack()
stack.push(5)
stack.push(5)
stack.push(10)
stack.push(25)
stack.push(65)

print(stack)

print("popped: ",stack.pop(), "  now stack: ", stack)



        