# 2644. 촌수계산
from collections import deque

def bfs(visited):
    # queue = deque([p1, 0])  # deque에 p1과 0이 개별적으로 들어감
    # 이렇게 써야 [p1, 0] 리스트가 하나의 요소
    queue = deque()
    # 출발지 저장
    queue.append([p1, 0])
    # 출발지 방문처리
    visited[p1] = True

    while queue:
        # 출발지와 촌수 언패킹
        s, count = queue.popleft()
        # 원하는 값
        if s == p2:
            print(count)
            return
        else:
            # 길이 있고 방문하지않은 곳이면
            for i in g[s]:
                if not visited[i]:
                    # 대기열 추가, 촌수 더하기
                    queue.append((i, count+1))
                    # 방문 처리
                    visited[i] = True
    print(-1)  # 연결되지않은 노드
    return


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
visited = [False] * (n+1)

bfs(visited)

