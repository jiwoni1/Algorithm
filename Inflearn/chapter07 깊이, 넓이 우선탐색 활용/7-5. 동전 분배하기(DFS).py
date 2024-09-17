# 7-5. 동전 분배하기(DFS)

# dfs는 상태트리 그리기!!
# 3명에게 나눠줌 -> 가지 3개 (경우의 수 3개)

def dfs(l):
    global res
    if l == n:   # 종료 조건
        if len(set(wallet)) != 3:  # 총액이 달라야함
            return
        else:
            # if (max(wallet) - min(wallet)) < res:  # 최소
            #     res = (max(wallet) - min(wallet))
            temp.append(max(wallet) - min(wallet))
    else:
        for i in range(3):  # 가지 3개
            wallet[i] += money[l]
            dfs(l+1)
            wallet[i] -= money[l]   # back 했을 때는 더해준거 빼야함


n = int(input())
money = []
for _ in range(n):
    money.append(int(input()))
wallet = [0, 0, 0]
temp = []
res = 2147000000

dfs(0)
print(min(temp))
# print(res)
