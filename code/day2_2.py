# -*- coding: utf-8 -*-
from collections import Counter
new_list = []
is_finish = False
# 将数据保存进set
with open("day2_data.txt") as f:
	boxID_list = f.read().split("\n")

boxid_len = len(boxID_list[0])
# 从每个box ID的第一个字母删除后开始比较，直到完成
for i in xrange(0, boxid_len):
	for boxID in boxID_list:
		new_list.append(boxID[:i] + boxID[(i+1):])
	# 获取到新得到的列表中，出现次数最高的，这边最高为两次
	most_ID = Counter(new_list).most_common(1)
	if most_ID[0][1] == 2:
		print most_ID[0][0]
		print i
		is_finish = True
		break
	new_list = []
	if is_finish:
		break