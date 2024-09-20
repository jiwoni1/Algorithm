# 2667. 단지번호 붙이기
import sys
from collections import deque


def bfs(x, y):
    global cnt, tot
    tot += 1  # no.마을번호
    cnt += 1  # 시작 지점은 1이므로 주민수 +1
    queue = deque()
    queue.append((x, y))
    map[x][y] = tot

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()  # 상하좌우 인근 주민 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 설정
                if map[nx][ny] == 1:
                    map[nx][ny] = tot  # 중복체크 (마을번호부여)
                    queue.append((nx, ny))
                    cnt += 1  # 주민 수 카운트
    ans.append(cnt)  # 마을별 주민 수
    cnt = 0  # 그 다음 마을의 주민 수를 위해 초기화


n = int(input())
map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
tot = 1
cnt = 0
ans = []

# 이중리스트를 순회하면서 1을 발견하면 (새로운 마을을 발견하면)
# 인근 주민을 찾기위해 BFS 실행
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            bfs(i, j)

ans.sort()
print(tot-1)
for i in ans:
    print(i)
