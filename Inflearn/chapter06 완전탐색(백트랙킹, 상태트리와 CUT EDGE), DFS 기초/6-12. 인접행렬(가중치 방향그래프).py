# 인접행렬(가중치 방향그래프)
import sys
sys.stdin = open("input.txt", "r")


n, m = map(int, sys.stdin.readline().split())
# info = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
#
# ans = [([0] * n) for _ in range(n)]  # 인접행렬을 담을 판
#
# for i in range(m):
#     ans[(info[i][0]-1)][(info[i][1]-1)] = info[i][2]   # 그대로 인접행렬에 담기
#
# for i in range(n):
#     print(*ans[i])

g = [[0]*(n+1) for _ in range(n+1)]  # 이차원리스트는 이렇게 생성해야함

for _ in range(m):
    s, e, n = map(int, input().split())  # 입력받음과 동시에 그래프에 담기
    g[s][e] = n

for i in range(1, n+2):
    print(*g[i])