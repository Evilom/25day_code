#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 20:25:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re
import fileinput
from collections import Counter, defaultdict


# 计算哈夫曼距离
def dist(x1, y1, x2, y2):
	return abs(x1-x2) + abs(y1-y2)

coordinates = [tuple(map(int, re.findall(r'\d+', line))) for line in open('day6_data.txt')]

# 从左边中找出最小和最大的坐标值
x_min, x_max = min(x for x, y in coordinates), max(x for x, y in coordinates)
y_min, y_max = min(y for x, y in coordinates), max(y for x, y in coordinates)

# question 1
counts = Counter()
infinite = set()
for x in range(x_min, x_max + 1):
	for y in range(y_min, y_max + 1):
		dist_list = sorted([(dist(x, y, px, py), i) for i, (px, py) in enumerate(coordinates)])
		if dist_list[0][0] != dist_list[1][0]:
			counts[dist_list[0][1]] += 1
		if x == x_min or x == x_max or y == y_min or y == y_max:
			infinite.add(dist_list[0][1])

for i in infinite:
	del counts[i]

print(max(counts.values()))

count = 0
for x in range(x_min, x_max + 1):
	for y in range(y_min, y_max + 1):
		if sum(dist(x, y, px, py) for (px, py) in coordinates) < 10000:
			count += 1
print(count)


# if __name__ == '__main__':
# 	coordinate_list = []
# 	min_dis = 720
# 	is_zero = False
# 	for line in open('day6_data.txt'):
# 		coordinate_list.append(deal_data(line))

# 	x_coordinates = np.arange(0, 360)
# 	y_coordinates = np.arange(0, 360)

# 	result_view = np.zeros((360, 360), dtype=np.int)

# 	for i in xrange(0, 360):
# 		for j in xrange(0, 360):
# 			point = 1
# 			for k in coordinate_list:
# 				man_dis = manhattan_distance(k, np.array([i, j]))
# 				if man_dis < min_dis:
# 					min_dis = man_dis
# 					nearest_point = point
# 					is_zero = False

# 				elif man_dis == min_dis:
# 					is_zero = True
# 				point += 1

# 			if not is_zero:
# 				result_view[i][j] = nearest_point
# 			min_dis = 720

# 	new_view = result_view[1:359, 1:359]

# 	first_row = result_view[0,:]
# 	end_row = result_view[359,:]
# 	first_col = result_view[:, 0]
# 	end_col = result_view[:, 359]
# 	max_area = 0
# 	for x in xrange(1, 51):
# 		if (x in first_col) or (x in end_col) or (x in first_row) or (x in end_row):
# 			continue

# 		cur_area = np.sum(new_view==x)
# 		if cur_area > max_area:
# 			max_area = cur_area

# 	print max_area