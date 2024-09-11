# # 7-2. 휴가(DFS활용)
# import sys
# # sys.stdin = open("in5.txt", "r")
#
#
# def dfs(l, p):
#     global high
#     if l > n+1:
#         return
#     else:
#         if high < p:
#             high = p
#         if l <= n:
#             dfs(l+info[l][0], p+info[l][1])
#             for i in range(l, n+1):   # 여기서 반복호출을 계속 하고있음
#                 dfs(i+1, p)   # dfs(3, 0)부터 계속 중복 호출중 그 이후도..
#
#
# n = int(input())
# info = [[0, 0]]
# high = -2147000000
#
# for _ in range(n):
#     T, P = map(int, input().split())
#     info.append([T, P])
#
#
# dfs(1, 0)
#
# print(high)


# 7-2. 휴가(DFS활용)
# 부분집합 느낌
# x날에 상담을 한 경우, 안한 경우 2가지 나눔
import sys
# sys.stdin = open("in5.txt", "r")


def dfs(l, p):
    global high
    if l > n+1:  # n+1이 넘어가면 날짜 초과
        return
    else:
        if l == n+1:   # 마지막까지 체크하면
            if high < p:   # 큰 수 비교
                high = p
        dfs(l+info[l][0], p+info[l][1])  # l일의 상담을 한 경우
        dfs(l+1, p)  # l일의 상담을 안한경우(얘 때문에 l이 n+1까지 갈 수 있음)


n = int(input())
info = [[0, 0]]
high = -2147000000

for _ in range(n):
    T, P = map(int, input().split())
    info.append([T, P])

dfs(1, 0)

print(high)
