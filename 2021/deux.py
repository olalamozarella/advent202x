import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    depth, position = 0, 0
    for row in rows:
        splitted = row.split(" ")
        number = int(splitted[1])
        if splitted[0] == "forward":
            position += number
        elif splitted[0] == "down":
            depth += number
        elif splitted[0] == "up":
            depth -= number
        else:
            print("WTF?")
    return depth * position


# solution for the second part
def part2(rows):
    depth, position, aim = 0, 0, 0
    for row in rows:
        splitted = row.split(" ")
        number = int(splitted[1])
        if splitted[0] == "forward":
            position += number
            depth += aim * number
        elif splitted[0] == "down":
            aim += number
        elif splitted[0] == "up":
            aim -= number
        else:
            print("WTF?")
    return depth * position


# few simple tests
def test():
    test_inputs = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n".rstrip().split("\n")
    assert part1(test_inputs) == 150
    assert part2(test_inputs) == 900
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(2).rstrip().split("\n")
common.post_answer(2, 1, part1(inputs))
common.post_answer(2, 2, part2(inputs))
