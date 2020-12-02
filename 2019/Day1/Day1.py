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

# Dividing mass by three and flooring the result, subtrasting that total from 2 and returning the result
def calcFuel(mass):
    return math.floor(int(mass) / 3) - 2

# The folloing function will keep calling itself until the resulting number is <= 0.
# Dividing mass by three and flooring the result, subtrasting that total from 2 and returning the result
def calcFuelRecur(mass):
    # If calculated fuel result is less than or equal to 0, no fule is needed, return 0
    if math.floor(int(mass) / 3) - 2 <= 0:
        return 0
    # If the calculated fuel result is greater than 0, must go a level deeper
    else:
        return math.floor(int(mass) / 3) - 2 + calcFuelRecur(math.floor(int(mass) / 3) - 2)

# Holding total fule costs
totFuleCost = 0

# Opening input.txt file
f = open("input.txt", "r")

# Looping through every line of the file
for line in f:
    totFuleCost += calcFuelRecur(line)

# Printing total fule costs
print(totFuleCost)

# Closing the file
f.close()
