#第一题
a = 0
for line in open("day1_input.txt"):
    a += int(line)
    if not line:break
print(a)

# 第二题
# a = 0
# b = set()
# tw = False
# while tw == False:
#     for line in open("day1_input.txt"):
#         a += int(line)
#         if a in b:
#             print(a)
#             tw = True
#         b.add(a)
#         if (not line) or (tw == True):break

# a = 0
# b = []
# d = 0
# tw = 0
#
# while tw == 0:
#     for line in open("day1_input.txt"):
#         a = a+int(line)
#         b.append(a)
#         d = d+1
#         if d>2:
#             c = b[:]
#             c.sort()
#             for i in range(1,len(c)):
#                 if c[i] == c[i-1]:
#                     print(c[i])
#                     tw = 1
#                 if tw == 1:
#                     break
#         if not line:
#             break