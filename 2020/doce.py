import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
def part1(inputs):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # E, S, W, N
    direction = 0  # current direction: EAST
    position = [0, 0]
    for row in inputs:
        number = int(row[1:])
        if row[0] == "L":
            direction = (direction - int(number / 90)) % 4
        elif row[0] == "R":
            direction = (direction + int(number / 90)) % 4
        elif row[0] == "F":
            position[0] += directions[direction][0] * number
            position[1] += directions[direction][1] * number
        elif row[0] == "N":
            position[1] += number
        elif row[0] == "S":
            position[1] -= number
        elif row[0] == "W":
            position[0] -= number
        elif row[0] == "E":
            position[0] += number
    return abs(position[0]) + abs(position[1])


def part2(inputs):
    waypoint = [10, 1]
    position = [0, 0]

    for row in inputs:
        number = int(row[1:])
        if row[0] == "L":
            for i in range(0, int(number/90)):
                waypoint = [waypoint[1] * -1, waypoint[0]]
        elif row[0] == "R":
            for i in range(0, int(number / 90)):
                waypoint = [waypoint[1], waypoint[0] * -1]
        elif row[0] == "F":
            position[0] += waypoint[0] * number
            position[1] += waypoint[1] * number
        elif row[0] == "N":
            waypoint[1] += number
        elif row[0] == "S":
            waypoint[1] -= number
        elif row[0] == "W":
            waypoint[0] -= number
        elif row[0] == "E":
            waypoint[0] += number
    return abs(position[0]) + abs(position[1])


# Few simple tests
def test():
    inputs = "F10\nN3\nF7\nR90\nF11\n".rstrip().split("\n")
    assert part1(inputs) == 25
    assert part2(inputs) == 286
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(12).rstrip().split("\n")
result = part1(inputs)
common.post_answer(12, 1, result)

result = part2(inputs)
common.post_answer(12, 2, result)
