# 8-9. 가방문제(냅색 알고리즘)
# 물건의 갯수는 무제한 (여러 번 사용 가능)
n, limit = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
dy = [0] * (limit+1)

for i in range(limit+1):
    for w, v in info:
        if i-w >= 0:
            dy[i] = max(dy[i], dy[i-w]+v)

print(dy[-1])

# 강의 방식
n, limit = map(int, input().split())
for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, limit+1):
        dy[j] = max(dy[j], dy[j-w]+v)

print(dy[limit])
