# 4-4. 마구간 정하기
import sys
# sys.stdin = open("input.txt", "r")

n, c = map(int, input().split())
xi = []

for _ in range(n):
    xi.append(int(input()))

xi.sort()

def find_ans(s, e, res):
    if s > e:
        return res

    mid = (s+e) // 2
    # 모든 말의 거리는 mid 보다 크거나 같아야함
    tmp = 0
    cnt = 1

    # 첫번째 말은 맨 왼쪽에
    for i in range(1, n):
        if xi[i] - xi[tmp] >= mid:  # 여기가 2번
            tmp = i   # mid 거리보다 더 크거나 같으면 거기에 말 놓고 저장
            cnt += 1
    if cnt >= c:
        res = mid
        return find_ans(mid+1, e, res)
    else:
        return find_ans(s, mid-1, res)


print(find_ans(xi[0], (xi[-1]-xi[0]), 0))
