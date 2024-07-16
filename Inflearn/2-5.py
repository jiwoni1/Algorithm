import sys
# sys.stdin  = open("input.txt", "rt")

# 2-5 정다면체

# 1번째 방법
n, m = map(int, input().split())
if n > m:
    m = n

plus = m - n
# ans = list(i for i in range(n+1, n+1+plus+1))
# print(*ans)

print(*list(i for i in range(n+1, n+1+plus+1)))


# 2번쨰 방법
N, M = map(int, input().split())
cnt = [0] * (N+M+1)
ans = []

for n in range(1, N+1):
    for m in range(1, M+1):
        cnt[n+m] += 1

for idx in range(len(cnt)):
    if cnt[idx] == max(cnt):
        ans.append(idx)
print(*ans)







        



    