import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first and second part
def part1_2(rows):
    # load inputs into big array
    # flash_counter = 0
    # for 100 steps
    #   for each octopus:
    #     increment internal state
    #   perform flashing
    # return total_flashes
    octopus_map = [[int(x) for x in row] for row in rows]

    result_p1 = 0
    step = 0
    while True:
        step += 1
        octopus_map = [[state+1 for state in row] for row in octopus_map]
        flashes_in_this_step = flash(octopus_map)
        octopus_map = [[0 if state == "F" else state for state in row] for row in octopus_map]

        # solution for part 1: count all flashes in first 100 steps:
        if step <= 100:
            result_p1 += flashes_in_this_step

        # solution for part 2: return step index when all octopi will flash
        if flashes_in_this_step == 100:
            print("P2: All will flash in step", step)
            break

    return result_p1, step


# few simple tests
def test():
    test_inputs = \
        "5483143223\n" \
        "2745854711\n" \
        "5264556173\n" \
        "6141336146\n" \
        "6357385478\n" \
        "4167524645\n" \
        "2176841721\n" \
        "6882881134\n" \
        "4846848554\n" \
        "5283751526\n" \
        .rstrip().split("\n")
    assert part1_2(test_inputs) == (1656, 195)
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #
def flash(octopus_map):
    # step_flashes = 0
    # go over the whole map
    #   iteration_flashes = 0
    #   flash octopuses with state > 9
    #       increment neighbors (do not count octopuses with state "F")
    #       set state to "F"
    #       increment interation_flashes
    # if iteration_flashes != 0, repeat
    # else return step_flashes
    step_flashes = 0
    while True:
        iteration_flashes = 0
        for row in range(len(octopus_map)):
            for column in range(len(octopus_map[row])):
                if octopus_map[row][column] == "F":
                    continue
                elif octopus_map[row][column] > 9:
                    octopus_map[row][column] = "F"
                    iteration_flashes += 1
                    safely_increment_octopus(octopus_map, row, column - 1)
                    safely_increment_octopus(octopus_map, row, column + 1)
                    safely_increment_octopus(octopus_map, row - 1, column - 1)
                    safely_increment_octopus(octopus_map, row - 1, column)
                    safely_increment_octopus(octopus_map, row - 1, column + 1)
                    safely_increment_octopus(octopus_map, row + 1, column - 1)
                    safely_increment_octopus(octopus_map, row + 1, column)
                    safely_increment_octopus(octopus_map, row + 1, column + 1)
        if iteration_flashes == 0:
            break
        else:
            step_flashes += iteration_flashes
    return step_flashes


def safely_increment_octopus(octopus_map, row, column):
    if row < 0 or row >= len(octopus_map):
        return
    if column < 0 or column >= len(octopus_map[row]):
        return
    if octopus_map[row][column] == "F":
        return
    octopus_map[row][column] += 1


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(11).rstrip().split("\n")
result_p1, result_p2 = part1_2(inputs)
common.post_answer(11, 1, result_p1)
common.post_answer(11, 2, result_p2)
