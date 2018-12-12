# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 0011 12:54
# @Author  : evilom
# @Email   : evilom@qq.com
# @File    : day6.py
# @Software: PyCharm
# #第一题
# import re
# import numpy as np
# from collections import Counter
# import time
# start = time.process_time()
# #存放坐标
# data = []
# #曼哈顿矩阵
# area = np.zeros((360,360))
# #提取坐标
# for line in open("day6_input.txt"):
#     data.append(line)
# data_posion = np.zeros((len(data),2))
# #计算与每个点曼哈顿距离，并将最小距离匹配的存入矩阵
# for i in range(len(data)):
#     num = re.findall(r"\d+",data[i])
#     data_posion[i][0] = num[0]
#     data_posion[i][1] = num[1]
# for i in range(360):
#     for j in range(360):
#         distance = []
#         for posion in data_posion:
#             distance.append(abs(i-posion[0])+abs(j-posion[1]))
#         #判断是否有多点距离一样小
#         a = distance[:]
#         a.remove(min(distance))
#         b = set(a)
#         if min(distance) in b:
#             area[i][j] = len(data) + 1
#         else:
#             area[i][j] = distance.index(min(distance))
# #获取未封闭数字
# del_num = Counter(area[:,0])
# del_num.update(Counter(area[:,359]))
# del_num.update(Counter(area[0,:]))
# del_num.update(Counter(area[359,:]))
# #获取所有数字区域
# area_list = Counter(area[:,0])
# for i in range(1,359):
#     area_list.update(Counter(area[:,i]))
# print(sorted(area_list.keys()))
# #移除未封闭数字
# for num in del_num.keys():
#     area_list.pop(num)
# print(max(area_list.values()))
# end = time.process_time()
# print("final is in ",end-start)
#第二题
import re
import numpy as np
from collections import Counter
import time
start = time.process_time()
#存放坐标
data = []
#曼哈顿矩阵
area = np.zeros((360,360))
#提取坐标
for line in open("day6_input.txt"):
    data.append(line)
data_posion = np.zeros((len(data),2))
#计算与每个点曼哈顿距离，并将最小距离匹配的存入矩阵
for i in range(len(data)):
    num = re.findall(r"\d+",data[i])
    data_posion[i][0] = num[0]
    data_posion[i][1] = num[1]
#计算与每个坐标距离总和，如果小于设定值就写1
for i in range(360):
    for j in range(360):
        distance = []
        for posion in data_posion:
            distance.append(abs(i-posion[0])+abs(j-posion[1]))
        total_dis = sum(distance)
        if total_dis < 10000:area[i][j] = 1
#统计矩阵内元素个数
regin_size = Counter(area[0])
for i in range(1,359):
    regin_size.update(Counter(area[i]))
print(regin_size)
end = time.process_time()
print("final is in ",end-start)



