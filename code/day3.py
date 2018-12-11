# #第一题
# import re
# import numpy as np
# a = []
# #根据题意设定储存矩阵
# b = np.zeros((1000,1000))
# c = []
# for line in open("day3_input.txt"):
#     #提取输入中的数值
#     a = re.findall(r"\d+",line)
#     #根据得到数值计算索引，并在索引指定变量空间存1
#     for i in range(int(a[3])):
#         for j in range(int(a[4])):
#             b[int(a[1])+i][int(a[2])+j] += 1
# #去除矩阵中无重叠元素
# for i in b:
#     for j in i:
#         if j>1:c.append(j)
# print(len(c))
#第二题
import re
import numpy as np
a = []
#根据题意设定储存矩阵
b = np.zeros((1000,1000))
for line in open("day3_input.txt"):
    #提取输入中的数值
    a = re.findall(r"\d+",line)
    #根据得到数值计算索引，并在索引指定变量空间存1
    for i in range(int(a[3])):
        for j in range(int(a[4])):
            b[int(a[1])+i][int(a[2])+j] += 1
for line in open("day3_input.txt"):
    is_tar = True
    a = re.findall(r"\d+", line)
    for i in range(int(a[3])):
        for j in range(int(a[4])):
            #判断是否重叠
            if b[int(a[1]) + i][int(a[2]) + j] > 1:
                is_tar = False
                break
        if is_tar ==False:break
    if is_tar == True:print(a[0])