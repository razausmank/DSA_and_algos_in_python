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
        child_index = (2*index) + 1 
        if child_index >= self.size : 
            return None
        return child_index 
    
    def traverse_down_right(self,index): 
        child_index = (2*index) + 2 
        if child_index >= self.size : 
            return None 
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
            print('in heapify down true loop')
            if index == self.tail : 
                return  
        
            if self.traverse_down_left(index) and self.traverse_down_right(index): 
                min_index = self.traverse_down_left(index) if self.array[self.traverse_down_left(index)] >= self.array[self.traverse_down_right(index)] else self.traverse_down_right(index) 
                
                if  self.array[index] < self.array[min_index]: 
                    self.swap_values(index, min_index) 
                    index = min_index
                else :  
                    return  
                    
            elif self.traverse_down_left(index) : 
                min_index = self.traverse_down_left(index) 
                  
                if  self.array[index] < self.array[min_index]: 
                    self.swap_values(index, min_index) 
                    index = min_index
                else :  
                    return  
                
            
            
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
        print(index)

        parent_index = self.traverse_up(index)
        if self.array[index] > self.array[parent_index] : 
            print("heapify up")
            self.heapify_up(index)   
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
    heap.insert(200)

# notes 
# Below is an analysis of your implementation. Overall the structure is mostly correct, but there are a couple of logical issues that can lead to incorrect behavior (or even an infinite loop) in some edge cases. Here are the points to consider:

# ---

# ### 1. **The Termination Condition in `heapify_down`**

# In your `heapify_down` method you begin each loop with

# ```python
# if index == self.tail:
#     return
# ```

# **Issue:**  
# This check is intended to stop when you reach a “leaf.” However, in a binary heap (stored as an array) all leaves are not necessarily at the very last index (`self.tail`). In a complete binary tree, all nodes with indices from `floor(size/2)` to `size - 1` are leaves. It is quite possible that you call `heapify_down` on a node that is a leaf (has no children) but whose index is not equal to `self.tail`. In that situation, neither child exists so both
# ```python
# self.traverse_down_left(index)
# ```
# and
# ```python
# self.traverse_down_right(index)
# ```
# will return a valid index. Then none of your `if/elif` conditions match, and the `while True` loop never breaks.

# **How to Fix:**  
# Instead of checking `if index == self.tail`, you should check whether the left child exists. For example, you could do:
  
# ```python
# def heapify_down(self, index):
#     while True:
#         left = self.traverse_down_left(index)
#         right = self.traverse_down_right(index)
        
#         # If no left child exists, then no children exist.
#         if left is None:
#             return
        
#         # Choose the child with the larger value.
#         if right is not None and self.array[right] > self.array[left]:
#             swap_index = right
#         else:
#             swap_index = left

#         if self.array[index] < self.array[swap_index]:
#             self.swap_values(index, swap_index)
#             index = swap_index
#         else:
#             return
# ```
# This way you properly check for the existence of children and break out of the loop when the current node is a leaf.

# ---

# ### 2. **Handling the Direction After Removal**

# Your `remove` method currently works as follows:
  
# 1. Find the index of the element to remove.
# 2. Swap it with the last element (using `self.tail`).
# 3. Remove the last element.
# 4. Then check:
#    - If the removed element’s index is **not** 0 (i.e. not the root), you compare it to its parent and, if it is larger than its parent, you call `heapify_up`.
#    - If the index is 0, you call `heapify_down`.

# **Issue:**  
# When the removed element is replaced by the last element, that new element might need to be “repaired” in **both directions**. In a typical heap‐removal procedure, after swapping in the last element you decide whether to move it up or down (or sometimes even both, though one direction will eventually “absorb” the needed adjustment).  
  
# Your code only calls:
# - `heapify_up` if the swapped element is greater than its parent.
# - `heapify_down` only if the removed element was at the root.
  
# This leaves a gap when the removed element is not at the root but the new element is smaller than one or both of its children. In that case, the new element might violate the heap property with respect to its children, yet you never call `heapify_down`.

# **How to Fix:**  
# A common approach is to always perform one of the two adjustments. One strategy is:
  
# - First, try to “sink” (heapify down) the swapped element.
# - Then, if the element did not move (or if you suspect that it might still be too large for its parent) you can “bubble up” (heapify up) if needed.
  
# Alternatively, you can compare the swapped element both with its parent and its children and decide which direction to repair:
  
# ```python
# def remove(self, data):
#     index = self.find(data)
#     if index is None:
#         return "Index doesn't exist"
    
#     # Swap with last element and remove
#     self.swap_values(index, self.tail)
#     self.array.pop()
#     self.size -= 1
#     self.tail -= 1

#     # If the removed element was the last one, no fixup is needed.
#     if index >= self.size:
#         return

#     # Decide which way to go.
#     parent_index = self.traverse_up(index)
#     # If there is a parent and the new element is greater than the parent, bubble up.
#     if parent_index is not None and self.array[index] > self.array[parent_index]:
#         self.heapify_up(index)
#     else:
#         # Otherwise, sink it down.
#         self.heapify_down(index)
# ```
# This way you cover both cases. (Note: in a production system you might even call both in sequence because in some edge cases one call might not completely fix the position—but with a proper heapify procedure one of the directions will settle the element into its correct spot.)

# ---

# ### 3. **Other Observations**

# - **Naming:**  
#   In your `heapify_down` method the variable `min_index` is used to store the index of the child with the larger value. Although this works correctly, it might be clearer to rename it to something like `swap_index` or `max_child_index` since this is a *max* binary heap.

# - **Redundant Attributes:**  
#   You maintain both `self.size` and `self.tail` even though they are both derived from the length of the underlying array (with `tail == self.size - 1`). This isn’t a logical error, but it adds extra state that you must be careful to update consistently.

# ---

# ### **Summary**

# 1. **`heapify_down` termination condition:**  
#    Replace the check `if index == self.tail` with a check on whether the left child exists. This prevents an infinite loop when the node is a leaf but not the last element in the array.

# 2. **Removal “fixup” direction:**  
#    In `remove`, after swapping in the last element you should consider that the new element might violate the heap property downward (even if it does not violate it upward). Deciding which direction to heapify (or even calling both if necessary) will help maintain the heap invariant.

# Addressing these issues should improve the correctness of your max binary heap implementation.