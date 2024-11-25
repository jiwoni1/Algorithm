# 1654. 랜선 자르기

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

s, e = 1, max(lines)

while s <= e:    # 이분탐색 종료 조건
    m = (s + e) // 2

    cnt = sum(line // m for line in lines)   # 랜선 나누고 총 몇 개인지

    if cnt >= n:  # n개 이상이면 랜선 길이 더 키우기
        s = m + 1
    else:   # 미만이면 랜선 길이 더 짧게
        e = m - 1

print(e)