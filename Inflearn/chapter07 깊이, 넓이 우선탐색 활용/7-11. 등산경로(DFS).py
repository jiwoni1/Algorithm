# 7-11. 등산경로(DFS)

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
max_x, max_y, min_x, min_y = 0, 0, 0, 0
com_max = -21640000
com_min = 21640000

for i in range(n):
    for j in range(n):
        if map[i][j] < com_min:
            com_min = map[i][j]
            min_x = i
            min_y = j
        if map[i][j] > com_max:
            com_max = map[i][j]
            max_x = i
            max_y = j


def dfs(x, y):
    global cnt
    if x == max_x and y == max_y:
        cnt += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if map[x][y] < map[nx][ny]:
                    visited[nx][ny] = True  # 방문 체크
                    dfs(nx, ny)
                    visited[nx][ny] = False  # 방문 체크 해제


dfs(min_x, min_y)
print(cnt)




