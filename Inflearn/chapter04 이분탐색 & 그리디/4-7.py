# 4-7. 창고조정

l = int(input())
boxes = list(map(int, input().split()))
m = int(input())


for _ in range(m):
    boxes.sort(reverse=True)
    boxes[0] -= 1
    boxes[-1] += 1

print(max(boxes) - min(boxes))