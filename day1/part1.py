ocean_depths_file = open('day1\input1.txt', 'r')
ocean_depths = ocean_depths_file.readlines()


previous_depth = ocean_depths[0]
numberOfMeasurements = len(ocean_depths)

largerCounter = 0

for i in range(1, numberOfMeasurements):
    if(int(ocean_depths[i]) > int(previous_depth)):
        largerCounter = largerCounter + 1
    previous_depth = ocean_depths[i]


print(largerCounter)
