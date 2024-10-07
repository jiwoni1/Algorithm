# 인프런 7-17. 피자 배달 거리(DFS활용)
# 재귀 호출에서 독립적인 리스트가 필요하다면,
# 매번 새로운 리스트를 만들어야 하고, 그렇지 않으면 이전 호출에서 사용한 리스트가 그대로 다음 호출에 영향을 미칩니다.
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
pizza = []


res = 2147000000


def dfs(l, x, tmp):
    global res
    if l == m:   # 조합 (피자집들 중에서 m개의 피자집만 뽑는)
        if res > sum(tmp):
            res = sum(tmp)
            return
    else:
        for j in range(x+1, len(pizza)):  # 조합
            tmp_n = [0] * len(house)   # 거리비교 new 버전
            for i in range(len(house)):  # 거리 비교
                new = abs(pizza[j][0] - house[i][0]) + abs(pizza[j][1] - house[i][1])
                # print(f'j : {j}, i : {i}, tmp: {tmp}, n: {n} new: {new}')
                if tmp[i] > new:  # 더 가까운 피자 가게가 있다면
                    tmp_n[i] = new  # 거리 다시 설정
                else:
                    tmp_n[i] = tmp[i]  # 아니라면 그대로
            dfs(l+1, j, tmp_n)  # 그 다음 조합만들기


# 1. 집, 피자 찾기
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            pizza.append((i, j))

t = [2347000000] * len(house)


# 2. 거리 계산
dfs(0, -1, t)
print(res)


