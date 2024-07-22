import sys
# sys.stdin  = open("input.txt", "rt")

# 2-2. K번째 수

for i in range(1, int(input())+1):
    n, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))

    lst = lst[s-1:e]
    lst.sort()

    print(f'#{i} {lst[k-1]}')