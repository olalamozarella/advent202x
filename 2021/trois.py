import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    # calculate most and least common digits
    most_common, least_common = calculate_most_common(rows)

    # join array of chars (for example ['1','0','1','1','0']) into integer
    gamma = int("".join(str(x) for x in most_common), 2)
    epsilon = int("".join(str(x) for x in least_common), 2)

    # result
    return gamma * epsilon


# solution for the second part
def part2(rows):
    # input number may have any length
    binary_length = len(rows[0])

    # filter input rows by oxygen criteria, until there is only one row remaining
    oxy_list = rows
    for i in range(0, binary_length):
        if len(oxy_list) == 1:
            break
        most_common, least_common = calculate_most_common(oxy_list)
        keeping = most_common[i]
        if keeping == 'X':
            keeping = '1'
        oxy_list = [x for x in oxy_list if x[i] == keeping]
    oxy = int(oxy_list[0], 2)

    # filter input rows by co2 criteria, until there is only one row remaining
    co2_list = rows
    for i in range(0, binary_length):
        if len(co2_list) == 1:
            break
        most_common, least_common = calculate_most_common(co2_list)
        keeping = least_common[i]
        if keeping == 'X':
            keeping = '0'
        co2_list = [x for x in co2_list if x[i] == keeping]
    co2 = int(co2_list[0], 2)

    # result
    return oxy * co2


# few simple tests
def test():
    test_inputs = "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n".rstrip().split("\n")
    assert part1(test_inputs) == 198
    assert part2(test_inputs) == 230
    print("All tests passed!")


# ---------------------------------------- HELPER FUNCTIONS ---------------------------------------- #
# takes list of binary strings, calculates most and least common digits
# example input:  00100\n11110\n10110\n
# example output: most_common=['1','0','1','1','0'], least_common=['0','1','0','0','1']
# note: if both '0' and '1' are equally common, result is 'X'
def calculate_most_common(inputs):
    binary_length = len(inputs[0])
    zeros_counter = [0] * binary_length
    ones_counter = [0] * binary_length
    for row in inputs:
        for index, digit in enumerate(row):
            if digit == '0':
                zeros_counter[index] += 1
            else:
                ones_counter[index] += 1
    most_common, least_common = [0] * binary_length, [0] * binary_length
    for index, digit in enumerate(zeros_counter):
        if zeros_counter[index] > ones_counter[index]:
            most_common[index] = '0'
            least_common[index] = '1'
        elif zeros_counter[index] < ones_counter[index]:
            most_common[index] = '1'
            least_common[index] = '0'
        else:
            most_common[index] = 'X'
            least_common[index] = 'X'
    return most_common, least_common

# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(3).rstrip().split("\n")
common.post_answer(3, 1, part1(inputs))
common.post_answer(3, 2, part2(inputs))
