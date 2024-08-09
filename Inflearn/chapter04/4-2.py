# 4-2. 랜선자르기(결정알고리즘)
import sys
# sys.stdin = open("input.txt", "r")

k, n = map(int, input().split())
lines = []

for _ in range(k):
    lines.append(int(input()))

# 최대 길이의 선을 찾는 함수
def find_ans(lst, s, e, res):
    if s > e:   # s가 e보다 클때는 이분검색이 끝난 것
        return res

    mid = (s+e) // 2
    total = 0   # 자른 선의 총 갯수

    for i in lst:
        total += i // mid

    if total < n:   # n보다 작을 때는 선의 길이가 더 짧아야하므로 end를 mid-1로 범위를 줄임
        return find_ans(lst, s, mid-1, res)
    else:  # n보다 크거나 같을 경우에는 선의 길이가 더 길어도 됌. start를 mid+1로 범위를 줄임
        res = mid   # 일단 res에 공통 선의 길이 값을 담아줌
        return find_ans(lst, mid+1, e, res)


print(find_ans(lines, 1, max(lines), 0))
