import common
import re


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# solution for the first part
def part1(rows):
    # 0) counter = 0
    # 1) for each row:
    # 2) split row by "|"
    # 3) split right side by " "
    # 4) for each string in splitted:
    # 5) if length is 2,3,4,7: increment counter

    counter = 0;
    for row in rows:
        a = row.split("|")
        b = a[1].split(" ")
        for x in b:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                counter += 1

    return counter


# solution for the second part
def part2(rows):
    # 1 totalResult = 0

    # 2 for each row
    #   split left and right side
    #   split left side to digits

    # 3   find 1 (string length == 2)
    #   seg[2] = "ab", seg[5] = "ab"

    # 4   find 7 (string length 3)
    #   seg[0] = string - seg[2]

    # 5   find 4 (string length 4)
    #   seg[1] = "ef", seg[3] = "ef"

    # 6   find 9 (string length 6, must have seg[2], must have seg[1]
    #   seg[6] = string - seg[0] - seg[1] - seg[2]
    #   seg[4] = all characters - string

    # 7.1   find 0 (string length 6, must have only one from seg[1]
    #   if string contains seg[1][0]: seg[1] = seg[1][0]; seg[3] = seg[3][1]
    #   else seg[1] = seg[1][1]; seg[3] = seg[3][0]

    # 7.2  find 6 (string length 6, must have only one from seg[5]
    #   if string contains seg[5][0]: seg[5] = seg[5][0]; seg[2] = seg[2][1]
    #   else seg[5] = seg[5][1]; seg[2] = seg[2][0]

    # 8  split right side to digits
    #   define result = 0
    #   for each digit:
    #     def convert_digit_to_int(string, seg) => int
    #     result * 10 + int

    # 9  totalResult += result
    # return totalResult

    # 10 def convert_digit_to_int(string, seg) => int
    #   if contains seg0 1 2 4 5 6 => 0
    #   if contains seg 2 5 => 1
    #   if contains seg 0 2 3 4 6 => 2
    #   if contains seg 0 2 3 5 6 => 3
    #   if contains seg 1 2 3 5 => 4
    #   if contains seg 0 1 3 5 6 => 5
    #   if contains seg 0 1 3 4 5 6 => 6
    #   if contains seg 0 2 5 => 7
    #   if contains seg 0 1 2 3 4 5 6 => 8
    #   if contains seg 0 1 2 3 5 6 => 9

    # 1
    totalResult = 0

    # 2
    for row in rows:
        segments = [""] * 7

        left_right = row.split("|")
        left_digits = left_right[0].rstrip().split(" ")

        # 3
        for digit in left_digits:
            if len(digit) == 2:
                segments[2] = digit
                segments[5] = digit
                break

        # 4
        for digit in left_digits:
            if len(digit) == 3:
                segments[0] = remove_characters_from_string(digit, segments[2])
                break

        # 5
        for digit in left_digits:
            if len(digit) == 4:
                segments[1] = remove_characters_from_string(digit, segments[2])
                segments[3] = segments[1]
                break

        # 6
        for digit in left_digits:
            if len(digit) == 6 and contains_all_characters(digit, segments[2]) and contains_all_characters(digit, segments[1]):
                characters_to_remove = segments[0] + segments[1] + segments[2]
                segments[6] = remove_characters_from_string(digit, characters_to_remove)
                segments[4] = remove_characters_from_string("abcdefg", digit)
                break

        # 7.1
        for digit in left_digits:
            if len(digit) == 6:
                if segments[1][0] in digit and segments[1][1] not in digit:
                    segments[1] = segments[1][0]
                    segments[3] = segments[3][1]
                    break
                elif segments[1][1] in digit and segments[1][0] not in digit:
                    segments[1] = segments[1][1]
                    segments[3] = segments[3][0]
                    break

        # 7.2
        for digit in left_digits:
            if len(digit) == 6:
                if segments[5][0] in digit and segments[5][1] not in digit:
                    segments[5] = segments[5][0]
                    segments[2] = segments[2][1]
                    break
                elif segments[5][1] in digit and segments[5][0] not in digit:
                    segments[5] = segments[5][1]
                    segments[2] = segments[2][0]
                    break

        # 8
        right_digits = left_right[1].lstrip().split(" ")
        row_result = 0
        for digit in right_digits:
            row_result *= 10
            row_result += convert_digit_to_int(digit, segments)
        totalResult += row_result

    return totalResult


# function that removes all occurences of specified characters from input_string
# returns string with removed characters
def remove_characters_from_string(input_string, characters_to_remove):
    result_string = input_string
    for character in characters_to_remove:
        result_string = result_string.replace(character, "")
    return result_string


# function that checks if input_string contains all characters from characters_to_check
# returns True if contains, False if not
def contains_all_characters(input_string, characters_to_check):
    for character in characters_to_check:
        if character in input_string:
            continue
        else:
            return False
    return True


def convert_digit_to_int(input_string, segments):
    #   if contains seg0 1 2 4 5 6 => 0
    #   if contains seg 2 5 => 1
    #   if contains seg 0 2 3 4 6 => 2
    #   if contains seg 0 2 3 5 6 => 3
    #   if contains seg 1 2 3 5 => 4
    #   if contains seg 0 1 3 5 6 => 5
    #   if contains seg 0 1 3 4 5 6 => 6
    #   if contains seg 0 2 5 => 7
    #   if contains seg 0 1 2 3 4 5 6 => 8
    #   if contains seg 0 1 2 3 5 6 => 9
    if contains_all_characters(input_string, segments[0]+segments[1]+segments[2]+segments[3]+segments[4]+segments[5]+segments[6]):
        return 8
    elif contains_all_characters(input_string, segments[0]+segments[1]+segments[2]+segments[4]+segments[5]+segments[6]):
        return 0
    elif contains_all_characters(input_string, segments[0]+segments[1]+segments[3]+segments[4]+segments[5]+segments[6]):
        return 6
    elif contains_all_characters(input_string, segments[0]+segments[1]+segments[2]+segments[3]+segments[5]+segments[6]):
        return 9
    elif contains_all_characters(input_string, segments[0]+segments[2]+segments[3]+segments[4]+segments[6]):
        return 2
    elif contains_all_characters(input_string, segments[0]+segments[2]+segments[3]+segments[5]+segments[6]):
        return 3
    elif contains_all_characters(input_string, segments[0]+segments[1]+segments[3]+segments[5]+segments[6]):
        return 5
    elif contains_all_characters(input_string, segments[1]+segments[2]+segments[3]+segments[5]):
        return 4
    elif contains_all_characters(input_string, segments[0]+segments[2]+segments[5]):
        return 7
    elif contains_all_characters(input_string, segments[2]+segments[5]):
        return 1

    print("something is terribly wrong!")
    assert False


# few simple tests
def test():
    test_inputs = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\nedbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\nfgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\nfbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\naecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\nfgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\ndbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\nbdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\negadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\ngcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\n".rstrip().split("\n")
    assert part1(test_inputs) == 26
    assert part2(test_inputs) == 61229
    print("All tests passed!")


# ------------------------------------- HELPER FUNCTIONS ----------------------------------- #


# ----------------------------------------- MAIN ------------------------------------------- #
test()

inputs = common.get_input(8).rstrip().split("\n")
common.post_answer(8, 1, part1(inputs))
common.post_answer(8, 2, part2(inputs))
