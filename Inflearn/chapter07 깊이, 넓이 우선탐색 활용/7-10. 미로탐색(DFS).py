# 7-10. 미로탐색(DFS)

g = [list(map(int, input().split())) for _ in range(7)]
g[0][0] = 1  # 출발지 체크
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    if x == 6 and y == 6:   # 끝에 도착하면 방법 +1
        cnt += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7:
                if g[nx][ny] == 0:  # 길이 있으면
                    g[nx][ny] = 1   # 방문체크
                    dfs(nx, ny)   # dfs
                    g[nx][ny] = 0   # 방문체크 풀기


dfs(0, 0)
print(cnt)