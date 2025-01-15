""" Advent of Code - Day 4 Part 2 """
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

zeilen: list[str] = []
counter: int = 0

with open(Path(BASE_DIR, "day04_input"), "r", encoding="utf8") as file:
    for line in file:
        zeilen.append(line.strip("\n"))

for i in range(len(zeilen)):
    for j in range(len(zeilen[i])):
        if (1 <= i <= len(zeilen) - 2
            and 1 <= j <= len(zeilen[i]) - 2
            and zeilen[i][j] == "A"
        ):

            if (    zeilen[i - 1][j - 1] == "M"
                and zeilen[i - 1][j + 1] == "M"
                and zeilen[i + 1][j + 1] == "S"
                and zeilen[i + 1][j - 1] == "S"
            ):
                counter += 1

            if (    zeilen[i - 1][j - 1] == "S"
                and zeilen[i - 1][j + 1] == "M"
                and zeilen[i + 1][j + 1] == "M"
                and zeilen[i + 1][j - 1] == "S"
            ):
                counter += 1

            if (    zeilen[i - 1][j - 1] == "S"
                and zeilen[i - 1][j + 1] == "S"
                and zeilen[i + 1][j + 1] == "M"
                and zeilen[i + 1][j - 1] == "M"
            ):
                counter += 1

            if (    zeilen[i - 1][j - 1] == "M"
                and zeilen[i - 1][j + 1] == "S"
                and zeilen[i + 1][j + 1] == "S"
                and zeilen[i + 1][j - 1] == "M"
            ):
                counter += 1

print(f"X-MAS occurs a total of {counter} times.")
