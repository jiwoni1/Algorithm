import sys
# sys.stdin  = open("in1.txt", "rt")

# 2-6 자릿수의 합

n = int(input())
nums = list(input().split())

# 각 자연수의 자릿수의 합을 구하는 함수
def digit_sum(x):
    tmp = 0
    com = -1
    ans = 0

    for num in x:
        for i in num:
            tmp += int(i)
        if com < tmp:
            com = tmp
            ans = num
        tmp = 0

    return ans

print(digit_sum(nums))

# 2번째 방법. 몫과 나머지 이용
n = int(input())
nums = list(map(int, input().split()))

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    return total


max = -2467000000
res = 0
for x in nums:
    if max < digit_sum(x):
        max = digit_sum(x)
        res = x
print(res)







        



    