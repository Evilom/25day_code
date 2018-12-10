#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 09:34:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : 1.1

# while is_contiune:
# 	data_len = len(polymer_data)
# 	for x in xrange(0, data_len):
# 		if(x + 1) == data_len:
# 			print data_len
# 			is_contiune = False
# 			break

# 		if polymer_data[x].islower() != polymer_data[x+1].islower():
# 			if polymer_data[x] == polymer_data[x+1].swapcase():
# 				del polymer_data[x]
# 				del polymer_data[x]
# 				x = 0
# 				break

# print ''.join(polymer_data)

def remain_polymer(polymer_data):
	while True:
		y = 0
		remove_num = []
		data_len = len(polymer_data)
		for x in xrange(0, data_len-1):
			if polymer_data[x].islower() != polymer_data[x+1].islower():
				if polymer_data[x] == polymer_data[x+1].swapcase():
					if x in remove_num:
						continue
					remove_num.extend([x, x+1])


		if not remove_num:
			break

		for i in remove_num:
			del polymer_data[i - y]
			y += 1

	return len(polymer_data)

if __name__ == '__main__':
	with open('day5_data.txt') as f:
		polymer_data = list(f.read())
		
	pritn remain_polymer(polymer_data)
