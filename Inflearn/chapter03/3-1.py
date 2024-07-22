# 3-1. 회문검사 => 항상 초기화를 잘 하자!!
import sys
sys.stdin = open("input.txt", "r")

# 1번째 방법 (내가 한거)
# n = int(input())
#
# for tc in range(1, n+1):
#     com = ""
#     word = input()
#     word = word.lower()  # lower()는 반환하는 값이라 변수에 담아주기
#     for i in range(len(word)-1, -1, -1):
#         com += word[i]
#
#     if word == com:
#         print(f'#{tc} YES')
#     else:
#         print(f'#{tc} NO')

# 2번째 방법. 더 빠른 방법
n = int(input())

for tc in range(1, n+1):
    word = input()
    word = word.lower()
    size = len(word)
    for i in range(size//2):
        if word[i] != word[-1-i]:
            print(f'#{tc} NO')
            break
    else:
        print(f'#{tc} YES')

# 3. 파이썬스러운 방법
n = int(input())

for tc in range(1, n+1):
    word = input()
    word = word.lower()

    if word == word[::-1]:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

