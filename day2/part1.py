import re

horizontal = 0
depth = 0
aim = 0

ocean_movement_file = open('day2\input.txt', 'r')
ocean_movement = ocean_movement_file.readlines()

for i in range(0, len(ocean_movement)):
    if "forward" in ocean_movement[i]:
        horizontal = horizontal + int(re.search(r'\d+', ocean_movement[i]).group())

    if "down" in ocean_movement[i]:
        depth = depth + int(re.search(r'\d+', ocean_movement[i]).group())

    if "up" in ocean_movement[i]:
        depth = depth - int(re.search(r'\d+', ocean_movement[i]).group())
            


answer = depth*horizontal
print(answer)
