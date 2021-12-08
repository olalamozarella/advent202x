import common
import time


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(row):
    # 1) load inputs into int array
    # 2) find min and max numbers in array
    # 3) for each number between min and max:
    # - calculate fuel for every number between max and min
    # - check if this is less fuel than in previous tries
    # 4) return least fuel

    # 1)
    crab_horizontal_positions = [int(x) for x in row[0].split(",")]

    # 2)
    min_position = min(crab_horizontal_positions)
    max_position = max(crab_horizontal_positions)

    # 3)
    best_score = 99999999
    for end_position in range(min_position, max_position):
        score = 0
        for crab in range(0, len(crab_horizontal_positions)):
            score += abs(crab_horizontal_positions[crab] - end_position)
        if score < best_score:
            best_score = score
    # 4)
    print("Here is solution for part 1: ", best_score)
    return best_score


def part2(row):
    # 1) load inputs into int array
    # 2) find min and max numbers in array
    # 3) for each number between min and max:
    # - calculate fuel for every number between max and min
    # - check if this is less fuel than in previous tries
    # 4) return least fuel

    # 1)
    crab_horizontal_positions = [int(x) for x in row[0].split(",")]

    # 2)
    min_position = min(crab_horizontal_positions)
    max_position = max(crab_horizontal_positions)
    print("min:", min_position, "max:", max_position)

    # 3)
    best_score = 99999999
    for end_position in range(min_position, max_position):
        print("trying position:", end_position)
        score = 0
        for crab in range(0, len(crab_horizontal_positions)):
            distance = abs(crab_horizontal_positions[crab] - end_position)
            current_fuel_step = 1
            for x in range(0, distance):
                score += current_fuel_step
                current_fuel_step += 1
        if score < best_score:
            best_score = score
    # 4)
    print("Here is solution for part 2: ", best_score)
    return best_score


# few simple tests
def test():
    test_inputs = "16,1,2,0,4,2,7,1,2,14\n".rstrip().split("\n")
    assert part1(test_inputs) == 37
    assert part2(test_inputs) == 168
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(7).rstrip().split("\n")
common.post_answer(7, 1, part1(inputs))
common.post_answer(7, 2, part2(inputs))
