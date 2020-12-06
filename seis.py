import common
from collections import Counter

# get inputs from webpage, remove last character - empty row, then split by empty rows
inputs = common.get_input(6)[:-1].split("\n\n")
# inputs = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb\n"[:-1].split("\n\n")  # test input

# Loop through all groups
result_part1 = 0
result_part2 = 0
for group in inputs:
    # Part 1: calculate number of unique letters in each group using collections.Counter
    counts = Counter(group.replace('\n', ''))  # Counter returns dictionary {letter:occurrences}, eg. {'a':0; 'b':1, ..}
    result_part1 += len(counts.keys())  # we just need to know how many keys are in dictionary

    # Part 2: count only letters that are present in each row (letter count has to be equal to row count)
    for letter in counts:
        if counts[letter] == (group.count("\n") + 1):  # group with one row has 0'\n', two rows => 1'\n', three rows => 2'\n'
            result_part2 += 1
    # Part 2: we can also do the same thing in one line using list comprehension - but it is ugly!
    # result_part2 += len([letter for letter in counts if counts[letter] == (group.count("\n") + 1)])

# send result to server
common.post_answer(6, 1, result_part1)
common.post_answer(6, 2, result_part2)
