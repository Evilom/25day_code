cur_freq = 0
freq_set = {0}
is_start = True
while is_start:
	for line in open("day1_data.txt.txt"):
		cur_freq += int(line)
		if cur_freq in freq_set:
			first_twice = cur_freq
			is_start = False
			break
		else:
			freq_set.add(cur_freq) 
print first_twice