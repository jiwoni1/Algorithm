import sys
# sys.stdin  = open("input.txt", "rt")

# 2-1. K번째 약수

N, K = map(int, input().split())

div = []

for i in range(1, N+1):
    if N % i == 0:
        div.append(i)
    if len(div) == K:
        print(div[K-1])
        break
else:  # break를 하지 않았다면
    print(-1)

# 2번째 방법
# cnt = 0

# for i in range(1, N+1):
#     if N % i == 0:
#         cnt += 1
#     if cnt == K:
#         print(i)
#         break
# else:
#     print(-1)