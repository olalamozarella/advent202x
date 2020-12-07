import common
import re


# ---------------------------------------- FUNCTIONS PART1 ---------------------------------------- #
# function that reads input and fills bag_dictionary
# returns dictionary containing "bag color":[list of possible bag colors on outside]
def parse_input(inputs):
    bag_dictionary = {}
    for row in inputs[:-1].split("\n"):
        base_color = re.search("(\w+\s\w+)\sbags contain", row).group(1)
        if base_color not in bag_dictionary:
            bag_dictionary[base_color] = []
        inner_colors = re.findall("\d+\s(\w+\s\w+)", row)
        for color in inner_colors:
            if color in bag_dictionary:
                bag_dictionary[color].append(base_color)
            else:
                bag_dictionary[color] = [base_color]
    return bag_dictionary


# function that calculates all possible bag colors on outside
# returns list of all possible bag colors on outside
def calculate_outer_bags(dict, color, result=None):
    if result is None:
        result = set()  # create empty set at the start of recursion
    for outside_color in dict[color]:
        result.add(outside_color)  # add outside color to set
        calculate_outer_bags(dict, outside_color, result)  # recursively continue to outside color
    return result


# test of input parsing
def test_part1():
    test_input = "light red bags contain 1 bright white bag, 2 muted yellow bags.\n"\
                 "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"\
                 "bright white bags contain 1 shiny gold bag.\n"\
                 "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"\
                 "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"\
                 "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"\
                 "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"\
                 "faded blue bags contain no other bags.\n"\
                 "dotted black bags contain no other bags.\n"

    # assertions for dictionary keys and values
    bag_dictionary = parse_input(test_input)
    assert len(bag_dictionary) == 9
    assert bag_dictionary["light red"] == []
    assert bag_dictionary["dark orange"] == []
    assert bag_dictionary["bright white"] == ["light red", "dark orange"]
    assert bag_dictionary["muted yellow"] == ["light red", "dark orange"]
    assert bag_dictionary["shiny gold"] == ["bright white", "muted yellow"]
    assert bag_dictionary["dark olive"] == ["shiny gold"]
    assert bag_dictionary["vibrant plum"] == ["shiny gold"]
    assert bag_dictionary["faded blue"] == ["muted yellow", "dark olive", "vibrant plum"]
    assert bag_dictionary["dotted black"] == ["dark olive", "vibrant plum"]

    # assertions for bag calculations
    assert len(calculate_outer_bags(bag_dictionary, "light red")) == 0
    assert len(calculate_outer_bags(bag_dictionary, "dark orange")) == 0
    assert len(calculate_outer_bags(bag_dictionary, "dotted black")) == 7
    assert len(calculate_outer_bags(bag_dictionary, "bright white")) == 2
    assert len(calculate_outer_bags(bag_dictionary, "muted yellow")) == 2
    assert len(calculate_outer_bags(bag_dictionary, "shiny gold")) == 4
    assert len(calculate_outer_bags(bag_dictionary, "dark olive")) == 5
    assert len(calculate_outer_bags(bag_dictionary, "vibrant plum")) == 5
    assert len(calculate_outer_bags(bag_dictionary, "faded blue")) == 7

    print("All tests passed!")


# ---------------------------------------- FUNCTIONS PART2 ---------------------------------------- #
# function that reads input and fills bag_dictionary
# returns dictionary containing "bag color":[list of possible bag colors on inside]
def parse_input_part2(inputs):
    bag_dictionary = {}
    for row in inputs[:-1].split("\n"):
        base_color = re.search("(\w+\s\w+)\sbags contain", row).group(1)
        inner_colors = re.findall("(\d+)\s(\w+\s\w+)", row)
        bag_dictionary[base_color] = inner_colors
    return bag_dictionary


# function that calculates count of bags inside current bag
# returns count of bags inside current bag
def calculate_inner_bags(dict, color, result=None):
    result = 0  # set counter to zero at start of recursion
    for inside_color in dict[color]:
        inner_result = calculate_inner_bags(dict, inside_color[1], result)  # recursively continue to inside colors
        result += inner_result * int(inside_color[0]) + int(inside_color[0])
    return result


def test_part2():
    test_input = "shiny gold bags contain 2 dark red bags.\n"\
                 "dark red bags contain 2 dark orange bags.\n"\
                 "dark orange bags contain 2 dark yellow bags.\n"\
                 "dark yellow bags contain 2 dark green bags.\n"\
                 "dark green bags contain 2 dark blue bags.\n"\
                 "dark blue bags contain 2 dark violet bags.\n"\
                 "dark violet bags contain no other bags.\n"
    bag_dictionary = parse_input_part2(test_input)
    result = calculate_inner_bags(bag_dictionary, "dark violet")
    assert result == 0
    result = calculate_inner_bags(bag_dictionary, "dark blue")
    assert result == 2
    result = calculate_inner_bags(bag_dictionary, "dark green")
    assert result == 6
    result = calculate_inner_bags(bag_dictionary, "shiny gold")
    assert result == 126

    test_input = "light red bags contain 1 bright white bag, 2 muted yellow bags.\n"\
                 "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"\
                 "bright white bags contain 1 shiny gold bag.\n"\
                 "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"\
                 "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"\
                 "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"\
                 "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"\
                 "faded blue bags contain no other bags.\n"\
                 "dotted black bags contain no other bags.\n"
    bag_dictionary = parse_input_part2(test_input)
    result = calculate_inner_bags(bag_dictionary, "faded blue")
    assert result == 0
    result = calculate_inner_bags(bag_dictionary, "vibrant plum")
    assert result == 11
    result = calculate_inner_bags(bag_dictionary, "dark olive")
    assert result == 7
    result = calculate_inner_bags(bag_dictionary, "shiny gold")
    assert result == 32

    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test_part1()  # run the test for part1
test_part2()  # run the test for part2

inputs = common.get_input(7)
outer_dictionary = parse_input(inputs)
common.post_answer(7, 1, len(calculate_outer_bags(outer_dictionary, "shiny gold")))

inner_dictionary = parse_input_part2(inputs)
common.post_answer(7, 2, calculate_inner_bags(inner_dictionary, "shiny gold"))
