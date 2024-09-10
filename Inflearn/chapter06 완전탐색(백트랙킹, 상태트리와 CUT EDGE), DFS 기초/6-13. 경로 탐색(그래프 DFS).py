# 6-13. 경로 탐색(그래프 DFS)
import sys
# sys.stdin = open("input.txt", "r")


def dfs(s, route):   # 시작점, 경로 기록용
    global cnt
    for i in range(1, n+1):   # 1번 노드부터 갈 수 있는 노드 순회
        if g[s][i] == 1:  # 길이 있다면
            if i == n:   # n번 정점이라면
                cnt += 1
                # print(*([1]+route+[n]))
                return
            if ch[i] != 1:   # 방문하지 않은 노드라면
                ch[i] = 1    # 방문 표시
                dfs(i, route+[i])   # 그 노드에서 다시 시작
                ch[i] = 0  # 초기화


n, m = map(int, input().split())
ch = [0] * (n+1)  # 방문 표시
g = [[0]*(n+1) for _ in range(n+1)]
cnt = 0

for _ in range(m):
    s, e = map(int, input().split())
    g[s][e] = 1   # 그래프 그리기

ch[1] = 1
dfs(1, [])
# 또는 path = []를 따로 만들어서 거기에 append 했다가 pop하는 식으로 경로를 저장해도됨
print(cnt)

