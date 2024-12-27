input_file = open("input")

left_list = list()
right_list = list()

for line in input_file:
	line_items = line.split()
	left_list.append(int(line_items[0]))
	right_list.append(int(line_items[1]))

left_list.sort()
right_list.sort()

distance = 0

for x in range(len(left_list)):
	distance = distance + abs(left_list[x] - right_list[x])

print(distance)

input_file.close()
