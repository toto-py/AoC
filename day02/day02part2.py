input_file = open("input_test")

number_of_safe_reports = 0

for line in input_file:
	l = [int(x) for x in line.split()]

	level_removed = False
	i = 0
	levels_count = len(l)
	while i < levels_count - 1:
		print(i)
		if l[i] < l[i + 1] and 1 <= l[i + 1] - l[i] <= 3:
			safe = True
			print(l[i], "<", l[i + 1], " Safe")
		i += 1
'''
	if l[0] < l[1]:
		levels_count = len(l)
		for i in range(levels_count - 1):
			# 1 <-> 2 = safe
			if l[i] < l[i + 1] and 1 <= l[i + 1] - l[i] <= 3:
				safe = True
			elif l[i] < l[i + 2] and 1 <= l[i + 2] - l[i] <= 3:
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
'''

#if safe == True:
#	number_of_safe_reports += 1

print("Number of safe reports:", number_of_safe_reports)

input_file.close()
