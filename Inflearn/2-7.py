# 2-7. 소수
import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
cnt = 0

for x in range(2, n+1):
    for i in range(2, x):  # range(2, 2)일때는 빈 범위 생성 -> for문 안이 실행되지x
        if x % i == 0:
            break
    else:
        cnt += 1


print(cnt)

# 소수판단
for x in range(2, n+1):
    for i in range(2, int(x**0.5)+1):  # range(2, 2)일때는 빈 범위 생성 -> for문 안이 실행되지x
        if x % i == 0:
            break
    else:
        cnt += 1


print(cnt)

# 에라토스테네스 체
# n 이하의 소수를 구할 때 사용
# 배수를 다 지워버리기!

n = int(input())
cnt = 0
che = [0] * (n+1)

for i in range(2, n+1):
    if che[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            che[j] = 1
    else:
        continue

print(cnt)



        



    