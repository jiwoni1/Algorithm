# # 3-4. 두 리스트 합치기
import sys
sys.stdin = open("input.txt", "r")

# # 1번째 방법 (sort메서드 이용)
first_n = int(input())
first = list(map(int, input().split()))
second_n = int(input())
second = list(map(int, input().split()))

ans = first + second
ans.sort()

print(*ans)

# 2번째 방법 (포인터 변수 사용!!)
# 이미 오름차순으로 정렬되어있으므로 sort보다 더 빠르게 풀 수 있음 sort의 시간복잡도는 nlogn
an = int(input())
a = list(map(int, input().split()))
bn = int(input())
b = list(map(int, input().split()))
new = []

p1, p2 = 0, 0

while True:
    if a[p1] < b[p2]:
        new.append(a[p1])
        p1 += 1
        if p1 == an:
            new += b[p2:]
            break

    elif a[p1] >= b[p2]:
        new.append(b[p2])
        p2 += 1
        if p2 == an:
            new += a[p1:]
            break

print(*new)
