with open("input.txt") as file:
    
    instruction_list = file.read().strip()
    
floor = 0

for position, instruction in enumerate(instruction_list, start=1):
    
    if instruction == "(":
        
        floor += 1
        
    else:
        
        floor -= 1
        
    if floor == -1:
        
        print(position)
        
        break
        