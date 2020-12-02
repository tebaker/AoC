# Example: "15-16 p: ppppppppppplppppp"
# Need split on ":" first to make:
#   "15-16 p", " ppppppppppplppppp"
# Then split on "" on first half:
#   "15-16", "p"
def main():

    goodPass = 0
    badPass = 0

    f = open("input.txt", "r")
    for line in f:
        # Splitting pass info from password
        split = line.split(":")

        # Breaking up min-max info from char info on " "
        passInfo = split[0].split()

        # Breaking up min from max
        minMax = passInfo[0].split("-")

        minPass = int(minMax[0])
        maxPass = int(minMax[1])
        charPass = passInfo[1]
        # Removing leading whitespace from password
        password = split[1].strip()
    
        charMatch = 0


        if password[minPass - 1] == charPass and not password[maxPass - 1] == charPass:
            goodPass += 1
        elif not password[minPass - 1] == charPass and password[maxPass - 1] == charPass:
            goodPass += 1
        else:
            badPass += 1

    f.close()

    print(goodPass, badPass)

if __name__ == "__main__":
    main()