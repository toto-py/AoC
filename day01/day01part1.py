""" Advent of Code - Day 1 Part 1 """
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

left_list: list[int] = []
right_list: list[int] = []

with open(Path(BASE_DIR, "day01_input"), "r", encoding="utf8") as file:
    for line in file:
        line_items = [int(x) for x in line.split()]
        left_list.append(line_items[0])
        right_list.append(line_items[1])

left_list.sort()
right_list.sort()

distance: int = 0

for i in range(len(left_list)):
    distance = distance + abs(left_list[i] - right_list[i])

print(f"The total distance between the lists is {distance}")
