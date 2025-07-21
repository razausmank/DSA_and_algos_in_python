# *
# **
# ***
# ****
# *****


for i in range(5): 
    print("*" * (i + 1) ); 

# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    print("*" * i)
    
for i in range(5,0,-1):
    for j in range(i): 
        print("*" , end="")
    print("")
    
    
    
#     *
#    ***
#   *****
#  *******
# *********


for i in range(5,0,-1):
    print(" " * i , end="")
    print("*" * (5-i+1), end="") 
    print("*" * (5-i)) 
    
    
# *********
#  *******
#   *****
#    ***
#     *
print()

rows = 5 

for i in range(rows):
    print(" " * i, end="")
    print("*" * ((rows-i)*2)) 
    
    
#     *
#    **
#   ***
#  ****
# *****
rows = 5 
for i in range(rows):
    space = " " * (rows-i-1 ) 
    stars = "*" * (i+1)
    print(space+stars) 


# *****
#  ****
#   ***
#    **
#     *


rows = 5 

for i in range(rows): 
    space = " " * i 
    stars = "*" * (rows-i)
    print(space+stars)
    
    
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

rows = 5 
for i in range(rows): 
    space = " " * (rows-i-1) 
    stars = "*" * (i*2+1)
    print(space+stars)
    
for i in range(rows-1,0, -1): 
    stars = "*" * (i*2+1 ) 
    space = " " * (rows-i-1)
    print(space+stars)
    
    
    
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

rows = 5 

for i in range(5): 
    space = " " * (i)
    stars = "*" * ((rows-i)*2-1)
    print(space + stars)
    
for i in range(5): 
    space = " " * (rows-i-1)
    stars = "*" * (i*2+1)
    print(space + stars)
    