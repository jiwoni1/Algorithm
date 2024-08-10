# 4-6. 씨름선수(그리디)

# 그리디는 `정렬`문제
# n = int(input())
# lst = []
# for _ in range(n):
#     h, w = map(int, input().split())
#     lst.append((h, w))
#
# lst.sort()  # 키를 기준으로 정렬
# cnt = 1
#
# for i in range(n-1):
#     for j in range(i+1, n):
#         if lst[i][1] <= lst[j][1]:
#             break
#     else:
#         cnt += 1
#
# print(cnt)


# 2번째 방법 (for 문 하나로만, 최댓값 갱신)
n = int(input())
lst = []
for _ in range(n):
    h, w = map(int, input().split())
    lst.append((h, w))

lst.sort(reverse=True)

# 최댓값 갱신
largest = 0
cnt = 0

for i in range(n):
    if largest < lst[i][1]:
        cnt += 1
        largest = lst[i][1]

print(cnt)


