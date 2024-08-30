# 6-7. 동전교환
import sys
# sys.stdin = open("in4.txt", "r")

n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)  # 큰 수부터 더해야 호출을 줄일 수 있음
m = int(input())
min_cnt = 21470000000


# 트리
# 가지치기
def dfs(x, tot):
    global min_cnt
    if min_cnt < x:   # x보다 더 큰 레벨로 가면 볼 필요X
        return
    if tot > m:
        return
    elif tot == m:
        if min_cnt > x:
            min_cnt = x
        return
    else:
        for i in range(n):
            dfs(x+1, tot+coin[i])   # 중복을 허용하는 순열

# 가지치기용
for i in coin:
    if m % i == 0:
        temp = m // i
        if min_cnt > temp:
            min_cnt = temp

dfs(0, 0)
print(min_cnt)