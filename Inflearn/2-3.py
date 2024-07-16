import sys
# sys.stdin  = open("input.txt", "rt")

# K번째 큰 수

n, k = map(int, input().split())
card = list(map(int, input().split()))
lst = []
cnt = 0

for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            lst.append(card[a] + card[b] + card[c])

lst = list(set(lst))
lst.sort(reverse=True)
print(lst[k-1])
print(lst)

# res = set()
# res.add(1)  set은 add 메소드
# set은 sort가 없음 (list에만)

# for i in range(5,5):
#     print(i)   오류 안남, 값이 없음
