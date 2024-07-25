# 3-7. 사과나무
# 대칭? 다이아몬드를 구할 때는 반절접어보기, 변수화!
# if를 사용해서 범위를 바꾸는 것도 좋은 방법

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total = 0

# 첫번째 방법 (대칭점 찾기)
# for i in range(n):
#     a = abs(n // 2 - i)
#     for j in range(a, n-a):
#         total += arr[i][j]
#
# print(total)

# 두번째 방법 (if를 사용해서 범위를 늘리고 줄이기)
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        total += arr[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(total)

