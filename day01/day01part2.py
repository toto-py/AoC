input_file = open("input")

left_list = []
right_list = []

for line in input_file:
	line_items = [int(x) for x in line.split()]
	left_list.append(line_items[0])
	right_list.append(line_items[1])

similarity_score = 0

for x in range(len(left_list)):
	left_number = left_list[x]
	appearances_in_right_list = right_list.count(left_number)
	similarity_score = similarity_score + (left_number * appearances_in_right_list)

print("The similarity score is", similarity_score)

input_file.close()
