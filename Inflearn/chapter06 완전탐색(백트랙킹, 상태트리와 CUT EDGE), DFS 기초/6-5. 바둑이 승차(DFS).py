# 6-5. 바둑이 승차(DFS)
import sys
# sys.stdin = open("in3.txt", "r")


# 부분집합의 합과 비슷하게
# 가지치기
# 1. res 리스트를 이용
# def dfs(x, tot):
#     if sum(w) <= c:
#         res.append(sum(w))
#         return
#     if tot > c:
#         return
#     if x == n:
#         res.append(tot)
#         print(tot, x)
#         return
#     else:
#         dfs(x+1, tot+w[x])
#         dfs(x+1, tot)
#
#
# c, n = map(int, input().split())
# w = [int(input()) for x in range(n)]
# res = []
#
# dfs(0, 0)
# print(max(res))


def dfs(x, tot, tsum):
    global max_w
    if sum + (sum_x - tsum) < max_w:   # 다른 것들을 다 더한다고 쳤을 때, max_w보다 작으면 갈 필요가 X
        return
    if sum(w) <= c:
        max_w = sum(w)
        return
    if tot > c:
        return
    if x == n:
        if max_w <= tot:
            max_w = tot
        return
    else:
        dfs(x+1, tot+w[x], tsum+w[x])    # tsum 에는 무조건 값 넣기
        dfs(x+1, tot, tsum+w[x])


c, n = map(int, input().split())
w = [int(input()) for x in range(n)]
max_w = 0
sum_w = sum(x)

dfs(0, 0, 0)
print(max_w)