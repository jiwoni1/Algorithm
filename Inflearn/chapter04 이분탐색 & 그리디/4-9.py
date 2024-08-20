# 4-9. 증가수열 만들기(그리디)
from collections import deque

n = int(input())
nums = list(map(int, input().split()))
nums = deque(nums)
seq = []
ans = ''
last = 0

# 1. 왼쪽
while True:
    lt = nums[0]
    rt = nums[-1]

    if last < lt and last < rt:
        if lt < rt:
            seq.append(lt)
            last = lt
            ans += 'L'
            nums.popleft()
        else:
            seq.append(rt)
            last = rt
            ans += 'R'
            nums.pop()
    elif rt < last < lt or (len(nums) == 1 and last < lt):
        seq.append(lt)
        last = lt
        ans += 'L'
        nums.popleft()
    elif lt < last < rt:
        seq.append(rt)
        last = rt
        ans += 'R'
        nums.pop()
    else:
        break


print(len(seq))
print(ans)





