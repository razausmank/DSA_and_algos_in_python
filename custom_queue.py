class Queue: 
    def __init__(self): 
        self.head = None
        self.tail = None
        self.size = 0 
    
    def enqueue(self, data): 
        node = Node(data)
        
        if None == self.head : 
           self.head = node
        else: 
            self.tail.ptr = node 
            
        self.tail = node 
        self.size +=  1 
    
    def dequeue(self): 
        if self.is_empty() : 
            return "Its an empty queue"

        data = self.head.data 
        self.head = self.head.ptr 
        self.size -= 1 
        return data 
    
    def peek(self):
        return self.tail.data if self.tail  else "its an empty queue"     
    
    def print(self): 
        ptr = self.head 
        
        while ptr : 
            print(f"{ptr.data} | {ptr.ptr}")
            ptr = ptr.ptr 
    
    def is_empty(self):
        return True if self.size == 0 else False 
    
    def contains(self, data): 
        ptr = self.head 
        
        while ptr: 
            if data == ptr.data : 
                return True 
            ptr = ptr.ptr 

        return False 
        

class Node: 
    def __init__(self, data):
        self.data = data   
        self.ptr = None 
    
if __name__ == "__main__" : 
    
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    queue.print()
    
    print(queue.contains(30))
    print(queue.contains(60))
    print(queue.contains(10))
    
    
    print() 
    queue.dequeue()
    queue.print()
    
    print() 

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.print()
    
    print() 

    print(queue.contains(30))
    print(queue.contains(60))
    print(queue.contains(50))
    
    
    