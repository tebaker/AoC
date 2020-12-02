# --- Day 3: Crossed Wires ---
# The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.
# 
# Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).
# 
# The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

# Terminology:
#    Manhattan Distance - The distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|

# Importing regex for pattern matching for string splitting
import re

# Importing math for absolute value function
import math

# List that will hold all the coordinate data for wire 1
w1CoordDict = {}

# List that will hold all the coordinate data for wire 2 for the points that OVERLAP with wire 1
w2OverlapDict = {}

# Opening data text file
f = open('data.txt')

# Temp hold. Splitting text data by newline; giving string data for wire 1 and wire 2
splitHold = f.read().split('\n')

# Closing file
f.close()

# Arrays that will hold all the raw wire data. Splitting wire 1 and wire 2 text data by comma
# Data is now in the form of a string containing <Direction><Distance> data
w1RawDataArray = splitHold[0].split(',')
w2RawDataArray = splitHold[1].split(',')

# Holding most recently accessed x, y coords
lastXCoord = 0
lastYCoord = 0

# looping through the raw data for wire 1. Setting every x, y coord what the wire passes
for i in w1RawDataArray:
    # Direction is first character of raw string data. Either U, D, L, R
    dir = i[0]
    # Distance data is an int; everything that's left. [1:] -> takes index 1 to end
    dist = int(i[1:])

    # Switching on direction
    if dir == 'U':
        for j in range(0, dist):
            lastYCoord += 1
            w1CoordDict[lastXCoord, lastYCoord] = True
    elif dir == 'D':
        for j in range(0, dist):
            lastYCoord -= 1
            w1CoordDict[lastXCoord, lastYCoord] = True
    elif dir == 'L':
        for j in range(0, dist):
            lastXCoord -= 1
            w1CoordDict[lastXCoord, lastYCoord] = True
    elif dir == 'R':
        for j in range(0, dist):
            lastXCoord += 1
            w1CoordDict[lastXCoord, lastYCoord] = True
    else:
        print("ERROR: INVALID DIRECTION")

# Resetting the lastly accessed coordinated
lastXCoord = 0
lastYCoord = 0

# Index for user output
index = 0

# Holding the total step count at each overlap for wire 2
w2TotalSteps = 0

# Looping through the raw data for wire 2
for i in w2RawDataArray:
    # Direction is first character of raw string data. Either U, D, L, R
    dir = i[0]
    # Distance data is an int; everything that's left. [1:] -> takes index 1 to end
    dist = int(i[1:])

    # Printing and incrementing value of string for user output
    print("Evaluating: ", index, "of", str(len(w2RawDataArray)))
    index += 1

    # Switching on direction
    if dir == 'U':
        for j in range(0, dist):
            lastYCoord += 1

            w2TotalSteps += 1

            # Checking coords against wire 1 coord list. If true, add to overlap list
            if (lastXCoord, lastYCoord) in w1CoordDict:
                #print("Adding:", lastXCoord, lastYCoord)
                # If overlap data at x, y is not already in the dictionary, add data to dict. If not, skip
                if (lastXCoord, lastYCoord) not in w2OverlapDict:
                    w2OverlapDict[lastXCoord, lastYCoord] = w2TotalSteps
    elif dir == 'D':
        for j in range(0, dist):
            lastYCoord -= 1

            w2TotalSteps += 1
            
            # Checking coords against wire 1 coord list. If true, add to overlap list
            if (lastXCoord, lastYCoord) in w1CoordDict:
                #print("Adding:", lastXCoord, lastYCoord)
                # If overlap data at x, y is not already in the dictionary, add data to dict. If not, skip
                if (lastXCoord, lastYCoord) not in w2OverlapDict:
                    w2OverlapDict[lastXCoord, lastYCoord] = w2TotalSteps
    elif dir == 'L':
        for j in range(0, dist):
            lastXCoord -= 1

            w2TotalSteps += 1
            
            # Checking coords against wire 1 coord list. If true, add to overlap list
            if (lastXCoord, lastYCoord) in w1CoordDict:
                #print("Adding:", lastXCoord, lastYCoord)
                # If overlap data at x, y is not already in the dictionary, add data to dict. If not, skip
                if (lastXCoord, lastYCoord) not in w2OverlapDict:
                    w2OverlapDict[lastXCoord, lastYCoord] = w2TotalSteps
    elif dir == 'R':
        for j in range(0, dist):
            lastXCoord += 1

            w2TotalSteps += 1
            
            # Checking coords against wire 1 coord list. If true, add to overlap list
            if (lastXCoord, lastYCoord) in w1CoordDict:
                #print("Adding:", lastXCoord, lastYCoord)
                # If overlap data at x, y is not already in the dictionary, add data to dict. If not, skip
                if (lastXCoord, lastYCoord) not in w2OverlapDict:
                    w2OverlapDict[lastXCoord, lastYCoord] = w2TotalSteps
    else:
        print("ERROR: INVALID DIRECTION")


print("Complete Overlap Data:")
print(w2OverlapDict)

# Holding new x, y for finding w1 overlap
w1OverlapCheckX = 0
w1OverlapCheckY = 0

# Holding total number of steps made before first overlap
w1TotalSteps = 0
overlapFound = False

# Rerunning the loop for wire 1 until a path leads to the first overlap x, y found
for i in w1RawDataArray:
    # Direction is first character of raw string data. Either U, D, L, R
    dir = i[0]
    # Distance data is an int; everything that's left. [1:] -> takes index 1 to end
    dist = int(i[1:])

    # Switching on direction
    if dir == 'U':
        for j in range(0, dist):
            w1OverlapCheckY += 1
            w1TotalSteps += 1
            if w1OverlapCheckX == lastXCoord and w1OverlapCheckY == lastYCoord:
                # Overlap Found, beaking out of all loops
                overlapFound = True
                break
    elif dir == 'D':
        for j in range(0, dist):
            w1OverlapCheckY -= 1
            w1TotalSteps += 1
            if w1OverlapCheckX == lastXCoord and w1OverlapCheckY == lastYCoord:
                # Overlap Found, beaking out of all loops
                overlapFound = True
                break
    elif dir == 'L':
        for j in range(0, dist):
            w1OverlapCheckX -= 1
            w1TotalSteps += 1
            if w1OverlapCheckX == lastXCoord and w1OverlapCheckY == lastYCoord:
                # Overlap Found, beaking out of all loops
                overlapFound = True
                break
    elif dir == 'R':
        for j in range(0, dist):
            w1OverlapCheckX += 1
            w1TotalSteps += 1
            if w1OverlapCheckX == lastXCoord and w1OverlapCheckY == lastYCoord:
                # Overlap Found, beaking out of all loops
                overlapFound = True
                break
    else:
        print("ERROR: INVALID DIRECTION")

    # Breaking out of while if overlap found
    if overlapFound:
        print("Overlap found for wire 1 wire 2 crossover")
        break

# Printing wire 1 overlap results
print("w1TotalSteps:", w1TotalSteps)
print("Found at (", w1OverlapCheckX, ",", w1OverlapCheckY, ")")

# Holding the lowest overlapped x, y value
#lowestOverlappedX = 0
#lowestOverlappedY = 0

# Holding lowest overlapped manhattan distance
#lowestManhattanDist = 1000000

# Checking against all the overlaps for lowest Manhattan dist
#for overlap in w2OverlapDict:
#    xCoord = abs(overlap[0])
#    yCoord = abs(overlap[1])

#    manhattanDist = xCoord + yCoord

#    if manhattanDist < lowestManhattanDist:
#        # Found new lowest manhattan dist. Setting new lowest dist and new lowest x, y
#        lowestManhattanDist = manhattanDist
#        lowestOverlappedX = xCoord
#        lowestOverlappedY = yCoord

#        print("Manhattan Dist:", lowestManhattanDist, "lowest x", lowestOverlappedX, "lowest y", lowestOverlappedY)

# Answer 1: Manhattan Dist: 1 lowest x 1 lowest y 0
# Answer 2: Manhattan Dist: 721 lowest x 571 lowest y 150 CORRECT

# Part 2:
#   w2TotalSteps: 1188
#   Found at ( -1095 , -93 )
#   w1TotalSteps: 94900
#   Found at ( -1095 , -93 )

# Part 2, answer 1: 94900 + 1188 = 96088