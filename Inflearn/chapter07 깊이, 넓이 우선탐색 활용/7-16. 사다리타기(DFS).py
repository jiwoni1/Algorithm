# 7-16. 사다리 타기(DFS)

map = [list(map(int, input().split())) for _ in range(10)]
dx = [0, 0, -1]
dy = [1, -1, 0]
end = False


# 도착점부터 출발
def dfs(x, y):
    if x == 0:
        print(y)
        return
    else:   # 양 옆이 없을 때 위로
        if y - 1 >= 0 and map[x][y-1] == 1:
            map[x][y-1] = 0   # 다시 못가게
            dfs(x, y-1)   # 0 해제 안하는 이유 : back할 일이 없음
        elif y + 1 < 10 and map[x][y+1] == 1:
            map[x][y+1] = 0
            dfs(x, y+1)
        else:  # 위로
            map[x-1][y] = 0
            dfs(x-1, y)


for i in range(10):
    if map[9][i] == 2:
        dfs(9, i)
