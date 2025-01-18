""" Advent of Code - Day 3 """
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def part2() -> None:
    """ Day 3 Part 2 """
    result: int = 0
    instructions_enabled: bool = True

    regex_string: str = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    match: list[str] = []

    with open(
            Path(BASE_DIR, "day03_input"), "r",
            encoding="utf8"
            ) as file:
        for line in file:
            match_list = re.findall(regex_string, line)
            for match in match_list:
                print(match)
                if match[0] == "do()":
                    instructions_enabled = True
                elif match[1] == "don't()":
                    instructions_enabled = False
                elif instructions_enabled:
                    result += int(match[2]) * int(match[3])

    print(f"The result of the multiplication is {result:_}.")

part2()
