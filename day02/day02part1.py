""" Advent of Code - Day 2 Part 1 """
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

number_of_safe_reports: int = 0
report_is_safe: bool = False

with open(Path(BASE_DIR, "day02_input"), "r", encoding="utf8") as file:
    for line in file:
        line_items = [int(x) for x in line.split()]

        if line_items[0] < line_items[1]:
            for i in range(len(line_items) - 1):
                report_is_safe = (
                    line_items[i] < line_items[i + 1]
                    and
                    1 <= line_items[i + 1] - line_items[i] <= 3
                )
                if report_is_safe is not True:
                    break
        else:
            for i in range(len(line_items) - 1):
                report_is_safe = (
                    line_items[i] > line_items[i + 1]
                    and
                    1 <= line_items[i] - line_items[i + 1] <= 3
                )
                if report_is_safe is not True:
                    break

        if report_is_safe:
            number_of_safe_reports += 1

print("Number of safe reports:", number_of_safe_reports)
