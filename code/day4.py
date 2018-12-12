#第一题
import re
a = {}
guard = {}
data_time = {}
tar = {}
key_list = []
#将输入存放到字典当中,时间为键，事件作值
for line in  open("day4_input.txt"):a.setdefault(line[1:17],[]).append(line[19:])
#按时间顺序生成字典关键词列表
key_list = sorted(a.keys())
#按顺序存放日期与对应时间，并且寻找守卫编号以及对应值班日期
for i in key_list:
    #将日期与时间分开存在字典，方便查询
    data_time.setdefault(i[:10],[]).append(i[11:16])
    if a[i][0][0] == 'G':
        #如果是23点值班的守卫就不录入日期
        if i[11] == "0":guard.setdefault(re.sub("\D", "", a[i][0]),[]).append(i[:10])
#计算每个守卫总的睡眠时间并存入字典
for i in guard.keys():
    most_sleep = []
    for j in guard[i]:
        #存放睡眠起始时间用，要清零
        time_count = []
        for k in data_time[j]:
            #找到每次睡觉到醒来的时间，并存入most_sleep
            if a[j+" "+k][0][0] == "f":
                time_count.append(re.findall(r"\d+",k))
            elif a[j+" "+k][0][0] == "w":
                time_count.append(re.findall(r"\d+",k))
                most_sleep.append(time_count[0][1]+time_count[1][1])
                #防止time_count的元素大于2个，保证most_sleep的数据完整性
                time_count = []
    count_time = 0
    for j in most_sleep:
        count_time += int(j[2])*10+int(j[3])-int(j[0])*10+int(j[1])
#将睡眠总时间与守卫对应编号存入字典
    tar.setdefault(i,[]).append(count_time)
#寻找睡得最多守卫的最大睡眠分钟
most_sleep = []
#设置长度为60的列表，其索引就是所需分钟数
sleep_chart = [0 for i in range(60)]
for i in guard[max(tar,key=tar.get)]:
    time_count = []
    for j in data_time[i]:
        if a[i + " " + j][0][0] == "f":
            time_count.append(re.findall(r"\d+", j))
        elif a[i + " " + j][0][0] == "w":
            time_count.append(re.findall(r"\d+", j))
            most_sleep.append(time_count[0][1] + time_count[1][1])
            time_count = []
for i in most_sleep:
    for j in range(int(i[0])*10+int(i[1]),int(i[2])*10+int(i[3])):
        sleep_chart[j] += 1
#找出所有睡得最多分钟数
max_pos = [i for i,v in enumerate(sleep_chart) if v==max(sleep_chart)]
#输出守卫号*最多分钟数
print(max(tar,key=tar.get))
#最大的分钟数为最有可能
print(max(max_pos))
print(int(max(max_pos))*int(max(tar,key=tar.get)))
# #第二题
# import re
# a = {}
# guard = {}
# data_time = {}
# tar1 = {}
# tar2 = {}
# key_list = []
# #将输入存放到字典当中,时间为键，事件作值
# for line in  open("day4_input.txt"):a.setdefault(line[1:17],[]).append(line[19:])
# #按时间顺序生成字典关键词列表
# key_list = sorted(a.keys())
# #按顺序存放日期与对应时间，并且寻找守卫编号以及对应值班日期
# for i in key_list:
#     #将日期与时间分开存在字典，方便查询
#     data_time.setdefault(i[:10],[]).append(i[11:16])
#     if a[i][0][0] == 'G':
#         #如果是23点值班的守卫就不录入日期
#         if i[11] == "0":guard.setdefault(re.sub("\D", "", a[i][0]),[]).append(i[:10])
# #计算每个守卫总的睡眠时间并存入字典
# for i in guard.keys():
#     most_sleep = []
#     # 设置长度为60的列表，其索引就是所需分钟数
#     sleep_chart = [0 for i in range(60
#                                     )]
#     for j in guard[i]:
#         #存放睡眠起始时间用，要清零
#         time_count = []
#         for k in data_time[j]:
#             #找到每次睡觉到醒来的时间，并存入most_sleep
#             if a[j+" "+k][0][0] == "f":
#                 time_count.append(re.findall(r"\d+",k))
#             elif a[j+" "+k][0][0] == "w":
#                 time_count.append(re.findall(r"\d+",k))
#                 most_sleep.append(time_count[0][1]+time_count[1][1])
#                 #防止time_count的元素大于2个，保证most_sleep的数据完整性
#                 time_count = []
#     for j in most_sleep:
#         for k in range(int(j[0]) * 10 + int(j[1]), int(j[2]) * 10 + int(j[3])):
#             sleep_chart[k] += 1
#     tar1.setdefault(i,[]).append(max(sleep_chart))
#     tar2.setdefault(i,[]).append(max([l for l,v in enumerate(sleep_chart) if v==max(sleep_chart)]))