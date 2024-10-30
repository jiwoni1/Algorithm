# 8-11. 최대점수 구하기(냅색 알고리즘)
# 문제가 하나일 때부터 두 개, 세 개,, 점점 확장해가기
# 바로 이전 케이스 참조

# 1. 2차원 배열
# n, m = map(int, input().split())
# # 한 번만 쓸 수 있으니 2차원 배열로 다이나믹 테이블
# # dy[i][j]: 문제 i 번까지 j 시간 내에 풀었을 때의 최대 점수
# dy = [[0] * (m+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     s, t = map(int, input().split())
#     for j in range(1, m+1):
#         if j-t >= 0:
#             # 바로 이전의 j 시간의 최대 점수와 비교
#             dy[i][j] = max(dy[i-1][j], dy[i-1][j-t]+s)
#         else:
#             dy[i][j] = dy[i-1][j]
#
# print(dy[n][m])


# 2. 1차원 배열 (2차원 배열은 nm이 올라가면 메모리 차지도 너무 크고 그래서 시간 복잡도 up)
# 1차원 배열을 사용하려면 중복을 피해야함(한 문제를 여러번 푸는 것)
# 그래서 뒤에서부터 숫자를 적용함(그럼 다시 참조를 안하니까)

n, m = map(int, input().split())
# dy[i]: i 시간안에 얻을 수 있는 최대 점수
dy = [0] * (m+1)
for i in range(n):
    s, t = map(int, input().split())
    for j in range(m, t-1, -1):     # 뒤(m)에서부터 dy[t]까지 숫자 적용 => 한 문제는 한 번씩만
        dy[j] = max(dy[j], dy[j-t]+s)  # i 문제를 푼다고 가정했으므로 i 문제를 푸는 시간 빼기

print(dy[m])





