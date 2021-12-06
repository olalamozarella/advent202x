import common
import time


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    start_time = time.time()
    result = lanternfish_bruteforce(rows, 80)
    execution_time = (time.time() - start_time)
    print('lanternfish_bruteforce: ' + str(execution_time))

    start_time = time.time()
    result = lanternfish_optimized(rows, 80)
    execution_time = (time.time() - start_time)
    print('lanternfish_optimized: ' + str(execution_time))
    return result


# solution for the second part
def part2(rows):
    return lanternfish_optimized(rows, 256)


# function for solving the lanternfish task, using just dumb iterating over all numbers
# not viable for more than ~150 days/iterations
def lanternfish_bruteforce(input_rows, number_of_days):
    # 1) create array of fish (numbers)
    # 2) for 80 days/iterations, calculate results of one day
    #  - create empty array for results
    #  - go through all inputs
    #      decrement number
    #      if result > 0: write it to result array
    #      else: write 6 (for old fish) and 8 (for new fish) to the result array
    # 3) repeat 80 times, return result

    # 1)
    current_day_fish = [int(x) for x in input_rows[0].split(",")]

    # 2)
    for day in range(number_of_days):
        print("Day:", day)
        next_day_fish = []
        for fish in current_day_fish:
            fish -= 1
            if fish < 0:
                next_day_fish.append(6)
                next_day_fish.append(8)
            else:
                next_day_fish.append(fish)
        current_day_fish = next_day_fish

    # 3)
    return len(next_day_fish)


# optimized function for solving the lanternfish task
def lanternfish_optimized(input_rows, number_of_days):
    # 1) create counting array (8 numbers, every number representing count of fish in that exact day stage)
    # 2) parse inputs, fill the counting array
    # 3) iterate over the days and update the counters
    # 4) sum all counters and return

    # 1)
    counting_array = [0] * 9

    # 2)
    current_day_fish = [int(x) for x in input_rows[0].split(",")]
    for fish in current_day_fish:
        counting_array[fish] += 1

    # 3)
    for day in range(number_of_days):
        next_counting_array = [0] * 9
        next_counting_array[0] = counting_array[1]
        next_counting_array[1] = counting_array[2]
        next_counting_array[2] = counting_array[3]
        next_counting_array[3] = counting_array[4]
        next_counting_array[4] = counting_array[5]
        next_counting_array[5] = counting_array[6]
        next_counting_array[6] = counting_array[7] + counting_array[0]
        next_counting_array[7] = counting_array[8]
        next_counting_array[8] = counting_array[0]
        counting_array = next_counting_array

    result = 0
    for c in counting_array:
        result += c
    return result


# few simple tests
def test():
    test_inputs = "3,4,3,1,2\n".rstrip().split("\n")
    assert part1(test_inputs) == 5934
    assert part2(test_inputs) == 26984457539
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(6).rstrip().split("\n")
common.post_answer(6, 1, part1(inputs))
common.post_answer(6, 2, part2(inputs))
