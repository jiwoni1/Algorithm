# 2-10. 점수계산
import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
test = list(map(int, input().split()))
plus = 0
score = 0

for i in test:
    if i == 1:
        plus += 1
        score += plus
    else:
        plus = 0

print(score)
