# 7-4.동전 바꿔주기(DFS)

def dfs(l, s):
    global cnt
    if s > t:  # s가 더 크면 끝
        return
    if s == t:
        cnt += 1
        return
    if l == k:  # 범위 넘어가면 끝
        return
    else:
        n = info[l][1]   # 다 더해보기
        for i in range(n, -1, -1):   # 점점 줄여가기
            dfs(l+1, s+info[l][0]*i)
        # for i in range(cn[l]+1):
        #     dfs(l+1, s+cv[l] * i)


cnt = 0
t = int(input())
k = int(input())
info = []
for _ in range(k):
    p, n = map(int, input().split())
    info.append([p, n])
    # 이렇게 따로 넣어도 ok
    # cv.append(p)
    # cn.append(n)

info.sort(reverse=True)

dfs(0, 0)
print(cnt)
