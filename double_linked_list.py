class DoubleLinkedList(): 
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def add_node(self, data):
        node = Node(data=data)
        
        if  None == self.head :
            self.head = node 
        else : 
            node.bck_ptr = self.tail 
            self.tail.frw_ptr = node 
            
        self.tail = node  
        
    def print(self): 
        ptr = self.head 
        
        while ptr : 
            print(f" {"None" if ptr.bck_ptr is None  else id(ptr.bck_ptr) } | {ptr.data} | {"None" if ptr.frw_ptr is None else id(ptr.frw_ptr) } - node add - {id(ptr)}")
            ptr = ptr.frw_ptr
    
    def find(self, data):
        ptr = self.head 
        
        while ptr : 
            if data == ptr.data : 
                return ptr.data 
            
            ptr = ptr.frw_ptr

        return -1 
    
    # not handling if the node is first or last
    def remove_node(self , position): 
        ptr = self.head 
        
        for i in range(1,position):
            ptr = ptr.frw_ptr           
        
        back_node = ptr.bck_ptr 
        front_node = ptr.frw_ptr
        
        back_node.frw_ptr = front_node
        front_node.bck_ptr = back_node 
        
        return ptr 
    
class Node(): 
    def __init__(self, data):
        self.frw_ptr = None 
        self.data = data
        self.bck_ptr = None
        
        

list = DoubleLinkedList()
list.add_node(10) 
list.add_node(20)
list.add_node(30)
list.add_node(40)

list.print()

print(list.find(30))

print(list.remove_node(3))

print()

list.print()
