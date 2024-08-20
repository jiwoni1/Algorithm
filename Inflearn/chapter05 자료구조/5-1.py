# 5-1. 가장 큰 수(스택)
import sys
# sys.stdin = open("input.txt", "r")

num, m = map(int, (input().split()))
num = str(num)
# num = list(map(int, str(num)))
n = len(num)
cnt = 0
stack = [int(num[0])]



# 나보다 앞에 있는 숫자가 나보다 작으면 안돼
for i in range(1, n):
    if cnt == m:
        stack.append(int(num[i]))
    else:
        while stack and stack[-1] < int(num[i]):
            stack.pop()
            cnt += 1
            if cnt == m:
                break
        stack.append(int(num[i]))

if cnt < m:
    for _ in range(m-cnt):
        stack.pop()
    # stack = stack[:(cnt-m)]

for i in stack:
    print(i, end='')
# res = ''.join(map(str, stack))



