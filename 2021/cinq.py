import common
import re
import math


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    return hydrothermal_vents(rows, 1000, True)


# solution for the second part
def part2(rows):
    return hydrothermal_vents(rows, 1000, False)


# as part1 and part2 are very similar, we will use one function to calculate both
# only the parameter ignore_diagonal will be different
#
# params:
# - input_rows - array of strings (input rows) without \n
# - map_size - specifies how big is the map (10 for example inputs, 1000 for real inputs)
# - ignore_diagonal - if True, only vertical or horizontal lines will be counted (diagonals will be skipped)
def hydrothermal_vents(input_rows, map_size, ignore_diagonal):
    # Calculation steps:
    # 1) create map (array 1000x1000)
    # 2) while not end of file:
    #  - 2a) parse start and end point from the line
    #  - 2b) calculate points in between start and end point, write them to map
    # 3) count all points in map which are > 1

    # 1
    vents_map = [[0 for x in range(map_size)] for y in range(map_size)]

    # 2
    current_row = 0
    while current_row < len(input_rows):
        # 2a
        splitted = re.split("->|,", input_rows[current_row])
        splitted = [int(x.strip()) for x in splitted]
        gradient = splitted[2] - splitted[0], splitted[3] - splitted[1]
        greatest_common_divisor = math.gcd(gradient[0], gradient[1])
        gradient = int(gradient[0] / greatest_common_divisor), int(gradient[1] / greatest_common_divisor)

        # part 1 only use horizontal and vertical lines - diagonal lines are ignored
        if ignore_diagonal is True and not (gradient[0] == 0 or gradient[1] == 0):
            # print("skipping ", rows[current_row])
            current_row += 1
            continue

        # 2b
        current_point = splitted[0], splitted[1]
        end_point = splitted[2], splitted[3]
        while current_point != end_point:
            vents_map[current_point[0]][current_point[1]] += 1
            current_point = current_point[0] + gradient[0], current_point[1] + gradient[1]
        vents_map[end_point[0]][end_point[1]] += 1
        current_row += 1

    # 3
    counter_more_than_one = 0
    for i in range(map_size):
        for j in range(map_size):
            if vents_map[i][j] > 1:
                counter_more_than_one += 1

    return counter_more_than_one


# few simple tests
def test():
    test_inputs = \
        "0,9 -> 5,9\n" \
        "8,0 -> 0,8\n" \
        "9,4 -> 3,4\n" \
        "2,2 -> 2,1\n" \
        "7,0 -> 7,4\n" \
        "6,4 -> 2,0\n" \
        "0,9 -> 2,9\n" \
        "3,4 -> 1,4\n" \
        "0,0 -> 8,8\n" \
        "5,5 -> 8,2\n" \
        .rstrip().split("\n")
    assert part1(test_inputs) == 5
    assert part2(test_inputs) == 12
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(5).rstrip().split("\n")
common.post_answer(5, 1, part1(inputs))
common.post_answer(5, 2, part2(inputs))
