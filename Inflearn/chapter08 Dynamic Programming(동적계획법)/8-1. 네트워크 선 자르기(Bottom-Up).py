# 8-1. 네트워크 선 자르기(Bottom-Up)
# 작은 단위로 쪼개서 점화식을 구해 큰 범위로 늘려가는 것

n = int(input())
# nm의 선을 자르는 방법
dy = [0] * (n+1)
dy[1] = 1  # 1m의 선 자르는 방법 1가지
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-2] + dy[i-1]  # 점화식

print(dy[n])