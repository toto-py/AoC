""" Advent of Code - Day 4 Part 1 """
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

zeilen: list[str] = []
counter: int = 0

test: int = 2

with open(Path(BASE_DIR, "day04_input"), "r", encoding="utf8") as file:
    for line in file:
        zeilen.append(line.strip("\n"))

for i in range(len(zeilen)):
    for j in range(len(zeilen[i])):
        if zeilen[i][j] == "X":

            # links nach rechts
            # 3 Treffer in Testdatei
            if (j <= len(zeilen[i]) - 4
                and zeilen[i][j + 1] == "M"
                and zeilen[i][j + 2] == "A"
                and zeilen[i][j + 3] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i} S {j + 1}: {zeilen[i][j + 1]}")
                # print(f"Z {i} S {j + 2}: {zeilen[i][j + 2]}")
                # print(f"Z {i} S {j + 3}: {zeilen[i][j + 3]}")
                # print("----------")

            # rechts nach links
            # 2 Treffer in Testdatei
            if (j >= 3
                and zeilen[i][j - 1] == "M"
                and zeilen[i][j - 2] == "A"
                and zeilen[i][j - 3] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i} S {j - 1}: {zeilen[i][j - 1]}")
                # print(f"Z {i} S {j - 2}: {zeilen[i][j - 2]}")
                # print(f"Z {i} S {j - 3}: {zeilen[i][j - 3]}")
                # print("----------")

            # oben nach unten
            # 1 Treffer in Testdatei
            if (i <= len(zeilen) - 4
                and zeilen[i + 1][j] == "M"
                and zeilen[i + 2][j] == "A"
                and zeilen[i + 3][j] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i + 1} S {j}: {zeilen[i + 1][j]}")
                # print(f"Z {i + 2} S {j}: {zeilen[i + 2][j]}")
                # print(f"Z {i + 3} S {j}: {zeilen[i + 3][j]}")
                # print("----------")

            # unten nach oben
            # 2 Treffer in Testdatei
            if (i >= 3
                and zeilen[i - 1][j] == "M"
                and zeilen[i - 2][j] == "A"
                and zeilen[i - 3][j] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i - 1} S {j}: {zeilen[i - 1][j]}")
                # print(f"Z {i - 2} S {j}: {zeilen[i - 2][j]}")
                # print(f"Z {i - 3} S {j}: {zeilen[i - 3][j]}")
                # print("----------")

            # links oben nach rechts unten
            # 1 Treffer in Testdatei
            if (i <= len(zeilen) - 4
                and j <= len(zeilen[i]) - 4
                and zeilen[i + 1][j + 1] == "M"
                and zeilen[i + 2][j + 2] == "A"
                and zeilen[i + 3][j + 3] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i + 1} S {j + 1}: {zeilen[i + 1][j + 1]}")
                # print(f"Z {i + 2} S {j + 2}: {zeilen[i + 2][j + 2]}")
                # print(f"Z {i + 3} S {j + 3}: {zeilen[i + 3][j + 3]}")
                # print("----------")

            # rechts unten nach links oben
            # 4 Treffer in Testdatei
            if (i >= 3
                and j >= 3
                and zeilen[i - 1][j - 1] == "M"
                and zeilen[i - 2][j - 2] == "A"
                and zeilen[i - 3][j - 3] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i - 1} S {j - 1}: {zeilen[i - 1][j - 1]}")
                # print(f"Z {i - 2} S {j - 2}: {zeilen[i - 2][j - 2]}")
                # print(f"Z {i - 3} S {j - 3}: {zeilen[i - 3][j - 3]}")
                # print("----------")

            # links unten nach rechts oben
            # 4 Treffer in Testdatei
            if (i >= 3
                and j <= len(zeilen[i]) - 4
                and zeilen[i - 1][j + 1] == "M"
                and zeilen[i - 2][j + 2] == "A"
                and zeilen[i - 3][j + 3] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i - 1} S {j + 1}: {zeilen[i - 1][j + 1]}")
                # print(f"Z {i - 2} S {j + 2}: {zeilen[i - 2][j + 2]}")
                # print(f"Z {i - 3} S {j + 3}: {zeilen[i - 3][j + 3]}")
                # print("----------")

            # rechts oben nach links unten
            # 1 Treffer in Testdatei
            if (i <= len(zeilen) - 4
                and j >= 3
                and zeilen[i + 1][j - 1] == "M"
                and zeilen[i + 2][j - 2] == "A"
                and zeilen[i + 3][j - 3] == "S"
            ):
                counter += 1
                # print(f"Z {i} S {j}: {zeilen[i][j]}")
                # print(f"Z {i + 1} S {j - 1}: {zeilen[i + 1][j - 1]}")
                # print(f"Z {i + 2} S {j - 2}: {zeilen[i + 2][j - 2]}")
                # print(f"Z {i + 3} S {j - 3}: {zeilen[i + 3][j - 3]}")
                # print("----------")

print(f"XMAS occurs a total of {counter} times.")

# for i in range(len(zeilen)):
#     for j in range(len(zeilen[i])):
#         if zeilen[i][j] == "X":
#             # print("X")
#             if j<=len(zeilen[i]) - 4 and zeilen[i][j+1] == "M" \
#                 and zeilen[i][j+2] == "A" and zeilen[i][j+3] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i} S {j + 1}: {zeilen[i][j + 1]}")
#                 # print(f"Z {i} S {j + 2}: {zeilen[i][j + 2]}")
#                 # print(f"Z {i} S {j + 3}: {zeilen[i][j + 3]}")
#                 # print("----------")
#                 # geht von links nach rechts fängt aber an der 4 letzten
#                 # stelle an, da sonnst kein vollständiges wort
#                 # zustandekommen würde.
#                 counter += 1

#             if j<=len(zeilen[i]) + 4 and zeilen[i][j-1] == "M" \
#                 and zeilen[i][j-2] == "A" and zeilen[i][j-3] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i} S {j - 1}: {zeilen[i][j - 1]}")
#                 # print(f"Z {i} S {j - 2}: {zeilen[i][j - 2]}")
#                 # print(f"Z {i} S {j - 3}: {zeilen[i][j - 3]}")
#                 # print("----------")
#                 counter += 1
#                 # Rechts nach links

#             if i<=len(zeilen) - 4 and zeilen[i+1][j] == "M" \
#                 and zeilen[i+2][j] == "A" and zeilen[i+3][j] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i + 1} S {j}: {zeilen[i + 1][j]}")
#                 # print(f"Z {i + 2} S {j}: {zeilen[i + 2][j]}")
#                 # print(f"Z {i + 3} S {j}: {zeilen[i + 3][j]}")
#                 # print("----------")
#                 counter += 1
#                 #oben nach unten

#             if i<=len(zeilen) + 4 and zeilen[i-1][j] == "M" \
#                 and zeilen[i-2][j] == "A" and zeilen[i-3][j] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i - 1} S {j}: {zeilen[i - 1][j]}")
#                 # print(f"Z {i - 2} S {j}: {zeilen[i - 2][j]}")
#                 # print(f"Z {i - 3} S {j}: {zeilen[i - 3][j]}")
#                 # print("----------")
#                 counter += 1
#                 #unten nach oben

#             if i<=len(zeilen) - 4 and j<=len(zeilen[i]) - 4 \
#                 and zeilen[i+1][j+1] == "M" and zeilen[i+2][j+2] == "A" \
#                 and zeilen [i+3][j+3] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i + 1} S {j + 1}: {zeilen[i + 1][j + 1]}")
#                 # print(f"Z {i + 2} S {j + 2}: {zeilen[i + 2][j + 2]}")
#                 # print(f"Z {i + 3} S {j + 3}: {zeilen[i + 3][j + 3]}")
#                 # print("----------")
#                 counter += 1
#                 #schräg nach rechts unten

#             if i<=len(zeilen) + 4 and j<=len(zeilen[i]) + 4 \
#                 and zeilen[i-1][j-1] == "M" and zeilen[i-2][j-2] == "A" \
#                 and zeilen [i-3][j-3] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i - 1} S {j - 1}: {zeilen[i - 1][j - 1]}")
#                 # print(f"Z {i - 2} S {j - 2}: {zeilen[i - 2][j - 2]}")
#                 # print(f"Z {i - 3} S {j - 3}: {zeilen[i - 3][j - 3]}")
#                 # print("----------")
#                 counter += 1
#                 #schräg nach links oben

#             if i<=len(zeilen) + 4 and j<=len(zeilen[i]) - 4 \
#                 and zeilen[i-1][j+1] == "M" and zeilen[i-2][j+2] == "A" \
#                 and zeilen [i-3][j+3] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i - 1} S {j + 1}: {zeilen[i - 1][j + 1]}")
#                 # print(f"Z {i - 2} S {j + 2}: {zeilen[i - 2][j + 2]}")
#                 # print(f"Z {i - 3} S {j + 3}: {zeilen[i - 3][j + 3]}")
#                 # print("----------")
#                 counter += 1
#             #schräg nach rechts oben

#             if i<=len(zeilen) - 4 and j<=len(zeilen[i]) + 4 \
#                 and zeilen[i+1][j-1] == "M" and zeilen[i+2][j-2] == "A" \
#                 and zeilen [i+3][j-3] == "S":
#                 # print(f"Z {i} S {j}: {zeilen[i][j]}")
#                 # print(f"Z {i + 1} S {j - 1}: {zeilen[i + 1][j - 1]}")
#                 # print(f"Z {i + 2} S {j - 2}: {zeilen[i + 2][j - 2]}")
#                 # print(f"Z {i + 3} S {j - 3}: {zeilen[i + 3][j - 3]}")
#                 # print("----------")
#                 counter += 1
#             #schräg nach links unten
# print(counter)
