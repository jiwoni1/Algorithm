# 3-7. 곳감(모래시계)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# # 1. 회전시키기
# for _ in range(m):
#     row, dir, count = map(int, input().split())
#     row -= 1
#     new_list = [i for i in range(n)]    # 초기화
#
#     for i in range(n):
#         if dir == 0:  # 왼쪽
#             new_idx = i - count
#             if new_idx < 0:  # 음수라면 +n만큼
#                 new_idx += n
#             new_list[new_idx] = arr[row][i]  # 인덱스 재배치
#
#         else:  # 오른쪽
#             new_idx = i + count
#             if new_idx >= n:
#                 new_idx -= n
#             new_list[new_idx] = arr[row][i]
#
#     arr[row] = new_list   # 위에서 초기화를 매번하기때문에 서로 다른 주소값을 참조

# 1-2. pop과 insert를 이용해 회전
for _ in range(m):
    row, dir, count = map(int, input().split())
    row -= 1

    if dir == 0:
        for _ in range(count):
            arr[row].append(arr[row].pop(0))
    else:
        for _ in range(count):
            arr[row].insert(0, arr[row].pop())



# 2. 모래시계 합하기
total = 0
for i in range(n):
    s = n//2 - abs(i - n//2)
    for j in range(s, n-s):
        total += arr[i][j]

print(total)
#
# # 2-2. 범위 나누고 모래시계
# total = 0
# s, e = 0, n - 1
# for i in range(n):
#     for j in range(s, e+1):
#         total += arr[i][j]
#     if i < n//2:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
# print(total)

