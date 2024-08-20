# 3-2. 숫자만 추출
import sys
# sys.stdin = open("input.txt", "r")

word = input()
num = ""
cnt = 0
for i in word:
    if i.isnumeric():
        num += i

num = int(num)
print(num)
# 약수 구하기
for i in range(2, num):
   if num % i == 0:
       cnt += 1
print(cnt+2)



