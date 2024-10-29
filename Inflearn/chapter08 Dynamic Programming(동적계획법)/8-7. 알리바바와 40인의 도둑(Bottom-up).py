# 8-8. 알리바바와 40인의 도둑(Bottom-up)

n = int(input())
stones = []
# dy[i][j]: stones[i][j]가 마지막 좌표일 때, 최소 에너지
# dy = [[216000000] * n for _ in range(n)]
dy = [[0] * n for _ in range(n)]
for i in range(n):
    stone = list(map(int, input().split()))
    stones.append(stone)


# dy 채우기
di = [-1, 0]
dj = [0, -1]
dy[0][0] = stones[0][0]
for i in range(1, n):
    dy[0][i] = dy[0][i-1] + stones[0][i]
    dy[i][0] += dy[i-1][0] + stones[i][0]

for i in range(1, n):
    for j in range(1, n):
        # for k in range(2):   # 왼쪽, 위쪽의 경로를 가져온 뒤, 더 작은거에 에너지 더하기
        #     ni = i + di[k]
        #     nj = j + dj[k]
        #     if 0 <= ni < n and 0 <= nj < n:
        #         dy[i][j] = min(dy[ni][nj]+stones[i][j], dy[i][j])
        # if dy[i][j] >= 216000000:
        #     dy[i][j] = stones[i][j]
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + stones[i][j]


print(dy[n-1][n-1])

