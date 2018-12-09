# 第一题
# cont_list = []
# for line in open("day2_input.txt"):
#     str_list = list(line)
#     str_set = set(str_list)
#     cont_sum = []
#     for i in str_set:cont_sum.append(str_list.count(i))
#     cont_list.extend(set(cont_sum))
# print(cont_list.count(2)*cont_list.count(3))

# 第二题
from collections import Counter
input_list = []
tw = False
#获取输入存至列表
for line in open("day2_input.txt"):input_list.append(line)
#循环去除每个元素的字符进行比较，寻找相同元素
for i in range(1,len(input_list[0])):
    fu_list = []
    for j in input_list:
        if i<len(j):fu_list.append(j[:i]+j[i+1:])
        else:fu_list.append(j[:i])
    dup = Counter(fu_list)
    if  dup:
        tw = True
        break
if tw:print(dup)





# from collections import Counter
#
# list_num = []
# for line in open("day2_input.txt"):
#     set_num = set(Counter(line).values())
#     set_num.remove(1)
#     list_num.extend(list(set_num))
# print(list_num.count(2)*list_num.count(3))