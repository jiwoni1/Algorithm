# 7-1. 최대점수 구하기(DFS)
import sys
# sys.stdin = open("input.txt", "r")

# 부분집합 만들기
def dfs(l, s, t):   # 시작 지점, 누적 점수, 누적 시간
    global high
    if t > m:   # 시간 제한을 초과했다면
        return   # 가지치기
    else:
        for i in range(l, n+1):   # 조합을 만들듯이
            if high < s:    # 최고 점수보다 높을 경우
                high = s
            if i < n:    # 마지막 케이스까지 더할수있도록 고려
                dfs(i+1, s+lst[i][0], t+lst[i][1])   # 점수 더하고 시간구하기


n, m = map(int, input().split())
lst = []   # 점수와 시간을 담을 곳
high = 0
for _ in range(n):
    score, time = map(int, input().split())
    lst.append([score, time])

dfs(0, 0, 0)
print(high)

# 방법 2
# def dfs(l, s, t):
#     global high
#     if t > m:
#         return
#     if l == n:
#         if s > high:
#             high = s
#     else:
#         dfs(l+1, s+lst[l][0], t+lst[l][1])
#         dfs(l+1, s, t)  # 포함되지 않는 경우