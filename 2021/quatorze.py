import common
from collections import Counter


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    return polymers_bruteforce(rows, 10)


# solution for the second part
def part2(rows):
    return polymers_optimized(rows, 40)


# few simple tests
def test():
    test_inputs = \
        "NNCB\n" \
        "\n" \
        "CH -> B\n" \
        "HH -> N\n" \
        "CB -> H\n" \
        "NH -> C\n" \
        "HB -> C\n" \
        "HC -> B\n" \
        "HN -> C\n" \
        "NN -> C\n" \
        "BH -> H\n" \
        "NC -> B\n" \
        "NB -> B\n" \
        "BN -> B\n" \
        "BB -> N\n" \
        "BC -> B\n" \
        "CC -> N\n" \
        "CN -> C\n" \
        .rstrip().split("\n")
    assert polymers_bruteforce(test_inputs, 10) == 1588
    assert polymers_optimized(test_inputs, 10) == 1588
    assert part1(test_inputs) == 1588
    assert part2(test_inputs) == 2188189693529
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #
# helper function for solving polymer reactions using bruteforce string arrays
def polymers_bruteforce(rows, steps):
    # load starting polymer into list
    # load rules into dictionary
    #
    # for 10 steps:
    #   copy original_polymer into working_polymer
    #   for each character in original_polymer:
    #     append character in working_polymer
    #     check if pair is present in rules dictionary
    #       yes: append result into working_polymer
    #   working_polymer becomes original_polymer for next iteration
    #
    # get most and least common element
    # subtract and return result

    original_polymer = list(rows[0])  # store original polymer into list (we will iterate through characters and append a lot of stuff, so list has better performance as string)
    rules = {}
    for row_index in range(2, len(rows)):
        splitted = rows[row_index].split(" -> ")
        key = tuple(splitted[0])  # dictionary key is a tuple, not string due to better performance (we would need to create new string for every search later)
        rules[key] = splitted[1]

    for step in range(0, steps):
        working_polymer = []
        for char_index in range(0, len(original_polymer) - 1):
            working_polymer.append(original_polymer[char_index])
            pair = (original_polymer[char_index], original_polymer[char_index + 1])
            if pair in rules:
                working_polymer.append(rules[pair])
        working_polymer.append(original_polymer[-1])  # last character is added outside of for loop
        original_polymer = working_polymer

    counts = Counter(original_polymer)
    most_common = counts.most_common()[0]
    least_common = counts.most_common()[-1]
    result = most_common[1] - least_common[1]
    print("polymers_bruteforce most_common:", most_common, "; least_common:", least_common, "result:", result)

    return result


# helper function for solving polymer reactions using more optimized way
def polymers_optimized(rows, steps):
    # create dictionary of products: pair => (pair1, pair2)  ; note: use defaultdict() for performance
    # create dictionary of polymer_counts: pair => count  ; note: use defaultdict() for performance
    # fill polymer_counts with starting polymer
    # store first and last character separately (will be used in the end)
    #
    # for 40 iterations:
    #   create copy of polymer_counts (working_copy)
    #   for each polymer in polymer_counts:
    #     find products
    #     increment their counts in working_copy
    #   polymer_counts = working_copy
    #
    # create counter for each element
    # for each pair in polymer_counts
    #   add polymer_count to the counters of both elements
    # increment counters for first and last element
    # divide all counter by 2
    # find most and least common

    empty_polymer_counts = {}
    products = {}
    for row_index in range(2, len(rows)):
        splitted = rows[row_index].split(" -> ")
        key = splitted[0]
        value = (splitted[0][0] + splitted[1], splitted[1] + splitted[0][1])
        products[key] = value
        empty_polymer_counts[key] = 0

    polymer_counts = empty_polymer_counts.copy()
    original_polymer = rows[0]
    for i in range(0, len(original_polymer) - 1):
        pair = original_polymer[i] + original_polymer[i + 1]
        polymer_counts[pair] += 1

    for step in range(0, steps):
        working_copy = empty_polymer_counts.copy()
        for pair in polymer_counts:
            new_products = products[pair]
            working_copy[new_products[0]] += polymer_counts[pair]
            working_copy[new_products[1]] += polymer_counts[pair]
        polymer_counts = working_copy

    element_counter = {}
    for pair in polymer_counts:
        element1, element2 = pair[0], pair[1]
        if element1 not in element_counter:
            element_counter[element1] = polymer_counts[pair]
        else:
            element_counter[element1] += polymer_counts[pair]
        if element2 not in element_counter:
            element_counter[element2] = polymer_counts[pair]
        else:
            element_counter[element2] += polymer_counts[pair]
    element_counter[original_polymer[0]] += 1
    element_counter[original_polymer[-1]] += 1

    most_common = False
    least_common = False
    for element in element_counter:
        divided_value = int(element_counter[element] / 2)
        if least_common is False or divided_value < least_common[1]:
            least_common = (element, divided_value)
        if most_common is False or divided_value > most_common[1]:
            most_common = (element, divided_value)

    result = most_common[1] - least_common[1]
    print("polymers_optimized most_common:", most_common, "; least_common:", least_common, "result:", result)
    return result


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(14).rstrip().split("\n")
common.post_answer(14, 1, part1(inputs))
common.post_answer(14, 2, part2(inputs))
