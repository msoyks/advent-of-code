with open("input.txt") as file:
    
    instruction_list = file.read().strip()
    
floor = instruction_list.count("(") - instruction_list.count(")")
    
print(floor)