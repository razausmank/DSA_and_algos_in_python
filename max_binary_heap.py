import math 

class MaxBinaryHeap:
    def __init__(self):
        self.array = [] 
        self.size = 0  
        self.tail = -1 # tail will be the index 
        
    def insert(self, data): 
        self.array.append(data)
        self.size += 1 
        self.tail += 1 
        
        print(self.array)        
        if self.size > 1 : 
            self.heapify_up(self.tail)
        print(self.array)        
        
            

    def traverse_up(self, index): 
        parent_index = None 
        if 0 != index:
            parent_index = math.floor((index-1)/2) 
        
        return parent_index
    
    def traverse_down_left(self,index): 
        child_index = 2(index) + 1 
        if child_index > self.size : 
            return -1 
        return child_index 
    
    def traverse_down_right(self,index): 
        child_index = 2(index) + 2 
        if child_index > self.size : 
            return -1 
        return child_index
    
    def heapify_up(self, index):
        # run an infinite loop
        while True:
            # check if index is the root node 
            # if it is break the loop 
            if index == 0 : 
                return  
            # compare the element with its parent
            # if the element is less than its parents break the loop 
            parent_index = self.traverse_up(index)
            parent  = self.array[parent_index]
            if self.array[index] < parent: 
                return 

            self.swap_values(index , parent_index)
            index = parent_index
            # if it is greater then swap both of them 

    def swap_values(self, index_a, index_b): 
        temp = self.array[index_a]
        self.array[index_a] = self.array[index_b] 
        self.array[index_b] = temp   
    
    def find(self, data):
        index = None 
        if data in self.array: 
            index = self.array.index(data)
        return index 
    
    def heapify_down(self, index): 
         while True: 
                
            if index == self.tail : 
                return  
        
            left_child_index = self.traverse_down_left(index)
            right_child_index = self.traverse_down_right(index)
            
            main_index = left_child_index if self.array[left_child_index] > self.array[right_child_index] else right_child_index 
            
            if self.array[index] < self.array[main_index]: 
                self.swap_values(index, main_index)
                
            index = main_index 
            
    def remove(self, data): 
        # we find the element 
        index = self.find(data)
        if None == index :  
            return "Index doesn't exist "
        # we swap it out with the last element 
        self.swap_values(index, self.tail)
        # and then we remove it 
        self.array.pop()
        self.size -= 1 
        self.tail -= 1 
        
        # the element we swapped it with we check both its parent element first if its bigger 
        # we check its child element 
        # depending on that we heapify up or we heapify down 

        if 0 != index : 
            print(index)
            parent_index = self.traverse_up(index)
            if self.array[index] > self.array[parent_index] : 
                self.heapify_up(index)    
                # break this 
            else: 
                print('here')
                self.heapify_down(index)
            # now  if the element is smaller than the parent node get both children nodes and find out the smaller one 
           
            
            
            
if  "__main__" == __name__: 
    heap = MaxBinaryHeap() 

    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(40)
    print()
    heap.insert(10)
    heap.insert(50)
    heap.insert(20)
    print(heap.array)
    heap.remove(50)
    print(heap.array)
    