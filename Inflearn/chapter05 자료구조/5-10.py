# 5-10. 최소힙
import sys
import heapq as hq
# sys.stdin = open("input.txt", "r")

a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:   # 출력할 자료가 없을때
            print(-1)
        else:
            print(hq.heappop(a))  # 루트노드 뽑기
    else:
        hq.heappush(a, n)   # a라는 리스트에 n값을 푸시해라
        # 최소힙의 형태로 넣어짐




