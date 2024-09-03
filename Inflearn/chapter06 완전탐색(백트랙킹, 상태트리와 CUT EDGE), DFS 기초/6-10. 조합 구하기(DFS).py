# 6-10. 조합 구하기

n, m = map(int, input().split())
ans = [0] * m
cnt = 0


def dfs(l, x):
    global cnt
    if l == m:
        print(*ans)
        cnt += 1
        return
    else:
        for i in range(x, n+1):  # i 다음 숫자부터만 사용가능 (조합)
            ans[l] = i
            dfs(l+1, i+1)


dfs(0, 1)
print(cnt)