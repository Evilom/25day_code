#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 21:04:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np
from day3_q1 import claim_area, deal_data

if __name__ == '__main__':
	with open('day3_data.txt') as f:
		data_list = f.read().split('\n')

	claim_area = claim_area(data_list)

	for data in data_list:
		left_edge, top_edge, wide, tall = deal_data(data)
		data_area = claim_area[top_edge:(top_edge+tall), left_edge:(left_edge+wide)]
		if (data_area == np.ones((tall, wide), dtype=np.int)).all():
			print data
			break