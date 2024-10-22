# 8-3. 도전과제 : 계단오르기(Top-Down : 메모이제이션)
# 넓은 의미에서의 DP

n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2


def dfs(n):
    if dy[n] > 0:
        return dy[n]
    else:
        dy[n] = dfs(n-1) + dfs(n-2)
        return dy[n]


print(dfs(n))

# 8-3. 도전과제 : 돌다리 건너기(Bottom-Up)

dy = [0] * (n+1)  # 메모이제이션 용
dy[1] = 2
dy[2] = 3
# 작은 범위부터 차곡차곡 범위 늘려가기 (바텀업 방식)
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])
