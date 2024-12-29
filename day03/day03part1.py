import re

input_file = open("input")

result = 0

for line in input_file:
	match_list = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
	for match in match_list:
		numbers = [int(x) for x in match]
		result += numbers[0] * numbers[1]

print(f"The result of the multiplication is {result}.")

input_file.close()
