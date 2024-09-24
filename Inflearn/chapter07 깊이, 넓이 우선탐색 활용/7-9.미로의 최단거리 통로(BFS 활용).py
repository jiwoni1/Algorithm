# 7-9. 미로의 최단거리 통로(BFS 활용)
from collections import deque


def bfs(x, y, l):
    queue = deque([])
    queue.append((x, y, l))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    g[x][y] = 2

    while queue:
        x, y, l = queue.popleft()
        if x == 6 and y == 6:   # 도착지 도착하면 바로 끝(최단거리)
            return l
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7:
                if g[nx][ny] == 0:
                    queue.append((nx, ny, l+1))
                    g[nx][ny] = 2
    return -1    # 큐를 다 돌았는데도 (6,6)을 가지 못했다면 -1


g = [list(map(int, input().split())) for _ in range(7)]
print(bfs(0, 0, 0))
