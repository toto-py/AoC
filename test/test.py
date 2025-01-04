from pathlib import Path
BASE_Dir = Path(__file__).parent

print(BASE_Dir)

# Type hints
left_list: list[int] = []
right_list: list[int] = []

x: list[int] = []
x.append(1)
print(x)

y = 1
print(y)
y = "a"
print(y)

with open(BASE_Dir / "input", "r") as fp:
	for zeile in fp:
		print(zeile)
		# saubere_zeile = zeile.strip()
		# geteilte_zeile = saubere_zeile.split()
		# zahlen_liste = [int(x)for x in geteilte_zeile]
		# liste_der_listen.append(zahlen_liste)
