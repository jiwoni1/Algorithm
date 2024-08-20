# 5-5. 공주 구하기(큐 자료구조로 해결)
import sys
# sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
num = 0

from collections import deque

princes = list(range(1, n+1))
princes = deque(princes)

while len(princes) > 1:
    num += 1
    if num == k:
        princes.popleft()
        num = 0
    else:
        princes.append(princes.popleft())  # 다시 뒤로가

print(*princes)

# while len(princes) > 1:
#     for _ in range(k-1):
#         princes.append(princes.popleft())
#     princes.popleft()



