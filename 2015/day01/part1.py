with open("input.txt") as file:
    
    instruction_list = file.read().strip()
    
floor = 0

for instruction in instruction_list:
    
    if instruction == "(":
        
        floor += 1
        
    else:
        
        floor -= 1
    
print(floor)