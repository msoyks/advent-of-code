import math

with open("input.txt") as file:
    
    masses = [int(mass) for mass in file.readlines()]
    
total_fuel = 0

for mass in masses:
    
    weight = mass
    
    # Take the mass
    
    # Divide it by 3
    
    weight /= 3
    
    # Round down (floor)
    
    weight = math.floor(weight)
    
    # Subtract 2
    
    weight -= 2
    
    # Add to total
    
    total_fuel += weight
    
print(total_fuel)