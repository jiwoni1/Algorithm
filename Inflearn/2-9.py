# 2-9. 주사위 게임

n = int(input())
max_n = -2467000000

for _ in range(n):
    nums = list(map(int, input().split()))

    if len(set(nums)) == 1:
        money = 10000 + nums[0] * 1000
    elif nums[0] == nums[1] or nums[0] == nums[2]:
        money = 1000 + nums[0] * 100
    elif nums[1] == nums[2]:
        money = 1000 + nums[1] * 100
    else:
        money = max(nums) * 100

    if money > max_n:
        max_n = money

print(max_n)