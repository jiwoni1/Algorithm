# 8-12. 플로이드 워샬 알고리즘
# 플로이드 와샬 알고리즘: 모든 정점에서 모든 정점까지 최단 경로
# 1을 거쳐서 갈 때, 최단 경로 -> 2를 거쳐서 갈 때 최단 경로

n, m = map(int, input().split())
dy = [[2164000000] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dy[i][i] = 0

# 인접 행렬만 초기화
for _ in range(m):
    s, e, p = map(int, input().split())
    dy[s][e] = p

# n번 노드를 거쳐서 갈 때의 최단거리
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 경유지 들린 것과 아닌 것중에 최단거리
            dy[i][j] = min(dy[i][j], dy[i][k]+dy[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if dy[i][j] == 2164000000 and i != j:
            dy[i][j] = 'M'
        print(dy[i][j], end=' ')
    print()










