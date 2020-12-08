import common
import time


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
def ordenador(command_list):  # "ordenador" is "computer" in Spanish
    instructions_performed = []  # list of all instruction pointers that have already been processed
    infinite = False  # flag signalling whether command exited by infinite loop or not

    # main loop
    instruction_pointer = 0  # index of current instruction
    acc_counter = 0
    while True:
        # check if we have reached end of command_list
        if instruction_pointer >= len(command_list):
            break

        # check if program is running in infinite loop
        if instruction_pointer in instructions_performed:
            infinite = True
            break
        instructions_performed.append(instruction_pointer)

        # process instruction
        splitted = command_list[instruction_pointer].split(" ")
        instruction = splitted[0]
        parameter = int(splitted[1])
        if instruction == "nop":
            instruction_pointer += 1
        elif instruction == "acc":
            acc_counter += parameter
            instruction_pointer += 1
        elif instruction == "jmp":
            instruction_pointer += parameter

    return infinite, acc_counter


def replace_nop_jmp(command_list):
    # try to replace jmp command with nop, or nop with jmp and check if it solves infinite loop
    modified_instruction_pointer = 0
    while True:
        row = command_list[modified_instruction_pointer]
        if row[:3] == "nop":
            modified_command_list = command_list.copy()
            modified_command_list[modified_instruction_pointer] = row = "jmp" + row[3:]
            result = ordenador(modified_command_list)
            if result[0] is False:
                return result[1]
        elif row[:3] == "jmp":
            modified_command_list = command_list.copy()
            modified_command_list[modified_instruction_pointer] = row = "nop" + row[3:]
            result = ordenador(modified_command_list)
            if result[0] is False:
                return result[1]
        modified_instruction_pointer += 1


def test():
    input = "nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6\n"
    commands = input[:-1].split("\n")  # remove last character and split
    result = ordenador(commands)
    assert result == (True, 5)
    print("Test 1 passed!")

    assert replace_nop_jmp(commands) == 8
    print("Test 2 passed!")

# ---------------------------------------- MAIN ---------------------------------------- #
test()

input = common.get_input(8)[:-1].split("\n")  # remove last character and split
result = ordenador(input)
common.post_answer(8, 1, result)

print("Waiting 5 seconds to avoid server rejection")
time.sleep(5)
common.post_answer(8, 2, replace_nop_jmp(input))
