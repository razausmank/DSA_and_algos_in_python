class Stack: 
    
    
    def __init__(self):
        self.head = None
        self.length = 0 
        
    def push(self, data): 
        node = self.__Node(data)
        
        if self.head == None: 
            self.head = node 
        else: 
            node.ptr = self.head 
            self.head = node
            
        self.length += 1 
    
    def pop(self): 
        if 0 == self.length : 
            return "Stack is empty"  
        data = self.head.data 
        self.head = self.head.ptr 
        self.length -= 1 
        
        
        return data 
    
    def print(self): 
        if 0 == self.length : 
            return print("stack is empty") 
        ptr = self.head 
        
        while ptr : 
            print(f"{ptr.data} | {ptr.ptr}")
            ptr = ptr.ptr 
            
        print(f"head is {self.head.data}")
        
    def peek(self): 
        return self.head.data
    
    def is_empty(self): 
        return True if 0 == self.length else False 
    
    class __Node(): 
        def __init__(self, data):
            self.data = data
            self.ptr = None  
            
if __name__ == "__main__" : 
    stack = Stack() 

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print()
    print()

    print(stack.pop())

    print()

    print(stack.print())

    print(stack.length)
    print()

    print(stack.pop())

    stack.print()
    print('asd')

    print(stack.pop())
    stack.print()
    print()


    print(stack.pop())


