ocean_depths_file = open('day1\input1.txt', 'r')
ocean_depths = ocean_depths_file.readlines()

numberOfMeasurements = len(ocean_depths)
ocean_depths_summations = []

for i in range(0, numberOfMeasurements):
    ocean_depths[i] = int(ocean_depths[i])

for i in range(0, numberOfMeasurements-2):
    ocean_depths_summations.append(ocean_depths[i]+ ocean_depths[i+1] +ocean_depths[i+2])


previous_depth_sum = ocean_depths_summations[0]
largerCounter = 0

for i in range(1, len(ocean_depths_summations)):
    if(ocean_depths_summations[i] > previous_depth_sum):
        largerCounter = largerCounter + 1
    previous_depth_sum = ocean_depths_summations[i]


print(largerCounter)