import common
import time


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
def magic(inputs, end):
    start = time.time()
    last_occurences = {}
    next_number = 0
    splitted = inputs.split(",")
    for index in range(0, len(splitted)):
        next_number = int(splitted[index])
        if index != len(splitted) - 1:
            last_occurences[next_number] = index + 1
    index += 1
    while index < end:
        current_number = next_number
        if current_number not in last_occurences:
            next_number = 0
        else:
            next_number = index - last_occurences[current_number]
        last_occurences[current_number] = index
        index += 1
    duration = time.time() - start
    print("Result for '" + inputs + "'(" + str(end) + ") = " + str(next_number) + ", time:" + str(duration))
    return next_number


# improved/faster version of this algorithm (simplify while loop, find a better formula, ...)
def magic_improved(inputs, end):
    pass

# Few simple tests
def test():
    assert magic("0,3,6", 2020) == 436
    assert magic("1,3,2", 2020) == 1
    assert magic("2,1,3", 2020) == 10
    assert magic("1,2,3", 2020) == 27
    assert magic("2,3,1", 2020) == 78
    assert magic("3,2,1", 2020) == 438
    assert magic("3,1,2", 2020) == 1836
    print("Tests for 2020 passed!")

    # BEWARE - current implementation takes ~24 seconds for each test
    assert magic("0,3,6", 30000000) == 175594
    assert magic("1,3,2", 30000000) == 2578
    assert magic("2,1,3", 30000000) == 3544142
    assert magic("1,2,3", 30000000) == 261214
    assert magic("2,3,1", 30000000) == 6895259
    assert magic("3,2,1", 30000000) == 18
    assert magic("3,1,2", 30000000) == 362
    print("Tests for 30000000 passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(15).rstrip()
result = magic(inputs, 2020)
common.post_answer(15, 1, result)

result = magic(inputs, 30000000)
common.post_answer(15, 2, result)
