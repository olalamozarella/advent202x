import common


# This is where the magic happens
def stromceky(down, right):
    x, tree_counter = 0, 0
    for row in rows[down:-1:down]:
        x = (x + right) % len(row)
        if row[x] == '#':
            tree_counter += 1
    print("And the result for R{:d} D{:d} is........ {:d}".format(right, down, tree_counter))
    return tree_counter


# get input
rows = common.get_input(3).split("\n")
#rows = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#\n".split("\n")

# Part 1:
part1_result = stromceky(1, 3)
common.post_answer(3, 1, part1_result)

# Part 2:
part2_result = stromceky(1, 1) * part1_result * stromceky(1, 5) * stromceky(1, 7) * stromceky(2, 1)
common.post_answer(3, 2, part2_result)
