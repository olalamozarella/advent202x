import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# In part one bitmask overrides input numbers (bits 0 and 1 in bitmask override bits in input numbers).
# Implemented by splitting each bitmask to two separate masks - first for bitwise OR, second for bitwise AND.
# We can then perform "number (bitwise OR) mask_or (bitwise AND) mask_and" to get result.
def part1(rows):
    mask_or = mask_and = 0
    memory = {}
    for row in rows:
        if row[:4] == "mask":
            mask = row[7:]
            mask_and = int(mask.replace("X", "1"), 2)   # mask for bitwise OR (all "X" replaced by ones)
            mask_or = int(mask.replace("X", "0"), 2)  # mask for bitwise AND (all "X" replaced by zeros)
        elif row[:3] == "mem":
            index = int(row[4:row.find("]")])
            value = int(row[row.find("= ")+2:])
            memory[index] = (value | mask_or) & mask_and
        else:
            print("BAD INPUT:" + row)
    return sum(memory.values())


# Part 2 implemented by splitting each bitmask to two separate masks - first for bitwise OR, second for bitwise AND.
# However, each "X" can be either 0 or 1 - we need to calculate all possible combinations.
# Example: mask 1X00X1 can be interpreted in four ways:
#   100001 => mask_or=100001, mask_and=101101
#   100011 => mask_or=100011, mask_and=101111
#   110001 => mask_or=110001, mask_and=111101
#   110011 => mask_or=110011, mask_and=111111
# Calculating address is then simple: address = (index | mask_ones) & mask_zeros
def part2(rows):
    def p2_recurse(index, x_indexes, mask_or, mask_and, addrmasks):
        if index == len(x_indexes) - 1:
            mask_or[x_indexes[index]] = "0"
            mask_and[x_indexes[index]] = "0"
            addrmasks.append((int("".join(mask_or), 2), int("".join(mask_and), 2)))
            mask_or[x_indexes[index]] = "1"
            mask_and[x_indexes[index]] = "1"
            addrmasks.append((int("".join(mask_or), 2), int("".join(mask_and), 2)))
            return
        mask_or[x_indexes[index]] = "0"
        mask_and[x_indexes[index]] = "0"
        p2_recurse(index + 1, x_indexes, mask_or, mask_and, addrmasks)
        mask_or[x_indexes[index]] = "1"
        mask_and[x_indexes[index]] = "1"
        p2_recurse(index + 1, x_indexes, mask_or, mask_and, addrmasks)

    memory = {}
    addrmasks = []  # tuples of (mask_or, mask_and), calculated for each mask from input
    for row in rows:
        if row[:4] == "mask":  # calculate addrmasks - list of tuples (mask_or, mask_and)
            addrmasks.clear()
            mask = list(row[7:])
            mask_and = list("1"*36)
            x_indexes = [i for i, letter in enumerate(mask) if letter == "X"]
            p2_recurse(0, x_indexes, mask, mask_and, addrmasks)
        elif row[:3] == "mem":  # for each addrmask calculate address, then set value
            index = int(row[4:row.find("]")])
            value = int(row[row.find("= ") + 2:])
            for mask_or, mask_and in addrmasks:
                address = (index | mask_or) & mask_and
                memory[address] = value
        else:
            print("BAD INPUT:" + row)
    return sum(memory.values())


# Few simple tests
def test():
    test_input = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0\n".rstrip().split("\n")
    assert part1(test_input) == 165
    test_input = "mask = 0X0X1110X1010X1X10010X0011010X100110\nmem[40190] = 23031023\nmem[13516] = 384739600\nmask = XX00111XX1010X0110011110X1XX110010X1\nmem[12490] = 3068791\nmem[61106] = 3432\nmem[48664] = 204086010\n".rstrip().split("\n")
    assert part1(test_input) == 19364060907
    test_input = "mask = 1000110000X000110101001X0X01X0010111\nmem[19225] = 57\nmem[37520] = 978\n".rstrip().split("\n")
    assert part1(test_input) == 75168891566
    test_input = "mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1".rstrip().split("\n")
    assert part2(test_input) == 208
    print("All tests passed!")

# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(14).rstrip().split("\n")
common.post_answer(14, 1, part1(inputs))
common.post_answer(14, 2, part2(inputs))
