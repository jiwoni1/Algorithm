# # 7-12. 단지 번호 붙이기 (DFS, BFS)
# from collections import deque
#
# n = int(input())
# map = [list(map(int, input())) for _ in range(n)]
# tot = 0
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# cnt_list = []
#
#
# def bfs(x, y):
#     cnt = 1
#     queue = deque([])
#     queue.append([x, y])
#     map[x][y] = tot + 2
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == 1:
#                 queue.append([nx, ny])
#                 map[nx][ny] = tot + 2
#                 cnt += 1
#     cnt_list.append(cnt)
#
#
# # 1 찾기
# for i in range(n):
#     for j in range(n):
#         if map[i][j] == 1:
#             bfs(i, j)
#             tot += 1
#
# print(tot)
# cnt_list.sort()
# for i in cnt_list:
#     print(i)
#
# 7-12. 단지 번호 붙이기 (DFS, BFS)
from collections import deque

n = int(input())
map = [list(map(int, input())) for _ in range(n)]
tot = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1
cnt_list = []


def dfs(x, y):
    global cnt
    map[x][y] = tot + 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == 1:

            map[nx][ny] = tot + 2
            dfs(nx, ny)
            cnt += 1
            # cnt -= 1
            # map[nx][ny] = 1



# 1 찾기
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            dfs(i, j)
            cnt_list.append(cnt)
            cnt = 1
            tot += 1

print(tot)
cnt_list.sort()
for i in cnt_list:
    print(i)