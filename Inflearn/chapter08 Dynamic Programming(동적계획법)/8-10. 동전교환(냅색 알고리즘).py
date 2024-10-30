# 8-10. 동전교환(냅색 알고리즘)

# 1. 그리디 -> 안됌
# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort(reverse=True)
# m = int(input())
# ans = 0
#
# for i in coins:
#     ans += m // i
#     m = m % i
#
# print(ans)


# dp; 냅색 알고리즘 O(NM)
# n = int(input())
# coins = list(map(int, input().split()))
# m = int(input())
# # dy[i]: i원을 거슬러주는데 사용된 동전의 최소 개수
# dy = [1000] * (m+1)
# dy[0] = 0    # 초기화
#
# for i in coins:
#     for j in range(i, m+1):
#         dy[j] = min(dy[j], dy[j-i]+1)
#
# print(dy[m])

# 3. BFS 이용(최소 경로) O(NM)
from collections import deque
n = int(input())
coins = list(map(int, input().split()))
m = int(input())
visited = [False] * (m+1)   # 이미 방문한 금액은 방문 금지(맨 처음으로 방문한 게 최소 개수)
visited[0] = True  # 맨 처음은 살려야됌


def bfs():
    queue = deque([(0, 0)])  # (현재 금액, 동전 개수)

    while queue:
        current_sum, cnt = queue.popleft()
        if current_sum == m:  # 목표 금액에 젤 먼저 도착한 거 : 최소 동전 개수
            return cnt
        else:
            for coin in coins:   # 동전들 다 더해보면서
                next_sum = current_sum + coin   # 그 다음
                if next_sum <= m and not visited[next_sum]:  # 방문하지 않아야함 -> 그래야 최소 개수
                    queue.append((next_sum, cnt+1))


print(bfs())
