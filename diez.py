import common
from collections import Counter


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# calculate difference between each two consecutive numbers, store in array
def part1(inputs):
    inputs_int = sorted([int(i) for i in inputs[:-1].split("\n")] + [0])
    differences = [0, 0, 0, 1]
    for index in range(0, len(inputs_int) - 1):
        differences[inputs_int[index + 1] - inputs_int[index]] += 1
    return differences[1] * differences[3]


# calculate ways to reach each number using collections.Counter
# foreach number in input, increase counters of number+1, number+2, number+3
# result is number
def part2(inputs):
    inputs_int = sorted([int(i) for i in inputs[:-1].split("\n")] + [0])
    c = Counter({0: 1})
    for x in inputs_int:
        c[x+1] += c[x]
        c[x+2] += c[x]
        c[x+3] += c[x]
    return c[inputs_int[-1] + 3]


def test():
    inputs = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4\n"
    assert part1(inputs) == 35
    assert part2(inputs) == 8
    inputs = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3\n"
    assert part1(inputs) == 220
    assert part2(inputs) == 19208
    inputs = "1\n3\n5\n6\n9\n"  # combinations are: 13569: 3569 369 1369
    assert part2(inputs) == 4
    print("All tests passed!")

# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(10)
result = part1(inputs)
common.post_answer(10, 1, result)

result = part2(inputs)
common.post_answer(10, 2, result)
