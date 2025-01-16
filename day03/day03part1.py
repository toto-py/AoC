""" Advent of Code - Day 3 Part 1 """
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

result: int = 0

with open(Path(BASE_DIR, "day03_input"), "r", encoding="utf8") as file:
    for line in file:
        match_list = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        for match in match_list:
            numbers = [int(x) for x in match]
            result += numbers[0] * numbers[1]

print(f"The result of the multiplication is {result:_}.")
