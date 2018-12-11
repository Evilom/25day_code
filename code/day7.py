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
for i in key_list:
    data_time.setdefault(i[:10],[]).append(i[11:16])
    if a[i][0][0] == 'G':guard.setdefault(re.sub("\D", "", a[i][0]),[]).append(i[:10])
for i in guard.keys():
    most_sleep = []
    sleep_time = [0 for i in range(59)]
    for j in guard[i]:
        time_count = []
        for k in data_time[j]:
            if a[j+" "+k][0][0] == "f":
                time_count.append(re.findall(r"\d+",k))
            elif a[j+" "+k][0][0] == "w":
                time_count.append(re.findall(r"\d+",k))
                most_sleep.append(time_count[0][1]+time_count[1][1])
                time_count = []
    for i in most_sleep:
        for j in range(int(i[0])*10+int(i[1]),int(i[2])*10+int(i[3])):
            sleep_time[j] += 1
    tar.setdefault(i,[]).append(str(sleep_time.index(max(sleep_time)))+" "+str(max(sleep_time)))
print(tar)