# --- Day 2: 1202 Program Alarm ---
#
# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
# To run one, start by looking at the first integer (called position 0).
# Here, you will find an opcode - either 1, 2, or 99.
# The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt.
# Encountering an unknown opcode means something went wrong.
#
# Opcode 1 adds together numbers read from two positions and stores the result in a third position.
# The three integers immediately after the opcode tell you these three positions - the first
# two indicate the positions from which you should read the input values,
# and the third indicates the position at which the output should be stored.

# Position 0: Opcode
#   1) Addition, 2) multiplication
# Position 1: Location of first number
# Position 2: Location of second number
# Position 3: Location of sum or product of first and second number

# Opening data file. <path to file>, <mode of accessing file>
f = open('input.txt', 'r')

# Splitting file by ',', storing result in opcode array
opcodeArray = f.read().split(',')

# Closing file
f.close()

# Index i = 0
i = 0

# Looping through all the opcodes
while i < len(opcodeArray):

    # Storing opcode
    oc = int(opcodeArray[i])

    # Getting locations of value 1 and value 2
    locVal1 = int(opcodeArray[i+1])
    locVal2 = int(opcodeArray[i+2])

    # Values for calculation
    val1 = int(opcodeArray[locVal1])
    val2 = int(opcodeArray[locVal2])

    # Getting storage location of result
    locResult = int(opcodeArray[i+3])


    print(oc, locVal1, locVal2, locResult)


    # Holding result of calculation
    result = 0

    # If opcode = 1, add values
    if oc == 1:
        result = val1 + val2
    # If opcode = 2, multiply values
    elif oc == 2:
        result = val1 * val2
    # If not 1, or 2... ERROR
    elif oc == 99:
        print("Opcode 99: Haulting program")
        break
    else:
        print("ERROR: INVALID OPCODE")

    # Storing result back into array at location of opcode 3
    opcodeArray[locResult] = result

    # Incrementing index by 4 to get next set of opcodes
    i += 4

# Printing value at position 0 for puzzle
print("Location at element 0: ", opcodeArray[0])

# First guess: 172
# Second guess: 613553