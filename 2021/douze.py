import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    # create dictionary of links
    # foreach row
    #   add to dictionary for the first node
    #   add to dictionary for the second node
    #
    # call magic_function for start_node
    # count results
    dictionary = {}
    for row in rows:
        splitted = row.split("-")
        if splitted[0] not in dictionary:
            dictionary[splitted[0]] = [splitted[1]]
        else:
            dictionary[splitted[0]].append(splitted[1])
        if splitted[1] not in dictionary:
            dictionary[splitted[1]] = [splitted[0]]
        else:
            dictionary[splitted[1]].append(splitted[0])

    current_path = []
    results = []
    magic_function_p1(dictionary, "start", current_path, results)
    return len(results)


# solution for the second part
def part2(rows):
    # create dictionary of links
    # foreach row
    #   add to dictionary for the first node
    #   add to dictionary for the second node
    #
    # call magic_function for start_node
    # count results
    dictionary = {}
    for row in rows:
        splitted = row.split("-")
        if splitted[0] not in dictionary:
            dictionary[splitted[0]] = [splitted[1]]
        else:
            dictionary[splitted[0]].append(splitted[1])
        if splitted[1] not in dictionary:
            dictionary[splitted[1]] = [splitted[0]]
        else:
            dictionary[splitted[1]].append(splitted[0])

    current_path = []
    results = []
    magic_function_p2(dictionary, "start", current_path, results)
    print("part2 result:", len(results))
    return len(results)


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #
# recursive function for finding all paths (small caves can be visited max once)
def magic_function_p1(dictionary, current_node, previous_path, results):
    # load all caves for current_node
    # for cave:
    #   if cave == "end":
    #      write current path to results
    #      return
    #   else: have we entered this cave yet?
    #      no: magic_function(cave)
    #      yes:
    #          is small letter or "start"?
    #              return
    #          else:
    #              magic_function(cave)

    current_path = previous_path.copy()  # we don't want to change the path for previous function calls - we need a copy
    current_path.append(current_node)
    for cave in dictionary[current_node]:
        if cave == "end":
            results.append(current_path)
            continue
        else:
            if cave not in current_path:
                magic_function_p1(dictionary, cave, current_path, results)
            else:
                if cave == "start" or cave.islower() is True:
                    continue
                else:
                    magic_function_p1(dictionary, cave, current_path, results)


# recursive function for finding all paths (small caves can be visited max two times)
# it is a copy of magic_function_p1, but refactored a bit (removed else-s and indentation levels) and added last if
def magic_function_p2(dictionary, current_node, previous_path, results):
    # load all caves for current_node
    # for cave:
    #   if cave == "end":
    #      write current path to results
    #      continue with next cave
    #   if cave == "start":
    #      continue with next cave (start cannot be used more than once)
    #   if we have not entered this cave yet:
    #      enter the cave (call magic_function) - this cave was not entered yet
    #      continue with next cave
    #   if is capital letter
    #      enter the cave (call magic_function) - we can enter capital caves as many times as we like
    #      continue with next cave
    #
    #   (if we get here, current cave is lowercase and not "start" or "end", and we visited it already at least once)
    #   if was any small cave visited twice?
    #      no: call magic_function - we can enter this small cave for the second time
    #      yes: continue with next cave - we have already used the second visit for some other cave

    current_path = previous_path.copy()  # we don't want to change the path for previous function calls - we need a copy
    current_path.append(current_node)
    for cave in dictionary[current_node]:
        if cave == "end":
            end_path = current_path.copy().append(cave)
            results.append(end_path)
            continue
        if cave == "start":
            continue
        if cave not in current_path:
            magic_function_p2(dictionary, cave, current_path, results)
            continue
        if cave.isupper() is True:
            magic_function_p2(dictionary, cave, current_path, results)
            continue
        if any_small_cave_visited_twice(current_path) is False:
            magic_function_p2(dictionary, cave, current_path, results)


# function that checks if any small cave (lowercase letter) exists two times in the path
# returns True if such cave exists in path
# returns False if no small cave exists twice in the path
def any_small_cave_visited_twice(path):
    # pick lowercase caves from path
    # foreach cave, check count
    #   if count >=2, return True
    # return False (no caves returned True)
    lowercase_caves = [cave for cave in path if cave.islower()]
    for cave in lowercase_caves:
        if lowercase_caves.count(cave) >= 2:
            return True
    return False


# ----------------------------------------- TEST --------------------------------------------#
# few simple tests
def test():
    test_inputs = \
        "start-A\n" \
        "start-b\n" \
        "A-c\n" \
        "A-b\n" \
        "b-d\n" \
        "A-end\n" \
        "b-end\n" \
        .rstrip().split("\n")
    assert part1(test_inputs) == 10
    assert part2(test_inputs) == 36

    test_inputs = \
        "dc-end\n" \
        "HN-start\n" \
        "start-kj\n" \
        "dc-start\n" \
        "dc-HN\n" \
        "LN-dc\n" \
        "HN-end\n" \
        "kj-sa\n" \
        "kj-HN\n" \
        "kj-dc\n" \
        .rstrip().split("\n")
    assert part1(test_inputs) == 19
    assert part2(test_inputs) == 103

    test_inputs = \
        "fs-end\n" \
        "he-DX\n" \
        "fs-he\n" \
        "start-DX\n" \
        "pj-DX\n" \
        "end-zg\n" \
        "zg-sl\n" \
        "zg-pj\n" \
        "pj-he\n" \
        "RW-he\n" \
        "fs-DX\n" \
        "pj-RW\n" \
        "zg-RW\n" \
        "start-pj\n" \
        "he-WI\n" \
        "zg-he\n" \
        "pj-fs\n" \
        "start-RW\n" \
        .rstrip().split("\n")
    assert part1(test_inputs) == 226
    assert part2(test_inputs) == 3509

    print("All tests passed!")

# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(12).rstrip().split("\n")
common.post_answer(12, 1, part1(inputs))
common.post_answer(12, 2, part2(inputs))
