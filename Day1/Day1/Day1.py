# --- Day 1: The Tyranny of the Rocket Equation ---
#
# Santa has become stranded at the edge of the Solar System while delivering presents to other planets!
# To accurately calculate his position in space, safely align his warp drive,]
# and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# The Elves quickly load you into a spacecraft and prepare to launch.
#
# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
# They haven't determined the amount of fuel required yet.
#
# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
#
# The file "Input.txt" contains all the modules that need calculating
#####################################################################################################################

# Importing math for floor function
import math

# Holding total fule costs
totFuleCost = 0

# Opening input.txt file
f = open("input.txt", "r")

# Looping through every line of the file
for line in f:
    # Converting line from string to int, dividing line by three and taking the floor of the result,
    # subtrasting total from 2 and total back to totFuleCost
    totFuleCost += math.floor(int(line) / 3) - 2

# Printing total fule costs
print(totFuleCost)

# Closing the file
f.close()