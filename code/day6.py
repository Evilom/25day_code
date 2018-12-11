#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 20:25:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np
from collections import Counter
# 处理文本中的行数据，得到坐标
def deal_data(data):
	return np.array(eval(data))

# 计算p和q点距离，p，q格式为（33, 11）
def manhattan_distance(p, q):
	return np.sum(np.abs(p - q))


if __name__ == '__main__':
	coordinate_list = []
	min_dis = 720
	is_zero = False
	for line in open('day6_data.txt'):
		coordinate_list.append(deal_data(line))

	x_coordinates = np.arange(0, 360)
	y_coordinates = np.arange(0, 360)

	result_view = np.zeros((360, 360), dtype=np.int)

	for i in xrange(0, 360):
		for j in xrange(0, 360):
			point = 1
			for k in coordinate_list:
				man_dis = manhattan_distance(k, np.array([i, j]))
				if man_dis < min_dis:
					min_dis = man_dis
					nearest_point = point
					is_zero = False

				elif man_dis == min_dis:
					is_zero = True
				point += 1

			if not is_zero:
				result_view[i][j] = nearest_point
			min_dis = 720

	print result_view

	new_view = result_view[1:359, 1:359]

	first_row = result_view[0,:]
	end_row = result_view[359,:]
	first_col = result_view[:, 0]
	end_col = result_view[:, 359]
	max_area = 0
	for x in xrange(1, 51):
		if (x in first_col) or (x in end_col) or (x in first_row) or (x in end_row):
			continue

		cur_area = np.sum(new_view==x)
		if cur_area > max_area:
			max_area = cur_area

	print max_area