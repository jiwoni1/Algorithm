# 4-1. 이분검색
import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 1. 정렬
nums.sort()

# 2. 이분탐색
start = 0
end = len(nums)

while start <= end:
    mid = (start + end) // 2

    if m > nums[mid]:
        start = mid + 1
    elif m == nums[mid]:
        print(mid+1)
        break
    else:
        end = mid - 1



