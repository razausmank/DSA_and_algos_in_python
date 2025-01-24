import gc 
class LinkedList(): 
    def __init__(self): 
        self.head = None 
        self.tail = None 

    def add_node(self, data): 
        node = Node(data=data)  
            
        if self.head is None : 
            self.head = node
        else : 
            self.tail.pointer = node 
            
        self.tail = node
        
    def print(self):
        ptr = self.head 
        while ptr != None: 
            print(f"{id(ptr)} | {ptr.data} | {id(ptr.pointer)}")
             
            ptr = ptr.pointer
    
    def remove_node(self, position): 
        ptr = self.head 

        if position == 1 : 
            self.head = ptr.pointer
            return self.head.data
 
        for i in range(1,position-1):
            ptr = ptr.pointer           
            
        bfr_ptr = ptr
        if bfr_ptr.pointer.pointer == None: 
            bfr_ptr.pointer = None 
            self.tail = bfr_ptr
        else:     
            bfr_ptr.pointer = ptr.pointer.pointer
        return ptr.data
    
    def find(self, data): 
        ptr = self.head 
        
        while ptr: 
            if ptr.data == data : 
                return ptr.data  
            ptr = ptr.pointer 
        
        return -1     
        
class Node(): 
    def __init__(self, data , pointer=None ): 
        self.data = data
        self.pointer = pointer 
        
    # def __str__(self):
    #     return f" {self.data} | {self.pointer} "
    

    
test = Node(data='test')

# print(test)

list = LinkedList()
list.add_node(10)
list.add_node(20)
list.add_node(30)
list.add_node(40)
list.add_node(50)
list.add_node(60)
list.add_node(70)
list.add_node(80)
list.add_node(90)


list.print()
print(list.head.data)

print(list.remove_node(1))

list.print()

print(list.head.data)

print(list.find(150)) 