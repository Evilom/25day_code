#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-08 23:29:34
# @Author  : wbx (wbx@fzu.com.cn)
# @Link    :
# @Version : 1.0

import re
import numpy as np

timestamps = {}  # 存储各守卫值班及睡觉时间信息
guard_id = ''
falls_asleep = 0
wake_up = 0
asleep_time = 0
asleep_range = np.zeros((1, 60))
max_asleep = 0

# 获取所有数据并进行排序
with open("day4_input.txt") as f:
	data_list = sorted(f.read().split('\n'))
	f.close()

# print data_list
# 对数据进行分组
for data in data_list:
	if '#' in data:
		guard_id = int((re.findall('#\d+', data))[0][1:])  # 更新或获取守卫id
		if not timestamps.has_key (guard_id):
			timestamps[guard_id] = np.zeros((1, 60))

	if 'falls' in data:
		falls_asleep = int(data[15:17])

	if 'up' in data:
		wake_up = int(data[15:17])
		asleep_time = wake_up - falls_asleep
		asleep_range[:, falls_asleep:wake_up] = np.ones((1, asleep_time))
		timestamps[guard_id] += asleep_range
		asleep_range = np.zeros((1, 60))

# 第一题
for key, val in timestamps.items():
	if np.sum(val) > max_asleep:
		pro_id = key
		pro_val = val
		max_asleep = np.sum(val)

re = np.where(pro_val == np.max(pro_val))
print (re[1][0]*pro_id)

# 第二题
most_time = 0
for key, val in timestamps.items():
	if np.max(val) > most_time:
		g_id = key
		g_time = np.max(val)

re = np.where(timestamps[g_id] == g_time)
print (re[1][0]*g_id)