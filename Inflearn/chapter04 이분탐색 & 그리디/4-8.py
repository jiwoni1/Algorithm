# 4-8. 침몰하는 타이타닉(그리디)

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

lp = 0
rp = n-1
cnt = 0

while lp <= rp:
    if weight[lp] + weight[rp] <= m:
        lp += 1
        rp -= 1
        cnt += 1
    else:
        rp -= 1
        cnt += 1

print(cnt)
