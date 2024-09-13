# 2178 미로 탐색

# 4 6
# 101111
# 101010
# 101011
# 111011

import sys
from collections import deque

n, m = map(int, input().split())
# 한줄씩 들어오는 이차원배열은 다음과 같이 받을 수 있다
g = []
for _ in range(n):
    # 하나씩 끊어서 리스트를 만듦
    g.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs(x, y):
    # 경로를 결정하는 queue
    queue = deque()
    # 튜플 형태로 넣기
    queue.append((x, y))
    # 상하좌우
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        # 튜플언패킹: 튜플을 꺼낼 때 각각의 요소를 변수에 할당할 수 있음
        # 리스트로 넣어도 똑같이 언패킹 가능
        x, y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위설정
            if 0 <= nx < n and 0 <= ny < m:
                # 방문하지않은 곳이면
                if g[nx][ny] == 1:
                    # 대기열에 넣자
                    queue.append((nx, ny))
                    # 여기까지 오는데 몇 블럭 걸렸나
                    g[nx][ny] = g[x][y] + 1


bfs(0,0)
print(g[n-1][m-1])

# 다른 방법 count를 queue에 또 넣어주는 것
# g[nx][ny] = 10 등 다른 숫자로 바꾸고
# queue.append(nx, ny, count+1) 이렇게
# 그리고 x, y가 n-1, m-1이 되면 count 출력