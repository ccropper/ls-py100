"""
10. Assume that obj already has a value of 42 when the code below 
starts running. Which of the subsequent statements reassign the 
variable? Which statements mutate the value of the object that obj 
references? Which statements do neither? If necessary, you can read 
the documentation.
"""

obj = 'ABcd' # reassigns obj
obj.upper() # neither; returns a new object that is uppercase
obj = obj.lower() # reassigns obj
print(len(obj)) # neither; returns None
obj = list(obj) # reassigns obj
obj.pop() # mutates obj and returns the popped value
obj[2] = 'X' # mutates obj
obj.sort() # mutates obj
set(obj) # neither
obj = tuple(obj) # reassigns obj