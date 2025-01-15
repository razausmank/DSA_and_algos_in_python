
class DynamicArray(): 
    def __init__(self, init_size=5):
        self.array = [None] * init_size 
        self.pointer = 0 
        
    def __str__(self):
        return f"{self.array[0:self.pointer]}"
        
    def __getitem__(self, key): 
        return self.array[key] 
    
    def append(self, item): 
        if ( self.pointer >= len(self.array)): 
            self.increase_array_size()
        self.array[self.pointer] = item
        self.pointer += 1 
        
    def increase_array_size(self): 
        self.array = self.array + ([None] * ( len(self.array) )) 
        
    def remove(self, target_index): 
        if (target_index > len(self.array) ) : 
            raise IndexError("Index Out of Bounds - i.e write an index that isnt bigger than the array size stupid")
        
        if(target_index > self.pointer): 
            return 
        
        temp = self.array 
        new_length = len(temp) - 1
        self.array = [None] * new_length
        
        counter = 0  
        for index in range(0,len(temp)):
            if index == target_index  : 
                continue
            self.array[counter] = temp[index]
            counter += 1  
        self.pointer -= 1 
        
    def find(self, item):
        for i in range(0, len(self.array)): 
            if ( self.array[i] == item ): 
                return i 
        
        return -1 
             
            
arr = DynamicArray() 

arr.append(1) 
arr.append(2) 
arr.append(3) 
arr.append(4) 
arr.append(5) 
arr.append(6) 

print(len(arr.array))
print(arr.array)

arr.remove(8)
print(len(arr.array))
print(arr.array)
print(arr)
arr.append(7) 
print(arr)
arr.remove(6)
print(arr)
print( arr.find(5) )