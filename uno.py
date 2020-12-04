import common

# get inputs from webpage using session cookie
rows = common.get_input(1).split()

# part 1 - find two numbers which sum is 2020, then print their product (result of multiplication)
for index1 in range(len(rows)):
    for index2 in range(index1+1, len(rows)):
        number1 = int(rows[index1])
        number2 = int(rows[index2])
        if number1 + number2 == 2020:
            print("Part 1: Bingo! " + str(number1) + " " + str(number2))
            print("Part 1: Give them number " + str(number1*number2))

# part 2 - find three numbers which sum is 2020, then print their product (result of multiplication)
for index1 in range(len(rows)):
    for index2 in range(index1+1, len(rows)):
        for index3 in range(index2+1, len(rows)):
            number1 = int(rows[index1])
            number2 = int(rows[index2])
            number3 = int(rows[index3])
            if number1 + number2 + number3 == 2020:
                print("Part 2: Bingo! " + str(number1) + " " + str(number2) + " " + str(number3))
                print("Part 2: Give them number " + str(number1*number2*number3))
