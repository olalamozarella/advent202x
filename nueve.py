import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
def part1(inputs, preamble_length):
    for current_row in range(preamble_length, len(inputs)):
        if is_sum(inputs, current_row, preamble_length):
            continue
        else:
            print("Part 1: Number " + inputs[current_row] + " is not sum of any two previous numbers")
            return current_row


def is_sum(inputs, current_row, preamble_length):
    for row1 in range(current_row - preamble_length, current_row - 1):
        for row2 in range(row1 + 1, current_row):
            if int(inputs[row1]) + int(inputs[row2]) == int(inputs[current_row]):
                return True  # current number is sum of two other numbers
    return False


# We need to find a group of numbers (at least two numbers), whose sum equals to our target number.
# We can start with two numbers in front of target row, then go down using these rules:
#  1) if sum of current group is too big, discard the last number in group
#  2) if sum of current group is too low, increase group size
def part2(inputs, target_row):
    inputs_int = [int(row) for row in inputs]
    target_number = inputs_int[target_row]
    group_size = 2
    group_upper_index = target_row
    while True:
        group = inputs_int[group_upper_index - group_size:group_upper_index]
        current_sum = sum(group)
        if current_sum == target_number:
            print("Part 2: result is group " + str(group))
            return min(group) + max(group)
        elif current_sum > target_number:
            group_upper_index -= 1
            if group_size > 2:
                group_size -= 1
        else:
            group_size += 1


def test():
    print("Running tests...")
    inputs = "35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576\n"[:-1].split("\n")
    assert part1(inputs, 5) == 14
    assert part2(inputs, 14) == 62
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(9)[:-1].split("\n")
result_row = part1(inputs, 25)
common.post_answer(9, 1, inputs[result_row])

result = part2(inputs, result_row)
common.post_answer(9, 2, result)
