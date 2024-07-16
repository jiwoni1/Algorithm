import sys
# sys.stdin  = open("input.txt", "rt")

# 대표값

# n = int(input())
# score = list(map(int, input().split()))
# gaps = []
# com = 9999
# ans = 0
#
# avg = sum(score) / n
# # 반올림
# avg = round(avg)
#
#
# for i in range(n):
#     gap = avg - score[i]
#     if gap < 0:
#         gap = -(gap)
#     if gap < com:
#         com = gap
#     gaps.append(gap)
#
# com_ans = gaps.index(com)
#
# for i in range(com_ans+1, n):
#     if gaps[i] == gaps[com_ans] and score[com_ans] < score[i]:
#         ans = i
#         break
# else:
#     ans = com_ans
#
# print(avg, ans+1)

n = int(input())
scores = list(map(int, input().split()))

# avg = round(sum(scores) / n)
avg = int((sum(scores) / n)+0.5)  # 사사오입

com = 2147000000
score = 0
num = 0

for idx, x in enumerate(scores):
    gap = abs(avg-x)
    if gap < com:
        com = gap
        score = x
        num = idx
    elif gap == com:
        if score < x:
            score = x
            num = idx
print(avg, num+1)


    