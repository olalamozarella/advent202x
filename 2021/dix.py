import common


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first and second part
def part1_2(rows):
    # for each row
    #   for each character
    #     is left bracket? store in temporary array
    #     is right bracket?
    #       compare to the last stored bracket in temporary array => check if string is corrupted or not
    #       corrupted? return corrupted bracket
    result_p1 = 0
    scores_p2 = []
    for row in rows:
        score_p2 = 0
        working_list = []
        corrupted = False
        for character in row:
            if character in ("(", "[", "{", "<"):
                working_list.append(character)
            elif character == ")":
                if working_list[-1] == "(":
                    working_list.pop()
                else:
                    result_p1 += 3
                    corrupted = True
                    break
            elif character == "]":
                if working_list[-1] == "[":
                    working_list.pop()
                else:
                    result_p1 += 57
                    corrupted = True
                    break
            elif character == "}":
                if working_list[-1] == "{":
                    working_list.pop()
                else:
                    result_p1 += 1197
                    corrupted = True
                    break
            elif character == ">":
                if working_list[-1] == "<":
                    working_list.pop()
                else:
                    result_p1 += 25137
                    corrupted = True
                    break
        if corrupted:
            continue
        while len(working_list) != 0:
            remaining_character = working_list[-1]
            score_p2 *= 5
            if remaining_character == "(":
                score_p2 += 1
            elif remaining_character == "[":
                score_p2 += 2
            elif remaining_character == "{":
                score_p2 += 3
            elif remaining_character == "<":
                score_p2 += 4
            else:
                assert False, "something weird has happened"
            working_list.pop()
        scores_p2.append(score_p2)

    # sort and pick middle score
    scores_p2 = sorted(scores_p2)
    middle_index = int(len(scores_p2) / 2)
    result_p2 = scores_p2[middle_index]
    return result_p1, result_p2


# few simple tests
def test():
    test_inputs = \
        "[({(<(())[]>[[{[]{<()<>>\n" \
        "[(()[<>])]({[<{<<[]>>(\n" \
        "{([(<{}[<>[]}>{[]{[(<()>\n" \
        "(((({<>}<{<{<>}{[]{[]{}\n" \
        "[[<[([]))<([[{}[[()]]]\n" \
        "[{[{({}]{}}([{[{{{}}([]\n" \
        "{<[[]]>}<{[{[{[]{()[[[]\n" \
        "[<(<(<(<{}))><([]([]()\n" \
        "<{([([[(<>()){}]>(<<{{\n" \
        "<{([{{}}[<[[[<>{}]]]>[]]\n" \
        .rstrip().split("\n")
    assert part1_2(test_inputs) == (26397, 288957)
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(10).rstrip().split("\n")
result = part1_2(inputs)
common.post_answer(10, 1, result[0])
common.post_answer(10, 2, result[1])
