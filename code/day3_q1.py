#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-07 11:12:46
# @Author  : Wang Bixian (wbx_92@163,com)
# @Link    : 
# @Version : 1.0

import re
import numpy as np


# 对每行数据信息的提取，得到左边缘，上边缘，宽，高
def deal_data(data):
	d = re.split(' ', data)
	left_edge = int((d[2].split(',')[0]))
	top_edge = int((d[2].split(',')[1][:-1]))
	wide = int((d[3].split('x')[0]))
	tall = int((d[3].split('x')[1]))
	return left_edge, top_edge, wide, tall


# 得到最后的图
def claim_area(data_list):
	claim_area = np.zeros((1000, 1000), dtype=np.int)
	for data in data_list:
		left_edge, top_edge, wide, tall = deal_data(data)
		fabric_diagram = np.zeros((1000, 1000), dtype=np.int)
		fabric_diagram[top_edge:(top_edge+tall), left_edge:(left_edge+wide)] = np.ones((tall, wide), dtype=np.int)
		claim_area += fabric_diagram
	return claim_area



if __name__ == '__main__':
	inches = 0
	with open('day3_data.txt') as f:
		data_list = f.read().split('\n')

	claim_area = claim_area(data_list)
	print claim_area
	for i in claim_area:
		for j in i:
			if j != 0 and j != 1:
				inches += 1

	print inches