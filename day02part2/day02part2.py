input_file = open("input 2")

number_of_safe_reports = 0

for line in input_file:
	l = [int(x) for x in line.split()]

	tolerate_bad_level = True
	if l[0] < l[1]:
		for i in range(len(l) - 1):
			if l[i] < l[i + 1] and 1 <= l[i + 1] - l[i] <= 3:
				safe = True
			else:
				if tolerate_bad_level == True:
					safe = True
					tolerate_bad_level = False
				else:
					safe = False
					break

	else:
		for i in range(len(l) - 1):
			if l[i] > l[i + 1] and 1 <= l[i] - l[i + 1] <= 3:
				safe = True
			else:
				if tolerate_bad_level == True:
					safe = True
					tolerate_bad_level = False
				else:
					safe = False
					break

	if safe == True:
		number_of_safe_reports = number_of_safe_reports + 1

print("Number of safe reports:", number_of_safe_reports)

input_file.close()
