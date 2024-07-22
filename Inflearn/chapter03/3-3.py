# 3-3. 카드 역배치
import sys
# sys.stdin = open("input.txt", "r")

# 1번째 방법(slice 이용)
card = [i for i in range(21)]

for _ in range(10):
  ai, bi = map(int, input().split())
  r_card = card[bi: ai-1: -1]
  card = card[:ai] + r_card + card[bi+1:]

print(*card[1:])

# 2번째 방법(스와프 이용)
card = list(range(21))

for _ in range(10):
  s, e = map(int, input().split())
  for i in range((e-s+1)//2):

    card[s+i], card[e-i] = card[e-i], card[s+i]

card.pop(0)
for i in card:
  print(i, end=" ")
