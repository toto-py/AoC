""" Advent of Code - Day 1 Part 2 """
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

left_list: list[int] = []
right_list: list[int] = []

with open(Path(BASE_DIR, "day01_input"), "r", encoding="utf8") as file:
    for line in file:
        line_items = [int(x) for x in line.split()]
        left_list.append(line_items[0])
        right_list.append(line_items[1])

similarity_score: int = 0

for i, left_number in enumerate(left_list):
    appearances_in_right_list = right_list.count(left_number)
    similarity_score = similarity_score + (left_number * appearances_in_right_list)

print(f"The similarity score is {similarity_score}")
