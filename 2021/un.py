import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    counter = 0
    previous = 9999
    for row in rows:
        if int(row) > previous:
            counter += 1
        previous = int(row)
    return counter


# solution for the second part
def part2(rows):
    counter = 0
    for row in range(3, len(rows)):
        previous = int(rows[row-1]) + int(rows[row-2]) + int(rows[row-3])
        current = int(rows[row]) + int(rows[row-1]) + int(rows[row-2])
        if current > previous:
            counter += 1
    return counter


# few simple tests
def test():
    test_inputs = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263\n".rstrip().split("\n")
    assert part1(test_inputs) == 7
    assert part2(test_inputs) == 5
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(1).rstrip().split("\n")
common.post_answer(1, 1, part1(inputs))
common.post_answer(1, 2, part2(inputs))
