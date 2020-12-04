import common
import re

# Get input
passports = common.get_input(4).split("\n\n")

# Part 1 - count passports that contain all required fields
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
part1_answer = 0
for passport in passports:
    valid = True
    for field in required_fields:
        if field not in passport:
            valid = False
    if valid is True:
        part1_answer += 1
common.post_answer(4, 1, part1_answer)

# Part 2 - each field must follow specific rules
part2_answer = 0
for passport in passports:
    try:
        splitted = re.split(":|\n| ", passport)
        byr = int(splitted[splitted.index("byr") + 1])
        if byr < 1920 or byr > 2002:
            continue
        iyr = int(splitted[splitted.index("iyr") + 1])
        if iyr < 2010 or iyr > 2020:
            continue
        eyr = int(splitted[splitted.index("eyr") + 1])
        if eyr < 2020 or eyr > 2030:
            continue
        hgt = splitted[splitted.index("hgt") + 1]
        if hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193:
            pass
        elif hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76:
            pass
        else:
            continue
        hcl = splitted[splitted.index("hcl") + 1]
        if hcl[0] != "#" or len(hcl) != 7 or int(hcl[1:], 16) < 0:
            continue
        ecl = splitted[splitted.index("ecl") + 1]
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        pid = splitted[splitted.index("pid") + 1]
        if len(pid) != 9 or int(pid) < 0:
            continue
        part2_answer += 1
    except ValueError:  # index() not found or conversion to int/hex failed
        continue
common.post_answer(4, 2, part2_answer)
