# 8-6. 최대 선 연결하기
# 같은 방식으로 LIS(Longest Increasing Subsequence)
n = int(input())
nums = list(map(int, input().split()))
dy = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dy[i] = max(dy[j]+1, dy[i])

print(max(dy))







