from stack import Stack 

def flip_a_bracket(input): 
    brackets = { 
        '(' : ')',
        '{' : '}',
        '[' : ']', 
        ')' : '(',
        '}' : '{',
        ']' : '[', 
    }
    
    return brackets[input]

if "__main__"  == __name__ : 
    stack = Stack()
    input_string = "{[()])}"
    # invalid pairs of brackets 
    # [({})
    # {[()])}
    # ({[)]}
    
    # valid pairs 
    # [({})]
    # (([]))
    # {[()()]}
    
    # we process the input by characters 
    for c in input_string:
        
        # if the stack is empty we put the characters into the stack 
        if stack.is_empty():
            stack.push(c)
            continue
        
        # if the stack is not empty we match the last stack element from the reversed next characters 
        # if they match we pop the last stack element and move on to the next character
        if c == flip_a_bracket(stack.peek()) : 
            stack.pop() 
            continue 
        
        # if they don't match we just put it in the stack 
        stack.push(c)        
    
    # after the input characters are finished we check the stack length if its 0 then 
    
    print("Valid brackets pair") if stack.is_empty() else print("brackets do not match are invalid") 
        
    