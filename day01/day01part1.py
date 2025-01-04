"""Advent of Code - Day 1 Part 1"""

with open("day01/input", "r", encoding="utf8") as file:
    left_list = []
    right_list = []
    for line in file:
        line_items = [int(x) for x in line.split()]
        left_list.append(line_items[0])
        right_list.append(line_items[1])

left_list.sort()
right_list.sort()

distance: int = 0

for x in range(len(left_list)):
    distance = distance + abs(left_list[x] - right_list[x])

print(f"The total distance between the lists is {distance}")
