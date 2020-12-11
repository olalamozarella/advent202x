import common
from copy import deepcopy
import time


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# Function that counts occupied seats in all directions.
# Can be used for both part1 (count only adjacent seats) and part2 (count closest seat in each direction).
def count_occupied_neighbors(previous_run, row, col, is_part2=False):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    current_count = 0
    for dx, dy in directions:  # foreach direction
        row2, col2 = row, col
        while True:  # loop in this direction until you reach edge/first seat/is part1 (checking only closest seat)
            row2, col2 = row2 + dx, col2 + dy
            if row2 < 0 or row2 >= len(previous_run) or col2 < 0 or col2 >= len(previous_run[row]):
                break  # edge reached
            elif previous_run[row2][col2] == "#":
                current_count += 1
                break  # this direction is occupied
            elif previous_run[row2][col2] == "L":
                break  # this direction is vacant
            if is_part2 is False:
                break  # this direction contained floor, part2 doesn't continue further
    return current_count


# Logic for AoC Day 11 (both part 1 and part 2):
# Part 1:
# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied (#) and FOUR or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.
# Part 2:
# - Same as part 1, but if there is a floor in that direction, check the seat behind it.
# - If a seat is occupied (#) and FIVE or more seats adjacent to it are also occupied, the seat becomes empty.
def seat_magic(inputs, is_part2=False):
    max_occupied_seats = 4 if is_part2 else 3
    previous_run = [list(x) for x in inputs.rstrip().split("\n")]
    previous_occupied = 0
    while True:
        current_run = deepcopy(previous_run)
        total_occupied = 0
        for row in range(0, len(previous_run)):
            for col in range(0, len(previous_run[row])):
                if previous_run[row][col] == ".":
                    continue
                current_count = count_occupied_neighbors(previous_run, row, col, is_part2)
                if previous_run[row][col] == "L" and current_count == 0:
                    current_run[row][col] = "#"
                elif previous_run[row][col] == "#" and current_count > max_occupied_seats:
                    current_run[row][col] = "L"
                if current_run[row][col] == "#":
                    total_occupied += 1
        if previous_occupied == total_occupied:
            print("And we have result: " + str(total_occupied))
            return total_occupied
        else:
            previous_occupied = total_occupied
            previous_run = current_run


# Few simple tests
def test():
    inputs = "LLL\n.L.\nLLL\n"
    assert seat_magic(inputs) == 6
    assert seat_magic(inputs, True) == 6
    inputs = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL\n"
    assert seat_magic(inputs) == 37
    assert seat_magic(inputs, True) == 26
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(11)
print("Starting part 1")
start = time.time()
result = seat_magic(inputs)
end = time.time()
print("Time:" + str(end - start))
common.post_answer(11, 1, result)

print("Starting part 2")
start = time.time()
result = seat_magic(inputs, True)
end = time.time()
print("Time:" + str(end - start))
common.post_answer(11, 2, result)
