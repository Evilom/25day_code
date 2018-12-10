#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 10:35:43
# @Author  : Wbx
# @Link    : http://example.org
# @Version : $Id$

from day5_1 import remain_polymer

if __name__ == '__main__':
	with open('day5_data.txt') as f:
		polymer_data = f.read()
	'''
	此方法太久了，跑半天出不来
	for x in xrange(ord('a'), ord('z')):
		new_data = polymer_data.replace(chr(x), '').replace(chr(x).swapcase(), '')

		while is_contiune:
			data_len = len(new_data)
			data = list(new_data)
			for x in xrange(0, data_len):
				if(x + 1) == data_len:
					print data_len
					is_contiune = False
					break

				if data[x].islower() != data[x+1].islower():
					if data[x] == data[x+1].swapcase():
						del data[x]
						del data[x]
						x = 0
						break

		new_len = len(data)
		if new_len < min_len:
			min_len = new_len

	print min_len
	'''
	min_len = 50000
	for x in xrange(ord('a'), ord('z')):
		new_data = polymer_data.replace(chr(x), '').replace(chr(x).swapcase(), '')

		data_len = remain_polymer(list(new_data))
		if data_len < min_len:
			min_len = data_len

	print min_len