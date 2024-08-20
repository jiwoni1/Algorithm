import heapq as hq
import sys

n = int(input())
lst = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if not lst:
            print(0)
        else:
            print(-hq.heappop(lst))
    elif num > 0:
        hq.heappush(lst, -num)






