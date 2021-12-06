import common
import time


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# bruteforce approach for part 1 - calculate waiting time for each bus, pick lowest one
def part1(inputs):
    timestamp = int(inputs[0])
    buses = [int(x) for x in inputs[1].split(",") if x != "x"]
    best_bus = -1
    shortest_wait = 9999
    for bus in buses:
        minutes_to_departute = bus - (timestamp % bus)
        if minutes_to_departute < shortest_wait:
            shortest_wait = minutes_to_departute
            best_bus = bus
    return best_bus * shortest_wait


# bruteforce approach for part 2 - for each number/timestamp verify that conditions pass (my PC processes 15M numbers/s)
# - upgrade 1: go only through multiplies of biggest bus number (with this upgrade, my PC processes 680M numbers/s)
# - upgrade 2: print current number each 10 seconds
# - upgrade 3: start on predefined timestamp (allows to manually call it from multiple threads)
def part2_bruteforce(inputs, starting_timestamp=0):
    buses = []
    splitted = inputs[1].split(",")
    for index in range(len(splitted)):
        bus = splitted[index]
        if bus == "x":
            continue
        buses.append((index, int(bus)))
    buses.sort(key=lambda tup: tup[1], reverse=True)  # sort by second parameter from max to min
    current_timestamp = starting_timestamp
    next_log = time.time() + 10
    while True:
        result_timestamp = current_timestamp - buses[0][0]
        successful = True
        for index, bus in buses:
            if (result_timestamp + index) % bus != 0:
                successful = False
                break
        if successful:
            return result_timestamp
        current_timestamp += buses[0][1]
        now = time.time()
        if now > next_log:
            next_log = now + 10
            print("Time:" + str(now) + ", checking timestamp:" + str(current_timestamp))


# part 2 using chinese remainder theorem
def part2_crt(inputs):
    # parse all buses, store as "t = x mod y"
    # examples:
    #   if bus is on first index and its number is 17, store it as "(17-0) mod 17 => 0 mod 17"
    #   if bus is on third index and its number is 13, store it as "(13-2) mod 13 => 11 mod 13"
    chinese_inputs = []
    splitted = inputs[1].split(",")
    all_divisors_multiplied = 1
    for index in range(len(splitted)):
        bus = splitted[index]
        if bus == "x":
            continue
        bus = int(bus)
        chinese_inputs.append(((bus - index) % bus, bus))
        all_divisors_multiplied *= bus
    # calculate result of chinese remainder theorem (chinese_result)
    # by calculating partial result for each (remainder:divisor)
    chinese_result = 0
    for remainder, divisor in chinese_inputs:
        base = multiplied_base = all_divisors_multiplied / divisor
        while True:
            base_remainder = multiplied_base % divisor
            if base_remainder == remainder:
                chinese_result += multiplied_base  # found correct result, add to result
                break
            else:
                multiplied_base += base  # remainder is not correct - increment by base and try again
    # divide chinese result by total multiplier
    p2_result = int(chinese_result % all_divisors_multiplied)
    return p2_result


# Few simple tests
def test():
    inputs = "939\n7,13,x,x,59,x,31,19\n".rstrip().split("\n")
    assert part1(inputs) == 295
    assert part2_crt(inputs) == 1068781
    assert part2_bruteforce(inputs) == 1068781
    inputs = "666\n17,x,13,19\n".rstrip().split("\n")
    assert part2_crt(inputs) == 3417
    assert part2_bruteforce(inputs) == 3417
    inputs = "666\n67,7,59,61\n".rstrip().split("\n")
    assert part2_crt(inputs) == 754018
    assert part2_bruteforce(inputs) == 754018
    inputs = "666\n67,x,7,59,61\n".rstrip().split("\n")
    assert part2_crt(inputs) == 779210
    assert part2_bruteforce(inputs) == 779210
    inputs = "666\n67,7,x,59,61\n".rstrip().split("\n")
    assert part2_crt(inputs) == 1261476
    assert part2_bruteforce(inputs) == 1261476
    inputs = "666\n1789,37,47,1889\n".rstrip().split("\n")
    assert part2_crt(inputs) == 1202161486
    assert part2_bruteforce(inputs) == 1202161486
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

adv_inputs = common.get_input(13).rstrip().split("\n")
result = part1(adv_inputs)
common.post_answer(13, 1, result)

# test to check that bruteforce would eventually find result
# result: it is able to try 700M timestamps per second => would find the result after ~220h single core
# result = part2_bruteforce(inputs, 538695823547808)

result = part2_crt(adv_inputs)
print("Result:" + str(result))
common.post_answer(13, 2, result)
