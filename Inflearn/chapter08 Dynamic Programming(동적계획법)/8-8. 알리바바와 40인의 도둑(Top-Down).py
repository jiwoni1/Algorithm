# 8-8. 알리바바와 40인의 도둑(Top-Down)
# Top-Down: 규칙찾고, 재귀방식! 상태트리 나누기

n = int(input())
stones = [list(map(int, input().split())) for _ in range(n)]
# stones = []
# dy[i][j]: stones[i][j]가 마지막 좌표일 때, 최소 에너지
dy = [[0] * n for _ in range(n)]
# for i in range(n):
#     stone = list(map(int, input().split()))
#     stones.append(stone)

dy[0][0] = stones[0][0]
for i in range(1, n):
    dy[0][i] = stones[0][i] + dy[0][i-1]
    dy[i][0] = stones[i][0] + dy[i-1][0]


def dfs(x, y):
    if x == 0 or y == 0:  # 가장자리
        return dy[x][y]
    if dy[x][y] != 0:   # 메모이제이션
        return dy[x][y]
    else:
        top = dfs(x-1, y)
        left = dfs(x, y-1)
        dy[x][y] = min(top, left) + stones[x][y]
        return dy[x][y]


print(dfs(n-1, n-1))
