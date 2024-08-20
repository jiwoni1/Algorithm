# 5-6. 응급실
import sys, copy
# sys.stdin = open("input.txt", "r")

from collections import deque

n, m = map(int, input().split())
danger = list(map(int, input().split()))
new = []
for i in range(n):
    new.append((danger[i], i))  # m번째 환자를 알기위해 튜플로 인덱스와 매치
dq = deque(new)

q = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]


cnt = 0


while True:
    if dq[0][0] != max(dq)[0]:  # 가장 큰 수가 아니면
        dq.append(dq.popleft())  # 뒤로가기
    else:  # 가장 커
        if dq[0][1] == m:
            cnt += 1
            print(cnt)
            break
        else:
            dq.popleft()
            cnt += 1


# while True:
#     cur = q.popleft()
#     if any(cur[1]<x[1] for x in q):
#         # 하나라도 큰 게 있다면
#         q.append(cur)





