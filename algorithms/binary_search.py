import math

x = 4 
my_array = [ 1,2,3,4,5,6,7,8,9,10 ]

my_array_length = len(my_array)  
low = 0 
high = my_array_length - 1 
found = False 

while low != high : 
    
    if len(my_array[low:high]) % 2 == 0 : 
        mid_index = int(len(my_array[low:high]) / 2 ) - 1  
        mid_elem  = my_array[mid_index] + my_array[mid_index + 1]
    else: 
        mid_index = math.floor(len(my_array[low:high]) / 2 )
        mid_elem = my_array[mid_index] 
        
    print("iteration")
    if x == mid_elem : 
        found = True 
        break  
    elif x > mid_elem : 
        low = mid_index
    else : 
        high = mid_index    

print("found it" if found else "not found" )
        
        
        
        
        
# run the loop until low ==
        
        
    
    
    
    