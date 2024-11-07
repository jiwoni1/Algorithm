# 8-14. 위상정렬(그래프 정렬)
from collections import deque

n, m = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
# 진입차수; dy[i]: i번째 일을 하기 전에 해야할 일의 개수
dy = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    dy[b] += 1
    g[a][b] = 1

# 일의 순서를 나타내는 큐(진입차수가 0되면 큐로 들어옴)
queue = deque([])
for i in range(1, n + 1):
    if dy[i] == 0:
        queue.append(i)

while queue:
    work = queue.popleft()
    print(work, end=' ')
    for i in range(1, n+1):
        if g[work][i] != 0:   # 연결 끊기
            g[work][i] = 0
            dy[i] -= 1
            if dy[i] == 0:
                queue.append(i)





