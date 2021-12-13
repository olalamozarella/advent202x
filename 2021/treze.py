import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    # read input, store dots in set, folds in list
    # - working_set = list of (y, x); beware, x(column) increases to the right, y(row) increases down
    # - folds = list of ("x|y", index); y is row, x is column
    #
    # for each fold:
    #   create new set
    #   for each item in set:
    #      if fold is on x
    #        if item.x < fold.x:
    #          item remains on the same position => add (item.x, item.y) to the new set
    #        elif item.x > fold.x:
    #          item is mirrored => add (item.x - fold.x, item.y) to the new set
    #        else:
    #          item is directly on fold => ignore it
    #      if fold is on y
    #        if item.y < fold.y:
    #          item remains on the same position => add (item.x, item.y) to the new set
    #        elif item.y > fold.y:
    #          item is mirrored => add (item.x, item.y - fold.y) to the new set
    #        else:
    #          item is directly on fold => ignore it
    #   count remaining dots

    working_set = set()
    folds = []
    for row in rows:
        if len(row) == 0:
            continue
        if row[0] == "f":
            splitted = row.split(" ")[2].split("=")
            fold = (splitted[0], int(splitted[1]))
            folds.append(fold)
        else:
            splitted = row.split(",")
            dot = (int(splitted[0]), int(splitted[1]))
            working_set.add(dot)

    result_p1 = 0
    for fold_index, fold in enumerate(folds):
        new_set = set()
        for dot in working_set:
            if fold[0] == "x":
                if dot[0] < fold[1]:
                    new_set.add(dot)
                elif dot[0] > fold[1]:
                    distance_to_fold = dot[0] - fold[1]
                    mirrored_dot = (dot[0] - distance_to_fold - distance_to_fold, dot[1])
                    new_set.add(mirrored_dot)
                else:
                    print("x - point on fold is discarded")
            elif fold[0] == "y":
                if dot[1] < fold[1]:
                    new_set.add(dot)
                elif dot[1] > fold[1]:
                    distance_to_fold = dot[1] - fold[1]
                    mirrored_dot = (dot[0], dot[1] - distance_to_fold - distance_to_fold)
                    new_set.add(mirrored_dot)
                else:
                    print("y - point on fold is discarded")
        working_set = new_set
        print("After fold={0}, remaining dots={1}".format(fold_index, len(working_set)))
        if fold_index == 0:
            result_p1 = len(working_set)

    # no calculation for part 2, just print results
    part2(working_set)
    return result_p1


# solution for the second part - just prints the set
def part2(working_set):
    max_column = 0
    max_row = 0
    for dot in working_set:
        if dot[0] > max_column:
            max_column = dot[0]
        if dot[1] > max_row:
            max_row = dot[1]

    result_p2 = [[" "] * (max_column + 1) for row in range(0, max_row+1)]
    for dot in working_set:
        result_p2[dot[1]][dot[0]] = "#"
    for row in result_p2:
        joined_row = ''.join(str(x) for x in row)
        print(joined_row)


# few simple tests
def test():
    test_inputs = \
                  "6,10\n" \
                  "0,14\n" \
                  "9,10\n" \
                  "0,3\n" \
                  "10,4\n" \
                  "4,11\n" \
                  "6,0\n" \
                  "6,12\n" \
                  "4,1\n" \
                  "0,13\n" \
                  "10,12\n" \
                  "3,4\n" \
                  "3,0\n" \
                  "8,4\n" \
                  "1,10\n" \
                  "2,14\n" \
                  "8,10\n" \
                  "9,0\n" \
                  "\n" \
                  "fold along y=7\n" \
                  "fold along x=5\n" \
                  .rstrip().split("\n")
    assert part1(test_inputs) == 17
    # assert part2(test_inputs) == 0  # part2 is solved manually, no test available
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(13).rstrip().split("\n")
common.post_answer(13, 1, part1(inputs))

# part 2 is solved manually by looking at part1 output (just read the output, is should be 8 capital letters)
