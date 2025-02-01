""" Advent of Code - Day 4 Test """
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def test1() -> None:
    """ Die ganze Zeile mit New Line (\n) am Ende """
    with open(
            Path(BASE_DIR, "day04_example_inputtest"),
            "r", encoding="utf8"
            ) as file:
        lines: list[str] = []
        for line in file:
            print(line)
            lines.append(line)
    print(lines)

def test2() -> None:
    """ Aus der Zeile werden alle Whitespace-Zeichen vom Anfang und
        vom Ende entfernt (In diesem Fall New line und Leerzeichen) """
    with open(
            Path(BASE_DIR, "day04_example_inputtest"),
            "r", encoding="utf8"
            ) as file:
        lines: list[str] = []
        for line in file:
            print(line.strip())
            lines.append(line.strip())

def test3() -> None:
    """ Aus jeder Zeile wird New Line (\n) entfernt. """
    with open(
            Path(BASE_DIR, "day04_example_inputtest"),
            "r", encoding="utf8"
            ) as file:
        lines: list[str] = []
        for line in file:
            print(line.strip("\n"))
            lines.append(line.strip("\n"))

test1()
# test2()
