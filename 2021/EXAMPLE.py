import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    return -1


# solution for the second part
def part2(rows):
    return -1


# few simple tests
def test():
    test_inputs = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n".rstrip().split("\n")
    assert part1(test_inputs) == 0
    assert part2(test_inputs) == 0
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(0).rstrip().split("\n")
common.post_answer(0, 1, part1(inputs))
common.post_answer(0, 2, part2(inputs))
