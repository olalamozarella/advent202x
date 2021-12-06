import common
import re


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# parses text input to three different variables - list of categories, my ticket, list of other tickets
# return: ([categories], [my ticket], [other tickets])
def parse_inputs(inputs):
    sections = inputs.split("\n\n")
    categories = []
    for row in sections[0].split("\n"):
        matches = re.search('(.*):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)', row)
        name = matches.group(1)
        min1, max1 = int(matches.group(2)), int(matches.group(3))
        min2, max2 = int(matches.group(4)), int(matches.group(5))
        categories.append((name, min1, max1, min2, max2))
    my_ticket = [int(x) for x in sections[1].split("\n")[1].split(",")]
    other_tickets = []
    for row in sections[2].split("\n")[1:]:
        other_tickets.append([int(x) for x in row.split(",")])
    return categories, my_ticket, other_tickets


# loops over other tickets and removes invalid tickets
# return: [valid_other_tickets], invalid sum (result of part 1)
def remove_invalid_tickets(categories, other_tickets):
    valid_other_tickets = []
    invalid_sum = 0
    for ticket in other_tickets:
        ticket_valid = True
        for number in ticket:
            valid = False
            for category in categories:
                if (category[1] <= number <= category[2]) or (category[3] <= number <= category[4]):
                    valid = True
                    break
            if not valid:
                invalid_sum += number
                ticket_valid = False
        if ticket_valid is True:
            valid_other_tickets.append(ticket)
    return valid_other_tickets, invalid_sum


# calculates possible categories for each column
# return: possibilities = [(possible for cat 0), (possible for cat 1), ..., (possible for cat n)]
def calculate_possibilities(categories, my_ticket, valid_other_tickets):
    # each category is possible for each column at the beginning
    possibilities = [list(range(0, len(categories))) for column in my_ticket]
    # loop over all tickets (my + other), check if each column is valid
    for ticket in valid_other_tickets:
        for column, number in enumerate(ticket):
            for cat_index, category in enumerate(categories):
                if (category[1] <= ticket[column] <= category[2]) or (category[3] <= ticket[column] <= category[4]):
                    pass
                else:
                    possibilities[column][cat_index] = -1
    return possibilities


# reads calculated possibilities and picks only one possibility for each category
# return: list of numbers, each number is equal to category for that column
def match_categories(possibilities):
    matched_categories = [0] * len(possibilities)
    # loop over each column possibility
    # at most 20 runs are needed
    for run in range(20):
        for column, possibility in enumerate(possibilities):
            # if there is only one option, remove this option from all other columns
            if possibility.count(-1) == (len(possibilities) - 1):
                number = [x for x in possibility if x != -1][0]
                for possibility2 in possibilities:
                    possibility2[number] = -1
                matched_categories[column] = number
    return matched_categories


# implementation of part 1
def part1(inputs):
    categories, my_ticket, other_tickets = parse_inputs(inputs)
    valid_other_tickets, invalid_sum = remove_invalid_tickets(categories, other_tickets)
    return invalid_sum


# implementation of part 2
# return: one number (result of part 2)
def part2(inputs):
    categories, my_ticket, other_tickets = parse_inputs(inputs)
    valid_other_tickets, invalid_sum = remove_invalid_tickets(categories, other_tickets)
    possibilities = calculate_possibilities(categories, my_ticket, valid_other_tickets)
    matched_categories = match_categories(possibilities)
    result = 1
    for i in range(0, len(matched_categories)):
        if matched_categories[i] < 6:
            result *= my_ticket[i]
    return result


# Few simple tests
def test():
    inputs = "class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\nyour ticket:\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12"
    categories, my_ticket, other_tickets = parse_inputs(inputs)
    assert categories[0] == ("class", 1, 3, 5, 7)
    assert my_ticket == [7, 1, 14]
    assert other_tickets == [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]

    assert part1(inputs) == 71
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(16).rstrip()
result = part1(inputs)
common.post_answer(16, 1, result)

result = part2(inputs)
common.post_answer(16, 2, result)
