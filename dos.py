import common
import re

# get inputs from webpage using session cookie
rows = common.get_input(2).split("\n")

# loop through all rows, parse and check validity
part1_valid, part2_valid = 0, 0
for row in rows:
    result = re.search('(\d+)-(\d+)\s(\w):\s(\w+)', row)
    if result is None:
        continue
    minimum = int(result.group(1))
    maximum = int(result.group(2))
    character = result.group(3)
    password = result.group(4)
    # part 1 - check if character count is between min and max
    if minimum <= password.count(character) <= maximum:
        part1_valid += 1
    # part 2 - check if character is at first X-OR second position
    if (password[minimum-1] == character) ^ (password[maximum-1] == character):
        part2_valid += 1
print("Part 1: valid passwords=" + str(part1_valid))
print("Part 2: valid passwords=" + str(part2_valid))
