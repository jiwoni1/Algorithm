# 3-6. 격자판 최대합

# 이차원 배열 입력받기
# 1. arr = [for _ in range(n)]
# for i in range(n)
# arr[i] = list(map(int, input().split()))

# 2. arr = []
# for i in range(n)
# arr.append(list(map(int, input().split())))

# 3. arr = [list(map(int, input().split())) for _ in range(n)]

n = int(input())
arr = [0] * n
m = -2946000000


# for i in range(n):
#     arr[i] = list(map(int, input().split()))

arr = []  # 빈 배열로 초기화

for i in range(n):
    arr.append(list(map(int, input().split())))

# 행, 열
for i in range(n):
    plus1 = 0
    plus2 = 0
    for j in range(n):
        plus1 += arr[i][j]  # 행
        plus2 += arr[j][i]  # 열
    if plus1 < plus2:
        plus1 = plus2
    if m < plus1:
        m = plus1


plus1, plus2 = 0, 0
# 대각선
for i in range(n):
    plus1 += arr[i][i]
    plus2 += arr[i][n-1-i]

if plus1 < plus2:
    plus1 = plus2
if m < plus1:
    m = plus1

print(m)
