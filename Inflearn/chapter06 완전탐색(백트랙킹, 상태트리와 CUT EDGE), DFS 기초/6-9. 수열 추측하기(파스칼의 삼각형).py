# 6-9. 수열 추측하기
import sys, copy
# sys.stdin = open("in4.txt", "r")

# 1. 리스트를 만들어서 파스칼의 삼각형 계산 (시간 초과
# n, f = map(int, input().split())
# coms = []
# com = [0] * n
# flag = 0
#
#
#
# # 순열 만들기
# def find_com(l):
#     global flag
#     if flag == 1:  # 답이 나왔으면 함수 종료
#         return
#     if l == n:
#         # new_com =[]
#         # for i in com:
#         #     new_com.append(i)
#         # coms.append(new_com)
#
#         # 파스칼의 삼각형
#         new = []
#         old = copy.deepcopy(com)
#
#         while len(old) > 1:
#
#             for i in range(len(old)-1):
#                 new.append(old[i] + old[i+1])
#             old = copy.deepcopy(new)
#             new = []
#
#
#         if old[0] == f:
#             print(*com)
#             flag = 1
#             return
#         return
#     else:
#         for i in range(1, n+1):
#             if i not in com:
#                 com[l] = i
#                 find_com(l+1)
#                 com[l] = 0
#
#
# find_com(0)

# 2. 파스칼의 삼각형을 구하는 법을 규칙으로 구함
n, f = map(int, input().split())
b = [1] * n
com = [0] * n
temp = 0
flag = 0
# 파스칼의 삼각형 규칙
# C(combination) 공식으로 규칙 찾아서 풀어줌
for i in range(1, n-1):
    b[i] = (b[i-1] * (n-i)) // i


def dfs(l):
    global temp, flag
    if flag:
        return
    if l == n:
        for i in range(n):
            temp += b[i] * com[i]
        if temp == f:  # 답을 찾았을 때
            print(*com)
            flag = 1
            return
        else:
            temp = 0
            return
    else:
        for i in range(1, n+1):
            if i not in com:
                com[l] = i
                dfs(l+1)
                com[l] = 0


dfs(0)


