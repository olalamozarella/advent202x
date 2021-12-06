import common
import re


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    # read marked numbers
    marked_numbers = rows[0].split(",")

    # save score for the best board
    best_board_turns = 999
    best_board_score = 0

    # for all boards:
    current_row = 0
    while True:
        # read one board (5x5)
        board = (re.split("  | ", rows[current_row+2].lstrip()),
                 re.split("  | ", rows[current_row+3].lstrip()),
                 re.split("  | ", rows[current_row+4].lstrip()),
                 re.split("  | ", rows[current_row+5].lstrip()),
                 re.split("  | ", rows[current_row+6].lstrip())
                 )

        # prepare marking counters for each row and column
        row_counter = [0, 0, 0, 0, 0]
        col_counter = [0, 0, 0, 0, 0]

        # separate array for counting unmarked numbers
        unmarked_numbers = []
        for i in range(0, 5):
            for j in range(0, 5):
                unmarked_numbers.append(int(board[i][j]))

        # search for each number in the board; mark its row and column in the counters
        for index, number in enumerate(marked_numbers):
            # - mark number to the board
            for row in range(0, 5):
                if number in board[row]:
                    row_counter[row] += 1
                    for col in range(0, 5):
                        if number == board[row][col]:
                            col_counter[col] += 1
                    unmarked_numbers.remove(int(number))

            # - check winning (whether any row or col counter is 5)
            if 5 in row_counter or 5 in col_counter:
                unmarked_sum = 0
                for i in unmarked_numbers:
                    unmarked_sum += i
                if best_board_turns > index:
                    best_board_turns = index
                    best_board_score = int(number) * unmarked_sum
                print("won on ", index, "th number (", number, "), unmarked sum=", unmarked_sum)
                break

        # increment current_row for reading next board
        current_row += 6
        if current_row > len(rows)-2:
            break

    return best_board_score


# solution for the second part
def part2(rows):
    # read marked numbers
    marked_numbers = rows[0].split(",")

    # save score for the best board
    best_board_turns = 1
    best_board_score = 0

    # for all boards:
    current_row = 0
    while True:
        # read one board (5x5)
        board = (re.split("  | ", rows[current_row + 2].lstrip()),
                 re.split("  | ", rows[current_row + 3].lstrip()),
                 re.split("  | ", rows[current_row + 4].lstrip()),
                 re.split("  | ", rows[current_row + 5].lstrip()),
                 re.split("  | ", rows[current_row + 6].lstrip())
                 )

        # prepare marking counters for each row and column
        row_counter = [0, 0, 0, 0, 0]
        col_counter = [0, 0, 0, 0, 0]

        # separate array for counting unmarked numbers
        unmarked_numbers = []
        for i in range(0, 5):
            for j in range(0, 5):
                unmarked_numbers.append(int(board[i][j]))

        # search for each number in the board; mark its row and column in the counters
        for index, number in enumerate(marked_numbers):
            # - mark number to the board
            for row in range(0, 5):
                if number in board[row]:
                    row_counter[row] += 1
                    for col in range(0, 5):
                        if number == board[row][col]:
                            col_counter[col] += 1
                    unmarked_numbers.remove(int(number))

            # - check winning (whether any row or col counter is 5)
            if 5 in row_counter or 5 in col_counter:
                unmarked_sum = 0
                for i in unmarked_numbers:
                    unmarked_sum += i
                if best_board_turns < index:
                    best_board_turns = index
                    best_board_score = int(number) * unmarked_sum
                print("won on ", index, "th number (", number, "), unmarked sum=", unmarked_sum)
                break

        # increment current_row for reading next board
        current_row += 6
        if current_row > len(rows) - 2:
            break

    return best_board_score


# few simple tests
def test():
    test_inputs = \
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n" \
    "\n" \
    "22 13 17 11  0\n" \
    " 8  2 23  4 24\n" \
    "21  9 14 16  7\n" \
    " 6 10  3 18  5\n" \
    " 1 12 20 15 19\n" \
    "\n" \
    " 3 15  0  2 22\n" \
    " 9 18 13 17  5\n" \
    "19  8  7 25 23\n" \
    "20 11 10 24  4\n" \
    "14 21 16 12  6\n" \
    "\n" \
    "14 21 17 24  4\n" \
    "10 16 15  9 19\n" \
    "18  8 23 26 20\n" \
    "22 11 13  6  5\n" \
    " 2  0 12  3  7\n".rstrip().split("\n")
    # assert part1(test_inputs) == 4512
    assert part2(test_inputs) == 1924
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(4).rstrip().split("\n")
common.post_answer(4, 1, part1(inputs))
common.post_answer(4, 2, part2(inputs))
