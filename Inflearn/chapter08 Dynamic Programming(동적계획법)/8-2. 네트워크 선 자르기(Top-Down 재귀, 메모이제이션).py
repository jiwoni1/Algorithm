# 8-1. 네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)
# dfs(7) = 7m의 선을 자르는 방법
# dfs(7) = dfs(6) + dfs(5)
# 상태 트리를 만들어가면서 그 값을 기억(저장)해가면서 값이 있으면 커트해가면서
# 메모이제이션(기억)해가면서 구하는 방식


n = int(input())
# nm의 선을 자르는 방법
dy = [0] * (n+1)
dy[1] = 1  # 1m의 선 자르는 방법 1가지
dy[2] = 2


def dfs(n):
    if dy[n] != 0:  # 가지치기
        return dy[n]
    else:
        dy[n] = dfs(n-1) + dfs(n-2)
        return dy[n]


print(dfs(n))