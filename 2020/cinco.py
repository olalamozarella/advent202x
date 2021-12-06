import common

# get inputs, convert F,L to zeros + B,R to ones
inputs = common.get_input(5).replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").split("\n")

min_id, max_id, seat_ids = 999, 0, []
for item in inputs[:-1]:  # ignore last item from inputs - it is empty row
    seat_id = int(item[:7], 2) * 8 + int(item[-3:], 2)  # convert string to two binary numbers, multiply to get seat ID
    min_id = min(min_id, seat_id)  # update minimum
    max_id = max(max_id, seat_id)  # update maximum
    seat_ids.append(seat_id)

# part 1 - find max seat ID
common.post_answer(5, 1, max_id)

# part 2 - check which seat ID between min and max is missing
common.post_answer(5, 2, [x for x in range(min_id, max_id) if x not in seat_ids][0])
