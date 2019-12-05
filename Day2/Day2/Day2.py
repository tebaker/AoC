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

# Index i = 0
i = 0

# Looping through all the opcodes
while i < len(opcodeArray):
    # Storing opcode
    oc = int(opcodeArray[i])

    print("oc: ", oc)

    # Getting values of opsitions at opcodes 1 and 2
    val1 = int(opcodeArray[i+1])
    val2 = int(opcodeArray[i+2])

    print("val1: ", val1)
    print("val2: ", val2)

    # Getting storage location of result
    loc = int(opcodeArray[i+3])

    print("loc: ", loc)

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
    opcodeArray[loc] = result

    # Incrementing index by 4 to get next set of opcodes
    i += 4

# Printing value at position 0 for puzzle
print("Location at element 0: ", opcodeArray[0])

# Closing file
f.close()

# First guess: 172