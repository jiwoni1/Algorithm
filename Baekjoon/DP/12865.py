# 12865. 평범한 배낭
# 문제가 하나일 때부터 두 개, 세 개,, 점점 확장해가기
# 바로 이전 케이스 참조

# 1. 2차원 배열로 푸는 법
# n, k = map(int, input().split())
# # 한 번만 쓸 수 있으니 2차원 배열로 다이나믹 테이블
# # dy[i][j]: 물건 i 번까지 j 무게내에 담았을 때의 최대 가치
# dy = [[0] * (k+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     w, v = map(int, input().split())
#     for j in range(1, k+1):
#         if j-w >= 0:
#             # 바로 이전의 j 무게의 최대 가치와 비교(확장)
#             dy[i][j] = max(dy[i-1][j], dy[i-1][j-w]+v)
#         else:
#             dy[i][j] = dy[i-1][j]
#
# print(dy[n][k])


# 1차원 배열로 푸는 법(2차원 배열은(N*M) 메모리 너무 많이 잡아먹으므로 시간 느려지니까)
n, k = map(int, input().split())
# dy[i]: 버틸 수 있는 무게가 i일 때, 최대 가치
dy = [0] * (k+1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(k, w-1, -1):
        dy[j] = max(dy[j], dy[j-w]+v)  # i 물건을 넣어야하므로, w만큼 비우기

print(dy[k])


