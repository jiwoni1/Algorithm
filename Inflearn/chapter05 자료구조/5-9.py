# 5-9. 아나그램
import sys
# sys.stdin = open("input.txt", "r")

dict1 = {}
dict2 = {}

word1 = input()
word2 = input()

# 1. 직접적으로 풀어쓴 풀이
# Key값이 있으면 +1, 없으면 1
# for i in range(len(word1)):
#     if word1[i] in dict1:
#         dict1[word1[i]] += 1
#     else:
#         dict1[word1[i]] = 1
#
# for i in range(len(word2)):
#     if word2[i] in dict2:
#         dict2[word2[i]] += 1
#     else:
#         dict2[word2[i]] = 1
#
# if dict1 == dict2:
#     print("YES")
# else:
#     print("NO")


# 2. dict.get(key, 반환값)사용한 방법
# for word in word1:
#     dict1[word] = dict1.get(word, 0) + 1  # word key가 있으면 value값 반환, 없으면 0반환
# for word in word2:
#     dict2[word] = dict2.get(word, 0) + 1
#
# # dict 비교
# for i in dict1.keys():
#     if i in dict2.keys():  # dict1에 있는 키가 dict2에도 있다면
#         if dict1[i] != dict2[i]:  # value 값까지 같은지 비교
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")

# 3. 개선 코드
sh = {}

for i in word1:
    sh[i] = sh.get(i, 0) + 1
for i in word2:
    sh[i] = sh.get(i, 0) - 1
# 아나그램이라면 모든 value 값이 0

for i in word1:
    if sh.get(i) > 0:
        print("NO")
        break
else:
    print("YES")

# 4. 리스트 해쉬 이용

str1 = [0] * 52
str2 = [0] * 52

word1 = input()
word2 = input()

for i in word1:
    if i.isupper():
        str1[ord(i)-65] += 1
    else:
        str1[ord(i)-71] += 1

for i in word2:
    if i.isupper():
        str2[ord(i)-65] += 1
    else:
        str2[ord(i)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")



