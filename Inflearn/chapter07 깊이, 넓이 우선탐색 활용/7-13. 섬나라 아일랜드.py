# 7-13. 섬나라 아일랜드(BFS 활용)
import sys
from collections import deque


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    map[x][y] = 0
    # 대각선까지
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if map[nx][ny] == 1:
                    map[nx][ny] = 0
                    queue.append((nx, ny))


n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)