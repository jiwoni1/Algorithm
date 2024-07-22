# 3-5. 수들의 합
import sys
# sys.stdin = open("input.txt", "r")

# 1. 이중포문 이용, 시간복잡도 O(n**2)
# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
#
# cnt = 0
#
# for i in range(n):
#     sum = 0
#     for j in range(i, n):
#         if sum < m:
#             sum += nums[j]
#             if sum == m:
#                 cnt += 1
#                 break
#         elif sum > m:
#             break
#     if sum < m:  # 끝까지 다 돌았는데도 모자라면 끝
#         break
#
# print(cnt)


# 2. 투포인터 이용, 시간복잡도 더 빠름
n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
lt, rt = 0, 1  # left point, right point
tot = nums[lt]

while True:   # 비교를 반복

    if tot < m:
        if rt == n:   # 더할게 없는데 계속 더하라고 할 수 x
            break
        tot += nums[rt]
        rt += 1

    elif tot == m:
        cnt += 1
        tot -= nums[lt]
        lt += 1

    elif tot > m:
        tot -= nums[lt]
        lt += 1

print(cnt)


