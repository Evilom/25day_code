# #第一题
# polymer_str = ''
# sm_alp = ''.join([chr(i) for i in range(97,123)])
# big_alp = sm_alp.upper()
# is_des = True
# for line in open("day5_input.txt"):
#     polymer_str += line
#
# while is_des:
#     poly_len = len(polymer_str)
#     for i in range(26):
#         polymer_str = polymer_str.replace(big_alp[i]+sm_alp[i],'')
#         polymer_str = polymer_str.replace(sm_alp[i]+big_alp[i],'')
#     if poly_len == len(polymer_str):
#         is_des = False
# print(len(polymer_str))
#第二题
polymer_str = ''
sm_alp = ''.join([chr(i) for i in range(97,123)])
big_alp = sm_alp.upper()
alp_len = []
polymer_rem = ''
for line in open("day5_input.txt"):
    polymer_str += line
print(len(polymer_str))
for i in range(26):
    is_des = True
    polymer_rem = polymer_str
    polymer_rem = polymer_rem.replace(big_alp[i],'')
    polymer_rem = polymer_rem.replace(sm_alp[i],'')
    while is_des:
        poly_len = len(polymer_rem)
        for i in range(26):
            polymer_rem = polymer_rem.replace(big_alp[i]+sm_alp[i],'')
            polymer_rem = polymer_rem.replace(sm_alp[i]+big_alp[i],'')
        if poly_len == len(polymer_rem):
            is_des = False
    alp_len.append(len(polymer_rem))
print(min(alp_len))