# 6-10. 수들의 조합
import sys
# sys.stdin = open("in1.txt", "r")

n, k = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
m = int(input())

com = [0] * k
cnt = 0


# 1. 조합 구하기
def dfs(l, s):
    global cnt
    if l == k:
        # 2. m의 배수인 개수 구하기
        if sum(com) % m == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            com[l] = lst[i]
            dfs(l+1, i+1)


dfs(0, 0)
print(cnt)


# 따로 리스트에 저장하지않고 하는법
def dfs2(l, s, sum):
    global cnt
    if l == k:
        if sum % m == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            dfs2(l+1, i+1, sum+lst[i])   # 매개변수에 저장


dfs2(0, 0, 0)
print(cnt)