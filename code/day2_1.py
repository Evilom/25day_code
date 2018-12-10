# -*- coding: utf-8 -*-
from collections import Counter
list_num = []
for line in open("day2_data.txt"):
	# 获取字符串中字符出现次数的记录集合,并将1去除
	set_num = set(Counter(line).values())
	set_num.remove(1)
	list_num.extend(list(set_num))

print list_num.count(2)*list_num.count(3)