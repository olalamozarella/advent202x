import common


# return: array of ints, "+" is -10, "*" is -20, "(" is -30, ")" is -40
def parse_input(row):
    equation = []
    previous_char = ""
    for char in row:
        if char.isdigit():
            previous_char += char
            continue
        if previous_char != "":
            equation.append(int(previous_char))
            previous_char = ""
        if char == "+" or char == "*" or char == "(" or char == ")":
            equation.append(char)
    if previous_char != "":
        equation.append(int(previous_char))
    return equation


def calculate_equation(equation, part2_flag):
    # has parenthesis?
    #  find first and last parentheses
    #  calculate_equation for thing inside these parentheses
    #  replace parentheses with result
    while True:
        par1, par2 = -1, -1
        level = 0
        for index in range(len(equation)):
            if equation[index] == "(":
                level += 1
                if par1 == -1:
                    par1 = index
            if equation[index] == ")":
                level -= 1
                if level == 0:
                    par2 = index
                    break
        if par1 == -1 or par2 == -1:
            break
        result = calculate_equation(equation[par1+1:par2], part2_flag)
        new_equation = []
        if par1 != 0:
            new_equation += equation[:par1]
        new_equation += [result]
        if par2 != len(equation) - 1:
            new_equation += equation[par2+1:]
        equation = new_equation

    if part2_flag:
        # calculate addition first
        #  while there is + sign, calculate and replace
        #  then calculate left to right
        try:
            while True:
                addition_idx = equation.index("+")
                operand1 = equation[addition_idx - 1]
                operand2 = equation[addition_idx + 1]
                result = operand1 + operand2
                new_equation = []
                if addition_idx != 1:
                    new_equation += equation[:addition_idx-1]
                new_equation += [result]
                if addition_idx != len(equation) - 2:
                    new_equation += equation[addition_idx + 2:]
                equation = new_equation
        except ValueError:
            pass

    # calculate from left to right
    #  read three chars (number, operator, number)
    #  calculate result
    #  replace three chars with result
    result = equation[0]
    for index in range(1, len(equation), 2):
        operator = equation[index]
        operand = equation[index+1]
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
    return result


def part1(inputs):
    result = 0
    for row in inputs.rstrip().replace(" ", "").split("\n"):
        equation = parse_input(row)
        result += calculate_equation(equation, False)
    return result


def part2(inputs):
    result = 0
    for row in inputs.rstrip().replace(" ", "").split("\n"):
        equation = parse_input(row)
        result += calculate_equation(equation, True)
    return result


def test():
    assert part1("2 * 3 + (4 * 5)\n") == 26
    assert part1("5 + (8 * 3 + 9 + 3 * 4 * 3)\n") == 437
    assert part1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))\n") == 12240
    assert part1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2\n") == 13632
    print("P1 tests passed!")
    assert part2("1 + (2 * 3) + (4 * (5 + 6))\n") == 51
    assert part2("2 * 3 + (4 * 5)\n") == 46
    assert part2("5 + (8 * 3 + 9 + 3 * 4 * 3)\n") == 1445
    assert part2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))\n") == 669060
    assert part2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2\n") == 23340
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(18)
result = part1(inputs)
common.post_answer(18, 1, result)

result = part2(inputs)
common.post_answer(18, 2, result)
