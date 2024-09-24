# # 7-8. 사과나무(BFS) 첫번째 방법 : 끝에 도달하면 queue에 넣지 x
# import sys
# from collections import deque
#
# n = int(input())
# g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# apple = 0
# is_end = False   # 다이아몬드의 끝인가
#
#
# def bfs(x, y):
#     global apple, is_end
#     queue = deque([])
#     queue.append((x, y))
#     apple += g[x][y]
#     g[x][y] = -1
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
#                     is_end = True    # 끝을 만난 이후부터는 queue에 넣지X
#                 if g[nx][ny] >= 0 and is_end is False:
#                     queue.append((nx, ny))
#                     apple += g[nx][ny]
#                     g[nx][ny] = -1     # 방문 체크
#                 elif g[nx][ny] >= 0 and is_end:    # 다이아몬드 끝
#                     apple += g[nx][ny]
#                     g[nx][ny] = -1     # 방문 체크
#
#
# bfs(n//2, n//2)
# print(apple)


# 7-8. 사과나무(BFS) 2번째 방법 : 레벨이 n//2가 되면 queue에서 안뺌! 다이아몬드 끝
import sys
from collections import deque

n = int(input())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
apple = 0
is_end = False   # 다이아몬드의 끝인가


def bfs(x, y, l):
    global apple
    queue = deque([])
    queue.append((x, y, l))
    apple += g[x][y]
    g[x][y] = -1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y, l = queue.popleft()
        if l == n//2:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] >= 0:
                    queue.append((nx, ny, l+1))
                    apple += g[nx][ny]
                    g[nx][ny] = -1     # 방문 체크



bfs(n//2, n//2, 0)
print(apple)