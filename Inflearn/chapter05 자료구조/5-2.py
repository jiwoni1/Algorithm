# 5-2. 쇠막대기(스택)
import sys
# sys.stdin = open("input.txt", "r")

# 1번째 방법. stack 을 활용안한 느낌
# info = list(input())
# stack = []
# present = 0   # 현재 막대기의 갯수
# ans = 0   # 총 막대기의 갯수
#
# for i in info:
#     if not stack:
#         stack.append(i)
#     else:
#         if stack[-1] == '(' and i == '(':   # 막대기 시작(막대기 갯수 +1)
#             present += 1
#             ans += 1
#         elif stack[-1] == '(' and i == ')':  # 레이저(현재 있는 막대기 갯수만큼 새로운 막대기 생성)
#             ans += present
#         elif stack[-1] == ')' and i == ')':   # 막대기 끝(막대기 갯수 -1)
#             present -= 1
#         stack.append(i)
#
# print(ans)


lst = list(input())
stack = []
cnt = 0

# for i in lst:
#     if i == '(':
#         stack.append(i)
#     else:  # i == ')'
#         if stack[-1] == '(':
#             stack.pop()
#             cnt += len(stack)
#         else:  # stack 에는 '('밖에 없음...(즉, ))의 조건을 찾을 수 없음)
#             stack.pop()
#             cnt += 1
# print(cnt)

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(i)
    else:  # i == ')'
        if lst[i-1] == '(':  # 레이저
            stack.pop()
            cnt += len(stack)  # 새롭게 생성된 막대기 수 더하기
        else:  # ))의 경우
            stack.pop()  # 막대기 끝
            cnt += 1  # 마지막 막대기
print(cnt)


