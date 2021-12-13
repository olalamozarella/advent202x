import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first and second part
def part1_2(rows):
    # 1 Create two-dimensional array of inputs (each row has one index)
    # Create lowest point array = 0
    # 2 Go through all array elements and find the lowest point of its way
    # 3 Check if we have already reach that lowest point, if yes, skip it, if not, save it
    # 4 Each lowest point increase by 1 and sum all of increased lowest points

    # 1 - todo E, result is 2D array like [[1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3]
    # array size will be 100x100 in real inputs, 10x10 in test inputs
    array2D = []
    for x in range(0, len(rows)):
        inputs = []
        for y in range(0, len(rows[x])):
            inputs.append(int(rows[x][y]))
        array2D.append(inputs)

    # 2
    lowest_point_list = []
    lowest_point_map = [[-1 for x in range(len(array2D[0]))] for y in range(len(array2D))]
    for row in range(0, len(array2D)):
        for column in range(0, len(array2D[row])):
            lowest_point = find_lowest_point((row, column), array2D, lowest_point_map)
            # 3
            if lowest_point not in lowest_point_list:
                lowest_point_list.append(lowest_point)

    # 4
    total_result_p1 = 0
    for x in range(0, len(lowest_point_list)):
        height = array2D[int(lowest_point_list[x][0])][int(lowest_point_list[x][1])]

        # if point has height 9 and all other point around it are also 9, our algorithm considers it a low point
        # however, the AoC result does not count such point as a low point - therefore, we have to use this nasty hack
        if height == 9:
            continue

        total_result_p1 += array2D[int(lowest_point_list[x][0])][int(lowest_point_list[x][1])] + 1

    # 5 calculate part 2 using lowest_point_map
    # - calculate occurences for each lowest_point in lowest_point_map
    # - pick three biggest, multiply, return result
    basin_sizes = {}
    for lowest_point in lowest_point_list:
        basin_sizes[lowest_point] = 0

    for row in range(0, len(lowest_point_map)):
        for column in range(0, len(lowest_point_map[row])):
            point = lowest_point_map[row][column]
            height = array2D[row][column]
            # if point has height 9 and all other point around it are also 9, our algorithm considers it a low point
            # however, the AoC result does not count such point as a low point - therefore, we have to use this nasty hack
            if height == 9:
                continue
            basin_sizes[point] += 1
    sorted_sizes = sorted(basin_sizes.values(), reverse=True)
    total_result_p2 = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]

    print("Total result for part 1: ", total_result_p1)
    print("Total result for part 2: ", total_result_p2)
    return total_result_p1, total_result_p2


def find_lowest_point(position_to_check, input_map, lowest_point_map):
    # 1 (performance optimization) check if lowest_point_map[position_to_check] is already filled
    #     if yes, return point from map
    # 2 find current height
    # 3 find next lowest point in all four directions
    # 4 if we are already at lowest point:
    #     (performance optimization) add current position to lowest_point_map
    #     return current position
    #   else (one of the neighbors is lower)
    #     call find_lowest_point() for next point
    #     (performance optimization) store result in lowest_point_map[position_to_check]
    #     return point

    # 1
    if lowest_point_map[position_to_check[0]][position_to_check[1]] != -1:
        return lowest_point_map[position_to_check[0]][position_to_check[1]]

    # 2
    current_height = input_map[position_to_check[0]][position_to_check[1]]

    # 3
    next_positions = (
        (position_to_check[0] - 1, position_to_check[1]),  # up
        (position_to_check[0] + 1, position_to_check[1]),  # down
        (position_to_check[0], position_to_check[1] - 1),  # left
        (position_to_check[0], position_to_check[1] + 1)  # right
    )
    next_lowest_height = current_height
    for next_position in next_positions:
        # skip position outside map range
        if next_position[0] < 0 or next_position[0] >= len(input_map) \
          or next_position[1] < 0 or next_position[1] >= len(input_map[0]):
            continue
        next_height = input_map[next_position[0]][next_position[1]]
        if next_height < next_lowest_height:
            next_lowest_height = next_height
            next_position_to_check = next_position

    # 4
    if next_lowest_height >= current_height:
        lowest_point_map[position_to_check[0]][position_to_check[1]] = position_to_check
        print("point {0} with height={1} is a lowest point".format(position_to_check, current_height))
        return position_to_check
    else:
        # print("point {0} with height={1} is not a lowest point, trying point {2} with height={3}"
        #       .format(position_to_check, current_height, next_position_to_check, next_lowest_height))
        lowest_point = find_lowest_point(next_position_to_check, input_map, lowest_point_map)
        lowest_point_map[position_to_check[0]][position_to_check[1]] = lowest_point
        return lowest_point


# few simple tests
def test():
    test_inputs = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678\n".rstrip().split("\n")
    assert part1_2(test_inputs) == (15, 1134)  # one function calculates results for both parts
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(9).rstrip().split("\n")
result1, result2 = part1_2(inputs)
common.post_answer(9, 1, result1)
common.post_answer(9, 2, result2)
