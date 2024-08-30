# 6-8. 순열 구하기
import sys
# sys.stdin = open("in1.txt", "r")

n, m = map(int, input().split())
res = [0] * m
cnt = 0


def dfs(l, lst):
    global cnt
    if l == m:
        print(*lst)
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if i not in lst:    # 안에 있으면 넘어가기 (중복x)
                res[l] = i
                dfs(l+1, lst+[i])


dfs(0, [])
print(cnt)