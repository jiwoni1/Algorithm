# 3-8. 봉우리

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 1. 첫번째 방법
# 주변 탐색
# r = [-1, 0, 1, 0]
# c = [0, 1, 0, -1]
#
# for i in range(n):
#     for j in range(n):
#         for q in range(4):
#             ni = i + r[q]
#             nc = j + c[q]
#             if 0 <= ni < n and 0 <= nc < n:
#                 if map[i][j] <= map[ni][nc]:
#                     break    # 옆이 더 크면 봉우리 X
#         else:
#             cnt += 1     # break 가 한 번도 없었으면 봉우리
#
#
# print(cnt)

# 2. 테두리 형성, all함수 사용
map.insert(0, [0]*n)
map.append([0]*n)

for i in range(n+2):
    map[i].insert(0, 0)
    map[i].append(0)

# 순회
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(map[i][j] > map[i+dx[k]][j+dy[k]] for k in range(4)):   # all 함수 : 안에 조건문이 모두 True여야 True
            cnt += 1

print(cnt)

