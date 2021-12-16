import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
# we will assign a score to each item in 2D array (sum of all items which I need to cross to get to the current item)
# we just need to find the lowest cost path from top left to bottom right (e.g. lowest possible score)
#
# we will split it to two scoring functions:
# A) dumb scoring function
#   - will just go through all rows and all items
#   - for each item it calculates scores when coming from left,right,top,bottom and stores the lowest one
#
# B) recursive scoring function
#   - will start at top left corner
#   - recalculates scores for all neighbors
#   - continues recursively to neighbor with next lowest score
# WARN - recursive function did not work properly, so I just ran the dumb function multiple times in row to get result

def part1(rows):
    # parse inputs into 2D array
    # create 2D array of lowest scores
    height_map = [[int(x) for x in row] for row in rows]
    score_map = [[False for x in row] for row in rows]
    score_map[0][0] = 0

    # fill score map row by row
    dumb_scoring_function(height_map, score_map)

    # start recursion at left top corner
    recursive_scoring_function(height_map, score_map, (0, 0))

    print("Score map")
    for row in score_map:
        print(row)
    return score_map[-1][-1]


# solution for the second part
def part2(rows):
    # parse inputs into 2D array
    # create 2D array of lowest scores
    height_map = [[int(x) for x in row] for row in rows]

    # enlarge both height and score maps by factor of 5
    row_count = len(height_map[0])
    column_count = len(height_map)
    enlarged_height_map = [[0 for x in range(column_count * 5)] for row in range(row_count * 5)]

    for vertical_segment in range(5):
        for horizontal_segment in range(5):
            for row_index in range(row_count):
                for col_index in range(column_count):
                    enlarged_row_index = vertical_segment * row_count + row_index
                    enlarged_col_index = horizontal_segment * column_count + col_index
                    enlarged_score = (height_map[row_index][col_index] + vertical_segment + horizontal_segment)
                    if enlarged_score > 9:
                        enlarged_score -= 9
                    enlarged_height_map[enlarged_row_index][enlarged_col_index] = enlarged_score

    enlarged_score_map = [[False for x in row] for row in enlarged_height_map]
    enlarged_score_map[0][0] = 0

    # fill score map using dumb function
    # check result score
    # try again, check if the result score has changed

    last_score = 0
    step = 0
    same_result_steps = 0
    while True:
        dumb_scoring_function(enlarged_height_map, enlarged_score_map)
        current_score = enlarged_score_map[-1][-1]
        print("step={0}, current score={1}".format(step, current_score))
        step += 1
        if current_score == last_score:
            same_result_steps += 1
            if same_result_steps > 10:
                break
        else:
            same_result_steps = 0  # we want to have same result at least 10 times in row
            last_score = current_score

    return enlarged_score_map[-1][-1]


# few simple tests
def test():
    test_inputs = \
        "1163751742\n" \
        "1381373672\n" \
        "2136511328\n" \
        "3694931569\n" \
        "7463417111\n" \
        "1319128137\n" \
        "1359912421\n" \
        "3125421639\n" \
        "1293138521\n" \
        "2311944581\n" \
        .rstrip().split("\n")
    assert part1(test_inputs) == 40
    assert part2(test_inputs) == 315
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #
# function that calculates scores row by row, calculating score from top or left, and picking lower option
def dumb_scoring_function(height_map, score_map):
    for row_index in range(len(height_map)):
        for col_index in range(len(height_map[row_index])):
            if row_index == 0 and col_index == 0:
                continue
            current_height = height_map[row_index][col_index]
            score_from_top, score_from_left, score_from_bottom, score_from_right = 9999, 9999, 9999, 9999
            if row_index > 0 and score_map[row_index - 1][col_index] is not False:
                score_from_top = score_map[row_index - 1][col_index] + current_height
            if col_index > 0 and score_map[row_index][col_index - 1] is not False:
                score_from_left = score_map[row_index][col_index - 1] + current_height
            if row_index < len(height_map) - 1 and score_map[row_index + 1][col_index] is not False:
                score_from_bottom = score_map[row_index + 1][col_index] + current_height
            if col_index < len(height_map[0]) - 1 and score_map[row_index][col_index + 1] is not False:
                score_from_right = score_map[row_index][col_index + 1] + current_height

            score = min(score_from_top, score_from_bottom, score_from_left, score_from_right)
            score_map[row_index][col_index] = score


# my try on pathfinding algorithm... not working properly
# height_map = 2D array for parsed inputs
# score_map = 2D array of lowest achieved scores for each point
# current_point = tuple(int, int) of current point
def recursive_scoring_function(height_map, score_map, current_point):
    # for all neighbors
    #   calculate score, write to array is smaller than current one
    #
    # sort all neighbors by size
    # from smallest to biggest neighbor:
    #   recurse for the neighbor

    current_score = score_map[current_point[0]][current_point[1]]
    neighbors = []
    # if current_point[0] > 0:
    #     neighbors.append((current_point[0] - 1, current_point[1]))
    if current_point[0] < len(height_map[0]) - 1:
        neighbors.append((current_point[0] + 1, current_point[1]))
    # if current_point[1] > 0:
    #     neighbors.append((current_point[0], current_point[1] - 1))
    if current_point[1] < len(height_map) - 1:
        neighbors.append((current_point[0], current_point[1] + 1))
    neighbors_to_visit = []
    for neighbor in neighbors:
        neighbor_score = current_score + height_map[neighbor[0]][neighbor[1]]
        if score_map[neighbor[0]][neighbor[1]] is False or neighbor_score <= score_map[neighbor[0]][neighbor[1]]:
            score_map[neighbor[0]][neighbor[1]] = neighbor_score
            neighbors_to_visit.append(neighbor)

    def get_score(item):
        return score_map[item[0]][item[1]]
    neighbors_to_visit = sorted(neighbors_to_visit, key=get_score)
    for neighbor in neighbors_to_visit:
        if score_map[neighbor[0]][neighbor[1]] <= current_score:
            continue
        recursive_scoring_function(height_map, score_map, neighbor)


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(15).rstrip().split("\n")
#common.post_answer(15, 1, part1(inputs))
common.post_answer(15, 2, part2(inputs))
