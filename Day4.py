# Hello World program in Python
    
#--- Day 4: Secure Container ---
#You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

#However, they do remember a few key facts about the password:

#It is a six-digit number.
#The value is within the range given in your puzzle input.
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#Other than the range rule, the following are true:

#111111 meets these criteria (double 11, never decreases).
#223450 does not meet these criteria (decreasing pair of digits 50).
#123789 does not meet these criteria (no double).
#How many different passwords within the range given in your puzzle input meet these criteria?

#Your puzzle input is 254032-789860.

# given an integer input, and the rules listed above, will find and set the current lowest value and store in currLowest array
def findCurrLowest(inputLow):
    # setting currLowest to puzzle input, low
    for i in str(inputLow):
        currLowest.append(i)
        
    # setting index to 0
    index = 0
    # setting a to left-most digit of currLowest
    a = currLowest[index]
    # setting a to one right of left-most digit of currLowest
    b = currLowest[index+1]
    
    # finding the lowest valid number
    while True:
        # if b = a; digit's valid, move to next set of a, b
        if b == a:
            index+=1
            a = currLowest[index]
            b = currLowest[index+1]
            
        # if b > a; digit's valid, but all numbers after b need to be increased to match b. That's the new currLowest
        if b > a:
            index+=1
            # setting every digit from index to end of array to b
            for i in xrange(index, len(currLowest)):
                currLowest[i] = b
            # breaking out of while
            break




# puzzle input, low
inputLow = 254032
# puzzle input, high
inputHigh = 789860

# holding the current lowest number being evaluated
currLowest = []

# holding the total number of passwords. Starting at 1 for the default case
totNumPasswords = 1

def main():
    findCurrLowest(inputLow)
    
    # printing found current lowest number
    print(currLowest)


if __name__ == "__main__":
    main()





























