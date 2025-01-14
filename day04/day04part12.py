""" Advent of Code - Day 4 Part 1 """
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

lines: list[str] = []
counter: int = 0

test: int = 3

with open(Path(BASE_DIR, "day04_example_input2"), "r", encoding="utf8") as file:
    for line in file:
        if test == 1:
            # Die ganze Zeile mit New Line (\n) am Ende
            print(line)
            lines.append(line)

        elif test == 2:
            # Aus der Zeile werden alle Whitespace-Zeichen vom Anfang und
            # vom Ende entfernt (In diesem Fall New line und Leerzeichen)
            print(line.strip())
            lines.append(line.strip())

        elif test ==3:
            # Aus jeder Zeile wird New Line (\n) entfernt.
            print(line.strip("\n"))
            lines.append(line.strip("\n"))

print(lines)
