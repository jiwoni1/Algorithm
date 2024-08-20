# 5-8. 단어 찾기(해시)
import sys
sys.stdin = open("input.txt", "r")

# n = int(input())
# note = []
# poem = []
# for _ in range(n):
#     note.append(input())
# for _ in range(n-1):
#     poem.append(input())
#
# for word in note:
#     if word not in poem:
#         print(word)
#         break

n = int(input())
# note = [input() for _ in range(n)]
# poem = [input() for _ in range(n-1)]

words = {}
for _ in range(n):
    word = input()
    words[word] = 1
for _ in range(n-1):
    word = input()
    words[word] += 1

for key, val in words.items():  # key, val를 출력하는 dict.items()
    if val == 1:
        print(key)
        break





