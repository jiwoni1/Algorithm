# 2-8. 뒤집은 소수

# n = int(input())
# nums = list(map(int, input().split()))
#
# # 숫자를 뒤집는 함수
# def reverse(x):
#     x = str(x)
#     new_x = ''
#     for i in range(len(x)-1, -1, -1):
#         new_x += x[i]
#     return int(new_x)
#
# # 소수인지 확인하는 함수
# def isPrime(x):
#     if x == 1:
#         return False
#     else:
#         for i in range(2, int(x**0.5)+1):
#             if x % i == 0:
#                 return False
#         return True
#
#
# for num in nums:
#     re = reverse(num)
#     if isPrime(reverse(num)):
#         print(re, end=" ")

# 2번째 방법. 자리수 이용 -> 몫 & 나머지

n = int(input())
nums = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True


for num in nums:
    re = reverse(num)
    if isPrime(re):
        print(re, end=" ")