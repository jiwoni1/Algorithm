# 4-5. 회의실 배정(그리디)

# 그리디는 거의 다 정렬 문제
# 회의가 `끝나는` 시간을 기준으로 정렬
# 많은 회의를 하려면 일찍 시작하는 것보다 빨리 끝나는게 더 중요

# 1. 재귀 (근데 백준에서는 recursion 에러 뜸..)
# n = int(input())
# meetings = []
# for _ in range(n):
#     meetings.append(list(map(int, input().split())))
#     # s, e = map(int, input().split())
#     # meetings.append((s, e))   # 튜플 형태로 넣어도 좋아
#
#
# meetings.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간을 기준으로 정렬
# # x[1]이 같을 경우 x[0]을 기준으로 정렬
#
#
# def find(i, cnt):
#     for j in range(i+1, n):
#         if meetings[i][1] <= meetings[j][0]:  # 회의 끝나는 시간보다 시작하는 시간이 더 크거나 같은 것 찾기
#             cnt += 1
#             return find(j, cnt)  # 또 찾기
#     return cnt
#
#
# print(find(0, 1))

# 재귀 안쓰고
# n = int(input())
# meetings = []
# for _ in range(n):
#     s, e = map(int, input().split())
#     meetings.append((s, e))
#
# meetings.sort(key=lambda x: (x[1], x[0]))
#
# cnt = 0
# et = 0
#
# for s, e in meetings:
#     if s >= et:
#         et = e
#         cnt += 1
#
# print(cnt)

