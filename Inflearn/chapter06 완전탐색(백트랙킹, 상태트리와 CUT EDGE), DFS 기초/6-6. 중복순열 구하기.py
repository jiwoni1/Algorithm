# 6-6. 중복순열 구하기
import sys
# sys.stdin = open("in2.txt", "r")
input = sys.stdin.readline
# 인풋이 문자열일 때는
s = input().rstrip()

# 트리
def dfs(l, lst):
    global cnt
    if l == m - 1:
        print(*lst)
        cnt += 1
        return
    else:
        for i in range(1, n+1):    # 각 노드마다 1, 2, 3...
            dfs(l+1, lst+[i])


n, m = map(int, input().split())
cnt = 0

for i in range(1, n+1):   # 맨 처음 요소를 채우기위함
    dfs(0, [i])

print(cnt)


# 2. 매개변수 1개만 받기
# def dfs(x):
#     global cnt
#     if x == m:
#         print(*res)
#         cnt += 1
#         return
#
#     else:
#         for i in range(1, n+1):
#             res[x] = i   # 계속 덮어씌우면서 저장
#             dfs(x+1)
#
#
# n, m = map(int, input().split())
# res = [0] * m
# cnt = 0
# print(cnt)